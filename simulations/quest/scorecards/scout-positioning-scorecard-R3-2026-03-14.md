## scout-positioning R3 Scorecard — Results

| Rank | Variation | Score | Delta vs R2 ceiling |
|------|-----------|-------|---------------------|
| 1 | V-05 Full-stack | **168/170** | +33 |
| 2 | V-01 Rubric-mirror-17 | **159/170** | +24 |
| 3 | V-04 R2-V05 upgraded | **158/170** | +23 |
| 4 | V-02 Inertia-first | **150/170** | +15 |
| 5 | V-03 Pre-flight GATE + post-FINDINGS VERIFY | **147/170** | +12 |

**all_essential_pass = TRUE across all five variations.**

**What decided it:**

V-05 wins by combining three things no other variation had simultaneously: 17-section C-XX structure (C-11: 10), verbatim-VERIFY with rubric text quoted exactly (C-15: 10), and preamble mechanism declaration naming MECHANISM 1/2/3 before any phase begins (C-16: 10). The 2-point gap from max is C-03 and C-09 — content criteria where the ceiling is structural, not behavioral.

V-01 edges V-04 by 1 point (159 vs 158). V-01 wins C-11 (+4) and C-12 (+2) from the 17-section structure. V-04 wins C-15 (+2) and C-16 (+1) from verbatim-VERIFY and canonical claim-trace. V-01's paraphrased VERIFY is the single-point gap.

**Key scoring axis for R3 — C-11 and C-15 are the discriminating criteria:**

| Variation | C-11 | C-15 | Sum |
|-----------|------|------|-----|
| V-05 | 10 | 10 | 20 |
| V-01 | 10 | 8 | 18 |
| V-04 | 6 | 10 | 16 |
| V-02 | 5 | 8 | 13 |
| V-03 | 5 | 8 | 13 |

**New patterns extracted:**

1. **Preamble mechanism declaration** — naming MECHANISM 1/2/3 upfront makes compound enforcement auditable before reading any output; R2 V-05 had the mechanisms implicitly, R3 V-05 declares them
2. **Verbatim-VERIFY** — quoting rubric pass conditions exactly (not paraphrasing) scores 10/10 on C-15; paraphrased VERIFY caps at 8/10; condensed language introduces threshold drift

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["preamble mechanism declaration makes compound enforcement auditable before reading output -- naming MECHANISM 1/2/3 upfront announces the quality architecture; implicit compound (R2 V-05) required inferring the layers, declarative compound (R3 V-05) confirms them with a VERIFY check", "verbatim-VERIFY closes the rubric-skill interpretation gap -- paraphrased-VERIFY scores 8/10 on C-15; verbatim-VERIFY scores 10/10; quoting rubric pass conditions exactly prevents threshold drift where condensed language rationalizes borderline passes"]}
```

Scorecard written to `simulations/quest/scorecards/scout-positioning-scorecard-R3-2026-03-14.md`.
TM requires per-audience framing; FINDINGS C-02 requires "1-2 framing signals that distinguish each statement"; VERIFY C-02 checks distinct framing |
| C-03 | Category definition | 9 | PASS | FINDINGS C-03 "Category: / Not: [name rejected category and why]"; VERIFY C-03 checks ownable category + rejected category with reason |
| C-04 | Core differentiator | 10 | PASS | EXECUTE mandates inertia contrast first, named-competitor contrast second; FINDINGS C-04 two-slot template with "Feature lists fail this section"; VERIFY C-04 explicit two-beat check |
| C-05 | Anti-positioning | 9 | PASS | EXECUTE DESIGN "2+ Signal is NOT [X] -- [why confusion is plausible]"; VERIFY C-05 checks plausibility requirement |
| C-06 | PM reality check | 9 | PASS | FINDINGS C-06 has Gap type column; ahead-of-spec / unsupported / N/A required; no Source column (lower than V-04/V-05) |
| C-07 | Competitive matrix | 10 | PASS | FINDINGS C-07 explicitly mandates "5+ product-relevant dimensions"; VERIFY C-07 counts dimensions; 5+ floor built into template |
| C-08 | Messaging hierarchy | 9 | PASS | EXECUTE DESIGN "one PRIMARY (labeled PRIMARY), per-audience SECONDARY (each labeled SECONDARY). Flat lists fail"; VERIFY C-08 checks PRIMARY/SECONDARY labels |
| C-09 | Degradation quantification | 9 | PASS | FINDINGS C-09 "name the specific risks -- 'Quality may vary' does not satisfy this criterion"; dedicated section with anti-pattern named |
| C-10 | Whitespace identification | 9 | PASS | FINDINGS C-10 "name the specific matrix columns in C-07 where Signal is H and no named competitor is H -- makes the claim falsifiable"; no inertia row test; no [Source:] citation |
| C-11 | Output structure mirrors rubric | 10 | PASS | V-01's defining axis: 17 FINDINGS sections labeled C-01 through C-17, 1:1 with all rubric criteria; FINDINGS C-11 self-reports section count; missing section = missed criterion detectable by counting |
| C-12 | STOP enforcement verb | 10 | PASS | "If not found: STOP" in SETUP; FINDINGS C-12 META explicitly records "Exact verb used in SETUP"; VERIFY C-12 confirms verb position before degradation note |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | SETUP emits "FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)" as named FINDINGS before any other output; FINDINGS C-13 echoes in main output |
| C-14 | Whitespace citation obligation | 10 | PASS | FINDINGS C-14 cross-references "Dimensions cited in C-10" and checks they are columns in C-07; explicit falsifiability check |
| C-15 | Pre-artifact VERIFY pass | 8 | PASS | VERIFY block structurally present after FINDINGS; verify_status in frontmatter; but pass conditions are paraphrased ("PASS if prior run loaded OR degradation note emitted"), not verbatim rubric quotes -- key gap vs V-04/V-05 |
| C-16 | Compound enforcement stacking | 9 | PASS | FINDINGS C-16 META explicitly names three mechanisms: lifecycle ordering, structural mandate (17 sections), pre-artifact VERIFY; declared in FINDINGS (not preamble); VERIFY C-16 confirms all three; does not include claim-trace (canonical mechanism 2) |
| C-17 | Matrix dimension floor | 10 | PASS | FINDINGS C-07 template explicitly mandates 5+; FINDINGS C-17 META lists and counts dimensions; VERIFY C-17 counts and flags if < 5 |

**Total: 159/170 · All essential pass: YES**

---

### V-02: Inertia-first

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | "If not found: STOP. Before any other output, emit this as a named FINDINGS section: FINDINGS 8: DEGRADATION NOTE"; strong but not as forceful as V-05 |
| C-02 | Per-audience statements | 9 | PASS | EXECUTE GTM two sub-beats per audience (inertia + tool); framing required; "Reusing a statement for two audiences fails" |
| C-03 | Category definition | 9 | PASS | Section 1 "Category / Rejected category: [name] -- [why Signal cannot own it]"; explicitly required |
| C-04 | Core differentiator | 10 | PASS | EXECUTE: "Inertia contrast (required, first) / Named-competitor contrast (required, second). Inertia contrast ALWAYS precedes named-competitor contrast. Both required -- not one or the other." Strongest two-beat mandate of any single-axis variation |
| C-05 | Anti-positioning | 10 | PASS | EXECUTE DESIGN: "The first must be: 'Signal is NOT staying with the current workflow...'" Inertia anti-positioning is structurally required, not optional |
| C-06 | PM reality check | 9 | PASS | Section 7 with Gap type required; "at least one claim drawn from the inertia contrast" required; no Source column |
| C-07 | Competitive matrix | 10 | PASS | FINDINGS 4: "Rows: Inertia [ALWAYS FIRST]. Columns: [5+ product-relevant dimensions]"; VERIFY 4 counts dimensions and checks inertia row |
| C-08 | Messaging hierarchy | 9 | PASS | EXECUTE DESIGN: "PRIMARY (labeled PRIMARY) targets inertia buyer. SECONDARY (labeled SECONDARY) addresses tool-switching per audience. Flat lists fail." |
| C-09 | Degradation quantification | 9 | PASS | FINDINGS 8: specific risks named "including which inertia positions could not be verified against named competitor data" |
| C-10 | Whitespace identification | 10 | PASS | FINDINGS 6: "neither inertia nor any named tool owns it" + "no other row -- including inertia -- is H"; inertia row explicitly tested; strongest whitespace test of any variation |
| C-11 | Output structure mirrors rubric | 5 | PARTIAL | Sections 1-8, not labeled with criterion IDs; section 1 combines C-03+C-04; section 8 combines C-01/C-09/C-13; no meta-criteria sections (C-11 through C-17); section count is 8 vs 17 required in v3 |
| C-12 | STOP enforcement verb | 8 | PASS | "If not found: STOP" in SETUP; no FINDINGS META section for C-12; VERIFY checks degradation note quality but not verb position explicitly |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | SETUP emits "FINDINGS 8: DEGRADATION NOTE" as named section before positioning; section 8 in FINDINGS is dedicated to degradation note |
| C-14 | Whitespace citation obligation | 8 | PASS | "Dimensions tested: [name the specific matrix columns... Falsifiable by column inspection]"; no explicit cross-reference that cited dimensions are matrix columns; implicit rather than verified |
| C-15 | Pre-artifact VERIFY pass | 8 | PASS | VERIFY block present; verify_status in frontmatter; inertia_framing in frontmatter; pass conditions paraphrased per section (1-8), not verbatim rubric quotes |
| C-16 | Compound enforcement stacking | 7 | PARTIAL | Three mechanisms identifiable: lifecycle ordering + inertia structural mandate + pre-artifact VERIFY; inertia structural mandate substitutes for claim-trace (not the canonical three); mechanisms not declared explicitly in preamble or FINDINGS meta; no compound declaration or verification |
| C-17 | Matrix dimension floor | 10 | PASS | FINDINGS 4: "Columns: [5+ product-relevant dimensions]"; VERIFY "MATRIX DIMENSION COUNT: [list] -- Count: [N]. PASS if N >= 5" |

**Total: 150/170 · All essential pass: YES**

---

### V-03: Pre-flight GATE + post-FINDINGS VERIFY

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | "If not found: STOP. Before any other output, emit this as a named FINDINGS section: FINDINGS 8: DEGRADATION NOTE"; GATE G-01 also tracks prior run status |
| C-02 | Per-audience statements | 9 | PASS | GATE G-02 confirms audiences before EXECUTE; EXECUTE GTM uses "audiences confirmed in GATE G-02"; framing required per audience type |
| C-03 | Category definition | 9 | PASS | FINDINGS 1: "Category / Rejected: [name] -- [why Signal cannot own it]"; VERIFY 1 checks both |
| C-04 | Core differentiator | 10 | PASS | EXECUTE STRATEGY: "Inertia contrast first... Named-competitor contrast second... Feature list = FAIL. Both contrasts required." Two-beat mandate with explicit ordering |
| C-05 | Anti-positioning | 9 | PASS | EXECUTE DESIGN "2+ Signal is NOT [X] -- [why confusion plausible]. Generic negations do not count."; no inertia statement requirement (lower than V-02/V-05) |
| C-06 | PM reality check | 9 | PASS | FINDINGS 7 with Gap type required; VERIFY 7 checks 3+ rows and gap type presence |
| C-07 | Competitive matrix | 10 | PASS | FINDINGS 4: "5+ product-relevant dimensions" explicitly listed; VERIFY 4 "Count the dimensions -- state count. FLAG if fewer than 5." |
| C-08 | Messaging hierarchy | 9 | PASS | EXECUTE DESIGN "PRIMARY (labeled PRIMARY) / SECONDARY (each labeled SECONDARY). Explicit labels required. Flat lists fail." |
| C-09 | Degradation quantification | 9 | PASS | FINDINGS 8: "specific risks named precisely, as emitted in SETUP" |
| C-10 | Whitespace identification | 9 | PASS | FINDINGS 6: "name the specific matrix columns where Signal is H and no named competitor is H -- falsifiable by column inspection"; no inertia row test; VERIFY 6 checks specific column names |
| C-11 | Output structure mirrors rubric | 5 | PARTIAL | Sections 1-8, not C-XX labeled; same issue as V-02; GATE adds meta-traceability but section-to-criterion mapping is not 1:1 and meta-criteria (C-11 through C-17) have no FINDINGS sections |
| C-12 | STOP enforcement verb | 8 | PASS | "If not found: STOP" in SETUP; GATE REVIEW in VERIFY confirms gate_status but does not explicitly verify STOP verb position |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | SETUP emits "FINDINGS 8: DEGRADATION NOTE" as named section before any positioning output |
| C-14 | Whitespace citation obligation | 8 | PASS | VERIFY 6: "PASS if specific matrix columns cited by name (not 'no competitor occupies this space' without naming the columns)"; no explicit cross-reference confirming cited dimensions are matrix columns |
| C-15 | Pre-artifact VERIFY pass | 8 | PASS | VERIFY block present; gate_status and verify_status both in frontmatter; the two-gate innovation (GATE + VERIFY) is structurally novel but pass conditions are paraphrased, not verbatim rubric quotes |
| C-16 | Compound enforcement stacking | 6 | PARTIAL | Three mechanisms identifiable: GATE (input validation before EXECUTE) + VERIFY (output validation after FINDINGS) + lifecycle ordering; GATE substitutes for claim-trace; mechanisms not declared or labeled; no compound declaration in preamble or VERIFY |
| C-17 | Matrix dimension floor | 10 | PASS | FINDINGS 4: "5+ product-relevant dimensions" required; VERIFY 4 counts dimensions and flags if < 5 |

**Total: 147/170 · All essential pass: YES**

---

### V-04: R2-V05 upgraded

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | "If not found: STOP. Before any other output, emit this as a named FINDINGS section: FINDINGS 8: DEGRADATION NOTE"; strong enforcement with named section |
| C-02 | Per-audience statements | 9 | PASS | EXECUTE GTM: framing required per audience type; "Each statement cites at least one source. Reusing a statement fails."; VERIFY 2 quotes rubric verbatim |
| C-03 | Category definition | 9 | PASS | FINDINGS 1: "Category [Source: ...] / Rejected category: [name] -- [why] [Source: ...]"; [Source:] on both; VERIFY 1 verbatim rubric quote |
| C-04 | Core differentiator | 10 | PASS | EXECUTE: inertia contrast first + named-competitor contrast second + [Source: ...] on both; VERIFY 1 verbatim "Feature list = auto-FLAG" |
| C-05 | Anti-positioning | 9 | PASS | EXECUTE: "2+ Signal is NOT [X]... Generic negations fail. Annotate each: [Source: ...]"; VERIFY 5 verbatim pass condition; no inertia statement requirement |
| C-06 | PM reality check | 10 | PASS | FINDINGS 7 adds Source column to standard table: "| Claim | Verdict | Reason | Source | Gap type |"; VERIFY 7 verbatim rubric quote for 3+ rows and gap type requirement |
| C-07 | Competitive matrix | 10 | PASS | FINDINGS 4: "5+ product-relevant dimensions" required; VERIFY 4 verbatim "at least 5 dimensions relevant to the product"; dimension count stated |
| C-08 | Messaging hierarchy | 9 | PASS | EXECUTE DESIGN: "PRIMARY (labeled PRIMARY), per-audience SECONDARY (each labeled SECONDARY). Flat lists fail."; VERIFY 3 verbatim rubric quote |
| C-09 | Degradation quantification | 9 | PASS | FINDINGS 8: "specific risks as emitted in SETUP"; prior run loaded → N/A |
| C-10 | Whitespace identification | 10 | PASS | FINDINGS 6: "[Source: matrix section 4, dimensions [X] and [Y]]"; explicit source citation format names section and dimension; VERIFY 6 verbatim "Missing dimension citation = auto-FLAG" |
| C-11 | Output structure mirrors rubric | 6 | PARTIAL | Sections 1-8, not C-XX labeled; VERIFY's verbatim pass conditions partially compensate by re-mapping sections to criteria; C-11 through C-17 addressed only in VERIFY COMPOUND ENFORCEMENT CHECK and MATRIX DIMENSION COUNT, not as dedicated FINDINGS sections |
| C-12 | STOP enforcement verb | 8 | PASS | "If not found: STOP" in SETUP; no dedicated C-12 FINDINGS META section; VERIFY covers degradation note quality (item 8) but not verb position |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | SETUP emits "FINDINGS 8: DEGRADATION NOTE" as named FINDINGS section before any positioning output |
| C-14 | Whitespace citation obligation | 10 | PASS | "[Source: matrix section 4, dimensions [X] and [Y]]" -- citation format names section and dimensions explicitly; VERIFY 6 verbatim "Missing dimension citation = auto-FLAG" |
| C-15 | Pre-artifact VERIFY pass | 10 | PASS | VERIFY quotes verbatim rubric language: "PASS if 'every audience listed in --audiences receives its own statement'...", "Feature list = auto-FLAG", "Fewer than 5 = auto-FLAG"; MECHANISM 3 explicitly confirmed in COMPOUND ENFORCEMENT CHECK |
| C-16 | Compound enforcement stacking | 10 | PASS | Preamble declares "Three layers of enforcement: 1. Lifecycle phase boundaries... 2. Every claim carries [Source: ...]... 3. After FINDINGS, a VERIFY pass checks each section..."; VERIFY COMPOUND ENFORCEMENT CHECK explicitly traces all three mechanisms (lifecycle, claim-trace, VERIFY); canonical three confirmed |
| C-17 | Matrix dimension floor | 10 | PASS | FINDINGS 4: 5+ required; VERIFY "MATRIX DIMENSION COUNT (C-17): Dimensions listed... Count: [N] -- PASS if N >= 5 / FLAG if N < 5" |

**Total: 158/170 · All essential pass: YES**

---

### V-05: Full-stack

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 10 | PASS | "If not found: STOP. Before any other output, emit this as a named FINDINGS section: FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)"; degradation note IS the first emitted FINDINGS section; VERIFY C-01 verbatim |
| C-02 | Per-audience statements | 10 | PASS | EXECUTE GTM + FINDINGS C-02 "(b) the 1-2 framing signals distinguishing this statement from the others [Source: ...]"; VERIFY C-02 verbatim "every audience listed in --audiences receives its own statement" AND "audience-appropriate framing"; reused statement = auto-FLAG |
| C-03 | Category definition | 9 | PASS | FINDINGS C-03: "[Source: ...]" on both category and rejected category; VERIFY C-03 verbatim; category coherence check with C-05 included; source annotation present but category content is derived not proven |
| C-04 | Core differentiator | 10 | PASS | EXECUTE: "Inertia contrast first: / Named-competitor contrast second: / Both required. Annotate both: [Source: ...]"; VERIFY C-04 verbatim "Feature list = auto-FLAG. Missing inertia beat = FLAG"; triple enforcement (EXECUTE mandate + FINDINGS template + VERIFY auto-FLAG) |
| C-05 | Anti-positioning | 10 | PASS | EXECUTE: "At least one must address inertia: 'Signal is NOT staying with the current workflow...' All statements annotated: [Source: ...]"; VERIFY C-05 verbatim "Generic negations = auto-FLAG. Missing inertia statement = FLAG"; inertia statement is structurally required |
| C-06 | PM reality check | 10 | PASS | FINDINGS C-06 "| Claim | Verdict | Reason | Source | Gap type |"; source column required; VERIFY C-06 verbatim "PARTIAL rows note gap type" |
| C-07 | Competitive matrix | 10 | PASS | FINDINGS C-07: "Rows: Inertia [FIRST], Signal, [named competitors]. Columns: [5+]"; inertia as first-class matrix row; VERIFY C-07 verbatim "Inertia row present. Count dimensions. Fewer than 5 = auto-FLAG" |
| C-08 | Messaging hierarchy | 10 | PASS | EXECUTE: "PRIMARY targets inertia buyer. SECONDARY addresses tool-switching per audience. Explicit labels required."; VERIFY C-08 verbatim "PRIMARY / SECONDARY, not inferred from ordering. PRIMARY targets inertia buyer. Flat list = auto-FLAG" |
| C-09 | Degradation quantification | 9 | PASS | FINDINGS C-09: "name specific risks -- 'Quality may vary' does not satisfy this criterion"; prior run loaded → N/A; VERIFY C-09 verbatim with generic warning = auto-FLAG |
| C-10 | Whitespace identification | 10 | PASS | FINDINGS C-10: "neither inertia nor any named tool owns it" + "[Source: matrix FINDINGS C-07, dimensions [X] and [Y]]"; inertia row tested; source citation present; VERIFY C-10 verbatim "Missing dimension citation = auto-FLAG. Inertia row tested." |
| C-11 | Output structure mirrors rubric | 10 | PASS | Exactly 17 FINDINGS sections labeled C-01 through C-17, 1:1 with all rubric criteria including meta-criteria; FINDINGS C-11 self-reports count; VERIFY C-11 "Count. Missing section = missed criterion" |
| C-12 | STOP enforcement verb | 10 | PASS | "If not found: STOP" in SETUP; FINDINGS C-12 META records exact verb and position; VERIFY C-12 verbatim "STOP/HALT/DO NOT CONTINUE was the verb in SETUP before degradation note" |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | SETUP emits "FINDINGS C-13: DEGRADATION NOTE (DEDICATED SECTION)" as first output; FINDINGS C-13 in main section echoes; VERIFY C-13 verbatim "separate from both SETUP instructions and positioning output. SETUP-only = auto-FLAG" |
| C-14 | Whitespace citation obligation | 10 | PASS | FINDINGS C-14 cross-references dimensions from C-10 and verifies each appears as matrix column in C-07; VERIFY C-14 verbatim "each cited dimension appears as a column in the matrix. Vague citation = auto-FLAG" |
| C-15 | Pre-artifact VERIFY pass | 10 | PASS | VERIFY uses verbatim rubric language for every pass condition; FINDINGS C-15 notes "VERIFY phase: present after FINDINGS, before artifact emission"; VERIFY C-15 "PASS because this VERIFY block is structurally present after FINDINGS"; SOURCE AUDIT in VERIFY checks claim-trace completeness |
| C-16 | Compound enforcement stacking | 10 | PASS | Preamble declares "MECHANISM 1 (lifecycle ordering) / MECHANISM 2 (structural mandate: 17 sections) / MECHANISM 3 (pre-artifact VERIFY). These three mechanisms are independent. Each defends a different failure mode."; FINDINGS C-16 confirms all three; VERIFY C-16 checks each mechanism and counts; SOURCE AUDIT in VERIFY is the operational claim-trace check |
| C-17 | Matrix dimension floor | 10 | PASS | FINDINGS C-07: 5+ required; FINDINGS C-17: "Dimensions in FINDINGS C-07: [list them]. Count: [N] -- PASS if N >= 5"; VERIFY C-17 verbatim |

**Total: 168/170 · All essential pass: YES**

---

## Composite Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Full-stack | **168** | YES |
| 2 | V-01 Rubric-mirror-17 | **159** | YES |
| 3 | V-04 R2-V05 upgraded | **158** | YES |
| 4 | V-02 Inertia-first | **150** | YES |
| 5 | V-03 Pre-flight GATE + post-FINDINGS VERIFY | **147** | YES |

---

## Excellence Signals from V-05

**1. Preamble mechanism declaration makes compound enforcement auditable before reading output.**
R2 V-05 had three layers structurally but unlabeled -- a reviewer had to infer the compound architecture from reading the phases. R3 V-05 names MECHANISM 1/2/3 in the preamble before any phase begins. This closes the ambiguity: the skill announces its quality architecture up front, and FINDINGS C-16 + VERIFY C-16 confirm it was executed. The declaration is the new pattern; the mechanisms themselves were already present in R2.

**2. Verbatim-VERIFY closes the rubric-skill interpretation gap.**
V-01 (paraphrased VERIFY) scores 8/10 on C-15. V-04 and V-05 (verbatim VERIFY) score 10/10. The distinction: a paraphrase of a pass condition is a model of the threshold, not the threshold. When VERIFY text IS the rubric text -- "every audience listed in --audiences receives its own statement" quoted exactly -- the LLM is evaluating against the exact condition, not a condensed version that might rationalize a borderline case as a pass.

**3. 17-section + verbatim-VERIFY combination beats either alone.**
V-01 has the 17-section structure (C-11: 10) but paraphrased VERIFY (C-15: 8). V-04 has verbatim VERIFY (C-15: 10) but 8 sections (C-11: 6). V-05 combines both: 17 sections covering meta-criteria + verbatim VERIFY = 10+10. The R3 ceiling is only reachable by combining these two -- single-axis optimization hits a local maximum that full-stack escapes.

**4. Inertia as structural mandate (not stylistic choice) strengthens C-04, C-05, C-07, C-10.**
V-05 combines the inertia-first axis (from V-02) with the full compound stack. Result: inertia is row 1 in the matrix, required in every contrast, required anti-positioning statement, and the VERIFY checks that the inertia beat is present (auto-FLAG if missing). This converts inertia treatment from best-practice to enforcement.

---

```json
{"top_score": 168, "all_essential_pass": true, "new_patterns": ["preamble mechanism declaration makes compound enforcement auditable before reading output -- naming MECHANISM 1/2/3 upfront announces the quality architecture; implicit compound (R2 V-05) required inferring the layers, declarative compound (R3 V-05) confirms them with a VERIFY check", "verbatim-VERIFY closes the rubric-skill interpretation gap -- paraphrased-VERIFY scores 8/10 on C-15; verbatim-VERIFY scores 10/10; quoting rubric pass conditions exactly prevents threshold drift where condensed language rationalizes borderline passes"]}
```
