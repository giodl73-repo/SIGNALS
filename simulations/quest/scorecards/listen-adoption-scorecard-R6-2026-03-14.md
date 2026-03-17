# Scorecard: listen-adoption — Round 6

**Rubric:** v6 | **Max:** 150 | **Golden threshold:** 80

---

## Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01–C-05 | 12 ea | P | P | P | P | P |
| C-06–C-08 | 10 ea | P | P | P | P | P |
| C-09–C-18 | 5 ea | P | P | P | P | P |
| **C-19** | 5 | P | P | **X** | P | P |
| **C-20** | 5 | P | P | P | P | P |
| **Total** | **150** | **150** | **150** | **145** | **150** | **150** |

---

## C-19 Analysis

**Four PASS:** V-01/V-04/V-05 use named CORRECTION BLOCK templates with explicit BEFORE/AFTER headers (named structural slots force content materialization). V-02 inverts this — corrected content goes INTO SECTION K's "Corrected content" cells — and guards C-19 with an explicit counter-example: *"A cell reading only 'updated the champion entry' without showing the row fails C-19."*

**V-03 FAIL:** The ORIGINAL/CORRECTED format exists in the template, but it's embedded in prose guidance under conditional "If Check fails:" paragraphs — no named block, no mode boundary. The conversational register + absence of a named structural slot = insufficient enforcement. The design notes explicitly name C-19 as V-03's "expected failure mode." A model running V-03 has plausible cover to write "I revised the champion entry to include I-PM" as prose without showing the row.

**C-20 analysis:** All five PASS. V-01/V-04/V-05 have named SECTION K after all content. V-02 has SECTION K as content consolidator. V-03 has "Audit Outcomes" table — explicitly labeled as distinct from the verification stage, with the required initial/revision/final columns.

---

## Ranking

| Rank | Variation | Score | Tie-break |
|------|-----------|-------|-----------|
| 1 | **V-04** | 150 | Top-of-prompt structural contract names C-19 and C-20 locations separately + explicit negative rule on SECTION K |
| 2 | **V-05** | 150 | Identical H-K to V-04; conversational A-G is untested secondary axis |
| 3 | **V-01** | 150 | Same mechanics as V-04 without the explicit structural contract — concern separation is implicit |
| 4 | **V-02** | 150 | Highest C-20 evaluability (one section); loses BEFORE comparison and inline gate re-run |
| 5 | **V-03** | 145 | C-19 FAIL — conversational format + no VERIFICATION MODE boundary |

---

## Excellence Signals (V-04)

1. **Top-of-prompt structural contract** names C-19 location (inline blocks) and C-20 location (SECTION K) separately by rule — V-01 achieves the same separation implicitly but doesn't name it, leaving both the V-02 consolidation path and V-03 narrative path open.
2. **Explicit negative rule on terminal section:** "SECTION K does NOT duplicate corrected content." Negative rules eliminate rationalization paths that positive instructions leave open.
3. **Structural contract verification in SECTION K:** "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK containing BEFORE and AFTER content exists at the referenced location" — creates a self-verifying invariant without cross-document tracing.
4. **V-02's counter-example pattern:** stating the failure mode ("a cell reading only 'updated...' without showing the row fails C-19") inside the template cell is more binding than external rubric guidance.
5. **V-05's VERIFICATION MODE boundary:** explicit header between conversational A-G and formal H-K preserves structural enforcement without requiring the full prompt to be formal.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["Top-of-prompt structural contract names C-19 location (inline CORRECTION BLOCKs) and C-20 location (terminal SECTION K) separately -- prevents model from conflating where correction content vs gate state should appear; explicit negative rule on terminal section ('SECTION K does NOT duplicate corrected content') is more robust than positive placement instructions alone", "Content consolidation design: putting corrected content INTO the terminal section satisfies C-19 and C-20 from a single evaluator location; trade-off is loss of BEFORE comparison and inline gate re-run; valid when evaluation economy outweighs transaction traceability", "Explicit counter-example in terminal section template cell definition: stating the exact failure mode at the point where the model fills in the value blocks the rationalization path more effectively than positive instructions alone", "VERIFICATION MODE boundary marker: explicit header between conversational content sections and formal verification sections preserves structural enforcement in H-K while allowing richer domain reasoning in A-G; conversational framing without this boundary fails C-19 because the model cannot infer the mode shift from register alone"]}
```
N J are all structurally required. All PASS.

Evidence note (C-16 through C-18): All five variations have criterion-specific audit blocks (GATES H/I/J or Checks 1/2/3) that name each criterion with an explicit pass condition. Revision obligation mechanisms differ in design but all enforce correction before commit: V-01/V-04/V-05 use inline CORRECTION BLOCK with re-run gate; V-02 uses SECTION K correction cells with a behavioral commitment; V-03 uses ORIGINAL/CORRECTED blocks within the verification stage. All five mechanisms satisfy C-18 because the structural format requires the correction to appear before the artifact is written. All PASS.

---

### New Aspirational Criteria -- C-19 and C-20

#### C-19: Correction transaction content visible in output

**Pass condition:** When a deficiency is found and C-18 requires revision, the revised structural content (updated table row, corrected inertia citation, revised mitigation entry, or equivalent) must appear in the output. A statement "the champion entry was updated" without showing the row fails C-19. Trivially satisfied when initial audit is all-pass.

---

**V-01 -- C-19: PASS**

SECTIONS H, I, and J each contain a formally labeled CORRECTION BLOCK template with explicit BEFORE and AFTER sections:

```
CORRECTION BLOCK -- C-13 (SECTION H)
BEFORE -- [section name]: [Reproduce original rows verbatim]
AFTER -- [section name]: [Write corrected rows with inertia ID citations]
GATE H re-run: [updated citation table; N >= 3]
```

The instruction "Reproduce the original table row(s)" and "Write the corrected content" forces structural content to appear. The SECTION K behavioral commitment adds: "For every 'Revision Performed: Yes' entry, the deficient content was revised, the corrected content appears in the corresponding CORRECTION BLOCK above." C-19 PASS.

---

**V-02 -- C-19: PASS**

V-02 inverts V-01's architecture: when a gate fails, corrected content goes directly into SECTION K's "Corrected content" cells. The CORRECTION RULE states: "When any of GATES H, I, or J fail, do NOT write inline correction blocks. Write the corrected content into the 'Corrected Content' column of SECTION K."

V-02 explicitly guards C-19 with: "A 'Corrected content' cell reading only 'updated the champion entry to include inertia ID' without showing the updated row fails C-19." Template provides full-row examples. C-19 PASS.

Note: V-02 has no BEFORE column -- only corrected (AFTER) content. An evaluator can verify the correction satisfies the pass condition but cannot compare before/after in situ. C-19 passes because the rubric requires only that the revised content is visible, not that original content is also preserved.

---

**V-03 -- C-19: FAIL**

V-03 uses a conversational second-person register with Check 1/2/3 in the "Verification stage." When a check fails, the correction format is:

```
Stage [name], corrected:
ORIGINAL: [reproduce the original content]
CORRECTED: [write the revised content]
```

The ORIGINAL/CORRECTED format does require reproducing content, but the conversational framing has two failure vectors the formal BEFORE/AFTER blocks do not:

1. The format is embedded in prose guidance under each "If [Check] fails:" paragraph, not in a named structural block. The model may treat ORIGINAL/CORRECTED as a guideline rather than a required template.
2. The conversational register signals reasoning-through-analysis rather than form-filling -- increasing the probability of narrative substitution ("the champion row now cites I-07") instead of content materialization.

The variation design notes explicitly identify C-19 as "the expected failure mode" for V-03 and rate expected C-19 outcome as UNCERTAIN. No named CORRECTION BLOCK creates a structural slot the model must populate. A model running V-03 can write "I have revised the champion entry to include I-PM as the EM inertia anchoring the bridge" and produce only that sentence without violating the template's visible structure. C-19 FAIL.

---

**V-04 -- C-19: PASS**

V-04 uses inline CORRECTION BLOCKs structurally identical to V-01. Additionally, V-04 adds a top-of-prompt structural contract that explicitly names C-19's mechanism:

```
Structural contract:
- Corrected content lives in inline CORRECTION BLOCKS (adjacent to the gate check) -- this is the C-19 location.
- SECTION K records gate states and references inline CORRECTION BLOCK locations -- this is the C-20 location.
- SECTION K does NOT duplicate corrected content.
```

This contract prevents model ambiguity about where to materialize corrected content. SECTION K's structural contract verification reinforces: "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK containing BEFORE and AFTER content exists in the output at the referenced location." C-19 PASS -- strongest structural enforcement.

---

**V-05 -- C-19: PASS**

V-05 shifts content sections A-G to conversational register but retains formal SECTION/GATE structure for H-K (marked by an explicit "VERIFICATION MODE" header). SECTIONS H, I, J use the same CORRECTION BLOCK template as V-04. SECTION K is identical to V-04. The register shift does not affect the verification sections. C-19 PASS.

---

#### C-20: Single named terminal section consolidates gate states

**Pass condition:** A single named structural section appears after all content sections; lists initial result (PASS/FAIL), revision performed (yes/no), and final result for each of C-13, C-14, C-15. Distinct from the C-16 self-audit block (which performs the check). C-20 fails automatically if C-16 fails.

---

**V-01 -- C-20: PASS**

SECTION K appears after SECTIONS H/I/J. Named "Gate State Record"; has Initial/Revision/Correction Location/Final columns for C-13, C-14, C-15. Explicitly stated as distinct from SECTIONS H/I/J ("which performed the checks; SECTION K consolidates the final state"). C-20 PASS.

---

**V-02 -- C-20: PASS**

SECTION K in V-02 is the "Gate State Record with Corrected Content" -- serves as both the C-19 and C-20 location. Records initial result, revision performed, corrected content (if Yes), and final result per criterion. Named section, appears after all content sections and gate checks. Behavioral commitment states all three Final Gate Results must show PASS. C-20 PASS.

Highest C-20 evaluability: evaluator checking C-18/C-19/C-20 reads only SECTION K. Trade-off: BEFORE content absent, inline gate re-run mechanism removed.

---

**V-03 -- C-20: PASS**

V-03's "Audit Outcomes" section (terminal section after verification stage checks) provides:

| Criterion | Initial Result | Revision Performed | Final Result |
|-----------|---------------|-------------------|-------------|
| C-13 -- Inertia propagation | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-14 -- Champion double-anchor | [PASS / FAIL] | [Yes / No] | [PASS] |
| C-15 -- Churn action test | [PASS / FAIL] | [Yes / No] | [PASS] |

Template explicitly labels this as distinct: "This section is distinct from the verification stage above (which performed the checks); this section records the consolidated result." Table has required columns (initial/revision/final) for C-13, C-14, C-15. Appears after all stages and checks. C-20 PASS.

Note: design notes rate this as PASS-RISK because conversational framing may blur the boundary. However, the named section with explicit table structure satisfies C-20's requirements as a design-time evaluation.

---

**V-04 -- C-20: PASS**

SECTION K identified as the C-20 location in the top-of-prompt structural contract. Table: Initial/Revision/Correction Block Location/Final per criterion. Explicit negative rule: "SECTION K does NOT contain or duplicate corrected content -- it references CORRECTION BLOCK locations." Structural contract verification statement creates a verifiable invariant. C-20 PASS -- highest design clarity.

---

**V-05 -- C-20: PASS**

SECTION K identical to V-04 (formal verification mode retained). C-20 PASS.

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-19 | 5 | 5 | 5 | **0** | 5 | 5 |
| C-20 | 5 | 5 | 5 | 5 | 5 | 5 |
| **Total** | **150** | **150** | **150** | **145** | **150** | **150** |

---

## Ranking

Four variations reach the maximum of 150. V-03 scores 145, excluded from the top tier by C-19 FAIL.

Within-score ordering for 150-tier by evaluability and design clarity:

| Rank | Variation | Score | Distinguishing Property |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 150 | Top-of-prompt structural contract explicitly names C-19 location (inline CORRECTION BLOCKs) and C-20 location (SECTION K); explicit negative rule on SECTION K; clearest concern separation |
| 2 | **V-05** | 150 | Same H-K enforcement as V-04; conversational A-G may improve Named Inertia and champion rationale depth -- secondary test axis not yet scored |
| 3 | **V-01** | 150 | Correct structural design with BEFORE/AFTER blocks and SECTION K Correction Location column; implicit concern separation (no structural contract at top) -- equivalent mechanics to V-04, weaker explicitness |
| 4 | **V-02** | 150 | Single-location evaluability (C-19 and C-20 checked in one place); BEFORE content absent; inline re-run gate removed; highest consolidation, lowest per-criterion transaction traceability |
| 5 | **V-03** | 145 | Conversational framing fails to enforce content materialization for C-19; ORIGINAL/CORRECTED template is structurally weaker than named CORRECTION BLOCK format |

---

## C-19 Failure Analysis: V-03

The failure is not about template absence -- the ORIGINAL/CORRECTED format exists. The failure is about structural enforcement grade.

**What V-03 provides for C-19:** "ORIGINAL: [reproduce the original content]" and "CORRECTED: [write the revised content]" -- both present in the template.

**Why this fails the design-time evaluation:**

1. The correction format is embedded in prose guidance under conditional paragraphs ("If Check 1 fails..."). No named structural block (e.g., "CORRECTION BLOCK -- C-13") creates a named slot the model must populate. The ORIGINAL/CORRECTED lines are formatting suggestions within a prose paragraph, not named structural elements.

2. The conversational register of the verification stage (same as content stages) does not signal a structural mode change. V-05 solves this with an explicit "VERIFICATION MODE" header between SECTION G and SECTION H. V-03 has no equivalent boundary marker, so the model may interpret its full output as single-register prose, making it easier to substitute narrative for structural content.

3. A model running V-03 that finds a C-14 deficiency may write: "I will revise the champion entry to include I-PM. C-01's EA position gives credibility to the EM team because..." -- embedding the correction narrative into Check 2 prose rather than producing a CORRECTED row. The ORIGINAL/CORRECTED template does not force a row; it suggests one.

**Causal path:** conversational register + no named block header + no VERIFICATION MODE boundary = insufficient structural enforcement for C-19.

---

## Excellence Signals

**From V-04 (top-ranked):**

1. **Top-of-prompt structural contract separates C-19 and C-20 by name.** V-04 states at the prompt's opening: "Corrected content lives in inline CORRECTION BLOCKS -- this is the C-19 location. SECTION K records gate states and references inline CORRECTION BLOCK locations -- this is the C-20 location." This prevents the model from conflating where each type of evidence should appear. V-01 achieves the same separation implicitly (both structures exist) but does not name the separation rule. A model encountering V-01 without the contract could rationalize consolidating content into SECTION K (V-02 pattern) or omitting structural content from inline blocks (V-03 pattern). V-04's explicit contract closes both failure paths.

2. **Explicit negative rule on the terminal section.** "SECTION K does NOT contain or duplicate corrected content -- it references CORRECTION BLOCK locations." Negative rules are stronger than positive placement instructions because they eliminate rationalization paths. "Put corrected content in inline blocks" allows the model to also put content in SECTION K. "SECTION K does NOT duplicate corrected content" removes that option entirely. This pattern generalizes: for any structural invariant involving location constraints, a negative rule on the terminal section prevents content bleeding across structural boundaries.

3. **Structural contract verification statement in SECTION K.** SECTION K's closing statement: "For every 'Revision Performed: Yes' entry, a CORRECTION BLOCK containing BEFORE and AFTER content exists in the output at the referenced location." This creates a self-verifying invariant -- the terminal section records a claim about the inline blocks, making the C-19/C-20 relationship evaluable without cross-document tracing.

**From V-02:**

4. **Content consolidation design.** V-02 discovers that both C-19 and C-20 can be satisfied from a single terminal section -- an evaluator checking C-18, C-19, and C-20 reads only SECTION K. Trade-off: loss of BEFORE content and per-section gate re-runs. The pattern is valuable when evaluation economy (one place to check) is more important than transaction traceability (before/after visible at point of change).

5. **Explicit counter-example in terminal section template cell.** V-02's SECTION K contains: "A 'Corrected content' cell reading only 'updated the champion entry to include inertia ID' without showing the updated row fails C-19." Defining failure by counter-example at the point where the model fills in the value is more binding than positive instructions -- it names the exact rationalization path to block, at the point of decision.

**Pattern distinguishing V-04 from V-01 (same score, different rank):**

V-01 achieves PASS on C-19 and C-20 through structural presence (inline blocks exist, SECTION K exists). V-04 achieves PASS through structural contract (the relationship between blocks and SECTION K is named, negative rules are applied, invariants are stated). V-04 is more robust to edge cases -- a model generating a long artifact with multiple corrections can follow the structural contract to ensure all CORRECTION BLOCKs appear in the right place and SECTION K references them correctly. V-01's implicit design relies on the model inferring the same contract from structure alone.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["Top-of-prompt structural contract names C-19 location (inline CORRECTION BLOCKs) and C-20 location (terminal SECTION K) separately -- prevents model from conflating where correction content vs gate state should appear; explicit negative rule on terminal section ('SECTION K does NOT duplicate corrected content') is more robust than positive placement instructions alone", "Content consolidation design: putting corrected content INTO the terminal section satisfies C-19 and C-20 from a single evaluator location; trade-off is loss of BEFORE comparison and inline gate re-run; valid when evaluation economy outweighs transaction traceability", "Explicit counter-example in terminal section template cell definition: stating the exact failure mode at the point where the model fills in the value blocks the rationalization path more effectively than positive instructions alone", "VERIFICATION MODE boundary marker: explicit header between conversational content sections and formal verification sections preserves structural enforcement in H-K while allowing richer domain reasoning in A-G; conversational framing without this boundary fails C-19 because the model cannot infer the mode shift from register alone"]}
```
