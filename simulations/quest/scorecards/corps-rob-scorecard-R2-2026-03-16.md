## Quest Score — corps-rob Round 2

**Rubric**: v2 (max 115) | **Variations**: V-01 through V-05 | **Date**: 2026-03-16

---

### Scoring Model

| Pool | Criteria | Max | Calculation |
|------|----------|-----|-------------|
| Essential | C-01 to C-05 | 60 | (passed/5) × 60 |
| Recommended | C-06 to C-08 | 30 | (passed/3) × 30 |
| Aspirational | C-09 to C-13 | 25 | (passed/5) × 25 |

PARTIAL counts as 0.5 pass in proportional scoring.

---

## V-01 — Severity Triage Protocol

**Axis**: C-12 (severity discrimination via silent pre-finding calibration step)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Stage identity | PASS | `## Stage:` header + ROLE: line present in template |
| C-02 | Role-loaded perspective | PASS | Template: "specific concern grounded in this role's lens — the most critical item they found"; setup reads `.roles/` |
| C-03 | ROB format compliance | PASS | Stage header, role identity, severity labels (HIGH/MED/LOW), explicit verdict all in template |
| C-04 | Actionable findings | PASS | Minimum 2 findings with Owner: and Resolution: per stage |
| C-05 | Go/No-Go in TPM | PASS | Explicit GO/NO-GO/GO WITH CONDITIONS label + "cite at least one finding or risk ID" |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference requirement anywhere in prompt |
| C-07 | Structured risk register | PASS | Risk register table (ID, Risk, Severity, Likelihood, Mitigation) with minimum 3 entries, 1 HIGH required |
| C-08 | Exec-office cascade | PASS | "name a specific S-office mission by name and trace its alignment or gap — generic references do not satisfy" |
| C-09 | Inter-stage blocker | FAIL | Not mentioned |
| C-10 | Cross-cutting theme | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No CONDITIONS: block; verdict format ends at Rationale sentence |
| C-12 | Severity discrimination | PASS | Explicit silent triage step (most critical = HIGH; least critical = LOW) + enforcement note: "Triage Note if all findings are HIGH" |
| C-13 | Risk register status lifecycle | FAIL | No Status column in risk register template |

**Score:**
- Essential: 5/5 × 60 = **60**
- Recommended: 2/3 × 30 = **20**
- Aspirational: 1/5 × 25 = **5**
- **Composite: 85** | All essential pass: YES | Golden: YES (≥80)

---

## V-02 — Conditional Verdict Itemization

**Axis**: C-11 (mandatory CONDITIONS: block template in every verdict)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Stage identity | PASS | `## Stage:` + ROLE: line |
| C-02 | Role-loaded perspective | PASS | Template: "specific concern — not a category, specific to this role's lens"; setup reads `.roles/` |
| C-03 | ROB format compliance | PASS | All four elements present per stage |
| C-04 | Actionable findings | PASS | 2+ findings with Owner/Resolution |
| C-05 | Go/No-Go in TPM | PASS | TPM section has GO/NO-GO + CONDITIONS: block |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register | PASS | Table with 3 entries, severity, likelihood, mitigation, 1 HIGH required |
| C-08 | Exec-office cascade | PASS | "name a specific S-office mission and trace its alignment or gap" |
| C-09 | Inter-stage blocker | FAIL | Not mentioned |
| C-10 | Cross-cutting theme | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | PASS | Mandatory CONDITIONS: block template in every verdict; N/A pattern for unconditional; enforcement: "re-write as APPROVED if no conditions can be named" |
| C-12 | Severity discrimination | PARTIAL | Template slots show HIGH/MED/LOW options; risk register requires 1 HIGH; but no triage step, no enforcement note for findings severity spread |
| C-13 | Risk register status lifecycle | FAIL | No Status column |

**Score:**
- Essential: 5/5 × 60 = **60**
- Recommended: 2/3 × 30 = **20**
- Aspirational: 1.5/5 × 25 = **7.5**
- **Composite: 87.5** | All essential pass: YES | Golden: YES

---

## V-03 — Living Risk Register

**Axis**: C-13 (Status column + update semantics as first-class artifact)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Stage identity | PASS | `## Stage:` + ROLE: line |
| C-02 | Role-loaded perspective | PASS | Template: "specific concern grounded in this role's lens"; setup reads `.roles/` |
| C-03 | ROB format compliance | PASS | All four elements per stage |
| C-04 | Actionable findings | PASS | 2+ findings with Owner/Resolution |
| C-05 | Go/No-Go in TPM | PASS | Explicit GO/NO-GO, "cite at least one risk by R-ID" |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register | PASS | Full table + Update Protocol section — strongest C-07 framing of any single-axis variation |
| C-08 | Exec-office cascade | PASS | "name a specific S-office mission by name — 'Strategic priorities' does not satisfy" |
| C-09 | Inter-stage blocker | FAIL | Not mentioned |
| C-10 | Cross-cutting theme | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No CONDITIONS: block in verdict template |
| C-12 | Severity discrimination | PARTIAL | Register requires "at least 1 HIGH severity"; no explicit below-HIGH requirement for stage findings; no triage step |
| C-13 | Risk register status lifecycle | PASS | Status column with OPEN/WATCH/MITIGATED vocabulary; Update Protocol section; "at least 2 distinct Status values" enforcement |

**Score:**
- Essential: 5/5 × 60 = **60**
- Recommended: 2/3 × 30 = **20**
- Aspirational: 1.5/5 × 25 = **7.5**
- **Composite: 87.5** | All essential pass: YES | Golden: YES

*V-02 and V-03 tie at 87.5 — each nails its target criterion but misses the other two v2 aspirationals.*

---

## V-04 — All Three New Criteria as Formatting Rules

**Axes**: RULE A (C-12) + RULE B (C-11) + RULE C (C-13) as named format errors

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Stage identity | PASS | `## Stage:` + ROLE: line with orientation |
| C-02 | Role-loaded perspective | PARTIAL | Template says "grounded in this role's lens" and reads `.roles/`; but three stacked format rules + FORMAT ERROR PROTOCOL + cross-stage count requirements create structural pressure toward compliance-over-authenticity — the risk the hypothesis explicitly names. Role named in header; finding specificity uncertain under mechanical rule load. |
| C-03 | ROB format compliance | PASS | All four elements present; CONDITIONS: block in template |
| C-04 | Actionable findings | PASS | 2+ per stage with Owner/Resolution |
| C-05 | Go/No-Go in TPM | PASS | Go/No-Go + CONDITIONS: block (RULE B applies) |
| C-06 | Cross-stage coherence | PASS | "At least 2 cross-stage references across the full run" explicit count; format: `[prior stage] F-[N]: confirm / escalate / contradict` |
| C-07 | Structured risk register | PASS | Full table + Status column (RULE C); 2+ distinct values required |
| C-08 | Exec-office cascade | PASS | Mission Cascade TABLE (structured, not just text): S-Office Mission / Program / Artifact/Topic / Alignment columns with ALIGNED/PARTIAL/GAP vocabulary |
| C-09 | Inter-stage blocker | PARTIAL | Cross-stage references required with confirm/escalate/contradict pattern — escalate could capture blockers but no explicit "blocker detection" named |
| C-10 | Cross-cutting theme | PARTIAL | Cross-stage references required but no document-level Synthesis/Themes section; repetition elevation not named |
| C-11 | Conditional verdict itemization | PASS | RULE B: named format rule; CONDITIONS: block in every verdict template; N/A for unconditional |
| C-12 | Severity discrimination | PASS | RULE A: "uniform-severity stage is a format error"; enforcement via `## Format Errors` section if violated |
| C-13 | Risk register status lifecycle | PASS | RULE C: Status column required, 2+ distinct values required, format error if absent |

**Score:**
- Essential: 4.5/5 × 60 = **54** *(C-02 PARTIAL)*
- Recommended: 3/3 × 30 = **30**
- Aspirational: 4/5 × 25 = **20** *(C-09, C-10 each 0.5)*
- **Composite: 104** | All essential pass: NO (C-02 PARTIAL) | Golden: YES

*Highest composite in the round. Trade-off: C-02 integrity is structurally at risk from rule density. All three v2 aspirationals pass.*

---

## V-05 — Descriptive Register + Living Risk Register + Severity Triage

**Axes**: Natural-voice framing (C-02 guard) + C-13 + C-12

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Stage identity | PASS | `## Stage:` + ROLE: line |
| C-02 | Role-loaded perspective | PASS | Strongest C-02 of round: "Not a checklist — this role's specific concerns about this specific topic. Generic findings that any role could have written indicate the persona was not loaded." Explicit anti-generic guard. |
| C-03 | ROB format compliance | PASS | Stage header, role identity, severity labels, verdict all in template |
| C-04 | Actionable findings | PASS | Minimum 2 findings with Owner and Resolution per stage |
| C-05 | Go/No-Go in TPM | PASS | GO/NO-GO/GO WITH CONDITIONS + conditions as numbered items if conditional |
| C-06 | Cross-stage coherence | PARTIAL | "When a concern resurfaces, name it: confirm, escalate, or contradict" — instruction present but no minimum count; C-06 pass condition requires "at least 2 references" |
| C-07 | Structured risk register | PASS | Full table with Status column; OPEN/WATCH/MITIGATED; minimum 3 rows; 2 distinct Status values |
| C-08 | Exec-office cascade | PASS | "named executive-level mission... the mission must be named and the alignment or gap must be specific — 'company priorities' is not enough" |
| C-09 | Inter-stage blocker | FAIL | Not mentioned |
| C-10 | Cross-cutting theme | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | PARTIAL | Template includes bracketed instruction: "list each condition as a numbered item — Conditions embedded only in prose rationale are insufficient"; but no mandatory CONDITIONS: block present-always pattern and no enforcement note |
| C-12 | Severity discrimination | PASS | "Severity from the role's own triage" section; "A run where every finding carries the same severity label signals triage was skipped" reminder at end |
| C-13 | Risk register status lifecycle | PASS | Status column with defined vocabulary; "at least 2 distinct Status values" explicitly required |

**Score:**
- Essential: 5/5 × 60 = **60**
- Recommended: 2.5/3 × 30 = **25**
- Aspirational: 2.5/5 × 25 = **12.5**
- **Composite: 97.5** | All essential pass: YES | Golden: YES

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | All Essential | Golden |
|-----------|-----------|-------------|--------------|-----------|---------------|--------|
| **V-04** | 54 (4.5/5) | 30 (3/3) | 20 (4/5) | **104** | NO | YES |
| **V-05** | 60 (5/5) | 25 (2.5/3) | 12.5 (2.5/5) | **97.5** | YES | YES |
| V-02 | 60 (5/5) | 20 (2/3) | 7.5 (1.5/5) | 87.5 | YES | YES |
| V-03 | 60 (5/5) | 20 (2/3) | 7.5 (1.5/5) | 87.5 | YES | YES |
| V-01 | 60 (5/5) | 20 (2/3) | 5 (1/5) | 85 | YES | YES |

**Rank**: V-04 > V-05 > V-02 = V-03 > V-01

---

## Excellence Signals

**From V-04 (composite leader):**

**1. Format-error encoding beats aspiration framing.**
Naming violations as "format errors" (RULE A/B/C) rather than quality improvements forces three aspirational criteria into default-on behavior. The FORMAT ERROR PROTOCOL appendix creates a self-checking loop at the end of every run. This is the structural mechanism that separates V-04's aspirational score (4/5) from every other variation (max 1.5/5).

**2. Explicit count requirements make soft instructions checkable.**
"At least 2 cross-stage references across the full run" converts C-06 from a behavioral preference ("name it when it resurfaces") into a verifiable count. V-05 uses softer language and gets C-06 PARTIAL. Count-anchoring is what unlocks C-06 PASS.

**3. Mission Cascade TABLE upgrades exec-office from instruction to artifact.**
A structured table with Alignment column (ALIGNED/PARTIAL/GAP vocabulary) produces a machine-scannable output rather than narrative. V-04 is the only variation to provide this structure, earning the strongest C-08 pass of the round.

**From V-05 (essential integrity leader):**

**4. Anti-generic negative instruction is the strongest C-02 guard.**
"Generic findings that any role could have written indicate the persona was not loaded" is a falsification instruction — it tells the model what a failure looks like. This is more effective at defending role authenticity than positive instructions ("write in this role's voice") alone. The reason V-05 sustains C-02 PASS under natural-voice framing while V-04 drops to PARTIAL under rule density is this explicit anti-generic signal.

---

## Round 2 Diagnosis

**C-02 vs. aspirational coverage is the core trade-off of this round.** V-04 achieves the highest composite by encoding all three v2 aspirationals as format rules, but the mechanical rule density presses C-02 toward PARTIAL. V-05 defends C-02 through natural-voice framing but only reaches 2.5/5 aspirationals.

**Single-axis variations plateau at 87.5.** V-02 and V-03 both nail their target criterion but fail the other two v2 aspirationals — confirming R1's pattern that single-axis variations produce local maxima, not broad uplift.

**The synthesis prompt for R3:** Combine V-04's format-error encoding for C-11/C-12/C-13 with V-05's anti-generic negative instruction for C-02. The format rules are structural — they belong in a clear RULES section. The anti-generic guard is a single sentence that belongs in the role-loading setup. These two concerns do not interfere with each other.

---

```json
{"top_score": 104, "all_essential_pass": false, "new_patterns": ["format-error encoding turns aspirational criteria into default-on behavior by naming violations as structural errors rather than quality improvements", "explicit count requirements (at least N) convert soft behavioral instructions into verifiable checkable conditions", "anti-generic negative instruction ('generic findings indicate the persona was not loaded') is a stronger C-02 guard than natural-voice framing alone"]}
```
