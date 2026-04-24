## R14 Scorecard — campaign-behavior (v12 rubric)

### Criteria Key

**Essential (50 pts):** C-01–C-05 @ 10 pts each
**Recommended (30 pts):** C-06–C-08 @ 10 pts each
**Aspirational (10 pts):** passed/31 × 10, rounded

---

### V-01 — Remediation Tiering in Field 7

**Essential criteria:**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 All 5 sub-skills | PASS | Phases 1–5 all present with tables, EXIT CRITERIA, clean-zone clauses |
| C-02 Blast radius ranking | PASS | Tiebreaker protocol declared in CONSOLIDATE header; ranking by blast radius stated |
| C-03 Spec gaps section | PASS | Dedicated **Spec gaps** section in CONSOLIDATE |
| C-04 Contract violations section | PASS | Dedicated **Contract violations** section with producer/consumer |
| C-05 Lifecycle exception paths | PASS | Ph4 combined exception table + sub-cases table present |

**Recommended criteria:**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Blast radius label per finding | PASS | Field 3 in every block carries wide/medium/narrow |
| C-07 Confirmation status per finding | PASS | Field 6 uses CONFIRMED/RUNTIME ANOMALY format |
| C-08 Sub-skill attribution | PASS | Field 2 names source phase in every block |

**Aspirational criteria (31):**

All criteria C-09–C-39 examined. Key checks:

- **C-19 7-field block:** Field 7 restructured as `spec: [...] | contract: [...] | implementation: [...]` — still 7 labeled fields. PASS
- **C-37 Q8 gate:** V-01 adds a 4th check (remediation-tier completeness) — the three required dimensions are preserved and extended. PASS
- **C-38 Exception sub-tables:** Ph1, Ph2, Ph3, Ph5 each have exception path sub-tables with named failure categories. PASS
- **C-39 I-NN inertia inventory:** I-NN table in Phase 0, locked; Q5 references I-NN codes by format `Finding [N] overrides I-[N]`. PASS
- **C-32 VALIDITY RULES:** Co-located with EXECUTIVE SUMMARY write instruction, explicit INVALID language for both C-30 and C-31 domains. PASS
- **C-34 Q2 EXECUTIVE SUMMARY preview:** Q2 explicitly previews inline citation format for EXECUTIVE SUMMARY bullets. PASS
- **C-36 Per-phase T-NN exit gates:** All 5 phases have T-NN resolution check with chain/resolved/miss counts. PASS

All 31/31 aspirational criteria pass.

**Score: 50 + 30 + (31/31 × 10) = 50 + 30 + 10 = 90**

---

### V-02 — Meta-Finding Elevation (M-NN)

**Essential:** All 5 pass — same structural base as V-01. PASS × 5

**Recommended:** All 3 pass. PASS × 3

**Aspirational (31):**

Key checks:

- **C-19 7-field block:** M-NN blocks have 7 numbered, labeled fields (Name/Source/Blast radius/Severity/SYSTEMIC/Classification/What must change). F-NN blocks unchanged. PASS
- **C-31 EXECUTIVE SUMMARY inline evidence:** VALIDITY RULES rule 2 covers both F-NN (`CONFIRMED -- evidence: [...]`) and M-NN (`meta-finding: I-NN inventory miss`). M-NN items are not CONFIRMED classifications — C-31's constraint applies to F-NN slots; M-NN format is a distinct well-structured token. PASS
- **C-37 Q8 gate:** Audits F-NN and M-NN blocks across all 3 required dimensions. PASS
- **C-38:** All four trace phases have exception sub-tables. PASS
- **C-39:** I-NN table locked at Phase 0 close; Q5 assigns M-NN codes to I-NN inventory misses by code reference. PASS
- **C-32 VALIDITY RULES:** EXECUTIVE SUMMARY has VALIDITY RULES co-located with rejection language for both C-30 and C-31 domains. PASS
- **C-34 Q2 preview:** Q2 previews EXECUTIVE SUMMARY inline citation compliance before section is written. PASS

All 31/31 pass.

**Score: 50 + 30 + 10 = 90**

---

### V-03 — H-NN Hypothesis Pre-Declaration

**Essential:** All 5 pass. PASS × 5

**Recommended:** All 3 pass. PASS × 3

**Aspirational (31):**

Key checks:

- **C-18 n≥3 calibration questions:** Q1–Q6, QH, Q7, Q8 = 9 questions total. PASS
- **C-25 Q6 sequence integrity gate:** Q6 present and intact; QH is an additional gate after Q6, not a replacement. PASS
- **C-32 VALIDITY RULES:** QH fires before EXECUTIVE SUMMARY is written; VALIDITY RULES is co-located with the EXECUTIVE SUMMARY write instruction, not with QH. No collision. PASS
- **C-34 Q2 preview:** Q2 explicitly previews EXECUTIVE SUMMARY inline citation compliance. QH fires after Q6 — Q2's preview scope is unaffected. PASS
- **C-38:** All four trace phases have exception sub-tables. PASS
- **C-39:** I-NN table + Q5 references I-NN codes by format. Meta-findings prose uses `I-NN inventory miss` language. PASS

Specific structural risk audited: QH between Q6 and EXECUTIVE SUMMARY does not duplicate Q2 scope (Q2 checks classification citations; QH checks hypothesis outcomes). VALIDITY RULES gate fires at EXECUTIVE SUMMARY write site, after QH. Order is: Q6 → QH → EXECUTIVE SUMMARY (VALIDITY RULES) → Q7 → CONSOLIDATE → Q8 → VERDICT. No ordering collision.

All 31/31 pass.

**Score: 50 + 30 + 10 = 90**

---

### V-04 — V-01 + V-02 (Remediation Tiers + M-NN)

**Essential:** All 5 pass. PASS × 5

**Recommended:** All 3 pass. PASS × 3

**Aspirational (31):**

Key checks:

- **C-19:** F-NN blocks have 7 fields; M-NN blocks have 7 fields. Both use three-tier field 7 (`spec/contract/implementation`). PASS
- **C-37 Q8 gate:** 4 checks applied to both F-NN and M-NN blocks; M-NN remediation tier check uses appropriate M-NN-specific guidance ("add assumption to I-NN inventory; add spec clause"). PASS
- **C-31:** VALIDITY RULES rule 2 covers F-NN inline evidence format and M-NN meta-finding token. PASS
- **C-38:** All four phases have exception sub-tables. PASS
- **C-39:** I-NN table + Q5 forward-verification by code. PASS
- **Interaction check (V-01 × V-02):** Field 7 tiers apply to M-NN blocks — meta-findings now have spec/contract/implementation tiers (`spec: add to I-NN inventory; implementation: add guard`). Structurally orthogonal — META-FINDINGS section is independent of finding-block field structure. No degradation.

All 31/31 pass.

**Score: 50 + 30 + 10 = 90**

---

### V-05 — Full Integration: V-01 + V-02 + V-03

**Essential:** All 5 pass. PASS × 5

**Recommended:** All 3 pass. PASS × 3

**Aspirational (31):**

Key checks:

- **C-19:** F-NN and M-NN blocks both have 7 labeled, numbered fields with three-tier field 7. PASS
- **C-18:** Q1–Q6 + QH + Q7 + Q8 = 9 calibration questions. PASS
- **C-25 Q6 gate:** Q6 intact; QH is additive. PASS
- **C-32 VALIDITY RULES:** Co-located with EXECUTIVE SUMMARY write instruction. QH fires before EXECUTIVE SUMMARY, not at the write site. No collision. PASS
- **C-34 Q2 preview:** Q2 previews EXECUTIVE SUMMARY compliance before QH fires. PASS
- **C-37 Q8 gate:** 4-check audit (7-field, T-NN, classification, remediation-tier) applied to F-NN and M-NN. PASS
- **C-38:** All four trace phases (1, 2, 3, 5) have exception path sub-tables. PASS
- **C-39:** I-NN table in Phase 0 locked; Q5 references I-NN codes by `Finding [N] overrides I-[N]` format; undeclared overrides get M-NN codes. PASS
- **Hypothesis outcomes in CONSOLIDATE:** New section `**Hypothesis outcomes:**` lists each H-NN result — does not conflict with any existing CONSOLIDATE sections (spec gaps, contract violations, etc.). PASS
- **VERDICT H-NN/M-NN citations:** VERDICT names `Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence` and `Meta-findings: [N] undeclared assumptions surfaced`. PASS

QH/VALIDITY RULES ordering audit (flagged in R14 variation notes): Order confirmed as Q6 → QH → EXECUTIVE SUMMARY (VALIDITY RULES at write site) → Q7 → CONSOLIDATE → Q8 → VERDICT. QH operates on hypothesis outcomes (H-NN), VALIDITY RULES operates on EXECUTIVE SUMMARY bullet format (C-30/C-31). Separate scopes, correct order. No interaction degradation.

All 31/31 pass.

**Score: 50 + 30 + 10 = 90**

---

### Rankings

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50 | 30 | 10 (31/31) | **90** |
| V-02 | 50 | 30 | 10 (31/31) | **90** |
| V-03 | 50 | 30 | 10 (31/31) | **90** |
| V-04 | 50 | 30 | 10 (31/31) | **90** |
| V-05 | 50 | 30 | 10 (31/31) | **90** |

All five variations maintain the 31/31 baseline from R13 V-05. R14's three axes (remediation tiering, M-NN elevation, H-NN pre-declaration) are structurally independent — none break any existing criterion, and V-05 confirms full composability. The new patterns belong in the next rubric cycle.

---

### Excellence Signals

From V-05 (representative of the full R14 stack):

1. **Remediation-tier ownership separation as Q8's 4th structural check** — V-01/V-04/V-05 make field 7 mechanically auditable rather than prose-evaluated; Q8's 4th check enforces `spec/contract/implementation` sub-field completeness, converting fix-layer assignment from guidance to gate
2. **M-NN items enter the EXECUTIVE SUMMARY blast-radius ranking pool** — assumption-gap findings can outrank regular F-NN findings when their blast radius warrants it; VALIDITY RULES rule 2 explicitly handles both F-NN (inline evidence) and M-NN (meta-finding token), preserving C-31 integrity for the new item class
3. **H-NN pre-declaration converts absence-of-evidence into a traceable outcome** — QH's CONFIRMED/REFUTED/NO-EVIDENCE trichotomy makes "the campaign looked and found nothing" distinguishable from "the campaign never evaluated this area"; no-evidence hypotheses become explicit follow-up signals rather than silent omissions

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Remediation-tier separation in field 7 (spec/contract/implementation) makes fix-layer ownership auditable by Q8 as a 4th structural check dimension", "M-NN meta-finding elevation promotes undeclared assumption gaps into the EXECUTIVE SUMMARY blast-radius ranking pool with appropriate VALIDITY RULES handling", "H-NN hypothesis pre-declaration plus QH audit converts absence-of-evidence into a traceable CONFIRMED/REFUTED/NO-EVIDENCE outcome distinguishable from a simulation that never looked"]}
```
