## Quest Score — campaign-evidence (Round 16, Rubric v16)

---

### Universal Assessment (all five variations)

All five variations are built on the R15 foundation and carry forward the full governance apparatus. The following criteria pass uniformly:

| Tier | Criteria | Verdict |
|------|----------|---------|
| Essential | C-01 to C-04 | **PASS** — 5-stage campaign, evidence-first sequence, falsifiable hypotheses, self-contained output |
| Recommended | C-05 to C-07 | **PASS** — stage attribution, consensus/conflict synthesis, calibrated (non-uniform) confidence |
| Aspirational baseline | C-08 to C-34 | **PASS** (27 criteria) — gaps surfaced, decision readiness compressed, named rules with preamble + point-of-use invocation, prospective coverage map with immutability clause, inline scope annotation, universal binary interrogative, stage-indexed invocation trail, entry/exit gates, gate record pre-templated, column-encoded sequencing, extensible governance, named role handoffs, negative invocations, access-scope declarations, derivable checksum, artifact provenance tags |

Differentiation lives in **C-35 through C-40** (six criteria).

---

### Differential Scoring — C-35 to C-40

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-35** Dual-phase PRE/POST interrogative | PASS | PASS | PASS | PASS | PASS |
| **C-36** Handoff carries artifact enumeration + provenance activation | PASS | PASS | PASS | PASS | PASS |
| **C-37** Named PRE/POST tables physically separated by execution text | FAIL | FAIL | FAIL | FAIL | **PASS** |
| **C-38** Complete apparatus pre-instantiated in preamble with timing directives | FAIL | FAIL | FAIL | FAIL | **PASS** |
| **C-39** Interrogative governance at column-header level | PASS | PASS | **PASS+** | PASS | FAIL |
| **C-40** SEQUENCING RULE scope declared for evidence-stage relative ordering | PASS | **PASS+** | PASS | PASS | PASS |

**Evidence notes:**

**C-35:** All variations implement two temporally distinct checkpoints (Will / Does). The consolidated table format (V-01 to V-04) satisfies the temporal distinction — cells are filled before and after execution — even without physical separation. V-05's named tables make the temporal discipline structural. All PASS C-35.

**C-37:**
- V-01, V-02, V-04: "Consolidated table" — PRE and POST are columns of the same table artifact. Execution text does not physically occupy the space between them. A reader could fill both columns in one sitting with no structural trace. FAIL.
- V-03: "Per-rule mini-tables" — each rule gets its own table, but the tables are still single artifacts; execution content does not appear between the PRE row and the POST row. FAIL.
- V-05: "Fixes R15 V-05 C-37 failure" — named NAMED-PRE and NAMED-POST tables are declared as distinct artifacts with execution content physically interleaved. The stage body occupies the space between them. PASS.

**C-38:** Requires both (a) blank preamble templates for every PRE/POST form AND (b) per-stage timing directives naming which form to fill and when. V-01 to V-04 inherit C-37's failure — the consolidated table structure cannot pre-instantiate two physically separate artifacts in the preamble. FAIL for all four. V-05, having fixed C-37, also satisfies C-38's full two-component requirement. PASS.

**C-39:**
- V-01, V-02, V-04: "Will/Does this rule hold?" as column header — the governing question IS the header. Generic but satisfies the criterion: any blank POST cell is an unanswered column header. PASS.
- V-03: "Will ATTRIBUTION hold?" — rule-specific interrogative header. The column name names the specific rule under interrogation. Strongest C-39 implementation. PASS.
- V-05: Primary axis is "Fixed dual-table + inertia framing" — table names are NAMED-PRE / NAMED-POST (labels, not questions). The interrogative form may appear as cell prompts, not column headers. FAIL.

**C-40:**
- V-01: SEQUENCING RULE declaration explicitly names both hypothesis placement and evidence-stage relative ordering as governed constraints. PASS.
- V-02: Strongest form — SEQUENCING split into SEQUENCING-HYPO and SEQUENCING-ORDER as two distinct peer rules, each with its own coverage-map row, invocation trail, and checksum contribution. The evidence-ordering constraint is independently trackable. Checksum shifts from ~40 to 47. PASS+.
- V-03: Both constraints declared within a single SEQUENCING RULE body. PASS.
- V-04: Intel-before-Web reversal declared as a SEQUENCING-governed decision, invoked at the S1 boundary. Evidence-stage ordering demonstrated as a live rule invocation rather than a preamble assertion. PASS.
- V-05: SEQUENCING RULE names "hypothesis-first mode" and "unordered collection" as excluded inertia antipatterns — evidence-stage ordering is in scope by negation (these are the violations the rule prevents). PASS.

---

### Per-Variation Scorecard

**Scoring formula:** Essential (60) + Recommended (30) + Aspirational (10 pts over 33 criteria, each ≈ 0.303 pts; PARTIAL = 0.152)

---

#### V-01 — Output format / generic interrogative headers

| Section | Score |
|---------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational: C-08 to C-36 (29 PASS) | 8.79 |
| C-37 FAIL | — |
| C-38 FAIL | — |
| C-39 PASS | +0.303 |
| C-40 PASS | +0.303 |
| **Total** | **≈ 93** |

Notes: Minimum-change C-39 implementation — "Will/Does this rule hold?" is interrogative but generic; the column asks about all rules simultaneously rather than naming each. C-37/C-38 failure is structural: the consolidated table cannot satisfy the physical-separation requirement regardless of header wording.

---

#### V-02 — Lifecycle emphasis / SEQUENCING split

| Section | Score |
|---------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational: C-08 to C-36 (29 PASS) | 8.79 |
| C-37 FAIL | — |
| C-38 FAIL | — |
| C-39 PASS | +0.303 |
| C-40 PASS+ | +0.303 |
| **Total** | **≈ 93** |

Notes: Strongest C-40 implementation — splitting SEQUENCING into two peer rules makes evidence-stage ordering independently auditable. Checksum shift to 47 demonstrates the extensibility property (C-29) in live action. However, the consolidated table format still fails C-37/C-38, matching V-01's score despite stronger C-40.

---

#### V-03 — Phrasing register / rule-specific interrogative headers

| Section | Score |
|---------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational: C-08 to C-36 (29 PASS) | 8.79 |
| C-37 FAIL | — |
| C-38 FAIL | — |
| C-39 PASS+ | +0.303 |
| C-40 PASS | +0.303 |
| **Total** | **≈ 93** |

Notes: Strongest C-39 implementation — "Will ATTRIBUTION hold?" names the specific rule in the column header. Any blank cell is an unanswered question about ATTRIBUTION specifically, not "a rule" generically. The rule name and its compliance commitment are co-located at the column-header level. The per-rule mini-table structure, however, still produces one table per rule (not two tables separated by execution text), failing C-37/C-38 at the same structural level as V-01 and V-02.

---

#### V-04 — Role sequence reversal (Intel → Web)

| Section | Score |
|---------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational: C-08 to C-36 (29 PASS) | 8.79 |
| C-37 FAIL | — |
| C-38 FAIL | — |
| C-39 PASS | +0.303 |
| C-40 PASS | +0.303 |
| **Total** | **≈ 93** |

Notes: The Intel→Web reversal demonstrates that SEQUENCING RULE governs evidence-stage relative ordering — the rule is invoked at the S1 boundary where the reversal takes effect, making the decision auditable by invocation-trail inspection rather than structural inference. This is a pedagogically strong C-40 demonstration. However, the consolidated table format fails C-37/C-38, and the score matches V-01.

---

#### V-05 — Fixed dual-table / inertia framing

| Section | Score |
|---------|-------|
| Essential | 60/60 |
| Recommended | 30/30 |
| Aspirational: C-08 to C-36 (29 PASS) | 8.79 |
| C-37 PASS | +0.303 |
| C-38 PASS | +0.303 |
| C-39 FAIL | — |
| C-40 PASS | +0.303 |
| **Total** | **≈ 94** |

Notes: Only variation to pass C-37 and C-38. The named-table separation converts temporal discipline from normative instruction to structural anachronism — filling the POST table before execution leaves the execution block blank; filling it after produces content at the right location. The C-38 complement — blank templates in preamble plus stage-body timing directives — eliminates the memory requirement for when to fill what. Fails C-39 because NAMED-PRE / NAMED-POST are artifact labels, not interrogatives; the governing question does not occupy the column header. Net: +2 criteria (C-37, C-38) versus −1 criterion (C-39) over V-01 to V-04.

---

### Rankings

| Rank | Variation | Score | Distinguishing Axis |
|------|-----------|-------|---------------------|
| 1 | **V-05** | **94** | Only variation passing C-37 + C-38; physical table separation enforces temporal discipline structurally |
| 2 | V-03 | 93 | Strongest C-39: rule-specific interrogative column headers |
| 2 | V-02 | 93 | Strongest C-40: SEQUENCING split into peer rules with independent invocation trail |
| 2 | V-04 | 93 | Best C-40 demonstration: Intel→Web reversal invoked at live stage boundary |
| 2 | V-01 | 93 | Minimum-change C-39 + C-40 baseline |

---

### Excellence Signals (from V-05)

**E-1 — Inertia antipattern enumeration in SEQUENCING RULE scope**
V-05 declares "hypothesis-first mode" and "unordered collection" as named excluded antipatterns within the SEQUENCING RULE. This converts C-40 compliance from a positive declaration ("evidence ordering is governed") to a two-sided declaration ("evidence ordering is governed; here are the named violations"). A decision-readiness verdict can now reference an antipattern by name: "SEQUENCING RULE: no hypothesis-first mode present." Violations become classifiable by category rather than detectable only by structural inspection. This is the first variation to name non-compliance modes explicitly in a rule declaration — promotable as a criterion requiring "SEQUENCING RULE declaration includes at least one named excluded mode."

**E-2 — Named artifact table separation as structural temporal enforcement**
The pattern in V-05 — two named table artifacts with execution content physically between them — does more than satisfy C-37. It removes the "creative act" problem from C-38: filling the POST table at the same time as the PRE table is not only normatively discouraged, it leaves a structural trace (execution block is empty). This is a general principle applicable beyond invocation tables: wherever a pre-commitment and a post-verification are required, physical interleaving of the execution artifact makes simultaneous fill anachronistic. The pattern deserves a name: **structural temporal pinning**.

---

```json
{"top_score": 94, "all_essential_pass": true, "new_patterns": ["Inertia antipattern enumeration in rule scope — naming excluded modes (hypothesis-first mode, unordered collection) within the SEQUENCING RULE declaration makes violations classifiable by category rather than detectable only by structural inspection; decision-readiness verdicts can reference named failure modes directly", "Structural temporal pinning — placing execution content physically between named PRE and POST table artifacts makes simultaneous fill leave a visible structural trace (empty execution block), converting temporal discipline from normative instruction to structural anachronism detectable without interpretation"]}
```
