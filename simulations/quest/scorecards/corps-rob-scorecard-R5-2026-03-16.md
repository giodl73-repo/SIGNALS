## Scorecard — corps-rob R5 (Rubric v5)

**Scoring key**: Essential = 12 pts each (60 total) · Recommended = 10 pts each (30 total) · Aspirational = 5 pts each (65 total) · Max = 155

---

### V-01 — Universal Zero-State Declaration Protocol

**Primary axis**: C-19 (zero-state declaration universalized across all check sections)

**Stage format**: Calibration Block + Findings + Verdict per stage. Post-stage: Calibration Errors + Role Concern Gaps + Triage Note Gaps. All three check sections carry RULE ZERO-STATE.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | `## Stage:`, ROLE line, severity-labeled findings, `VERDICT:` |
| C-02 | Role-loaded perspective | PASS | Setup reads org.yaml + .roles/; MOST CRITICAL declared per role |
| C-03 | ROB document format compliance | PASS | Header, role identity, numbered findings with severity, stage verdict all present |
| C-04 | Actionable findings (2x per stage) | PASS | Minimum 2 per stage with Owner + Resolution fields |
| C-05 | Go/No-Go in TPM stage | PASS | TPM format: `GO / NO-GO / GO WITH CONDITIONS` + `Rationale: [cite risk ID]` |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register in TPM | PASS | Risk register table with Severity, Likelihood, Mitigation, Status |
| C-08 | Exec-office cascade tracing | PASS | "At least one finding must name a specific S-office mission by name" |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No conditional itemization format rule |
| C-12 | Finding severity discrimination | PASS | Calibration Block mandates MOST CRITICAL→HIGH + LEAST CRITICAL→LOW spread; findings must match |
| C-13 | Risk register status lifecycle | PASS | Status column required; "2+ distinct values" stated |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block required before findings per stage |
| C-15 | Risk register update protocol | FAIL | TPM section: only Risk Register + Go/No-Go; no Update Protocol table |
| C-16 | Role-lens pre-declaration | FAIL | Stage format omits ROLE CONCERN block; Role Concern Gaps scan implies expectation but format doesn't mandate it |
| C-17 | Pre-commitment enforcement audit | PASS | Calibration Errors section audits PLANNED SPREAD pre-commitments; flags deviations by stage |
| C-18 | Universal per-stage triage note | FAIL | `[TRIAGE NOTE: required when spread is uniform]` — conditional, not universal |
| C-19 | Zero-deviation explicit declaration | PASS | Primary axis; RULE ZERO-STATE explicitly stated for all check sections; examples show `VIOLATIONS: NONE`, `GAPS: NONE`, `TRIAGE NOTE GAPS: NONE` |
| C-20 | Enforcement audit structured table | FAIL | Calibration Errors is prose/list; no named-column table format |
| C-21 | Named triage field vocabulary | FAIL | Triage Note is conditional and uses no labeled field vocabulary |

**Score breakdown**:
- Essential: 5/5 = **60**
- Recommended: C-07 + C-08 = **20**
- Aspirational: C-12, C-13, C-14, C-17, C-19 = 5 × 5 = **25**

**V-01 composite: 105** · All essential: YES · Golden: YES (105 ≥ 80)

---

### V-02 — Named-Column Enforcement Audit Table

**Primary axis**: C-20 (table format as formal requirement, prose prohibited) + C-19 (scoped to Enforcement Summary)

**Stage format**: Calibration Block + Findings + Verdict. TPM: Risk Register (with Status) + Update Protocol table + Go/No-Go. Post-stage: Enforcement Audit as named-column table.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | All four elements present |
| C-02 | Role-loaded perspective | PASS | Setup reads org.yaml + .roles/ |
| C-03 | ROB document format compliance | PASS | All structural elements per stage |
| C-04 | Actionable findings (2x per stage) | PASS | Owner + Resolution per finding |
| C-05 | Go/No-Go in TPM stage | PASS | `GO / NO-GO / GO WITH CONDITIONS` + risk ID citation |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register in TPM | PASS | Table with ID, Risk, Severity, Likelihood, Mitigation, Status |
| C-08 | Exec-office cascade tracing | PASS | "S-office mission by name" requirement stated |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No conditional itemization rule |
| C-12 | Finding severity discrimination | PASS | Calibration Block requires HIGH/LOW spread; findings must match |
| C-13 | Risk register status lifecycle | PASS | Status column; "2+ distinct values" |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block required per stage |
| C-15 | Risk register update protocol | PASS | Update Protocol table with Trigger Events / Owner Role / Revisit Cadence |
| C-16 | Role-lens pre-declaration | FAIL | No ROLE CONCERN block in stage format |
| C-17 | Pre-commitment enforcement audit | PASS | Enforcement Audit section required after final stage; covers Calibration Block spreads + Update Protocol |
| C-18 | Universal per-stage triage note | FAIL | Triage Note conditional (only when uniform) |
| C-19 | Zero-deviation explicit declaration | PASS | VIOLATIONS line explicitly required; "If no violations exist: write `VIOLATIONS: NONE`"; "affirmative declaration required" |
| C-20 | Enforcement audit structured table | PASS | Primary axis; FORMAT RULE states table required, prose prohibited; 4 named columns specified (Stage, Pre-Commitment Declared, Honored, Deviation) |
| C-21 | Named triage field vocabulary | FAIL | Triage Note not addressed beyond conditional note |

**Score breakdown**:
- Essential: 5/5 = **60**
- Recommended: C-07 + C-08 = **20**
- Aspirational: C-12, C-13, C-14, C-15, C-17, C-19, C-20 = 7 × 5 = **35**

**V-02 composite: 115** · All essential: YES · Golden: YES
*(Matches retroactive R4 V-02 score under v5 rubric — confirms calibration)*

---

### V-03 — Named Triage Field Vocabulary

**Primary axis**: C-21 (labeled field vocabulary as formal requirement, prose prohibited) + C-18 (universal Triage Note)

**Stage format**: Findings + Triage Note (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR, unconditional) + Verdict. No Calibration Block. TPM: Risk Register (with Status) + Go/No-Go. Post-stage: Triage Note Gaps.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | Stage header, ROLE, severity-labeled findings, VERDICT |
| C-02 | Role-loaded perspective | PASS | Setup reads org.yaml + .roles/ |
| C-03 | ROB document format compliance | PASS | All structural elements present |
| C-04 | Actionable findings (2x per stage) | PASS | Owner + Resolution per finding; minimum 2 |
| C-05 | Go/No-Go in TPM stage | PASS | TPM Go/No-Go with risk ID citation |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register in TPM | PASS | Table with Status column; "2+ distinct values" |
| C-08 | Exec-office cascade tracing | PASS | S-office mission naming requirement stated |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | Not mentioned |
| C-12 | Finding severity discrimination | PASS | HIGH DRIVER + LOW ANCHOR fields in every Triage Note require and document severity spread |
| C-13 | Risk register status lifecycle | PASS | Status: OPEN / WATCH / MITIGATED; 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | Triage Note with HIGH DRIVER / LOW ANCHOR demonstrates holistic calibration; "demonstrated HIGH-to-LOW spread" satisfies pass condition |
| C-15 | Risk register update protocol | FAIL | No Update Protocol in TPM section |
| C-16 | Role-lens pre-declaration | FAIL | No ROLE CONCERN block |
| C-17 | Pre-commitment enforcement audit | FAIL | No enforcement audit section; Triage Note Gaps audits compliance but Triage Notes are not pre-commitments |
| C-18 | Universal per-stage triage note | PASS | "required unconditionally -- present whether severity varies or is uniform"; every stage has the section |
| C-19 | Zero-deviation explicit declaration | PASS | "TRIAGE NOTE GAPS: NONE" required when scan finds no gaps; "A gap check that ends without this line leaves ambiguity" |
| C-20 | Enforcement audit structured table | FAIL | C-17 fails; C-20 not scoreable |
| C-21 | Named triage field vocabulary | PASS | Primary axis; three labels required on own lines; counter-example (failing) and passing example shown side by side; explicit prohibition stated |

**Score breakdown**:
- Essential: 5/5 = **60**
- Recommended: C-07 + C-08 = **20**
- Aspirational: C-12, C-13, C-14, C-18, C-19, C-21 = 6 × 5 = **30**

**V-03 composite: 110** · All essential: YES · Golden: YES
*(Matches retroactive R4 V-03 score under v5 rubric — confirms calibration)*

---

### V-04 — Zero-State Protocol + Named Triage Field Vocabulary

**Primary axes**: C-19 (RULE ZERO-STATE) + C-21 (RULE FIELD-LABELS) — prohibitions stated together, mutual reinforcement hypothesis

**Stage format**: Calibration Block + Findings + Triage Note (RULE FIELD-LABELS, unconditional) + Verdict. TPM: Risk Register (Status) + Go/No-Go. Post-stage: Triage Note Gaps + Calibration Gaps (new in V-04), both with RULE ZERO-STATE.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | All four elements |
| C-02 | Role-loaded perspective | PASS | Setup reads org.yaml + .roles/ |
| C-03 | ROB document format compliance | PASS | All structural elements present |
| C-04 | Actionable findings (2x per stage) | PASS | Owner + Resolution; minimum 2 |
| C-05 | Go/No-Go in TPM stage | PASS | TPM Go/No-Go with risk citation |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register in TPM | PASS | Risk register table with Status; "2+ distinct values" |
| C-08 | Exec-office cascade tracing | PASS | "Abstract references to 'strategic objectives' do not satisfy this" — named mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | Not mentioned |
| C-12 | Finding severity discrimination | PASS | Calibration Block requires HIGH/LOW pre-commitment; Triage Note HIGH DRIVER + LOW ANCHOR reinforce it |
| C-13 | Risk register status lifecycle | PASS | Status column; 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block per stage with MOST CRITICAL→HIGH / LEAST CRITICAL→LOW |
| C-15 | Risk register update protocol | FAIL | TPM only has Risk Register + Go/No-Go; no Update Protocol |
| C-16 | Role-lens pre-declaration | FAIL | No ROLE CONCERN block in stage format |
| C-17 | Pre-commitment enforcement audit | PASS | Calibration Gaps section audits Calibration Block PLANNED SPREAD pre-commitments; flags deviations |
| C-18 | Universal per-stage triage note | PASS | RULE FIELD-LABELS requires Triage Note in every stage unconditionally; all three labels required |
| C-19 | Zero-deviation explicit declaration | PASS | RULE ZERO-STATE; Triage Note Gaps: `TRIAGE NOTE GAPS: NONE`; Calibration Gaps: `CALIBRATION GAPS: NONE`; both carry explicit RULE ZERO-STATE obligations |
| C-20 | Enforcement audit structured table | FAIL | Calibration Gaps is prose/list section; no named-column table with 4 required columns |
| C-21 | Named triage field vocabulary | PASS | RULE FIELD-LABELS; `HIGH DRIVER:`, `LOW ANCHOR:`, `DISTRIBUTION FACTOR:` required as standalone labels; "prose sentences that contain the same information without these labels do not satisfy" |

**Score breakdown**:
- Essential: 5/5 = **60**
- Recommended: C-07 + C-08 = **20**
- Aspirational: C-12, C-13, C-14, C-17, C-18, C-19, C-21 = 7 × 5 = **35**

**V-04 composite: 115** · All essential: YES · Golden: YES

*Note: V-04 reaches the same composite as V-02 via different aspirational criteria (C-18 + C-21 instead of C-15 + C-20). V-04's two-rule pairing hypothesis confirmed: C-19 and C-21 coexist without compression.*

---

### V-05 — Full R5 Stack on R4 V-05 Base

**Primary axes**: All v2–v5 aspirational criteria via RULES A–K (C-11 through C-21 with the exception of C-09/C-10)

**Stage format**: ROLE CONCERN + Calibration Block + Findings + Triage Note (RULE G + RULE K) + Verdict (RULE B). TPM: Risk Register (RULE C) + Update Protocol (RULE E) + Go/No-Go (RULE B). Exec-office: Mission Cascade table. Post-stage: Enforcement Audit named-column table (RULE H + RULE J) + Enforcement Summary (RULE I). Catch-all Format Errors section (RULE I).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | All four elements; RULE format makes each explicit |
| C-02 | Role-loaded perspective | PASS | Setup reads org.yaml + .roles/; ROLE CONCERN per stage is topic-specific |
| C-03 | ROB document format compliance | PASS | All structural elements present per stage |
| C-04 | Actionable findings (2x per stage) | PASS | Owner + Resolution per finding; minimum 2 |
| C-05 | Go/No-Go in TPM stage | PASS | `GO / NO-GO / GO WITH CONDITIONS` + risk/finding ID citation |
| C-06 | Cross-stage coherence | PARTIAL | "When running --stage all, later stages *should* reference prior-stage findings... *aim for* at least 2 cross-stage references" — guidance with format, but not a RULE; 5 pts |
| C-07 | Structured risk register in TPM | PASS | Named-column risk register table (RULE C); Status required; 2+ distinct values |
| C-08 | Exec-office cascade tracing | PASS | Mission Cascade structured table: S-Office Mission / Program / Artifact/Topic / Alignment columns; "named mission" requirement; "strategic goals fails C-08" stated |
| C-09 | Inter-stage blocker detection | FAIL | No RULE for blocker detection; cross-stage coherence guidance covers escalation but not hard blockers |
| C-10 | Cross-cutting theme elevation | FAIL | Not addressed |
| C-11 | Conditional verdict itemization | PASS | RULE B; `CONDITIONS:` with numbered items (what/owner/finding ID) required when conditional; `CONDITIONS: N/A` required when unconditional |
| C-12 | Finding severity discrimination | PASS | RULE A; at least one HIGH per stage, at least one below HIGH across run; uniform severity requires RULE D or RULE G justification |
| C-13 | Risk register status lifecycle | PASS | RULE C; Status column; "at least 2 distinct status values must appear" |
| C-14 | Pre-finding severity calibration | PASS | RULE D; Calibration Block required per stage; MOST CRITICAL→HIGH / LEAST CRITICAL→LOW / PLANNED SPREAD |
| C-15 | Risk register update protocol | PASS | RULE E; Update Protocol table with Trigger Events / Owner Role / Revisit Cadence; "generic placeholders violate RULE E" |
| C-16 | Role-lens pre-declaration | PASS | RULE F; `ROLE CONCERN:` block required before Calibration Block in every stage; topic-specific sentence referencing artifact/domain; "generic role descriptions violate RULE F" |
| C-17 | Pre-commitment enforcement audit | PASS | RULE H; Enforcement Audit required covering all Calibration Block spreads (RULE D), Update Protocol (RULE E), ROLE CONCERN declarations (RULE F) |
| C-18 | Universal per-stage triage note | PASS | RULE G; Triage Note in every stage unconditionally; all three fields required; "missing Triage Note or incomplete Triage Note violates RULE G"; RULE K governs field-label format |
| C-19 | Zero-deviation explicit declaration | PASS | RULE I; applies to Enforcement Summary VIOLATIONS, Triage Note Gaps, Calibration Gaps, Format Errors section; "section that ends after confirming a clean result without printing this line violates RULE I"; Format Errors section carries it too |
| C-20 | Enforcement audit structured table | PASS | RULE J; named-column table required; prose does not satisfy; 4 named columns (Stage, Pre-Commitment Declared, Honored, Deviation); "table with unlabeled columns does not satisfy RULE J" |
| C-21 | Named triage field vocabulary | PASS | RULE K; exactly `HIGH DRIVER:` / `LOW ANCHOR:` / `DISTRIBUTION FACTOR:` required on own lines; "prose sentences that contain the same information without these field labels do not satisfy RULE K" |

**Score breakdown**:
- Essential: 5/5 = **60**
- Recommended: C-06 partial (5) + C-07 (10) + C-08 (10) = **25**
- Aspirational: C-11 through C-21 minus C-09, C-10 = 11 × 5 = **55**

**V-05 composite: 140** · All essential: YES · Golden: YES

---

## Ranking

| Rank | Variation | Composite | Golden | All Essential |
|------|-----------|-----------|--------|---------------|
| 1 | V-05 | **140** | YES | YES |
| 2 | V-02 | 115 | YES | YES |
| 2 | V-04 | 115 | YES | YES |
| 4 | V-03 | 110 | YES | YES |
| 5 | V-01 | 105 | YES | YES |

---

## Excellence Signals from V-05

**1. Rule-registry architecture**: Encoding each criterion as a named, numbered RULE (A–K) creates a first-class obligation layer. The Enforcement Audit can reference violations by rule name (`RULE D violated: leadership stage findings do not match Calibration Block`). This is structurally different from inline format instructions — the RULE names are auditable identifiers, not just prose guidance.

**2. Catch-all Format Errors protocol**: V-05 adds a Format Errors section that catches any RULE violation not already captured in the Enforcement Audit table. RULE I applies to it (`FORMAT ERRORS: NONE`). This closes the escape hatch where a format violation could be silently omitted from all audit sections — every criterion has a capture point.

**3. Dependency chain made explicit in prompt text**: "RULE J depends on RULE H; RULE K depends on RULE G" is stated both in the hypothesis and embedded in the format rules themselves (`RULE H must pass for RULE J to be scoreable`). This prevents a model from satisfying C-20 without C-17 or C-21 without C-18 by misreading rule order.

**4. Structured Mission Cascade table**: V-05 promotes the exec-office S-office mission requirement from prose to a named-column table (S-Office Mission / Program / Artifact/Topic / Alignment). This is the C-08 equivalent of what C-20 did for C-17 — the criterion moves from "names a mission" to "names a mission in a machine-scannable row."

**V-02 and V-04 tied delta explanation**: Both reach 115 via different paths. V-02 gets there via C-15 + C-20 (Update Protocol + table audit); V-04 gets there via C-18 + C-21 (universal Triage Note + named field vocabulary). Neither path dominates — they target disjoint criteria. V-05 subsumes both paths plus adds C-11, C-16, and C-21 that neither single-axis variation reached.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["rule-registry architecture: encoding each criterion as a named RULE creates auditable obligation identifiers the Enforcement Audit can reference by rule name", "catch-all Format Errors protocol: extending RULE I zero-state discipline to a post-audit section that captures any rule violation not covered by the Enforcement Audit table", "explicit dependency chain in prompt text: stating RULE J depends on RULE H and RULE K depends on RULE G prevents phantom criterion passes by making prerequisites part of the rule definition itself"]}
```
