**Round 7 complete.**

---

## Scorecard Summary

| Rank | Variation | Score | Miss |
|------|-----------|-------|------|
| **1 (tie)** | V-01 — Lifecycle Emphasis | **100** | — |
| **1 (tie)** | V-04 — Role Sequence + Lifecycle | **100** | — |
| 3 (tie) | V-02, V-03, V-05 | **99.3** | C-19 |

**Sole differentiator: C-19.** V-01 uses 5 explicit `Phase boundary: X is now sealed. Proceed to Phase N.` declarations. V-04 uses 2 role-completion declarations (`Role A complete. ... Role B begins.`) covering both main-phase transitions. All others use horizontal separators (`────`, `════`) for most transitions.

**C-21 and C-22 passed universally** — every R7 variation was designed with the R6 excellence signals in mind. The rubric has stabilized: when the target criteria are known in advance, all variations pass them.

---

## Excellence Signals for R8

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-signal Echo hypothesis (V-04 Role A) -- structurally constrained role that cannot reference signal artifact content identifies the Echo as a pre-analysis hypothesis before any signals are opened, creating an Echo-level epistemic bracket: what you expected to be surprised by (Role A, pre-signals) vs. what actually surprised you (Role C, post-analysis) -- extends C-22 temporal-anchoring logic from prior accuracy beliefs to prior surprise expectations", "Echo block carries explicit status-quo link field (V-05 Section 1) -- a fifth field naming what the default outcome would have assumed about this specific finding, making cost-of-inaction specific to the Echo rather than only general -- converts the Echo from a standalone finding into a comparative claim against the pre-retro baseline"]}
```
ventory, accuracy, gaps, and Echo all stay within the amended scope." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Phase 4: "Calibration Trend (if prior retro exists for this team or namespace) — Compare this retro's accuracy to a prior retro." |
| C-10 | Echo feeds back into signal design | PASS | Phase 4 Echo Feedback Loop table: Echo / Change Proposal / Type. "Not just 'we learned X' — but 'therefore we should do Y differently.'" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Phase 2 prose: "Formula: Score = (C×100 + P×50) / (C + P + W) [e.g. C=3, P=1, W=2 → (300+50)/6 = 58.3]" plus formula in column header |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 (Echo Identification) explicitly before Phase 2 (Signal Inventory and Accuracy Scoring); phase boundary marker enforces ordering |
| C-13 | Accuracy formula embedded in column header | PASS | Phase 2 column header: "Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=1,W=2 → 58.3]" — formula IS the header label |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 3 Conflict Audit table: "Preserve original Echo. Log tension here. Do not revise." + "Conflict audit result: CONFLICT DETECTED / NO CONFLICT" — both outcomes pre-populated |
| C-15 | Column header includes worked example | PASS | Phase 2 column header includes "[e.g. C=3,P=1,W=2 → 58.3]" inline |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 3: "This audit runs unconditionally. Silence is not a valid no-conflict signal. You must produce an explicit result in every retro." Explicit yes/no rows required. |
| C-17 | Echo block carries explicit LOCKED label | PASS | Phase 1: "**ECHO (LOCKED)**" as section heading + LOCK STATUS: LOCKED field in table |
| C-18 | Output divided into numbered/named phases | PASS | Phase 0 through Phase 5, each with descriptive name: PRIOR BELIEF CAPTURE / ECHO IDENTIFICATION / SIGNAL INVENTORY AND ACCURACY SCORING / CONFLICT AUDIT / GAP ANALYSIS AND ECHO FEEDBACK / FOIL CLOSE |
| C-19 | Explicit phase boundary markers declared | PASS | All 5 transitions carry declarations: "Phase boundary: Prior belief is now sealed. Proceed to Phase 1." / "Echo is now immutable. Proceed to Phase 2." / "Accuracy scoring is now sealed. Proceed to Phase 3." / "Conflict audit complete. Proceed to Phase 4." / "Gap analysis and feedback loop complete. Proceed to Phase 5." |
| C-20 | Status-quo foil section present | PASS | Phase 5 Status-Quo Foil table: Without This Retro / With This Retro columns, covering PRE-RETRO prior belief and POST-RETRO actual finding |
| C-21 | Echo Lock Record is multi-field immutability artifact | PASS | Phase 1 ECHO (LOCKED) table: four fields — WHEN locked (Phase 1 — before accuracy scoring), LOCK STATUS (LOCKED), Echo statement, Authorized conflict response (Log tension in Phase 3 conflict audit. Never revise this record.). All three required fields present. |
| C-22 | Foil captures prior belief before signals opened | PASS | Phase 0 explicitly labeled "run before opening any signal files." Phase 5 foil uses "PRE-RETRO prior belief (from Phase 0)" for Without column and "POST-RETRO actual finding" for With column. Bracket: Phase 0 (pre-signals) → Phase 5 (post-analysis). "The belief shift is demonstrated, not asserted." |

**Aspirational: 14/14**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (14/14 * 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-02 — Output Format (Table-Heavy with Formula Headers)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | TABLE 2: Namespace / Artifact Name / Date / Prediction at Signal Time / Result (C/P/W). "One row per artifact. No artifact known to exist may be omitted." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | TABLE 2 Result (C/P/W) column per artifact row with explicit prediction |
| C-03 | Gap analysis identifies missing signals | PASS | TABLE 4: # / Missing Signal Type / Namespace / Would It Have Changed the Decision? / Actionable Fix |
| C-04 | Exactly one Echo | PASS | TABLE 1 "ECHO (LOCKED)" header + "Exactly one Echo: the single most surprising finding, stated as one sentence." |
| C-05 | Overall accuracy judgment rendered | PASS | TABLE 3: "Overall Accuracy: [score / ratio / qualitative rating derived from totals row]" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | TABLE 4: "Actionable Fix (skill / question / threshold)" column |
| C-07 | Accuracy differentiated by namespace | PASS | TABLE 3 per-namespace rows: all 9 namespaces listed |
| C-08 | AMEND scope respected | PASS | "AMEND: If an AMEND instruction is present, apply it as a constraint to every table" |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | TABLE 6: Calibration Trend — Dimension / Prior Retro / This Retro / Direction |
| C-10 | Echo feeds back into signal design | PASS | TABLE 5: Echo Feedback Loop — Echo / Concrete Change Proposal / Change Type. "Not 'we learned X' — 'therefore we will do Y.'" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | TABLE 3 prose: "Formula applied to each namespace row: Score = (C×100 + P×50) / (C + P + W). Worked example: C=2, P=1, W=1 → (200+50)/4 = 62.5" plus formula in column header |
| C-12 | Echo phase precedes accuracy scoring | PASS | TABLE 1 (Echo) before TABLE 2 (Inventory) and TABLE 3 (Accuracy) |
| C-13 | Accuracy formula embedded in column header | PASS | TABLE 3 column header: "Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5]" |
| C-14 | Echo-accuracy conflict explicitly named | PASS | TABLE 3 "Conflict with Echo?" column: "This column runs unconditionally — enter NO CONFLICT or describe tension." Both outcomes pre-populated. TOTAL row: "Echo preserved. Conflicts logged above." |
| C-15 | Column header includes worked example | PASS | TABLE 3 column header includes "[e.g. C=2,P=1,W=1→62.5]" inline |
| C-16 | Conflict audit runs unconditionally | PASS | TABLE 3 "Conflict with Echo?" column runs for every namespace row unconditionally: "This column runs unconditionally — enter NO CONFLICT or describe tension." |
| C-17 | Echo block carries explicit LOCKED label | PASS | TABLE 1 row header: "ECHO (LOCKED)" + LOCK STATUS: LOCKED field |
| C-18 | Output divided into numbered/named phases | PASS | TABLE 0 through TABLE 7 — all numbered and named sections |
| C-19 | Explicit phase boundary markers declared | FAIL | After TABLE 0: "Seal this table before proceeding." + `────` (one partial declaration; does not name where to proceed). All other transitions (TABLE 1→2, 2→3, 3→4, 4→5, 5→6, 6→7) use only `────` horizontal separators. No "Phase boundary: X is sealed. Proceed to Y." declarations at 6 of 7 transitions. |
| C-20 | Status-quo foil section present | PASS | TABLE 7: "PRE-RETRO column uses Table 0 entries (captured before signals were opened). POST-RETRO column is filled now, after all tables complete." Without/With columns present. |
| C-21 | Echo Lock Record is multi-field immutability artifact | PASS | TABLE 1: four fields — WHEN locked (Before accuracy scoring (Table 2)), LOCK STATUS (LOCKED), Echo statement, Authorized conflict response (Log in Table 3 conflict column. Never revise this row.). All three required fields present. |
| C-22 | Foil captures prior belief before signals opened | PASS | TABLE 0 header: "fill before opening any signal file." TABLE 7 PRE column explicitly uses TABLE 0 entries: "PRE-RETRO column uses Table 0 entries (captured before signals were opened)." Temporal bracket established. |

**Aspirational: 13/14**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (13/14 * 10)
          = 60 + 30 + 9.3
          = 99.3
```

**Band: GOLDEN** (all essential pass, composite = 99.3)

---

## V-03 — Phrasing Register (Conversational/Imperative)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Step 2: artifact inventory table — Namespace / Artifact / Date / What Was Predicted / C/P/W. "Do not leave any out." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Step 2 C/P/W per artifact row with explicit "What Was Predicted" |
| C-03 | Gap analysis identifies missing signals | PASS | Step 4 Gap table: Gap / Namespace / Signal Type / Changes the Decision? / Fix. "Name the thing." |
| C-04 | Exactly one Echo | PASS | Step 1: "What is the single most surprising thing you discovered... One sentence. Only one. Write it here. Lock it." |
| C-05 | Overall accuracy judgment rendered | PASS | Step 2: "Give an overall verdict: score, ratio, or a plain 'strong / moderate / weak' grounded in the numbers above." |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Step 4: "Fix" column requiring "a specific skill to run, a question to ask, or a threshold to set." |
| C-07 | Accuracy differentiated by namespace | PASS | Step 2 per-namespace accuracy table with all 9 namespaces |
| C-08 | AMEND scope respected | PASS | "AMEND instruction (if provided): stay within that scope for everything — inventory, scoring, gaps, Echo. All of it." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Step 4: "If you have a previous retro for this team or namespace, compare trends: accuracy going up, down, or flat? If no prior retro, say so." |
| C-10 | Echo feeds back into signal design | PASS | Step 4: "Name the change: a new skill, a rubric edit, a threshold, a prompt." Echo → change table present |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Step 2 prose: "The formula: (C × 100 + P × 50) ÷ (C + P + W). Quick check: C=2, P=1, W=1 → (200 + 50) ÷ 4 = 62.5" plus column header formula |
| C-12 | Echo phase precedes accuracy scoring | PASS | Step 1 (Echo) before Step 2 (Inventory + Accuracy) |
| C-13 | Accuracy formula embedded in column header | PASS | Step 2 namespace table column header: "Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1→62.5]" |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Step 3: "Answer explicitly. Do not leave this blank." Conflict audit table with YES or NO required |
| C-15 | Column header includes worked example | PASS | Column header includes "[e.g. C=2,P=1,W=1→62.5]" inline |
| C-16 | Conflict audit runs unconditionally | PASS | Step 3: "Run the conflict audit. This runs every time, not just when you notice something." + "Answer explicitly. Do not leave this blank." — unconditional instruction with mandatory non-blank table |
| C-17 | Echo block carries explicit LOCKED label | PASS | Step 1: "**ECHO (LOCKED)**" as table heading + LOCK STATUS: LOCKED field |
| C-18 | Output divided into numbered/named phases | PASS | Step 0 through Step 5 — all numbered with descriptive names |
| C-19 | Explicit phase boundary markers declared | FAIL | All transitions use `════════════════════════════════════════` horizontal separators only. No "Phase boundary: X is sealed. Proceed to Step N." declarations at any of the 5 transitions. Step 1 ends with "That's your Echo. It does not change." — a lock statement but not a phase boundary marker. |
| C-20 | Status-quo foil section present | PASS | Step 5 foil table: "Without This Retro" / "With This Retro" columns present |
| C-21 | Echo Lock Record is multi-field immutability artifact | PASS | Step 1 ECHO (LOCKED) table: WHEN locked (Step 1 — before scoring), LOCK STATUS (LOCKED), Echo Statement, and "If later analysis wants to change this" column (Log the tension. Keep this record. Never revise it.). Three required fields present. |
| C-22 | Foil captures prior belief before signals opened | PASS | Step 0: "Do this now, before looking at any signal files." PRE-RETRO record written first. Step 5 foil: "The left column comes from your Step 0 record." PRE column anchored to Step 0 (pre-signals); POST filled from analysis. |

**Aspirational: 13/14**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (13/14 * 10)
          = 60 + 30 + 9.3
          = 99.3
```

**Band: GOLDEN** (all essential pass, composite = 99.3)

---

## V-04 — Role Sequence + Lifecycle (Combination)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Role B Signal Inventory table: Namespace / Artifact / Date / Prediction at Signal Time / C/P/W. "No artifact may be omitted." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Role B C/P/W per artifact with explicit Prediction at Signal Time |
| C-03 | Gap analysis identifies missing signals | PASS | Role C Section 2: Gap / Namespace / Signal Type / Decision Impact / Actionable Fix |
| C-04 | Exactly one Echo | PASS | Role A Echo Anchor Record: "one sentence hypothesis" — exactly one |
| C-05 | Overall accuracy judgment rendered | PASS | Role B: "ROLE B OUTPUT — OVERALL ACCURACY JUDGMENT: State score, ratio, or rating grounded in the per-namespace totals above." |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Role C Section 2: "Actionable Fix" column requiring "[skill / question / threshold]" |
| C-07 | Accuracy differentiated by namespace | PASS | Role B Per-Namespace Accuracy table with all 9 namespaces |
| C-08 | AMEND scope respected | PASS | "AMEND: If an AMEND instruction is provided, each role applies it as a scope constraint to its own output." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Role C Section 4: Calibration Trend table — Dimension / Prior Retro / This Retro / Direction |
| C-10 | Echo feeds back into signal design | PASS | Role C Section 3: Echo Feedback Loop — Echo / Change Proposal / Type |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Role B prose: "Formula: Score = (C×100 + P×50) / (C+P+W) [e.g. C=3, P=2, W=1 → (300+100)/6 = 66.7]" plus column header formula |
| C-12 | Echo phase precedes accuracy scoring | PASS | Role A (Echo Anchor) runs before Role B (Scorer) by role-sequence constraint. "No role may read the output of a later phase before completing its own." |
| C-13 | Accuracy formula embedded in column header | PASS | Role B column header: "Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=2,W=1→66.7]" |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Role C Section 1: conflict audit table — "Does Role B suggest revising the Echo Anchor? YES / NO" + "Tension (if any)" + "Resolution" + "Audit result: CONFLICT DETECTED / NO CONFLICT" — both outcomes pre-populated |
| C-15 | Column header includes worked example | PASS | Role B column header includes "[e.g. C=3,P=2,W=1→66.7]" inline |
| C-16 | Conflict audit runs unconditionally | PASS | Role C Section 1: "This audit runs in every retro. Silence is not a valid result." Table requires explicit audit result row. |
| C-17 | Echo block carries explicit LOCKED label | PASS | Role A: "**ECHO ANCHOR RECORD (LOCKED at Role A)**" as section heading + LOCK STATUS: LOCKED field |
| C-18 | Output divided into numbered/named phases | PASS | Role A / Role B / Role C — explicitly named. Role C sub-sections further named (Section 1–5). |
| C-19 | Explicit phase boundary markers declared | PASS | Role A→B: "Role A complete. Echo Anchor record is sealed. Signal files may now be opened. Role B begins." Role B→C: "Role B complete. Accuracy scoring is sealed. Role C begins." Both role transitions carry explicit sealed declarations. Role C sections are sub-sections within a single phase (Role C), not consecutive main phases — following R6 precedent. |
| C-20 | Status-quo foil section present | PASS | Role C Section 5 Foil Close: "Without This Retro (PRE — Role A record)" / "With This Retro (POST — Role B/C findings)" columns — four rows with explicit PRE/POST labels |
| C-21 | Echo Lock Record is multi-field immutability artifact | PASS | Role A ECHO ANCHOR RECORD table: WHEN locked (Role A — before signals opened), LOCK STATUS (LOCKED), Pre-analysis Echo hypothesis, Authorized conflict response (log tension in Role C conflict audit. Never revise this record.). All three required fields present. |
| C-22 | Foil captures prior belief before signals opened | PASS | Role A labeled "Runs: Before any signal files are opened." with hard constraint "Cannot reference any signal artifact content." Role C Section 5 PRE column: "Role A record, written before signals were opened." POST column: "Role B/C findings, written after all analysis complete." Structurally enforced bracket — not merely instructed. |

**Aspirational: 14/14**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (14/14 * 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-05 — Inertia Framing + Output Format (Combination)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Section 2 inventory table: Namespace / Artifact / Date / Prediction at Signal Time / C/P/W / Cost Without This Signal |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Section 2 C/P/W per artifact with explicit Prediction at Signal Time |
| C-03 | Gap analysis identifies missing signals | PASS | Section 4 Gap table: Gap / Namespace / Signal Type / Would It Have Changed Section 0 Default? / Actionable Fix |
| C-04 | Exactly one Echo | PASS | Section 1: "One sentence. The genuine surprise." ECHO (LOCKED) table with single Echo statement field |
| C-05 | Overall accuracy judgment rendered | PASS | Section 2: "Overall Accuracy vs Default: State the gap between what was assumed in Section 0 and what the per-namespace scores actually show." |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Section 4: "Actionable Fix" column requiring "[specific skill / question / threshold]" |
| C-07 | Accuracy differentiated by namespace | PASS | Section 2 per-namespace accuracy table with all 9 namespaces + Default Assumption vs Actual column |
| C-08 | AMEND scope respected | PASS | "AMEND: If an AMEND instruction is present, it applies to all sections." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Section 4 Calibration Trend table: Dimension / Prior Retro / This Retro / Direction |
| C-10 | Echo feeds back into signal design | PASS | Section 4 Echo feedback: "translate the locked Echo into a change proposal. Phrase it as cost-of-inaction." Echo / Cost of Not Acting / Change Proposal / Type table |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Section 2 column header has formula and worked example; formula stated in prose as well |
| C-12 | Echo phase precedes accuracy scoring | PASS | Section 1 (Echo) before Section 2 (Signal Inventory and Accuracy) |
| C-13 | Accuracy formula embedded in column header | PASS | Section 2 column header: "Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=2,W=1→80]" |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Section 3 Conflict Audit: "Does the Section 2 accuracy picture suggest revising the Section 1 Echo? YES / NO" + tension description + Resolution: "Echo preserved. Tension logged here." + "Audit verdict: CONFLICT DETECTED / NO CONFLICT" |
| C-15 | Column header includes worked example | PASS | Column header includes "[e.g. C=2,P=2,W=1→80]" inline |
| C-16 | Conflict audit runs unconditionally | PASS | Section 3: "CONFLICT AUDIT (unconditional — always runs)" heading + "Audit verdict: CONFLICT DETECTED / NO CONFLICT" mandatory row |
| C-17 | Echo block carries explicit LOCKED label | PASS | Section 1: "**ECHO (LOCKED)**" heading + LOCK STATUS: LOCKED field. "SEAL: Echo is locked." follows. |
| C-18 | Output divided into numbered/named phases | PASS | Section 0 through Section 5 — all numbered and named |
| C-19 | Explicit phase boundary markers declared | FAIL | Section 0→1: "SEAL: Default outcome record is complete. Signal files may now be opened." — qualifies as boundary declaration. Section 1→2: "SEAL: Echo is locked..." — qualifies. Sections 2→3, 3→4, 4→5: only `────────────────────────────────────────────────────────────────` separators; no sealing declarations. Three of five transitions missing. C-19 requires markers at each transition. |
| C-20 | Status-quo foil section present | PASS | Section 5 Foil Close: "Without This Retro (PRE — Section 0 record)" / "With This Retro (POST — Sections 2–4)" columns — five rows including decision quality |
| C-21 | Echo Lock Record is multi-field immutability artifact | PASS | Section 1 ECHO (LOCKED) table: five fields — WHEN locked (Section 1 — before inventory and accuracy), LOCK STATUS (LOCKED), Echo statement, "What the status-quo would have assumed instead", Authorized conflict response (Log tension in Section 3 conflict audit. Do not revise this record.). All three required fields present plus additional inertia-framing field. |
| C-22 | Foil captures prior belief before signals opened | PASS | Section 0: "Name the status-quo... write before opening signal files." + "SEAL: Default outcome record is complete. Signal files may now be opened." Section 5 PRE column: "Section 0 record, written before signals were opened." POST column: "filled now, after all sections complete." Temporal bracket established by SEAL declaration. |

**Aspirational: 13/14**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (13/14 * 10)
          = 60 + 30 + 9.3
          = 99.3
```

**Band: GOLDEN** (all essential pass, composite = 99.3)

---

## Ranking

| Rank | Variation | Score | Band | Aspirational | Miss |
|------|-----------|-------|------|--------------|------|
| **1 (tie)** | V-01 — Lifecycle Emphasis | **100** | GOLDEN | 14/14 | — |
| **1 (tie)** | V-04 — Role Sequence + Lifecycle | **100** | GOLDEN | 14/14 | — |
| 3 (tie) | V-02 — Output Format | **99.3** | GOLDEN | 13/14 | C-19 (no boundary declarations between tables) |
| 3 (tie) | V-03 — Phrasing Register | **99.3** | GOLDEN | 13/14 | C-19 (only `════` separators; no sealing declarations) |
| 3 (tie) | V-05 — Inertia Framing + Output Format | **99.3** | GOLDEN | 13/14 | C-19 (SEAL: declarations for first 2 transitions, missing for last 3) |

**V-01 and V-04 tied at 100.** All five variations pass all essential and recommended criteria. The sole differentiator is C-19: V-01 and V-04 carry explicit phase boundary declarations at every main-phase transition; V-02, V-03, and V-05 rely on horizontal separators (`────`, `════`) for most transitions.

**Miss analysis — V-02:** Tables 1→2 through 6→7 use `────` horizontal separators only. "Seal this table before proceeding." after TABLE 0 is the only boundary-adjacent instruction, and it does not name the destination phase. Six of seven transitions lack declarations.

**Miss analysis — V-03:** Steps 0→1 through 4→5 all use `════════════════════════════════════════` separators only. Step 1 ends with "That's your Echo. It does not change." — a lock statement but not a boundary declaration naming the next phase.

**Miss analysis — V-05:** Correctly uses "SEAL:" declarations for Section 0→1 and 1→2. Sections 2→3, 3→4, 4→5 revert to `────` separators. Partial C-19 compliance but not complete — C-19 requires declarations at each transition.

---

## Excellence Signals

**From V-04:**

**Pre-signal Echo hypothesis — Role A constraint creates an Echo-level epistemic bracket** — V-04 Role A is structurally constrained: "Cannot reference any signal artifact content." This forces the Echo hypothesis to be identified from intuition before any signal data is accessed — not merely before accuracy scoring (C-12) but before opening any signal files at all. The result is a two-stage Echo record: Role A hypothesis (what you expected to be surprised by) and Role C confirmed Echo (what actually surprised you). The bracket demonstrates whether your surprise expectations were themselves accurate, parallel to the accuracy-level prior belief foil. C-22 captures temporal anchoring of prior accuracy beliefs; no criterion captures temporal anchoring of surprise expectations. This pattern could extend C-22's epistemic logic to the Echo itself.

**From V-05:**

**Echo block carries explicit status-quo link field** — V-05 Section 1 Echo table includes a fifth field: "What the status-quo would have assumed instead: [what the default outcome (Section 0) implied about this]." This makes the cost-of-inaction specific to the Echo finding itself — not just to the overall signal set. C-21 requires the Echo lock record to document WHEN/WHAT/HOW; V-05 adds a fourth field linking the Echo to the baseline assumption, making the surprise explicitly comparative. The foil (C-20) documents what the team would have done without the retro; V-05's Echo field documents what the status-quo would have predicted about this specific finding. Not yet captured by any criterion.

---

**Round 7 Summary**

| Variation | Score | Aspirational | Miss |
|-----------|-------|--------------|------|
| V-01 Lifecycle Emphasis | **100** | 14/14 | — |
| V-04 Role Sequence + Lifecycle | **100** | 14/14 | — |
| V-02 Output Format | 99.3 | 13/14 | C-19 |
| V-03 Phrasing Register | 99.3 | 13/14 | C-19 |
| V-05 Inertia Framing | 99.3 | 13/14 | C-19 |

C-21 and C-22 (new in v7) are passed by all variations — every R7 prompt was designed with these patterns in mind. The rubric has stabilized at near-100 coverage; the differentiator remains structural enforcement of phase boundary declarations (C-19).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-signal Echo hypothesis (V-04 Role A) -- structurally constrained role that cannot reference signal artifact content identifies the Echo as a pre-analysis hypothesis before any signals are opened, creating an Echo-level epistemic bracket: what you expected to be surprised by (Role A, pre-signals) vs. what actually surprised you (Role C, post-analysis) -- extends the C-22 temporal-anchoring logic from prior accuracy beliefs to prior surprise expectations, making the surprise claim verifiable rather than retrospectively asserted", "Echo block carries explicit status-quo link field (V-05 Section 1) -- a fifth field in the Echo lock record naming what the default outcome (Section 0) would have assumed about this specific finding, making cost-of-inaction specific to the Echo rather than only general -- C-21 requires WHEN/WHAT/HOW fields; this pattern adds a fourth field linking the Echo surprise to the pre-retro baseline assumption, converting the Echo from a standalone finding into a comparative claim against the status-quo"]}
```
