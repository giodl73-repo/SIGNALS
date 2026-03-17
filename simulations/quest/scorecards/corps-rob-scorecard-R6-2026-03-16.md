## corps-rob R6 Scoring — v6 Rubric

---

### Scoring Key

| Tier | Count | Points Each | Pool |
|------|-------|-------------|------|
| Essential (C-01–C-05) | 5 | 12 | 60 |
| Recommended (C-06–C-08) | 3 | 10 | 30 |
| Aspirational (C-09–C-24) | 16 | 5 | 80 |
| **Max composite** | | | **170** |

---

## V-01 — Post-Stage Role-Concern Gap Scan

**Mechanism:** ROLE CONCERN GAPS as a mandatory post-stage section; absence = format error; RULE ZERO-STATE applied; Triage Note Gaps also required after Role Concern Gaps.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Stage identity and labeling | PASS | Stage format explicitly requires `## Stage: [stage-name]` |
| C-02 | Role-loaded perspective | PASS | ROLE CONCERN block required per stage — topic-specific fear before findings |
| C-03 | ROB document format | PASS | Stage header, role identity, findings with severity, verdict all required |
| C-04 | Actionable findings | PASS | Owner and Resolution fields specified per finding; min 2 per stage |
| C-05 | Go/No-Go in TPM | PASS | Go/No-Go section specified in TPM format |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference instruction or mechanism |
| C-07 | Structured risk register | PASS | Full table with ID, Risk, Severity, Likelihood, Mitigation, Status |
| C-08 | Exec-office cascade tracing | PASS | "At least one finding must name a specific S-office mission by name" |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No conditional itemization rule |
| C-12 | Finding severity discrimination | PASS | "severity must match planned spread" forces HIGH + non-HIGH per stage |
| C-13 | Risk register status lifecycle | PASS | Status column with OPEN / WATCH / MITIGATED, 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block required before findings; MOST CRITICAL → HIGH, LEAST CRITICAL → LOW |
| C-15 | Risk register update protocol | FAIL | No Update Protocol in TPM format |
| C-16 | Role-lens pre-declaration | PASS | Standalone ROLE CONCERN block before Calibration Block, topic-specific |
| C-17 | Pre-commitment enforcement audit | PASS | `## Calibration Errors` section audits declared spreads; flags deviations |
| C-18 | Universal per-stage triage note | FAIL | Triage Note only required "when spread is uniform" — conditional, not universal |
| C-19 | Zero-deviation explicit declaration | PASS | RULE ZERO-STATE: explicit `: NONE` required in all audit sections on clean result |
| C-20 | Enforcement audit structured table | FAIL | Calibration Errors is a labeled section, not a named-column table |
| C-21 | Named triage field vocabulary | FAIL | HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR not specified |
| C-22 | Post-stage role-concern gap scan | PASS | ROLE CONCERN GAPS section mandatory; zero-state required; absence = format error |
| C-23 | Post-stage triage note gap scan | PASS | TRIAGE NOTE GAPS required after Role Concern Gaps; zero-state applies |
| C-24 | Multi-type post-stage audit suite | PASS | Calibration Errors + Role Concern Gaps + Triage Note Gaps — 3 distinct scopes |

**Aspirational passing:** C-12, C-13, C-14, C-16, C-17, C-19, C-22, C-23, C-24 = 9 × 5 = 45

```
Composite = 60 + 20 + 45 = 125
```

---

## V-02 — Post-Stage Triage Note Gap Scan with Field-Level Compliance

**Mechanism:** Universal Triage Note with named fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR); TRIAGE NOTE GAPS mandatory section checking field-level compliance (absent section, missing field, placeholder content); ROLE CONCERN GAPS also required.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Stage identity and labeling | PASS | `## Stage: [stage-name]` required |
| C-02 | Role-loaded perspective | PASS | ROLE line + calibration ensures role perspective in findings |
| C-03 | ROB document format | PASS | Stage header, role, findings, verdict present |
| C-04 | Actionable findings | PASS | Owner + Resolution per finding; min 2 per stage |
| C-05 | Go/No-Go in TPM | PASS | Specified in TPM format |
| C-06 | Cross-stage coherence | FAIL | No cross-stage instruction |
| C-07 | Structured risk register | PASS | Full table with severity, likelihood, mitigation, status |
| C-08 | Exec-office cascade tracing | PASS | "At least one finding must name a specific S-office mission" |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No conditional itemization rule |
| C-12 | Finding severity discrimination | PASS | Calibration Block forces HIGH-to-LOW spread via PLANNED SPREAD |
| C-13 | Risk register status lifecycle | PASS | Status column required in risk register |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block before findings |
| C-15 | Risk register update protocol | FAIL | No Update Protocol in V-02 TPM format |
| C-16 | Role-lens pre-declaration | FAIL | Stage format shows Calibration → Findings → Triage Note; no standalone ROLE CONCERN block |
| C-17 | Pre-commitment enforcement audit | PASS | TRIAGE NOTE GAPS section audits C-18 pre-commitment (triage note obligation) |
| C-18 | Universal per-stage triage note | PASS | "Every stage must include a Triage Note section… unconditionally" |
| C-19 | Zero-deviation explicit declaration | PASS | Zero-state protocol explicitly stated for TRIAGE NOTE GAPS and ROLE CONCERN GAPS |
| C-20 | Enforcement audit structured table | FAIL | No named-column table; sections are labeled prose |
| C-21 | Named triage field vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR — all three required with explicit labels |
| C-22 | Post-stage role-concern gap scan | PASS | ROLE CONCERN GAPS section mandatory after Triage Note Gaps |
| C-23 | Post-stage triage note gap scan | PASS | TRIAGE NOTE GAPS mandatory with three failure conditions (a/b/c) including field-level |
| C-24 | Multi-type post-stage audit suite | FAIL | Only 2 audit sections (TRIAGE NOTE GAPS + ROLE CONCERN GAPS); no third distinct dimension |

**Aspirational passing:** C-12, C-13, C-14, C-17, C-18, C-19, C-21, C-22, C-23 = 9 × 5 = 45

```
Composite = 60 + 20 + 45 = 125
```

---

## V-03 — Multi-Type Post-Stage Audit Suite

**Mechanism:** RULE AUDIT-SUITE as an explicit named format requirement; three independent post-stage sections (Calibration Compliance, Role Concern Compliance, Triage Note Compliance) each with own scope, zero-state, and gaps list; anti-patterns named ("merged section does not satisfy", "same dimension three times does not satisfy").

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Stage identity and labeling | PASS | Stage header in format |
| C-02 | Role-loaded perspective | PASS | ROLE line + role orientation phrase in each stage |
| C-03 | ROB document format | PASS | All four structural elements present |
| C-04 | Actionable findings | PASS | Owner + Resolution specified |
| C-05 | Go/No-Go in TPM | PASS | Go/No-Go section in TPM |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register | PASS | Table with severity, likelihood, mitigation, status |
| C-08 | Exec-office cascade tracing | PASS | Named S-office mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No conditional itemization rule |
| C-12 | Finding severity discrimination | PASS | PLANNED SPREAD in Calibration Block forces varied severity |
| C-13 | Risk register status lifecycle | PASS | Status column in risk register |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block required before findings |
| C-15 | Risk register update protocol | PASS | Update Protocol table with Trigger Events, Owner Role, Revisit Cadence specified |
| C-16 | Role-lens pre-declaration | FAIL | Stage format: ROLE → Calibration → Findings → Verdict; no standalone ROLE CONCERN block |
| C-17 | Pre-commitment enforcement audit | PASS | Calibration Compliance section audits declared spreads — satisfies C-17 minimum |
| C-18 | Universal per-stage triage note | FAIL | Calibration Block has "[TRIAGE NOTE: required when spread is uniform]" — conditional only |
| C-19 | Zero-deviation explicit declaration | PASS | Each suite section carries explicit zero-state per RULE AUDIT-SUITE |
| C-20 | Enforcement audit structured table | FAIL | No named-column Enforcement Audit table; suite sections are labeled prose |
| C-21 | Named triage field vocabulary | FAIL | No HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR in V-03 format |
| C-22 | Post-stage role-concern gap scan | PASS | Role Concern Compliance section in the audit suite scans per-stage compliance |
| C-23 | Post-stage triage note gap scan | PASS | Triage Note Compliance section in the audit suite scans per-stage compliance |
| C-24 | Multi-type post-stage audit suite | PASS | RULE AUDIT-SUITE: Calibration + Role Concern + Triage Note = 3 distinct scopes; anti-patterns named |

**Aspirational passing:** C-12, C-13, C-14, C-15, C-17, C-19, C-22, C-23, C-24 = 9 × 5 = 45

```
Composite = 60 + 20 + 45 = 125
```

---

## V-04 — Role-Concern Gap Scan + Triage Note Gap Scan (Companion)

**Mechanism:** RULE BOOKEND-AUDIT names both gap-scan sections as companions; RULE ZERO-STATE for all audit sections; per-stage ROLE CONCERN block (C-16); per-stage Universal Triage Note with named fields (C-18, C-21); Calibration Errors also required, providing the natural third audit dimension.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Stage identity and labeling | PASS | Stage header in format |
| C-02 | Role-loaded perspective | PASS | ROLE CONCERN block required per stage; topic-specific |
| C-03 | ROB document format | PASS | All four elements present |
| C-04 | Actionable findings | PASS | Owner + Resolution; min 2 per stage |
| C-05 | Go/No-Go in TPM | PASS | Specified |
| C-06 | Cross-stage coherence | FAIL | Not mentioned |
| C-07 | Structured risk register | PASS | Full table, minimum 3 rows, at least 1 HIGH, status values |
| C-08 | Exec-office cascade tracing | PASS | Named S-office mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not mentioned |
| C-10 | Cross-cutting theme elevation | FAIL | Not mentioned |
| C-11 | Conditional verdict itemization | FAIL | No RULE B equivalent |
| C-12 | Finding severity discrimination | PASS | Severity must match declared spread; spread forces HIGH + non-HIGH |
| C-13 | Risk register status lifecycle | PASS | Status column required |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block before findings |
| C-15 | Risk register update protocol | FAIL | TPM format shows Risk Register + Go/No-Go only; no Update Protocol table |
| C-16 | Role-lens pre-declaration | PASS | Standalone ROLE CONCERN block in stage format, before Calibration Block |
| C-17 | Pre-commitment enforcement audit | PASS | `## Calibration Errors` required section — audits calibration spread pre-commitment |
| C-18 | Universal per-stage triage note | PASS | Triage Note with all three fields required unconditionally in stage format |
| C-19 | Zero-deviation explicit declaration | PASS | RULE ZERO-STATE: `: NONE` required in all audit and gap-check sections |
| C-20 | Enforcement audit structured table | FAIL | No named-column enforcement table |
| C-21 | Named triage field vocabulary | PASS | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR required with field labels |
| C-22 | Post-stage role-concern gap scan | PASS | ROLE CONCERN GAPS mandatory per RULE BOOKEND-AUDIT; absence = format error |
| C-23 | Post-stage triage note gap scan | PASS | TRIAGE NOTE GAPS mandatory per RULE BOOKEND-AUDIT; field-level failure codes (a/b/c) |
| C-24 | Multi-type post-stage audit suite | PASS | Calibration Errors + Role Concern Gaps + Triage Note Gaps = 3 independent sections with distinct scopes |

**Aspirational passing:** C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-24 = 11 × 5 = 55

```
Composite = 60 + 20 + 55 = 135
```

---

## V-05 — Full R6 Stack (RULES A–N)

**Mechanism:** Fourteen named structural rules covering all v2–v6 aspirational criteria; rule dependencies declared (RULE J requires RULE H; RULE K requires RULE G; RULE N requires RULE H + RULE L + RULE M); suite emergence: RULE L + RULE M + RULE D's Calibration Errors satisfy RULE N without a separate mechanism; FORMAT ERROR PROTOCOL catch-all for violations not captured by named audit sections.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Stage identity and labeling | PASS | Stage format: `## Stage: [stage-name]` |
| C-02 | Role-loaded perspective | PASS | RULE F: ROLE CONCERN block required, topic-specific |
| C-03 | ROB document format | PASS | All four structural elements required |
| C-04 | Actionable findings | PASS | Owner + Resolution per finding; min 2 per stage implied by spread requirements |
| C-05 | Go/No-Go in TPM | PASS | Go/No-Go section in TPM format with CONDITIONS: N/A or numbered items |
| C-06 | Cross-stage coherence | PASS | Explicit: "Aim for at least 2 cross-stage references… [prior stage] F-[N]: confirm / escalate / contradict"; format provided |
| C-07 | Structured risk register | PASS | Table with ID, Risk, Severity, Likelihood, Mitigation, Status — RULE C enforces |
| C-08 | Exec-office cascade tracing | PASS | Mission Cascade table required; named S-office mission; "strategic goals" fails |
| C-09 | Inter-stage blocker detection | FAIL | No dedicated rule |
| C-10 | Cross-cutting theme elevation | FAIL | No synthesis/themes section required |
| C-11 | Conditional verdict itemization | PASS | RULE B: numbered items required for conditional verdicts; `CONDITIONS: N/A` for unconditional |
| C-12 | Finding severity discrimination | PASS | RULE A: severity must vary per stage; at least one HIGH per stage; at least one below HIGH across run |
| C-13 | Risk register status lifecycle | PASS | RULE C: Status column required; 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | RULE D: Calibration Block before findings; spread matching required |
| C-15 | Risk register update protocol | PASS | RULE E: Update Protocol table with Trigger Events, Owner Role, Revisit Cadence |
| C-16 | Role-lens pre-declaration | PASS | RULE F: ROLE CONCERN block required as first named section; generic descriptions violate |
| C-17 | Pre-commitment enforcement audit | PASS | RULE H: Enforcement Audit required after final stage; covers Role Concern + Calibration + Update Protocol |
| C-18 | Universal per-stage triage note | PASS | RULE G: Triage Note required in every stage unconditionally; all three fields required |
| C-19 | Zero-deviation explicit declaration | PASS | RULE I: explicit zero-state in all audit/check sections including VIOLATIONS, CALIBRATION ERRORS, TRIAGE NOTE GAPS, ROLE CONCERN GAPS, FORMAT ERRORS |
| C-20 | Enforcement audit structured table | PASS | RULE J: Enforcement Audit must be a named-column table (Stage / Pre-Commitment Declared / Honored / Deviation) |
| C-21 | Named triage field vocabulary | PASS | RULE K: exactly `HIGH DRIVER:`, `LOW ANCHOR:`, `DISTRIBUTION FACTOR:` required |
| C-22 | Post-stage role-concern gap scan | PASS | RULE L: ROLE CONCERN GAPS section mandatory; absence = format violation; zero-state per RULE I |
| C-23 | Post-stage triage note gap scan | PASS | RULE M: TRIAGE NOTE GAPS mandatory with field-level failure codes (a/b/c) |
| C-24 | Multi-type post-stage audit suite | PASS | RULE N: RULE L + RULE M + RULE D's Calibration Errors = 3 independent sections with distinct scopes; scope diversity stated |

**Aspirational passing:** C-11 through C-24 (all 14) = 14 × 5 = 70

```
Composite = 60 + 30 + 70 = 160
```

---

## Summary Rankings

| Rank | Variation | Score | All Essential | Key Delta |
|------|-----------|-------|---------------|-----------|
| 1 | **V-05** | **160** | YES | RULES A–N: all 14 aspirational C-11–C-24; all 3 recommended |
| 2 | **V-04** | **135** | YES | +C-16+C-18+C-21 over V-01; C-24 from natural triple-section structure |
| 3 | **V-01** | **125** | YES | C-16+C-22+C-23+C-24; missing C-18, C-21, C-15 |
| 3 | **V-02** | **125** | YES | C-18+C-21+C-22+C-23; missing C-16, C-24 (only 2 audit sections) |
| 3 | **V-03** | **125** | YES | C-15+C-22+C-23+C-24; missing C-16, C-18, C-21 |

---

## Excellence Signals — V-05

**1. Named rule system with dependency declarations**
RULE J requires RULE H; RULE K requires RULE G; RULE N requires RULE H + RULE L + RULE M. Declaring dependency chains in the prompt means a model cannot satisfy a dependent criterion without satisfying its preconditions. This eliminates partial-compliance edge cases (e.g., a named-field triage note in a run that has no triage notes at all).

**2. Suite emergence rather than suite mandate**
RULE N is satisfied by the logical combination of three existing rules (RULE L + RULE M + RULE D's Calibration Errors) rather than requiring a separate standalone audit-suite instruction. The suite is an emergent property of three independently required mechanisms — the most structurally stable form of C-24 coverage.

**3. FORMAT ERROR PROTOCOL catch-all**
A dedicated `## Format Errors` section appended after the named audit sections captures any RULE violation not already recorded by Calibration Errors, Role Concern Gaps, or Triage Note Gaps. This closes the gap where a rule violation might not have its own dedicated audit section, making the format self-checking for the full RULES A–N surface area.

**4. CONDITIONS: N/A for unconditional verdicts**
RULE B requires `CONDITIONS: N/A` explicitly when a verdict is unconditional. This prevents silence from being misread as missing itemization — the same zero-state pattern from RULE I applied to conditional itemization.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["Named rule system with dependency declarations (RULE J requires RULE H, RULE K requires RULE G, RULE N requires RULE H+L+M) — dependency chains in the prompt prevent partial-compliance edge cases where a dependent criterion is satisfied without its preconditions", "Suite emergence: C-24 satisfied by three independently required rules (RULE L + RULE M + RULE D Calibration Errors) rather than a standalone audit-suite mandate — most structurally stable form of coverage", "FORMAT ERROR PROTOCOL catch-all section appended after named audit sections captures any rule violation not already recorded by the three dedicated audit mechanisms — closes the gap where a rule has no dedicated post-stage section"]}
```
