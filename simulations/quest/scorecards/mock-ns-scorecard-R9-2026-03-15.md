## Scoring: mock-ns Round 9 (Rubric v8)

---

### V-01 — Phrasing Register ("You" Address Throughout)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Essential | PASS | Header block complete, all six fields present |
| C-02 Essential | PASS | Category assignment table complete and correct |
| C-03 Essential | PASS | Mock body follows golden rubric structure |
| C-04 Essential | PASS | Flag present, category-matched |
| C-05 Essential | PASS | Artifact path convention correct |
| C-06 Recommended | PASS | Default table present with correct defaults |
| C-07 Recommended | PASS | All three category warnings complete; includes "REAL-REQUIRED at Tier 2+" |
| C-08 Recommended | PASS | Next-step line present |
| C-09 | PASS | Case 1 covers tier-conditional flag for critical namespaces |
| C-10 | PASS | Dedicated `> TOPICS.md:` emit line |
| C-11 | PASS | FLAG computed as named variable in S-3 before A-1 |
| C-12 | PASS | Exclusion column in default table with explicit EXCLUDED language |
| C-13 | PASS | Fidelity warning in lead position (A-2 before A-3) |
| C-14 | PASS | Prohibition at compute site (S-3) and consumption site (A-1) |
| C-15 | PASS | Three-column default table with dedicated Exclusion constraint column |
| C-16 | PASS | "You MUST NOT recompute FLAG anywhere in this run -- not in any step, any conditional branch..." |
| C-17 | PASS | "Your first instruction in this step: copy FLAG from S-3 verbatim" |
| C-18 | PASS | Named classes: conditional branch, fallback path, regeneration sequence, other execution context, paths bypassing normal step order |
| C-19 | PASS | "before you list any field, before any category lookup, before any formatting instruction, or any other instruction you carry out in this step. No other instruction in A-1 precedes this one." |
| C-20 | PASS | "if you rederive FLAG here, you will produce a category mismatch invisible to downstream tooling and will silently corrupt the artifact's trust tier" |
| C-21 | PASS | "Every execution path that reaches A-1 carries the FLAG value you emit here. No path is exempt." |
| C-22 | PASS | "or any other instruction you carry out in this step" |
| C-23 | PASS | "If you allow any path to modify FLAG after this point, the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site." |
| C-24 | PASS | "Every instruction you follow in this step -- named or unnamed -- is governed by this instruction. No instruction in this step is exempt." |
| C-25 | PASS | "the guarantee stated above is broken" — explicit causal bridge; affirmative closure precedes consequence |
| C-26 | PASS | "producing the same silent category mismatch described at the consumption site" |

**Composite**: (5/5 × 60) + (3/3 × 30) + (18/18 × 10) = 60 + 30 + 10 = **100**

---

### V-02 — Output Format (Tabular Prohibition Blocks)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 Essential | PASS × 5 | All five essential criteria structurally present and correct |
| C-06–C-08 Recommended | PASS × 3 | Default table, full fidelity warnings, next-step line |
| C-09 | PASS | Case 1 present |
| C-10 | PASS | Dedicated TOPICS.md emit line |
| C-11 | PASS | FLAG as named variable in S-3 before A-1 |
| C-12 | PASS | Exclusion column with EXCLUDED language |
| C-13 | PASS | A-2 positions warning as lead section |
| C-14 | PASS | Prohibition rows present at both S-3 table and A-1 table |
| C-15 | PASS | Three-column default table |
| C-16 | PASS | Scope row: "FLAG MUST NOT be recomputed anywhere in this run" |
| C-17 | PASS | First rule row: "Copy FLAG from S-3 verbatim. Do not rederive it." |
| C-18 | PASS | Path classes row names all required classes plus bypass-order clarifier |
| C-19 | PASS | Anti-displacement row + Declarative closure row together satisfy the criterion |
| C-20 | PASS | Failure consequence row at A-1 table: "silently corrupts the artifact's trust tier; the corruption is undetectable without manual header inspection" |
| C-21 | PASS | Affirmative closure row + No-exemption row |
| C-22 | PASS | Anti-displacement row: "or any other instruction in this step" |
| C-23 | PASS | Failure consequence row at S-3 table |
| C-24 | PASS | All-governed row + No-exemption row at A-1 |
| C-25 | PASS | Guarantee-break row: "This violation breaks the closure guarantee stated in the Affirmative closure row above" — row-isolated, cannot be skimmed |
| C-26 | PASS | Cross-site reference row: "...same silent category mismatch described at the consumption site (see A-1 Failure consequence row below)" — bidirectional navigation |

**Composite**: (5/5 × 60) + (3/3 × 30) + (18/18 × 10) = **100**

Notable: C-25 and C-26 appear as individually scannable rows rather than end-of-paragraph clauses. V-02 is the first form where the cross-site reference is bidirectional — the S-3 table names the A-1 row and the A-1 table is the reference target.

---

### V-03 — Inertia Framing (Consequence-Before-Prohibition at S-3)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 Essential | PASS × 5 | All essential criteria met |
| C-06–C-08 Recommended | PASS × 3 | Default table, full warnings, next-step line |
| C-09 | PASS | Case 1 present |
| C-10 | PASS | Dedicated TOPICS.md emit |
| C-11 | PASS | FLAG as named variable in S-3 |
| C-12 | PASS | Exclusion column present |
| C-13 | PASS | Lead-section warning |
| C-14 | PASS | Prohibition at both S-3 and A-1 |
| C-15 | PASS | Three-column default table |
| C-16 | PASS | "FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional branch, any fallback path..." |
| C-17 | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim" |
| C-18 | PASS | All three required path classes named plus bypass-order clarifier |
| C-19 | PASS | "before any field is listed, before any category lookup, before any formatting instruction, or any other instruction in this step. No instruction in A-1 precedes this rule." |
| C-20 | PASS | "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier" |
| C-21 | PASS | "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." |
| C-22 | PASS | "or any other instruction in this step" |
| C-23 | PASS | Failure consequence IS present at compute site (front-loaded FAILURE CONSEQUENCE block): mechanism and downstream effect both named |
| C-24 | PASS | "Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." |
| C-25 | **FAIL** | Structurally incompatible: consequence precedes the affirmative closure, so "the guarantee stated above is broken" has no referent. The front-loaded consequence is an independent warning, not a violation of a stated commitment. |
| C-26 | PASS | "producing the same silent category mismatch described at the consumption site" — present in the front-loaded consequence block; ordering-independent |

**Composite**: (5/5 × 60) + (3/3 × 30) + (17/18 × 10) = 60 + 30 + 9.44 = **99.4**

C-25 is the sole miss. The consequence-first form satisfies C-23 (consequence present) and C-26 (cross-site reference present) but cannot satisfy C-25 because the causal bridge — "this breaks the guarantee stated above" — requires the guarantee to precede the consequence.

---

### V-04 — Role Sequence + Lifecycle Emphasis (Merged CLASSIFY-AND-FLAG + Procedure Overview)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 Essential | PASS × 5 | All essential criteria met |
| C-06–C-08 Recommended | PASS × 3 | Default table, full warnings, next-step line |
| C-09 | PASS | Case 1 present |
| C-10 | PASS | Dedicated TOPICS.md emit |
| C-11 | PASS | FLAG computed as named variable in CLASSIFY-AND-FLAG step before A-1 |
| C-12 | PASS | Exclusion column present |
| C-13 | PASS | Lead-section warning |
| C-14 | PASS | Prohibition at compute site (S-2/CLASSIFY-AND-FLAG) and consumption site (A-1) |
| C-15 | PASS | Three-column default table |
| C-16 | PASS | "FLAG MUST NOT be recomputed anywhere in this run -- not in any step, any conditional branch..." |
| C-17 | PASS | "The first rule of this step is: copy FLAG from S-2 verbatim" |
| C-18 | PASS | Conditional branch, fallback path, regeneration sequence, other execution context, bypass-order clarifier |
| C-19 | PASS | Anti-displacement language with named instruction types and declarative closure |
| C-20 | PASS | "Inertia risk: re-deriving FLAG here produces a category mismatch invisible to downstream tooling" with detailed consequence |
| C-21 | PASS | "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." |
| C-22 | PASS | "or any other instruction in this step" |
| C-23 | PASS | "If any path modifies FLAG after this point..." — consequence follows affirmative closure |
| C-24 | PASS | "Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." |
| C-25 | PASS | "the guarantee stated above is broken" — affirmative closure precedes consequence; step merge does not break ordering |
| C-26 | PASS | "producing the same silent category mismatch described at the consumption site" |

**Composite**: (5/5 × 60) + (3/3 × 30) + (18/18 × 10) = **100**

Notable: Procedure overview table (before any step begins) makes the CLASSIFY-AND-FLAG → A-1 data flow visible upfront. The row "A-1: copy FLAG from S-2 verbatim" appears in the overview before the executor encounters any prohibition, pre-loading the constraint as architecture rather than instruction.

---

### V-05 — Full Convergence + Protection Chain Audit

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 Essential | PASS × 5 | All essential criteria met |
| C-06–C-08 Recommended | PASS × 3 | Default table, full warnings, next-step line |
| C-09 | PASS | Case 1 present |
| C-10 | PASS | Dedicated TOPICS.md emit |
| C-11 | PASS | FLAG as named variable in S-3 |
| C-12 | PASS | Exclusion column present |
| C-13 | PASS | Lead-section warning |
| C-14 | PASS | Prohibition at both sites |
| C-15 | PASS | Three-column default table |
| C-16 | PASS | Scope prohibition present in prose paragraph and in layer [1] audit entry |
| C-17 | PASS | "The first rule of this step is: copy FLAG from S-3 verbatim" |
| C-18 | PASS | Named path classes in prose + confirmed in layer [2] audit entry |
| C-19 | PASS | Anti-displacement language with named instruction types and declarative closure |
| C-20 | PASS | "Inertia risk: re-deriving FLAG here produces a category mismatch..." |
| C-21 | PASS | Prose + layer [3] audit: "every execution path that reaches A-1 carries the FLAG value emitted here; no path is exempt" |
| C-22 | PASS | "or any other instruction in this step" |
| C-23 | PASS | "any modification after this point produces a corrupted value at A-1 that is indistinguishable from a correctly-computed one" — in layer [4] |
| C-24 | PASS | "Every instruction in this step -- named or unnamed -- is governed by this rule. No instruction in this step is exempt." |
| C-25 | PASS | Prose: "the guarantee stated above is broken"; layer [5]: "such modification breaks the closure commitment stated in layer [3] above" — named and criterion-labelled |
| C-26 | PASS | Prose + layer [6]: "the failure produces the same silent category mismatch described at the consumption site in A-1" |

**Composite**: (5/5 × 60) + (3/3 × 30) + (18/18 × 10) = **100**

Notable: Each criterion is confirmed twice — once in the prose paragraph, once in the numbered audit entry. Layer [5] and [6] are individually labelled by criterion name (`Guarantee-break framing (C-25)`, `Cross-site reference (C-26)`), making the chain auditable against the rubric by label match.

---

## Summary Table

| Variant | Essential | Recommended | Aspirational | Composite | Band |
|---------|-----------|-------------|--------------|-----------|------|
| V-01 | 5/5 | 3/3 | 18/18 | **100** | Gold |
| V-02 | 5/5 | 3/3 | 18/18 | **100** | Gold |
| V-03 | 5/5 | 3/3 | 17/18 | **99.4** | Gold |
| V-04 | 5/5 | 3/3 | 18/18 | **100** | Gold |
| V-05 | 5/5 | 3/3 | 18/18 | **100** | Gold |

**Rank (tied at 100)**: V-01 = V-02 = V-04 = V-05 > V-03

---

## Excellence Signals

The four full-convergence variants produce three new structural patterns not present in R8 variants:

**1. Tabular prohibition rows with row-level isolation (V-02)**
C-25 (Guarantee-break) and C-26 (Cross-site reference) are the most commonly skipped clauses because they appear at the end of a long prose sentence. The tabular form isolates each layer as a discrete row the executor must explicitly pass. The S-3 table additionally includes a bidirectional cross-site pointer ("see A-1 Failure consequence row below"), the first form where the two consequence statements are explicitly linked by row reference rather than prose description.

**2. Front-loaded procedure overview as architectural priming (V-04)**
Before any instruction is processed, the executor reads a table mapping each step to its role. The A-1 row reads "Assemble artifact header; copy FLAG from S-2 verbatim" — the prohibition is encoded in the architecture description before it appears as a constraint. An executor who understands the step topology from the overview does not encounter the A-1 prohibition as a surprise constraint but as an architectural fact they already know.

**3. Numbered protection chain audit with criterion labels (V-05)**
The S-3 prose paragraph establishes the chain; the numbered audit at S-3 close converts it to a labelled checklist with each layer named by criterion (`C-25 guarantee-break framing`, `C-26 cross-site reference`). The closure statement "FLAG is now resolved with all six protection layers active" is the first form where the chain's completeness is asserted as an explicit auditable fact rather than implied by the prose. A subsequent executor or regenerated context can verify the six layers by label before proceeding to A-1.

**V-03 load-bearing finding**: C-25 fails under consequence-first ordering because the causal bridge "the guarantee stated above is broken" has no referent when the consequence precedes the closure. This confirms that C-25's function is structural — it makes the consequence logically dependent on a prior commitment, not merely adjacent to it. Front-loading the consequence (V-03) achieves high execution quality but breaks the dependency chain that C-25 establishes. C-25 is load-bearing as a logical connector, not merely as an inertia signal.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["tabular-row-isolation: C-25 and C-26 expressed as individually scannable table rows at both S-3 and A-1, with bidirectional cross-site row pointer making navigation explicit", "procedure-overview-architectural-priming: front-loaded step-role table before any instruction encodes the FLAG copy constraint as architecture the executor knows before encountering any prohibition", "numbered-protection-chain-audit: criterion-labelled numbered checklist at S-3 close converts implicit prose chain to auditable enumeration with explicit closure assertion all-six-layers-active"]}
```
