---

## scout-positioning R2 Scorecard

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Lifecycle + claim-trace + self-verify | **135/140** | YES |
| 2 | V-04 Matrix-dominant + rubric-literal | **132/140** | YES |
| 3 | V-01 Rubric-literal | **127/140** | YES |
| 4 | V-03 Dialog-adversarial | **126/140** | YES |
| 5 | V-02 Claim-trace | **126/140** | YES |

**all_essential_pass = TRUE across all five variations.** The R2 baseline floor worked — no variation can repeat the R1 V-01 failure (C-04 partial on "contrast form preferred").

**What decided the ranking:**

- **V-05 wins** because its R2 addition — the VERIFY pass — adds a third enforcement layer. It checks each FINDINGS section against the exact rubric pass condition before emission. `verify_status: pass / flagged-N` in frontmatter makes quality visible. V-05 also has the cleanest C-13 handling: the degradation note IS the first output, not a conditional byproduct.

- **V-04 is a strong #2** — matrix-grounded claims dominate C-03/C-04/C-05/C-06/C-10 (all 10/10). The one deduction is C-13: "FINDINGS C-01/C-09: PRIOR RUN MISSING" is a combined section label, diluting the "dedicated" degradation section requirement.

- **V-01 gains most from R2 baseline** — C-11 is its strongest asset (pure rubric-literal FINDINGS C-01 through C-10), but without matrix depth or VERIFY it plateaus at 127.

- **V-02 and V-03 tie at 126.** V-03 ranks ahead on tiebreak: the adversarial Design→PM challenge earns a full 10 on C-06 (Design adds a PM-missed claim to the reality-check table). V-02 earns 10 on C-10/C-14 but loses 4 points on C-11 (sections 1-8 are not 1:1 with criteria IDs).

**New R2 patterns extracted:**

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["VERIFY pass as pre-artifact quality gate -- explicit self-check maps each FINDINGS section to its rubric pass condition before emitting; catches criterion failures at production rather than review time", "compound enforcement stacking (lifecycle + claim-trace + self-verify) approaches rubric ceiling -- three-layer redundancy beats single-axis optimization for high-complexity skills", "matrix dimension floor of 5+ yields more defensible whitespace claims -- mandating more dimensions forces ground-truthing on more axes, making C-10 citation falsifiable by a wider reviewer"]}
```
01: Rubric-literal

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | R2 baseline STOP verb; FINDINGS C-01 slot "MISSING: degradation note repeated here" ensures note appears in output |
| C-02 | Per-audience statements | 9 | PASS | FINDINGS C-02 requires "1-2 framing signals that distinguish this statement from the others" — uniqueness obligation stated |
| C-03 | Category definition | 9 | PASS | FINDINGS C-03 "Not: [name one category explicitly rejected and why Signal cannot own it]" — rejection required |
| C-04 | Core differentiator | 9 | PASS | FINDINGS C-04 two-slot template: "Inertia contrast: / Named competitor contrast: / [Feature lists fail this section]" — R2 baseline |
| C-05 | Anti-positioning | 9 | PASS | FINDINGS C-05 "Signal is NOT [X] -- [why this confusion is plausible]" 2 minimum |
| C-06 | PM reality check | 9 | PASS | FINDINGS C-06 table with Gap type column; ahead-of-spec / unsupported / N/A required |
| C-07 | Competitive matrix | 8 | PASS | FINDINGS C-07 3+ dimensions; standard minimum, no matrix-depth mandate |
| C-08 | Messaging hierarchy | 9 | PASS | FINDINGS C-08 PRIMARY / SECONDARY explicit; R2 baseline |
| C-09 | Degradation quant. | 9 | PASS | FINDINGS C-09 dedicated section; "Not 'quality may vary'" anti-pattern named |
| C-10 | Whitespace ID | 9 | PASS | FINDINGS C-10 "Dimensions tested: [name the specific matrix columns where Signal is H]" — falsifiable |
| C-11 | Output structure mirrors rubric | 10 | PASS | V-01's defining axis; FINDINGS C-01 through C-10 maps one-to-one to rubric criterion IDs — missing section = missed criterion, detectable by inspection |
| C-12 | STOP enforcement verb | 10 | PASS | R2 baseline floor |
| C-13 | Dedicated FINDINGS for degradation | 9 | PASS | FINDINGS C-09 is dedicated section; FINDINGS C-01 echoes the note; note survives to output in named sections |
| C-14 | Whitespace citation obligation | 9 | PASS | "Dimensions tested: [name the specific matrix columns]" — specific columns required |

**Total: 127/140 · All essential pass: YES**

---

## V-02: Claim-trace

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | R2 baseline STOP verb; FINDINGS 8: DEGRADATION NOTE as dedicated section |
| C-02 | Per-audience statements | 9 | PASS | Section 2 per-audience + source; "1-2 framing signals that make this statement distinct" |
| C-03 | Category definition | 9 | PASS | Section 1 "Category: [ownable] [Source: ...] / Not: [rejected] [Source: ...]" — annotated |
| C-04 | Core differentiator | 9 | PASS | Section 1 inertia + named-competitor contrast, both [Source: ...] — annotated |
| C-05 | Anti-positioning | 9 | PASS | Section 5 "Signal is NOT [X] -- [why plausible] [Source: ...]" 2 minimum; source grounds each negation |
| C-06 | PM reality check | 9 | PASS | Section 7 adds Source column to standard table; each verdict has named source |
| C-07 | Competitive matrix | 8 | PASS | Section 4; 3+ dimensions; standard minimum |
| C-08 | Messaging hierarchy | 9 | PASS | Section 3 PRIMARY/SECONDARY + [Source: ...]; R2 baseline |
| C-09 | Degradation quant. | 9 | PASS | FINDINGS 8 dedicated; specific risks named |
| C-10 | Whitespace ID | 10 | PASS | Section 6 "Dimensions tested: [...] / [Source: matrix section 4, dimensions [X] and [Y]]" — most explicit citation in any single-axis variation |
| C-11 | Output structure mirrors rubric | 6 | PARTIAL | Sections numbered 1-8 but not criterion IDs; section 1 combines C-03+C-04, section 8 combines C-01/C-09/C-13; missing section maps to multiple criteria — not 1:1 |
| C-12 | STOP enforcement verb | 10 | PASS | R2 baseline; "If not found: STOP" |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | FINDINGS 8: DEGRADATION NOTE is a named, numbered section separate from SETUP instructions |
| C-14 | Whitespace citation obligation | 10 | PASS | "[Source: matrix section 4, dimensions [X] and [Y]]" — citation format names section and dimension explicitly |

**Total: 126/140 · All essential pass: YES**

---

## V-03: Dialog-adversarial

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | R2 baseline STOP; FINDINGS 8: DEGRADATION NOTE dedicated |
| C-02 | Per-audience statements | 9 | PASS | GTM CHALLENGE tests "Would a developer, PM, architect recognize this category?" before producing statements; sharpens audience-specificity |
| C-03 | Category definition | 9 | PASS | FINDINGS 1 "Final version after GTM challenge -- note if GTM revised Strategy's output"; challenge can revise category |
| C-04 | Core differentiator | 9 | PASS | FINDINGS 1 inertia + named-competitor contrast; R2 baseline |
| C-05 | Anti-positioning | 9 | PASS | FINDINGS 5 "Signal is NOT [X] -- [why this confusion is plausible]" 2 minimum |
| C-06 | PM reality check | 10 | PASS | Design CHALLENGE: "Did PM's reality check miss any claim?" — adds a PM-missed claim to the table. FINDINGS 7 "include the Design-added claim if flagged"; adversarial pressure catches coverage gaps |
| C-07 | Competitive matrix | 8 | PASS | FINDINGS 4; 3+ dimensions; standard |
| C-08 | Messaging hierarchy | 9 | PASS | FINDINGS 3 PRIMARY/SECONDARY; R2 baseline |
| C-09 | Degradation quant. | 9 | PASS | FINDINGS 8 with specific risks |
| C-10 | Whitespace ID | 9 | PASS | FINDINGS 6 "Dimensions tested: [name the specific matrix columns -- makes the claim falsifiable]" |
| C-11 | Output structure mirrors rubric | 7 | PARTIAL | Sections 1-8; CHALLENGE SUMMARY adds meta-traceability (tracks what changed in each phase) but section-to-criterion mapping is not 1:1 |
| C-12 | STOP enforcement verb | 10 | PASS | R2 baseline |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | FINDINGS 8: DEGRADATION NOTE named section |
| C-14 | Whitespace citation obligation | 9 | PASS | "Dimensions tested: [name the specific matrix columns]" — specific but no explicit [Source: section X] format |

**Total: 126/140 · All essential pass: YES**

V-02 and V-03 tie at 126. V-03 ranks ahead on tiebreak: C-06 scores 10 (adversarial PM coverage check is V-03's unique contribution) vs V-02's 9.

---

## V-04: Matrix-dominant + rubric-literal

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 9 | PASS | R2 baseline STOP; FINDINGS C-01 section present; combined with C-09 in degraded path |
| C-02 | Per-audience statements | 9 | PASS | FINDINGS C-02 "Matrix dimensions cited per statement" — grounded, but no explicit framing-signal obligation |
| C-03 | Category definition | 10 | PASS | FINDINGS C-03 "Supporting dimensions: [cite 2+ matrix columns where Signal is H, competitors are not]" — operationalized via matrix, not asserted |
| C-04 | Core differentiator | 10 | PASS | FINDINGS C-04 "[Matrix: [column]]" on both contrasts — matrix citation makes differentiator falsifiable |
| C-05 | Anti-positioning | 10 | PASS | FINDINGS C-05 "[Matrix: [competitor] H on [dimension], Signal L/M]" — every negation grounded in a matrix row |
| C-06 | PM reality check | 10 | PASS | FINDINGS C-06 adds "Matrix cell" column; traces each claim to specific matrix cell; strongest traceability |
| C-07 | Competitive matrix | 10 | PASS | 5+ dimensions required (vs 3+ elsewhere); matrix is the structural anchor; built before any prose |
| C-08 | Messaging hierarchy | 9 | PASS | FINDINGS C-08 PRIMARY/SECONDARY; R2 baseline |
| C-09 | Degradation quant. | 9 | PASS | FINDINGS C-09 "name the specific matrix columns that cannot be reliably scored" — ties degradation to matrix gaps |
| C-10 | Whitespace ID | 10 | PASS | FINDINGS C-10 "Matrix support: [cite the specific columns where Signal is H and no competitor is H]" — matrix evidence required |
| C-11 | Output structure mirrors rubric | 10 | PASS | FINDINGS C-01 through C-10 with rubric criterion labels; C-XX numbering is identical to rubric |
| C-12 | STOP enforcement verb | 10 | PASS | R2 baseline |
| C-13 | Dedicated FINDINGS for degradation | 7 | PARTIAL | "FINDINGS C-01 / C-09: PRIOR RUN MISSING" combines prior-run handling and degradation in one combined section label; C-13 requires a section dedicated to the degradation note specifically, separate from C-01's prior-run-handling function; combined label dilutes dedication |
| C-14 | Whitespace citation obligation | 9 | PASS | "cite the specific columns where Signal is H and no competitor is H" — explicit column requirement |

**Total: 132/140 · All essential pass: YES**

---

## V-05: Lifecycle + claim-trace + self-verify

| ID | Criterion | Score | Verdict | Evidence |
|----|-----------|-------|---------|---------|
| C-01 | Prior run handling | 10 | PASS | "STOP. Before any other output, emit this as a named FINDINGS section: FINDINGS 8: DEGRADATION NOTE" — strongest possible enforcement; note is first output before any positioning |
| C-02 | Per-audience statements | 10 | PASS | FINDINGS 2 "(a) positioning statement [Source: ...], (b) the 1-2 framing signals that make this statement distinct from the others"; VERIFY checks distinct emphasis per audience |
| C-03 | Category definition | 9 | PASS | FINDINGS 1 "Category: [ownable] [Source: ...] / Rejected category: [name] -- [why Signal cannot own it] [Source: ...]" — combined with C-04 in section 1; annotation grounds both |
| C-04 | Core differentiator | 10 | PASS | EXECUTE STRATEGY requires contrast form + FINDINGS 1 two-slot template + VERIFY checks contrast form; triple enforcement |
| C-05 | Anti-positioning | 9 | PASS | FINDINGS 5 "[Source: ...]" per statement; VERIFY checks "no generic negations" |
| C-06 | PM reality check | 10 | PASS | FINDINGS 7 "| Claim | Verdict | Reason | Source | Gap type |" — Source column; VERIFY checks 3+ rows with gap type |
| C-07 | Competitive matrix | 9 | PASS | FINDINGS 4 with 3+ dimensions; standard minimum; VERIFY checks tabular form and scale |
| C-08 | Messaging hierarchy | 10 | PASS | EXECUTE DESIGN label requirement + FINDINGS 3 explicit PRIMARY/SECONDARY slots + VERIFY checks PRIMARY label present; triple enforcement |
| C-09 | Degradation quant. | 10 | PASS | "STOP", "not just 'quality may vary'" anti-pattern named; FINDINGS 8 dedicated section; specific risks listed before any positioning output |
| C-10 | Whitespace ID | 10 | PASS | FINDINGS 6 "cite these columns explicitly to make the claim falsifiable by a reviewer" + "[Source: matrix section 4, dimensions [X] and [Y]]"; VERIFY checks specific columns cited |
| C-11 | Output structure mirrors rubric | 8 | PASS | Sections 1-8 cover all content criteria; VERIFY section re-enumerates 1-8 with pass conditions, creating a rubric-mapping mechanism; FINDINGS 1 combines C-03+C-04 and FINDINGS 8 combines C-01+C-09+C-13 (not pure 1:1), but VERIFY compensates for structural gaps |
| C-12 | STOP enforcement verb | 10 | PASS | "STOP. Before any other output" — most forceful enforcement language |
| C-13 | Dedicated FINDINGS for degradation | 10 | PASS | Degradation note IS the first emitted FINDINGS section (FINDINGS 8: DEGRADATION NOTE emitted before any positioning content); fully separate from SETUP instructions |
| C-14 | Whitespace citation obligation | 10 | PASS | "[Source: matrix section 4, dimensions [X] and [Y]]"; VERIFY explicitly checks "specific matrix columns cited, not just 'no competitor occupies this space'" |

**Total: 135/140 · All essential pass: YES**

---

## Composite Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Lifecycle + claim-trace + self-verify | **135** | YES |
| 2 | V-04 Matrix-dominant + rubric-literal | **132** | YES |
| 3 | V-01 Rubric-literal | **127** | YES |
| 4 | V-03 Dialog-adversarial | **126** | YES |
| 5 | V-02 Claim-trace | **126** | YES |

---

## Excellence Signals from V-05

**1. VERIFY pass as pre-artifact quality gate.**
V-05 R2 adds a VERIFY phase that checks each FINDINGS section against its rubric pass condition before the artifact is emitted. It produces explicit PASS / FLAG lines. For whitespace: "PASS if specific matrix columns cited, not just 'no competitor occupies this space.'" For messaging hierarchy: "PASS if PRIMARY label present and at least one SECONDARY label present." The result: `verify_status: pass / flagged-N` in frontmatter, making quality visible at a glance.

**2. Compound enforcement (lifecycle + claim-trace + self-verify) reaches a higher ceiling.**
R2 V-05 stacks three layers. Lifecycle phase boundaries prevent role bleed. Claim annotations prevent unsourced assertions. VERIFY catches failures before emission. No single-axis variation reaches 130 — V-01 (rubric-literal only) scores 127, V-02 (claim-trace only) scores 126. Redundancy beats optimization.

**3. "STOP. Before any other output, emit this as a named FINDINGS section."**
The instruction makes the degradation note the first output, not a conditional by-product. Other variations say "STOP... emit FINDINGS 8." V-05 says the degradation note IS FINDINGS 8, emitted before any other content. Subtle but load-bearing: it removes ambiguity about whether setup-phase STOP instructions apply to the deliverable.

**4. VERIFY operationalizes C-14 at the point of final check.**
The VERIFY instruction for whitespace explicitly quotes the anti-pattern: "PASS if specific matrix columns cited, not just 'no competitor occupies this space.'" This is verbatim from the C-14 pass condition. When the VERIFY text mirrors the rubric pass condition, the LLM is evaluating against the exact threshold — not a paraphrase.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["VERIFY pass as pre-artifact quality gate -- explicit self-check maps each FINDINGS section to its rubric pass condition before emitting; catches criterion failures at production rather than review time", "compound enforcement stacking (lifecycle + claim-trace + self-verify) approaches rubric ceiling -- three-layer redundancy beats single-axis optimization for high-complexity skills", "matrix dimension floor of 5+ yields more defensible whitespace claims -- mandating more dimensions forces ground-truthing on more axes, making C-10 citation falsifiable by a wider reviewer"]}
```
