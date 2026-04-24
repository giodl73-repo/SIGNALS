Now I have enough to score. Let me compile from what I've read:

- **Rubric v6**: C-01–C-05 essential (60 pts), C-06–C-08 recommended (30 pts), C-09–C-20 aspirational (10 pts), denominator /12
- **Base (R5 V-05)**: passes C-01–C-09, C-11–C-18; fails C-10 (universal); C-19 and C-20 are new to v6
- **R6 axis assignments**: V-01 targets C-20 (named artifact gate), V-02 targets C-19 (citation carry-through), V-03 targets C-20 (register), V-04 = V-01×V-02, V-05 = V-04 + register + inertia framing

---

# Quest-Rubric Scorecard — Round 6

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v6 (C-01 through C-20; E=5, R=3, A=12)
**Formula:** `composite = (E/5 × 60) + (R/3 × 30) + (A/12 × 10)`
**Golden threshold:** all 5 essential PASS AND composite ≥ 80

---

## Rubric Derivation

```
Essential criteria:    C-01, C-02, C-03, C-04, C-05          → E_count = 5
Recommended criteria:  C-06, C-07, C-08                      → R_count = 3
Aspirational criteria: C-09 through C-20                     → A_count = 12

Formula: composite = (essential_pass / 5 × 60)
                   + (recommended_pass / 3 × 30)
                   + (aspirational_pass / 12 × 10)

Golden threshold: all essential PASS AND composite >= 80
[DERIVE COMPLETE]
```

---

## Baseline Assumptions (R5 V-05 Inheritance)

R6 variations are built on R5 V-05 (section template + CONVERSION-MAP gate + Spec Analyst role). That base established: SA-1 SCHEMA BLOCK positionally first (C-17 PASS), CONVERSION-MAP boolean gate (C-18 PASS), CALIBRATION-PAIR foil pairs (C-13 PASS), closed enumeration via CONVERSION-MAP (C-14 PASS), structural verification gating Auditor (C-11 PASS). Universal gap entering R6: C-10 (no partial credit formula). New gaps in v6: C-19 (identifier citation in canonical row — base has instruction to cite but no carry-through enforcement) and C-20 (Author Entry Gate structural block — base has checklist-advisory "DO NOT begin until Spec Analyst Completion Gate cleared," which names the gate phase, not the artifact identifiers).

---

## Variation-by-Criterion Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** skill identity | PASS | PASS | PASS | PASS | PASS |
| **C-02** criteria testable | PASS | PASS | PASS | PASS | PASS |
| **C-03** pass condition enforced | PASS | PASS | PASS | PASS | PASS |
| **C-04** scoring formula explicit | PASS | PASS | PASS | PASS | PASS |
| **C-05** tier structure present | PASS | PASS | PASS | PASS | PASS |
| **C-06** failure modes cataloged | PASS | PASS | PASS | PASS | PASS |
| **C-07** specificity test included | PASS | PASS | PASS | PASS | PASS |
| **C-08** version and date stamped | PASS | PASS | PASS | PASS | PASS |
| **C-09** coverage of output sections | PASS | PASS | PASS | PASS | PASS |
| **C-10** partial credit in formula | FAIL | FAIL | FAIL | FAIL | FAIL |
| **C-11** external enforcement gate | PASS | PASS | PASS | PASS | PASS |
| **C-12** failure modes before criteria | PASS | PASS | PASS | PASS | PASS |
| **C-13** foil pair present | PASS | PASS | PASS | PASS | PASS |
| **C-14** closed enumeration | PASS | PASS | PASS | PASS | PASS |
| **C-15** specificity prohibitions converted | PASS | PASS | PASS | PASS | PASS |
| **C-16** fields have structural home | PASS | PASS | PASS | PASS | PASS |
| **C-17** SCHEMA BLOCK positionally first | PASS | PASS | PASS | PASS | PASS |
| **C-18** CONVERSION-MAP boolean gate | PASS | PASS | PASS | PASS | PASS |
| **C-19** identifier citation in canonical row | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-20** Author Entry Gate structural block | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** |

---

## Per-Variation Evidence and Scoring

### V-01 — Lifecycle Emphasis: Author Entry Gate with Named Artifact Blocking

**C-19 FAIL:** AUTHOR STATUS CHECK block is present with SA-2 row identifier fields in the INERTIA-RECORD, and A2a says "cite the row identifier — do not re-derive." However, the canonical CRITERION row template is `[final condition from INERTIA-RECORD]` with no explicit mandate to carry CM-NN forward into the Pass Condition column. No STRUCTURAL VERIFICATION citation check, no FINAL RUBRIC citation-retention note. The identifier appears in the working block but may be stripped during canonicalization.

**C-20 PASS:** "DO NOT BEGIN WRITING CRITERIA" (explicit imperative blocking phrasing). AUTHOR STATUS CHECK block names `SA-1 SCHEMA BLOCK` and `SA-2 CONVERSION-MAP` by identifier with PRESENT/ABSENT status fields. "Any ABSENT or INSUFFICIENT halts Author execution" closes the gate. Both conditions satisfied: imperative phrasing AND named artifact identifiers (not phase label).

**All other criteria:** Inherited from R5 V-05 base. C-10 FAIL (universal — formula has no partial credit).

```
Essential:    5/5 pass = 60.0 pts
Recommended:  3/3 pass = 30.0 pts
Aspirational: 10/12 pass (C-10, C-19 fail) = 10/12 × 10 = 8.33 pts
Composite: 98.33
Golden: YES
```

---

### V-02 — Role Sequence: Identifier Citation in Canonical Criterion Row

**C-19 PASS:** Three enforcement checkpoints prevent canonicalization stripping:
1. A2d instruction: "Citation rule: if specificity criterion, Pass Condition MUST include CM-NN reference — write `[final condition]; operationalizes SA-2 CM-[N]`."
2. STRUCTURAL VERIFICATION adds: "confirm the Pass Condition column includes 'operationalizes SA-2 CM-N'" per specificity criterion, with correction required before Auditor begins.
3. FINAL RUBRIC section: "For specificity criteria, Pass Condition MUST include CM-NN citation. Substitute Auditor-revised conditions where Revision Required = YES." Citation is an explicit copy-forward obligation at reproduction.

**C-20 FAIL:** Author Entry Gate reads: "AUTHOR ENTRY GATE — DO NOT begin writing criteria until: [ ] Spec Analyst Completion Gate is cleared." Imperative language present ("DO NOT begin writing criteria until") but blocking artifact named by phase label ("Spec Analyst Completion Gate"), not by artifact identifier (SA-1, SA-2). Checklist-advisory format (checkbox list) with phase-label reference fails the "names the specific artifacts by identifier" requirement. This is identical to the R5 V-05 base pattern identified as the C-20 gap.

```
Essential:    5/5 pass = 60.0 pts
Recommended:  3/3 pass = 30.0 pts
Aspirational: 10/12 pass (C-10, C-20 fail) = 10/12 × 10 = 8.33 pts
Composite: 98.33
Golden: YES
```

---

### V-03 — Phrasing Register: Formal-Imperative Phase Declarations

**C-19 FAIL:** The INERTIA-RECORD gains `CRITERION GATE: [OPEN — inertia test = NO] / [BLOCKED]` inline and `SA-2 row cited: [CM-NN]` field. However, the canonical CRITERION row template is still `[final condition from INERTIA-RECORD]` — no explicit citation carry-through rule to the Pass Condition column, no STRUCTURAL VERIFICATION citation check, no FINAL RUBRIC citation retention note. Same canonicalization stripping gap as V-01.

**C-20 PASS:** The AUTHOR ENTRY CHECK block names `SA-1 SCHEMA BLOCK` and `SA-2 CONVERSION-MAP` by identifier with PRESENT/ABSENT status. "AUTHOR: BLOCKED (write if any line shows ABSENT or NOT MET — write the missing item, then re-run AUTHOR ENTRY CHECK)" is equivalent imperative blocking phrasing. The model must commit to "AUTHOR: OPEN" or "AUTHOR: BLOCKED" — a hard status declaration that cannot be treated as advisory. Both conditions satisfied: equivalent imperative blocking (BLOCKED/stop) AND named artifact identifiers (SA-1 SCHEMA BLOCK, SA-2 CONVERSION-MAP, not just phase label).

**Note on C-13:** CALIBRATION-PAIR labels change to "GENERIC: [Status-Quo Rubric]" / "GROUNDED" and AU-3 uses "GENERIC: [Status-Quo Rubric]" / "GROUNDED." Foil pair present and labeled. C-13 PASS.

```
Essential:    5/5 pass = 60.0 pts
Recommended:  3/3 pass = 30.0 pts
Aspirational: 10/12 pass (C-10, C-19 fail) = 10/12 × 10 = 8.33 pts
Composite: 98.33
Golden: YES
```

---

### V-04 — Lifecycle Emphasis × Role Sequence (V-01 × V-02, Combination)

**C-19 PASS (from V-02 mechanism):** CRITERION row citation rule: "Pass Condition field must include the SA-2 identifier: `[final condition]; operationalizes SA-2 CM-[N]`." STRUCTURAL VERIFICATION checks: "for each specificity criterion (INERTIA-RECORD shows 'CM-NN'), the CRITERION row Pass Condition column includes 'operationalizes SA-2 CM-N'" with repair required before Auditor begins. FINAL RUBRIC: "For specificity criteria, Pass Condition MUST include CM-NN citation — do not simplify or omit it during reproduction." Three-point enforcement across the lifecycle.

**C-20 PASS (from V-01 mechanism):** "DO NOT BEGIN WRITING CRITERIA" imperative. ARTIFACT INVENTORY block names `SA-1 SCHEMA BLOCK` (with `skill = [value], fields = [list]`) and `SA-2 CONVERSION-MAP` (with row identifiers `CM-01` through `CM-N`) explicitly by identifier with PRESENT/EMPTY DECLARATION/ABSENT status. `AUTHOR ACCESS: [GRANTED / DENIED]` — the model must commit to a binary status. "Write DENIED and stop if any line shows ABSENT or INSUFFICIENT." STRUCTURAL VERIFICATION checks "ARTIFACT INVENTORY block is present and AUTHOR ACCESS = GRANTED." Both conditions satisfied: imperative blocking AND named artifact identifiers.

**Mechanism interaction:** V-04's ARTIFACT INVENTORY fires before A-2 begins (phase entry); the citation rule fires per criterion within A-2 (row content). The two mechanisms are at non-competing lifecycle positions. Structural Verification checks both independently: ARTIFACT INVENTORY + AUTHOR ACCESS at phase level, CM-NN in Pass Condition at row level.

```
Essential:    5/5 pass = 60.0 pts
Recommended:  3/3 pass = 30.0 pts
Aspirational: 11/12 pass (C-10 only fail) = 11/12 × 10 = 9.17 pts
Composite: 99.17
Golden: YES
```

---

### V-05 — Full Combination (Lifecycle × Role Sequence × Phrasing Register + Inertia Framing)

**C-19 PASS (from V-04 mechanism):** Same three-point enforcement as V-04. Additionally the FINAL RUBRIC section adds "Retain CM-NN citations in Pass Condition for specificity criteria — do not simplify during reproduction." (Stronger phrasing than V-04's version; both enforce.)

**C-20 PASS (doubly enforced):** ARTIFACT INVENTORY + AUTHOR: OPEN/BLOCKED status declaration. V-05 places ARTIFACT INVENTORY between SPEC ANALYST: CLOSED and AUTHOR: OPEN, requiring the model to write status declarations at both the SPEC ANALYST boundary and the AUTHOR boundary. The AUTHOR: BLOCKED declaration requires the model to commit to a status before A-1 begins. STRUCTURAL VERIFICATION checks "ARTIFACT INVENTORY block present with AUTHOR: OPEN."

**C-07 (stronger compliance):** The opening framing names "the Status-Quo Rubric" as a concrete competitor ("every rubric you write competes with the Status-Quo Rubric"). The INERTIA-RECORD test is renamed "Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this skill's spec?" AU-1 uses "Status-Quo Test" column. The CALIBRATION-PAIR labels use "STATUS-QUO RUBRIC" explicitly. C-07 is PASS in both V-04 and V-05; V-05's competitive framing intensifies specificity pressure throughout the pipeline. No numeric change (binary pass), but qualitative improvement.

**No regression from additional framing:** Adding Status-Quo Rubric labeling does not disturb C-13 (foil pair present — pair remains), C-14 (closed enumeration — CONVERSION-MAP inherited), or C-18 (boolean gate — unchanged).

```
Essential:    5/5 pass = 60.0 pts
Recommended:  3/3 pass = 30.0 pts
Aspirational: 11/12 pass (C-10 only fail) = 11/12 × 10 = 9.17 pts
Composite: 99.17
Golden: YES
```

---

## Summary and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 (tie) | **V-04** — lifecycle × role-sequence | 5/5 | 3/3 | 11/12 | **99.17** | YES |
| 1 (tie) | **V-05** — full combination | 5/5 | 3/3 | 11/12 | **99.17** | YES |
| 3 (tie) | V-01 — lifecycle (C-20 solo) | 5/5 | 3/3 | 10/12 | **98.33** | YES |
| 3 (tie) | V-02 — role-sequence (C-19 solo) | 5/5 | 3/3 | 10/12 | **98.33** | YES |
| 3 (tie) | V-03 — phrasing register (C-20 register) | 5/5 | 3/3 | 10/12 | **98.33** | YES |

**All variations achieve Golden.** V-04 and V-05 tied at first. V-05 is the qualitative winner: C-20 is doubly enforced and C-07 compliance is stronger, though neither changes the numeric score since both criteria are already PASS.

**Universal FAIL:** C-10 (partial credit absent from scoring formula) — not addressed by any R6 axis. No essential failures across the set.

---

## Excellence Signals

**E-1 (V-04 and V-05 — triple-checkpoint citation carry-through):** Single instruction to "cite the row identifier" is insufficient to survive canonicalization. V-02/V-04/V-05 add enforcement at three distinct points where identifier stripping might occur: (1) CRITERION row recording instruction with explicit format `[final condition]; operationalizes SA-2 CM-[N]`, (2) STRUCTURAL VERIFICATION citation scan with mandatory repair before Auditor begins, (3) FINAL RUBRIC reproduction note "MUST include CM-NN citation — do not simplify." Each checkpoint targets a different stage of the output lifecycle where a model in "clean final output" mode might strip the citation. Single-point instruction fails; three-point coverage survives.

**E-2 (V-04 and V-05 — AUTHOR ACCESS: GRANTED/DENIED commit with named artifact inventory):** The ARTIFACT INVENTORY format requires the model to write a binary commit word (GRANTED or DENIED) only after listing each artifact by identifier with present/absent status inline. This prevents the "completing the gate check while ignoring it" failure mode: if the model writes `SA-2 CONVERSION-MAP: [ABSENT]`, the next required token is `AUTHOR ACCESS: DENIED` — a false GRANTED is detectable by content inspection without reading criteria. Advisory checklist format allows the model to proceed despite unchecked boxes; the GRANTED/DENIED commit closes that gap.

**E-3 (V-05 — Status-Quo Rubric as named front-loaded competitor):** Renaming "inertia test" to "Status-Quo test" and placing the Status-Quo Rubric competitor description at the opening of the prompt (before any role instructions) reframes specificity as a competitive requirement rather than a quality criterion. The model is told "your rubric must include pass conditions that the Status-Quo Rubric cannot satisfy" before it reads the spec — this front-loads the discriminating-element pressure across the entire execution. The framing propagates through INERTIA-RECORD, CALIBRATION-PAIR, AU-1, and AU-3 column labels, creating a consistent competitive thread. This is a candidate for R7 C-21: "Status-Quo Rubric named as the discriminating foil in opening framing, propagated to all specificity-check sites."

---

## Roadmap Notes (for Round 7)

**C-10 (partial credit) remains the sole universal gap.** No R6 axis addresses it. Path to composite 100 requires C-10 PASS; the only mechanism would be a scoring formula that explicitly names partial credit weighting inline (e.g., "PASS = 1.0, PARTIAL = 0.5 for essential and recommended, PARTIAL = 0 for aspirational"). R5 Excellence Signal E-3 suggested seeking partial credit as a side-effect of a gate-based mechanism; no gate mechanism has produced it yet.

**R6 confirms additive combination:** V-01 (C-20 only, C-19 FAIL) + V-02 (C-19 only, C-20 FAIL) → V-04 (both C-19 and C-20 PASS) confirms the non-competing mechanism hypothesis. No interaction degradation detected.

**V-03 register adds no net score gain over V-01 for C-20** — both PASS C-20 and fail C-19. However, V-03's AUTHOR: BLOCKED/OPEN format may offer robustness advantage under adversarial conditions (a model cannot "skip" the BLOCKED declaration without producing a detectable structural omission). Candidate for R7 C-21 if isolation test confirms distinct coverage.

```json
{"top_score": 99.17, "all_essential_pass": true, "new_patterns": ["Triple-checkpoint citation carry-through — enforce CM-NN identifier at CRITERION row recording, STRUCTURAL VERIFICATION citation scan, and FINAL RUBRIC reproduction note — prevents canonicalization stripping that single-instruction approach cannot prevent", "AUTHOR ACCESS: GRANTED/DENIED commit word with named artifact inventory makes a false gate passage detectable by content inspection: model must commit to DENIED if any artifact is ABSENT, eliminating the advisory-checklist failure mode where unchecked boxes do not block execution", "Status-Quo Rubric named as front-loaded competitor in opening prompt framing, propagated to INERTIA-RECORD, CALIBRATION-PAIR, AU-1, and AU-3 column labels — reframes specificity from quality criterion to competitive requirement, applying discriminating-element pressure across all execution phases before the first criterion is written"]}
```
