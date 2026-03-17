## Quest Scorecard — campaign-brief / Round 12

**Rubric:** v11, 31 criteria, 310 pts max
**File:** `simulations/quest/golden/campaign-brief-variate-R12-2026-03-17.md`
**R12 investigation:** C-31 — does explicit COMPRESSION-IMMUNE PREAMBLE designation produce measurably different outcomes from distributed per-rule dual-mechanism (C-29 PASS + C-30 PASS, V-04 style)?

---

### Criteria Assessment — C-01 through C-28

All five variations carry identical structures for C-01 through C-28. Each has: complete block set (TOPIC, DELTA, STRATEGY, STATUS, BLOCKING-DETAIL trigger, CONFIDENCE, STORY, VERDICT); inertia framing at blocking gaps; bounded/unbounded classification at VERDICT level with `action:` sub-label; per-signal timestamps with inline annotation in `found` field; FULL/COMPRESSED threshold contract; STORY zero-signal clause; VERDICT never abbreviated. No degradation observed across variations.

| Criterion range | All variations | Notes |
|---|---|---|
| C-01–C-15 | PASS | Structural completeness, block ordering, field mandates |
| C-16 | PASS | Per-signal timestamps present in found field with structural-separation annotation |
| C-17–C-20 | PASS | Inertia framing, strategy minimum, coverage arithmetic |
| C-21 | PASS | Sparse-coverage synthesis protection in STORY rules |
| C-22 | PASS | Zero-signal synthesis clause present in STORY block rules |
| C-23 | PASS | Bounded/unbounded at VERDICT level with action sub-label |
| C-24 | PASS | Timestamp isolation dual-location (found-field annotation + STATUS execution note) |
| C-25 | PASS | Zero-signal clause in STORY execution note naming gap pattern as evidence set |
| C-26 | PASS | VERDICT action sub-label mandated unconditionally |
| C-27 | PASS | Synthesis mandate in STORY block rules, question 1 framing |
| C-28 | PASS | VERDICT COMPRESSION GUARD present in execution note |

All 28 base criteria: **PASS** across all variations. Base score = 280/310.

---

### Criteria C-29 through C-31 — Per-Variation

---

#### V-01 — C-31 absent (control), R11 V-04 form exactly

**C-29 — Zero-signal synthesis dual-mechanism**
- Positional: ZERO-SIGNAL SYNTHESIS RULE in preamble (lines 112–141), with TOKEN-PRESSURE GUARD declaring the rule fires unconditionally at any token budget
- Declarative: STORY execution note (lines 320–323): "This clause is the second structural location for the zero-signal rule; the preamble statement is the first."
- Orthogonal failure modes addressed: positional counters location elision; declarative counters conditional dormancy
- **C-29: PASS** (+10)

**C-30 — Timestamp isolation dual-mechanism**
- Positional: TIMESTAMP ISOLATION RULE in preamble (lines 143–160)
- Declarative: STATUS execution note COMPRESSED-COLLAPSE GUARD (lines 253–264): "names the failure mode so that the rule is absorbed as a conditional constraint, not merely noted as a positional instruction"
- Orthogonal failure modes: preamble position counters location elision; declarative COMPRESSED-COLLAPSE GUARD counters positional processing without rule absorption
- **C-30: PASS** (+10)

**C-31 — COMPRESSION-IMMUNE PREAMBLE consolidation**
- No section header above the preamble rules
- Two rules occupy adjacent paragraphs — co-located by adjacency, not consolidated under named structural contract
- No COMPRESSION-IMMUNE designation at any level
- **C-31: PARTIAL** (−10 from ceiling)

**V-01 Score: 300/310**

---

#### V-02 — Unified descriptive label, no COMPRESSION-IMMUNE designation

**C-29: PASS** (+10)
- Positional: ZERO-SIGNAL SYNTHESIS RULE under "--- COMPRESSION-CRITICAL EXECUTION RULES ---" header
- Declarative: STORY execution note (lines 607–609): "Zero-signal synthesis mandate (second location)... See COMPRESSION-CRITICAL EXECUTION RULES above."
- Both mechanisms present and functional

**C-30: PASS** (+10)
- Positional: TIMESTAMP ISOLATION RULE under same header
- Declarative: STATUS execution note (lines 547–551): "See COMPRESSION-CRITICAL EXECUTION RULES above for the full rule statement and COMPRESSED-COLLAPSE GUARD."
- Both mechanisms present

**C-31: PARTIAL** (−10)
- "--- COMPRESSION-CRITICAL EXECUTION RULES ---" is a descriptive label, not a structural contract designation
- Header names the rules as compression-critical but does not declare the section as structurally immune
- "COMPRESSION-IMMUNE" designation absent; label is presentational, not contractual
- Evidence: the execution notes reference "see above" not "invoke structural contract"

**V-02 Score: 300/310**

---

#### V-03 — COMPRESSION-IMMUNE PREAMBLE designation without execution-note cross-reference

**C-29: PASS** (+10)
- Positional: ZERO-SIGNAL SYNTHESIS RULE within `=== COMPRESSION-IMMUNE PREAMBLE ===` section (lines 687–737), TOKEN-PRESSURE GUARD present
- Declarative: STORY execution note (lines 895–898): "This clause restates the rule from the preamble above." — names the zero-signal case explicitly at point-of-use
- Both mechanisms present

**C-30: PASS** (+10)
- Positional: TIMESTAMP ISOLATION RULE within COMPRESSION-IMMUNE PREAMBLE section
- Declarative: STATUS execution note (lines 832–839): COMPRESSED-COLLAPSE GUARD names the failure mode explicitly
- COMPRESSED-COLLAPSE GUARD in preamble itself (lines 733–735) acknowledges "the declarative guard clause (restated in the STATUS execution note)" — two-mechanism architecture documented within the preamble
- Both mechanisms present

**C-31: PARTIAL** (−10)
- `=== COMPRESSION-IMMUNE PREAMBLE ===` designation present (lines 687, 737): "This section is a structural contract."
- The designation is real and explicit — C-31 PARTIAL is not for lack of designation
- What is absent: the execution notes do not invoke the preamble by its structural designation name
  - STORY note says "the preamble above" — not "the COMPRESSION-IMMUNE PREAMBLE"
  - STATUS note says "even if preamble placement was processed without full absorption" — no designation invocation
- The structural contract is one-directional: preamble declares itself immune; execution notes do not complete the circuit by referencing the section by its immunity designation
- C-31 PASS requires a bidirectional contract: designation at declaration + invocation by designation at point-of-use. V-03 has the declaration but not the invocation. The execution notes treat the preamble as "the preamble above" (positional reference) rather than "the COMPRESSION-IMMUNE PREAMBLE" (structural contract reference).
- This resolves the R12 falsification: designation alone is insufficient. Cross-reference by designation is independently necessary.

**V-03 Score: 300/310**

---

#### V-04 — Three-rule distributed scale test, inertia framing foregrounded

**C-29: PASS** (+10)
- Positional: ZERO-SIGNAL SYNTHESIS RULE in preamble (lines 979–1002), TOKEN-PRESSURE GUARD: "structural firewall against the rule's suppression"
- Declarative: STORY execution note (lines 1199–1202): "preamble statement is the first location; this mandate is the second"
- Both mechanisms intact at three-rule scale

**C-30: PASS** (+10)
- Positional: TIMESTAMP ISOLATION RULE in preamble (lines 1004–1020), COMPRESSED-COLLAPSE GUARD documents the orthogonal failure mode
- Declarative: STATUS execution note (lines 1138–1143): "preamble statement is the first location; this is the second"
- Both mechanisms intact

**Scale degradation check:** Third rule (VERDICT ACTION POSTURE RULE, lines 1022–1041) occupies its own preamble paragraph with VERDICT COMPRESSION GUARD, plus second-location in VERDICT execution note (lines 1230–1236). The third rule does not share its positional location with C-29 or C-30 rules — each rule has independent paragraph scope. No evidence of crowding degradation; C-29 and C-30 dual-mechanisms remain structurally independent.

**C-31: PARTIAL** (−10)
- No COMPRESSION-IMMUNE designation
- Three rules in distributed per-rule paragraphs — scale test confirms distributed dual-mechanism holds C-29 and C-30 at three rules, but does not trigger C-31
- Three-rule distributed form does not degrade below 300 — consolidation is not independently necessary on structural-degradation grounds

**V-04 Score: 300/310**

Scale finding: distributed dual-mechanism does not degrade at three-rule scale. This means C-31 consolidation is not necessary to prevent scale failure — its value is purely the stronger structural guarantee of the designated contract, confirmed by V-05.

---

#### V-05 — Full C-31 PASS: COMPRESSION-IMMUNE designation + execution-note cross-references

**C-29: PASS** (+10)
- Positional: ZERO-SIGNAL SYNTHESIS RULE (C-29 domain) within COMPRESSION-IMMUNE PREAMBLE. TOKEN-PRESSURE GUARD (lines 1305–1312): "The structural designation of this preamble as COMPRESSION-IMMUNE is the positional mechanism for this rule... The STORY execution note provides the declarative mechanism -- it references this preamble by designation."
- Declarative: STORY execution note (lines 1498–1504): "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE."
- Positional mechanism is explicitly named as the COMPRESSION-IMMUNE designation itself; declarative mechanism explicitly invokes the preamble by its structural name

**C-30: PASS** (+10)
- Positional: TIMESTAMP ISOLATION RULE (C-30 domain) in COMPRESSION-IMMUNE PREAMBLE. COMPRESSED-COLLAPSE GUARD (lines 1326–1335): "The structural designation of this preamble as COMPRESSION-IMMUNE is the positional mechanism for this rule... The STATUS execution note provides the declarative mechanism -- it references this preamble by designation."
- Declarative: STATUS execution note (lines 1434–1441): "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): ...This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE."
- Same bidirectional structure as C-29

**C-31: PASS** (+10)
- `=== COMPRESSION-IMMUNE PREAMBLE ===` designation with "This section is a structural contract" declaration (lines 1280–1288)
- Rules labeled by criterion domain (C-29 domain, C-30 domain) — making the structural chain traceable
- Preamble text explicitly states: "When execution notes in subsequent blocks reference this section by its designation, those notes are pointers to this contract -- they do not restate the rule, they invoke it." (lines 1287–1288)
- STATUS execution note invokes "COMPRESSION-IMMUNE PREAMBLE" by exact designation
- STORY execution note invokes "COMPRESSION-IMMUNE PREAMBLE" by exact designation
- Bidirectional structural contract: preamble declares structural immunity → execution notes invoke preamble by designation → preamble explains the pointer semantics
- The contract is self-referential and self-documenting: both the declaration and the invocation pattern are defined within the structure

**V-05 Score: 310/310**

---

### Composite Scores

| V | C-01–28 | C-29 | C-30 | C-31 | Total | Expected |
|---|---|---|---|---|---|---|
| V-01 | 280 | PASS +10 | PASS +10 | PARTIAL | **300/310** | 300 ✓ |
| V-02 | 280 | PASS +10 | PASS +10 | PARTIAL | **300/310** | 300 ✓ |
| V-03 | 280 | PASS +10 | PASS +10 | PARTIAL | **300/310** | 300 (confirmed) |
| V-04 | 280 | PASS +10 | PASS +10 | PARTIAL | **300/310** | 300 ✓ |
| V-05 | 280 | PASS +10 | PASS +10 | PASS +10 | **310/310** | 310 ✓ |

**Ranking:** V-05 (310) > V-01/V-02/V-03/V-04 (300, tied)

---

### R12 Investigation Resolution

**Primary falsification (V-03):** C-31 PARTIAL at 300/310. Designation alone is insufficient for C-31 PASS. The `=== COMPRESSION-IMMUNE PREAMBLE ===` header with "This section is a structural contract" exists in V-03 but execution notes reference the preamble as "the preamble above" (positional reference) not as "the COMPRESSION-IMMUNE PREAMBLE" (structural contract invocation). The bidirectional contract is broken — declaration exists, invocation by designation does not.

**R12 outcome matrix match:** V-01=300, V-03=300, V-05=310 → **C-31 requires designation AND cross-reference; V-05 is the definitive form.**

**Scale test (V-04):** Distributed dual-mechanism holds at three-rule scale. C-29 and C-30 both PASS with three compression-critical rules in independent preamble paragraphs. Scale degradation does not occur. C-31 consolidation is not independently necessary to prevent scale failure — its value is the stronger compression guarantee of the explicit named contract, not compensating for scale-induced degradation.

**V-02 vs V-03:** Descriptive label (COMPRESSION-CRITICAL EXECUTION RULES) and structural designation (COMPRESSION-IMMUNE PREAMBLE) both yield C-31 PARTIAL without execution-note cross-reference. The difference between V-02 and V-03 is not detectable at the C-31 level — both are PARTIAL for the same underlying reason: the structural contract is not bidirectional. V-02's V-02's cross-reference ("See COMPRESSION-CRITICAL EXECUTION RULES above") is closer to V-05's pattern but targets a descriptive label, not an immunity designation.

---

### Excellence Signals from V-05

**Signal 1 — Bidirectional structural contract via designation invocation**
V-05 introduces pointer semantics: execution notes "invoke" rather than "restate." The preamble defines this explicitly: "those notes are pointers to this contract -- they do not restate the rule, they invoke it." This means the declarative mechanism at point-of-use is not a redundant prose copy — it is a named reference to an authoritative structural unit. When the invocation fires (e.g., under token pressure), it carries the full weight of the COMPRESSION-IMMUNE designation, not just the inline text.

**Signal 2 — Criterion domain labeling within the consolidated section**
Rules are labeled "(C-29 domain)" and "(C-30 domain)" within the COMPRESSION-IMMUNE PREAMBLE. This enables execution notes to invoke a specific rule by its domain identity ("invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE") rather than by prose proximity. The domain labels make the structural chain traceable and precise.

**Signal 3 — Self-documenting mechanism architecture within per-rule guards**
In V-01 through V-04, the TOKEN-PRESSURE GUARD and COMPRESSED-COLLAPSE GUARD explain why the rule fires but not which mechanism they represent. In V-05, each guard explicitly identifies its role: "The structural designation of this preamble as COMPRESSION-IMMUNE is the positional mechanism for this rule... The [block] execution note provides the declarative mechanism." This makes the dual-mechanism architecture visible within the preamble itself — not just present but explained and traceable.

---

### R13 Investigation Candidate

Whether the domain-labeling pattern in V-05 (C-29 domain / C-30 domain) adds independently measurable protection when a third compression-critical rule is added to the COMPRESSION-IMMUNE PREAMBLE, compared to an unlabeled three-rule consolidated section. The question: does labeled domain assignment within the COMPRESSION-IMMUNE PREAMBLE enable more precise execution-note invocation and reduce the probability that a rule invocation is misidentified or omitted under token pressure?

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["bidirectional structural contract via designation invocation: execution notes invoke COMPRESSION-IMMUNE PREAMBLE by exact designation name rather than restating inline, creating pointer-to-contract semantics where the invocation carries the full weight of the immunity designation", "criterion domain labeling within consolidated preamble section: rules labeled by criterion domain (C-29 domain, C-30 domain) enable execution notes to invoke specific rules by domain identity rather than prose proximity, making the structural chain traceable and precise"]}
```
