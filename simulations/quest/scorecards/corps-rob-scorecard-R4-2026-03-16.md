## corps-rob R4 — Quest Score

### Scoring Framework (v4)

| Tier | Criteria | Points | Max |
|------|----------|--------|-----|
| Essential (C-01–C-05) | 5 | 12 each | 60 |
| Recommended (C-06–C-08) | 3 | 10 each | 30 |
| Aspirational (C-09–C-18) | 10 | 5 each | 50 |
| **Total** | | | **140** |

PASS = full credit · PARTIAL = half credit · FAIL = 0

---

### V-01 — Role-Lens Pre-Declaration

**Target**: C-16 (standalone ROLE CONCERN block as first-class artifact)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | `## Stage: [name]` headers in format template |
| C-02 | Role-loaded perspective | PASS | Loads .roles/, ROLE CONCERN requires topic-specific instantiation |
| C-03 | ROB document format compliance | PASS | Header, role identity, severity-labeled findings, verdict all in template |
| C-04 | Actionable findings | PASS | Min 2 per stage, Owner + Resolution fields required |
| C-05 | Go/No-Go in TPM | PASS | `### Go/No-Go` section with labeled verdict citing risk ID |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference requirement |
| C-07 | Structured risk register | PASS | Table with min 3 rows, 1 HIGH, Status column |
| C-08 | Exec-office cascade tracing | PASS | "name a specific S-office mission by name" |
| C-09 | Inter-stage blocker detection | FAIL | Not required |
| C-10 | Cross-cutting theme elevation | FAIL | No synthesis section |
| C-11 | Conditional verdict itemization | FAIL | No RULE B equivalent; conditions not itemized |
| C-12 | Finding severity discrimination | PASS | Calibration Block requires MOST CRITICAL→HIGH, LEAST CRITICAL→LOW, declared spread |
| C-13 | Risk register status lifecycle | PASS | Status: OPEN/WATCH/MITIGATED with 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block before findings with spread declaration |
| C-15 | Risk register update protocol | FAIL | No Update Protocol table in V-01 |
| C-16 | Role-lens pre-declaration | PASS | Standalone `### Role Concern` block before Calibration Block; topic-specific enforcement; ROLE CONCERN ENFORCEMENT appendix |
| C-17 | Pre-commitment enforcement audit | FAIL | "Role Concern Gaps" is a violation-triggered correction list, not an unconditional audit table; C-17 requires the audit even when zero violations |
| C-18 | Universal per-stage triage note | FAIL | Triage Note in Calibration Block is conditional (only when spread is uniform) |

**Score**: Essential 60/60 · Recommended 20/30 · Aspirational 20/50 = **100**

---

### V-02 — Pre-Commitment Enforcement Audit

**Target**: C-17 (post-run Enforcement Audit table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | Stage headers in format |
| C-02 | Role-loaded perspective | PASS | Reads org.yaml/.roles/ |
| C-03 | ROB document format compliance | PASS | All four elements present |
| C-04 | Actionable findings | PASS | Min 2 per stage, Owner + Resolution |
| C-05 | Go/No-Go in TPM | PASS | Labeled verdict citing risk ID |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference requirement |
| C-07 | Structured risk register | PASS | Table with Status, min 3 rows, 1 HIGH |
| C-08 | Exec-office cascade tracing | PASS | Named S-office mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not required |
| C-10 | Cross-cutting theme elevation | FAIL | No synthesis section |
| C-11 | Conditional verdict itemization | FAIL | No itemization rule for conditions |
| C-12 | Finding severity discrimination | PASS | Calibration Block declares MOST CRITICAL→HIGH, LEAST CRITICAL→LOW, spread |
| C-13 | Risk register status lifecycle | PASS | Status column with OPEN/WATCH/MITIGATED, 2+ distinct values required |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block before findings |
| C-15 | Risk register update protocol | PASS | Update Protocol table with Trigger Events, Owner Role, Revisit Cadence — all required |
| C-16 | Role-lens pre-declaration | FAIL | No standalone ROLE CONCERN block; Calibration Block lacks a role-lens pre-declaration field |
| C-17 | Pre-commitment enforcement audit | PASS | Full Enforcement Audit table (Stage/Pre-Commitment/Declared/Honored/Deviation); VIOLATIONS: NONE required even for clean runs; "A run without an Enforcement Audit section is incomplete" |
| C-18 | Universal per-stage triage note | FAIL | Triage Note only when spread is uniform (conditional) |

**Score**: Essential 60/60 · Recommended 20/30 · Aspirational 25/50 = **105**

---

### V-03 — Universal Per-Stage Triage Note

**Target**: C-18 (three-field Triage Note in every stage unconditionally)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | Stage headers in format |
| C-02 | Role-loaded perspective | PASS | Loads roles from org.yaml/.roles/ |
| C-03 | ROB document format compliance | PASS | All four elements present |
| C-04 | Actionable findings | PASS | Min 2 per stage, Owner + Resolution |
| C-05 | Go/No-Go in TPM | PASS | Labeled verdict citing risk ID |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference requirement |
| C-07 | Structured risk register | PASS | Table with Status, min 3 rows, 1 HIGH |
| C-08 | Exec-office cascade tracing | PASS | Named S-office mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not required |
| C-10 | Cross-cutting theme elevation | FAIL | No synthesis section |
| C-11 | Conditional verdict itemization | FAIL | No numbered conditions rule |
| C-12 | Finding severity discrimination | PASS | HIGH DRIVER + LOW ANCHOR fields in every Triage Note structurally enforce spread; "severity labels must reflect real triage" |
| C-13 | Risk register status lifecycle | PASS | Status column with OPEN/WATCH/MITIGATED, 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | Demonstrated HIGH-to-LOW spread (via "severity labels must reflect real triage") + universal Triage Note documenting reasoning satisfies C-14 via demonstrated-spread path |
| C-15 | Risk register update protocol | FAIL | No Update Protocol table |
| C-16 | Role-lens pre-declaration | FAIL | No ROLE CONCERN block — V-03 format omits the pre-calibration role declaration entirely |
| C-17 | Pre-commitment enforcement audit | FAIL | TRIAGE NOTE ENFORCEMENT appends a gap list — but Triage Notes are post-finding, not pre-commitment artifacts; C-17 requires auditing pre-commitment artifacts (Calibration Blocks, Update Protocols, ROLE CONCERN declarations) |
| C-18 | Universal per-stage triage note | PASS | Three-field Triage Note (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR) required in every stage; TRIAGE NOTE ENFORCEMENT requires "TRIAGE NOTE GAPS: NONE" even for clean runs |

**Score**: Essential 60/60 · Recommended 20/30 · Aspirational 20/50 = **100**

---

### V-04 — Role-Lens Pre-Declaration + Universal Triage Note

**Target**: C-16 + C-18 (stage bookend pair)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | Stage headers in format |
| C-02 | Role-loaded perspective | PASS | RULE OPEN requires topic-specific role instantiation |
| C-03 | ROB document format compliance | PASS | All four elements present |
| C-04 | Actionable findings | PASS | Min 2 per stage, Owner + Resolution |
| C-05 | Go/No-Go in TPM | PASS | Labeled verdict citing risk ID |
| C-06 | Cross-stage coherence | FAIL | No cross-stage reference requirement |
| C-07 | Structured risk register | PASS | Table with Status, min 3 rows, 1 HIGH |
| C-08 | Exec-office cascade tracing | PASS | Named S-office mission required |
| C-09 | Inter-stage blocker detection | FAIL | Not required |
| C-10 | Cross-cutting theme elevation | FAIL | No synthesis section |
| C-11 | Conditional verdict itemization | FAIL | No RULE B equivalent |
| C-12 | Finding severity discrimination | PASS | ROLE CONCERN frames the HIGH anchor; RULE CLOSE's HIGH DRIVER + LOW ANCHOR enforce spread documentation |
| C-13 | Risk register status lifecycle | PASS | Status column with OPEN/WATCH/MITIGATED |
| C-14 | Pre-finding severity calibration | PASS | Calibration Block after ROLE CONCERN, before findings, with MOST CRITICAL→HIGH, LEAST CRITICAL→LOW, PLANNED SPREAD |
| C-15 | Risk register update protocol | FAIL | No Update Protocol table in V-04 |
| C-16 | Role-lens pre-declaration | PASS | RULE OPEN — standalone ROLE CONCERN block before Calibration Block; topic-specific enforcement; FORMAT ERROR PROTOCOL if violated |
| C-17 | Pre-commitment enforcement audit | FAIL | FORMAT ERROR PROTOCOL is violation-triggered only (appends section only when RULE OPEN or RULE CLOSE violated); C-17 requires unconditional audit even with zero violations |
| C-18 | Universal per-stage triage note | PASS | RULE CLOSE — all three fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR) required in every stage; FORMAT ERROR PROTOCOL if violated |

**Score**: Essential 60/60 · Recommended 20/30 · Aspirational 25/50 = **105**

---

### V-05 — Full R4 Stack (RULES A-H)

**Target**: C-11 through C-18 (complete v2–v4 aspirational coverage)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage identity and labeling | PASS | Stage headers in format |
| C-02 | Role-loaded perspective | PASS | RULE F requires topic-specific ROLE CONCERN grounded in loaded role's lens |
| C-03 | ROB document format compliance | PASS | All four elements in format template |
| C-04 | Actionable findings | PASS | Min 2 per stage, Owner + Resolution |
| C-05 | Go/No-Go in TPM | PASS | Go/No-Go section with RULE B CONDITIONS itemization |
| C-06 | Cross-stage coherence | PARTIAL | "later stages should reference" + explicit format provided + "aim for at least 2" — strong signal but "should/aim" language does not constitute a hard requirement |
| C-07 | Structured risk register | PASS | RULE C — Status column, 2+ distinct values, min 3 rows, 1 HIGH |
| C-08 | Exec-office cascade tracing | PASS | Mission Cascade table with named S-office mission required; "strategic goals fails C-08" |
| C-09 | Inter-stage blocker detection | FAIL | No explicit inter-stage blocker rule; cross-stage coherence encourages references but not blocker identification |
| C-10 | Cross-cutting theme elevation | FAIL | No cross-cutting themes section or rule |
| C-11 | Conditional verdict itemization | PASS | RULE B — numbered items with what/owner/finding-ID when conditional; CONDITIONS: N/A when unconditional |
| C-12 | Finding severity discrimination | PASS | RULE A — at least 1 HIGH per stage, at least 1 below HIGH across run; RULE D justifies uniformity when needed |
| C-13 | Risk register status lifecycle | PASS | RULE C — Status column with OPEN/WATCH/MITIGATED, 2+ distinct values |
| C-14 | Pre-finding severity calibration | PASS | RULE D — Calibration Block before findings with MOST CRITICAL→HIGH, LEAST CRITICAL→LOW, PLANNED SPREAD; Triage Note in Calibration Block when uniform |
| C-15 | Risk register update protocol | PASS | RULE E — Update Protocol table with Trigger Events, Owner Role, Revisit Cadence; topic-specific values required |
| C-16 | Role-lens pre-declaration | PASS | RULE F — standalone ROLE CONCERN block before Calibration Block in every stage; topic-specific; violation captured in RULE H audit |
| C-17 | Pre-commitment enforcement audit | PASS | RULE H — Enforcement Audit table covering all RULE D spreads, RULE E Update Protocol, and RULE F ROLE CONCERN declarations; Stage/Pre-Commitment/Declared/Honored/Deviation; VIOLATIONS: NONE required even for clean runs |
| C-18 | Universal per-stage triage note | PASS | RULE G — three fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR) required in every stage unconditionally; missing or placeholder fields violate RULE G |

**Score**: Essential 60/60 · Recommended 25/30 · Aspirational 40/50 = **125**

---

### Summary Scorecard

| Variation | Target | Essential | Recommended | Aspirational | Composite | All Essential | Rank |
|-----------|--------|-----------|-------------|--------------|-----------|---------------|------|
| V-05 | C-11–C-18 | 60 | 25 | 40 | **125** | YES | #1 |
| V-02 | C-17 | 60 | 20 | 25 | **105** | YES | #2 |
| V-04 | C-16+C-18 | 60 | 20 | 25 | **105** | YES | #2 |
| V-01 | C-16 | 60 | 20 | 20 | **100** | YES | #4 |
| V-03 | C-18 | 60 | 20 | 20 | **100** | YES | #4 |

All five variations clear the golden threshold of 80.

---

### Criterion Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Conditional itemization | — | — | — | — | PASS |
| C-12 Severity discrimination | PASS | PASS | PASS | PASS | PASS |
| C-13 Status lifecycle | PASS | PASS | PASS | PASS | PASS |
| C-14 Pre-finding calibration | PASS | PASS | PASS | PASS | PASS |
| C-15 Update protocol | — | PASS | — | — | PASS |
| C-16 Role-lens pre-declaration | PASS | — | — | PASS | PASS |
| C-17 Enforcement audit | — | PASS | — | — | PASS |
| C-18 Universal triage note | — | — | PASS | PASS | PASS |

**Observation**: C-11 (conditional itemization) is only reached by V-05 — no single-axis R4 variation targets it because it was a v2 criterion stabilized in R1. V-05 inherits it from the R3 V-05 base (RULE B). C-17 is the discriminating criterion between V-02 and V-04: both score 105, but V-02 hits C-15+C-17 while V-04 hits C-16+C-18.

---

### Excellence Signals from V-05

**E-01 — Named rule coverage map**
Each criterion is encoded as a numbered RULE (A–H) targeting a non-overlapping structural location: RULE A governs finding generation, RULE B governs verdict formatting, RULE C governs the risk register, RULE D governs pre-finding calibration, RULE E governs the register update protocol, RULE F governs stage opening, RULE G governs stage closing, RULE H governs the post-run meta-audit. Giving each criterion a named rule eliminates ambiguity about which output location satisfies which requirement and creates explicit violation labels for the enforcement layer.

**E-02 — Enforcement Audit as unconditional meta-layer**
RULE H requires the Enforcement Audit table even when zero violations exist. This is the structural property that distinguishes C-17 from earlier gap-listing mechanisms (V-01's "Role Concern Gaps", V-03's "Triage Note Gaps", V-04's "Format Errors"): those three are violation-triggered. RULE H fires unconditionally, making pre-commitments falsifiable rather than merely advisable. The self-auditing obligation also has a secondary effect — it makes the model more deliberate when declaring pre-commitments in Calibration Blocks and ROLE CONCERN sections, because it knows it must verify them.

**E-03 — Stage bookend pair creates per-stage intent-and-result record**
RULE F (ROLE CONCERN) opens each stage with a pre-commitment declaration of what the loaded role most fears about this specific topic. RULE G (Triage Note) closes the finding zone with a calibration result documenting how severity was distributed and why. Together they bracket every stage: ROLE CONCERN commits the lens before findings begin; the Triage Note audits the calibration decision after findings end. The two rules occupy non-overlapping positions (pre-calibration vs. post-findings) and serve non-overlapping purposes (intent vs. result), so combining them in V-04 and V-05 produces additive coverage without format compression.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["named-rule coverage map: encoding each criterion as a non-overlapping structural RULE creates explicit violation labels and prevents criterion bleed across output locations", "enforcement audit as unconditional meta-layer: post-run self-audit table fires even with zero violations, making pre-commitments falsifiable and increasing calibration deliberateness upstream"]}
```
