Now I have all five variations fully read. Let me score them.

---

## Scorecard — topic-roadmap (topic-plan) Round 18

**Rubric version:** v18 | **Denominator:** 72 | **Date:** 2026-03-17

---

### Essential Criteria (C-01–C-08)

All five variations carry the full R17 V-05 structure. Every essential criterion passes across V-01 through V-05.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 INERTIA COMPETITOR DECLARATION at open | PASS | PASS | PASS | PASS | PASS |
| C-02 Phase ordering enforced | PASS | PASS | PASS | PASS | PASS |
| C-03–C-08 (structure, gating, scope isolation) | PASS | PASS | PASS | PASS | PASS |

**All essential: PASS across all variations.**

---

### Aspirational Criteria Basis (C-09–C-36)

All five variations carry the full R17 V-05 formulations. C-09–C-36 = **56/56** for all.

---

### Aspirational Criteria C-37–C-42

All five variations carry C-37–C-42 at FULL (as designed — isolating C-43 and C-44).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-37 Section scope isolation | 2 | 2 | 2 | 2 | 2 |
| C-38 Consequence gate dual-site | 2 | 2 | 2 | 2 | 2 |
| C-39 Exact literal in CONTRACT B | 2 | 2 | 2 | 2 | 2 |
| C-40 STRUCTURAL/VALUE taxonomy split | 2 | 2 | 2 | 2 | 2 |
| C-41 §9 names exact literal | 2 | 2 | 2 | 2 | 2 |
| C-42 Self-sufficiency assertion | 2 | 2 | 2 | 2 | 2 |

---

### C-43 — §9 guard body declares CONTRACT B as governing document

**C-43 full (2):** Governing reference inside the COMPLIANCE OBLIGATION statement itself; scorer traces value to CONTRACT B without reading outside §9.
**C-43 partial (1):** Governing reference exists but outside the obligation statement (preamble annotation, title, or parenthetical).
**C-43 fail (0):** No governing reference, or C-41 fails.

**V-01 — C-43 = 2 (FULL)**
Lines 424–431: `"COMPLIANCE OBLIGATION: Every §6 proposal row must carry the exact string 'Bias blocked by guard'... CONTRACT B is the governing authority for this value requirement: it defines the compliant value string, the STRUCTURAL and VALUE violation taxonomy, and the scorer self-sufficiency declaration. A scorer reading this compliance obligation statement identifies both the required value 'Bias blocked by guard' and CONTRACT B as the governing source for that value requirement, without consulting any section outside this §9 obligation statement."`
The governing declaration is located inside the COMPLIANCE OBLIGATION text itself. C-41 satisfied. Bidirectional pointer present.

**V-02 — C-43 = 0 (FAIL)**
Lines 834–840: The obligation names the exact literal and references CONTRACT B only for "the violation taxonomy defined in CONTRACT B" — taxonomy reference, not a governing authority declaration for the value requirement. No sentence inside the obligation asserts CONTRACT B as governing source. FAIL.

**V-03 — C-43 = 1 (PARTIAL)**
Lines 1152–1154: Governing reference appears as preamble annotation `[>> Governing authority: CONTRACT B defines the value compliance contract for this guard; see CONTRACT B block in Output Schema for the governing specification. <<]` — outside the COMPLIANCE OBLIGATION statement. The obligation itself (lines 1169–1175) names the literal independently and references CONTRACT B only for taxonomy, not as governing authority. Reference exists but at wrong structural location. PARTIAL.

**V-04 — C-43 = 2 (FULL)**
Lines 1542–1548: `"CONTRACT B is the governing authority for this value requirement: it names the required value, defines the violation taxonomy, and asserts scorer self-sufficiency. A scorer reading this compliance obligation statement traces the value requirement 'Bias blocked by guard' to CONTRACT B as its governing source, from this obligation statement alone without consulting any section outside §9."` Declaration inside the obligation statement. FULL.

**V-05 — C-43 = 2 (FULL)**
Lines 1991–2002: `"CONTRACT B is the governing authority for this value requirement... The guard-contract relationship is bidirectional: CONTRACT B declares the governed value; this §9 obligation names the value and declares CONTRACT B as source authority; CONTRACT B's self-sufficiency declaration names §9 as the enforcement site."` Full bidirectional pointer declared inside the obligation. FULL (maximal expression).

---

### C-44 — Self-sufficiency assertion names its own structural prerequisites

**C-44 full (2):** Both structural prerequisites named inside the assertion block by structural property type label (exact-value requirement + taxonomy-split requirement) as validity conditions; machine-detectable from assertion text alone.
**C-44 partial (1):** Falsifiability clause present but names only one prerequisite, or both named but outside the assertion block, or uses generic language.
**C-44 fail (0):** Prerequisites not named by structural property type; or C-42 fails.

**V-01 — C-44 = 0 (FAIL)**
Lines 186–192: The falsifiability clause reads: `"a CONTRACT B block that makes this self-sufficiency claim but fails the structural compliance test precondition... or fails the value compliance test precondition..."` Names prerequisites by **test type** ("structural compliance test precondition," "value compliance test precondition"), not by **structural property type** ("exact-value requirement," "taxonomy-split requirement"). FAIL.

**V-02 — C-44 = 2 (FULL)**
Lines 619–634: `"Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by guard' must be present in CONTRACT B as the defined compliant value... Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL and VALUE as separately labeled..."` Both prerequisites named by structural property type, inside the assertion block, as validity conditions for the claim. FULL.

**V-03 — C-44 = 2 (FULL)**
Lines 1005–1018: `"Prerequisite 1 -- exact-value requirement: the exact string 'Bias blocked by guard' must be present in CONTRACT B... Prerequisite 2 -- taxonomy-split requirement: CONTRACT B must define STRUCTURAL and VALUE as separately labeled..."` Both named inside the CONTRACT B block as validity conditions. FULL.

**V-04 — C-44 = 2 (FULL)**
Lines 1332–1347: `"Prerequisite 1 -- exact-value requirement: ...A self-sufficiency assertion made without the exact-value requirement present in CONTRACT B is internally inconsistent: test (b) cannot be executed without a reference literal, and the inconsistency is detectable from this block alone. Prerequisite 2 -- taxonomy-split requirement: ...the inconsistency is detectable from this block."` Both named by property type with explicit internal-inconsistency detection language. FULL.

**V-05 — C-44 = 2 (FULL)**
Lines 1736–1759: Dedicated `CONSISTENCY AUDIT CLAUSE` block with formal structural labels `EXACT-VALUE REQUIREMENT` and `TAXONOMY-SPLIT REQUIREMENT`. Each named as a validity condition with self-referential confirmation ("This CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT at the 'Compliant value' line above"). Machine-verifiable by label-matching alone. FULL (maximal expression).

---

### Composite Scores

| Var | C-09–C-36 | C-37 | C-38 | C-39 | C-40 | C-41 | C-42 | C-43 | C-44 | Total | Score |
|-----|:---------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:-----:|:-----:|
| V-01 | 56 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **0** | 70 | **9.72** |
| V-02 | 56 | 2 | 2 | 2 | 2 | 2 | 2 | **0** | **2** | 70 | **9.72** |
| V-03 | 56 | 2 | 2 | 2 | 2 | 2 | 2 | **1** | **2** | 71 | **9.86** |
| V-04 | 56 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **2** | 72 | **10.00** |
| V-05 | 56 | 2 | 2 | 2 | 2 | 2 | 2 | **2** | **2** | 72 | **10.00** |

**Formula:** total / 72 × 10

**Rank:** V-04 = V-05 (10.00) > V-03 (9.86) > V-01 = V-02 (9.72)

---

### Excellence Signals from Top-Scoring Variations

**V-05 over V-04** (both score 10.00, but V-05 establishes new structural patterns):

**Pattern 1 — Bidirectional architecture declared as named relationship**
V-04 satisfies C-43 by placing the governing declaration inside the obligation. V-05 goes further: the obligation explicitly names the relationship as *bidirectional* — CONTRACT B → §9 (CONTRACT B declares governed value), §9 → CONTRACT B (obligation names CONTRACT B as source authority), and CONTRACT B → §9 (self-sufficiency declaration names §9 as enforcement site). The architecture is a declared, closed loop, not just a one-way pointer. A scorer reading either artifact (§9 or CONTRACT B) can independently confirm the full guard-contract structure without reading the other.

**Pattern 2 — CONSISTENCY AUDIT CLAUSE: prerequisites as a named structural block with formal identifiers**
V-04 names prerequisites in falsifiability language inside the assertion. V-05 introduces a dedicated `CONSISTENCY AUDIT CLAUSE` block with formal uppercase identifiers (`EXACT-VALUE REQUIREMENT`, `TAXONOMY-SPLIT REQUIREMENT`) and includes self-referential satisfaction confirmations ("This CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT at the 'Compliant value' line above"). Internal consistency becomes verifiable by label-matching alone — find the named identifier, check its presence. No inference required. CONTRACT B becomes a self-auditing artifact in the fullest structural sense.

---

### Expected vs. Actual

All five variations match their expected scores exactly. The gradient confirms axis isolation: C-43 and C-44 are independently testable, C-43 partial is a distinct structural state below FULL, and combined full satisfaction achieves 10.00.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Bidirectional architecture declared as named relationship: CONTRACT B names §9 as enforcement site; §9 obligation names CONTRACT B as governing source; the closed-loop structure is declared explicitly, making the guard-contract relationship machine-traceable in both directions without cross-section reading", "CONSISTENCY AUDIT CLAUSE: a dedicated named block housing formal uppercase identifiers (EXACT-VALUE REQUIREMENT, TAXONOMY-SPLIT REQUIREMENT) with self-referential satisfaction confirmations makes internal consistency verifiable by label-matching alone, converting CONTRACT B from a coverage-claiming artifact to a formally self-auditing one"]}
```
