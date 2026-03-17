## Quest Score — corps-pr · Round 1

**Skill**: corps-pr | **Rubric**: v1 | **Variations scored**: V-01, V-02

---

## Rubric Criteria Reference

| ID | Weight | Category | Type |
|----|--------|----------|------|
| C-01 | 12 | Reviewer selection with files-changed signal | essential |
| C-02 | 12 | Per-role findings with P1/P2/P3 | essential |
| C-03 | 12 | Consensus analysis section | essential |
| C-04 | 12 | Go/no-go with justification | essential |
| C-05 | 12 | Role-specific lens on findings | essential |
| C-06 | 10 | Coverage gap callout for unowned files | recommended |
| C-07 | 10 | Per-role severity summary | recommended |
| C-08 | 10 | AMEND scope disclosure | recommended |
| C-09 | 5 | Root cause synthesis for divergent findings | aspirational |
| C-10 | 5 | Actionable conditions with named sign-off owners | aspirational |

---

## V-01 — Role Sequence (Inertia Advocate First)

### Criterion Evaluation

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step 1 mandates `\| File \| Owning Role \| Selection Reason \|` — the table schema structurally prevents omitting the files-changed mapping. Instruction: "A reviewer list with no file mapping is not acceptable." |
| C-02 | **PASS** | Step 2 requires P1/P2/P3 on every Inertia Advocate finding. Step 3 format block shows `[Finding N] **[P1/P2/P3]**: ...` per role. No severity-free finding can be emitted without violating the format. |
| C-03 | **PASS** | Step 5 is dedicated to Consensus Analysis with three required sub-elements: (a) Convergence, (b) Divergence, (c) Critical Finding. Explicit instruction: "Do not simply restate per-role findings." |
| C-04 | **PASS** | Step 6 requires "exactly one of: GO, NO-GO, or GO WITH CONDITIONS" plus primary reason. Instructs: "Do not leave the verdict ambiguous." |
| C-05 | **PASS** | Step 3 lists role-specific domain foci inline (compiler-lead: IR/codegen; security-architect: threat surface/auth). Inertia Advocate has a structural charter requiring at least one status-quo-sufficient finding — not achievable by generic review. |
| C-06 | **PASS** | Step 4 explicitly handles UNOWNED files from Step 1. Format mandates a coverage gap section naming unowned files. If all files owned: "Coverage: all changed files have org.yaml owners." |
| C-07 | **PASS** | Each role section closes with `[Role]: N findings — X P1, Y P2, Z P3` — a mandatory summary line, not implicit counting. |
| C-08 | **PASS** | AMEND Mode is a named section with a required scope disclosure block: what changed, roles added/removed, prior findings superseded. |
| C-09 | **PASS** | Step 5 item 2 says: "For each divergence: explain WHY the roles see it differently (structural reason, not just 'they have different perspectives')". Structural reason is required, not optional. |
| C-10 | **PASS** | Step 6 examples show `compiler-lead must verify IR output` and `requires security-architect sign-off after fix` — named-role conditions are modeled explicitly. |

### Score

| Category | Pass | Points |
|----------|------|--------|
| Essential (5) | 5/5 | 60 |
| Recommended (3) | 3/3 | 30 |
| Aspirational (2) | 2/2 | 10 |
| **Composite** | | **100** |

**Golden**: YES — all essential pass, composite 100 ≥ 80.

---

## V-02 — Output Format (Table-Driven)

### Criterion Evaluation

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | SELECTION TABLE schema includes `\| # \| File Changed \| Owning Role \| Signal (why this role) \|` — the Signal column enforces traceable selection reason per file. |
| C-02 | **PASS** | PER-ROLE FINDINGS TABLE includes a Severity column (`P1/P2/P3`) and the Domain Signal column. Table structure prevents unlabeled findings. Role summary line follows each table. |
| C-03 | **PASS** | CONSENSUS MATRIX section exists with Divergence Reason column. Post-matrix text requires "Most critical finding across all roles" and "Key divergence to resolve." Synthesis is forced by schema. |
| C-04 | **PASS** | GO / NO-GO table requires one of three verdicts plus Primary Reason. Ambiguous prose verdicts cannot satisfy the table format. |
| C-05 | **PASS** | Domain Signal column is required in every PER-ROLE FINDINGS TABLE row — defined as "what makes this a [role] finding, not generic review." A finding without a domain signal fails the table schema. |
| C-06 | **PASS** | COVERAGE GAP TABLE shows UNOWNED status per file, with a required callout note when any row is UNOWNED. |
| C-07 | **PASS** | "Role summary: N total — X P1, Y P2, Z P3" is required after each role table — distinct from the consensus section. |
| C-08 | **PARTIAL** | No AMEND Mode section exists in V-02. Default-mode runs pass by default (rubric: "A run in default mode passes by default"), but the prompt has no provision for AMEND disclosure when scope changes. Half credit: default covered, AMEND path unhandled. |
| C-09 | **PASS** | CONSENSUS MATRIX Divergence Reason column captures why roles disagree. Less directive than V-01 ("structural reason" is not required by explicit instruction), but the schema elicits it by column design. Marginal pass. |
| C-10 | **PARTIAL** | GO / NO-GO table only has `\| Decision \| Primary Reason \|` — no column for sign-off owner per condition. GO WITH CONDITIONS can be emitted without naming the role responsible for confirming resolution. The schema does not enforce C-10. |

### Score

| Category | Pass | Points |
|----------|------|--------|
| Essential (5) | 5/5 | 60 |
| Recommended (3) | 2.5/3 | 25 |
| Aspirational (2) | 1.5/2 | 7.5 |
| **Composite** | | **92.5** |

**Golden**: YES — all essential pass, composite 92.5 ≥ 80.

---

## Rankings

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | V-01 | 100 | YES | Perfect across all tiers |
| 2 | V-02 | 92.5 | YES | C-08 AMEND gap; C-10 sign-off owner not enforced by schema |

---

## Excellence Signals from V-01

**What made V-01 score 100 vs V-02's 92.5:**

1. **Inertia-first sequencing** — Running the Inertia Advocate before technical roles establishes a status-quo baseline that technical reviewers argue against explicitly. This generates structural divergence (C-09) rather than pile-on agreement — the Inertia Advocate's findings become a reference object that other roles must respond to.

2. **Explicit structural-reason requirement for divergence** — Step 5 says "structural reason, not just 'they have different perspectives'" — this instruction phrase forces the model to go beyond labeling disagreement to explaining it architecturally. V-02's Divergence Reason column elicits the same thing by schema, but without the anti-pattern warning.

3. **AMEND as a named, first-class mode** — V-01 treats AMEND as a dedicated section with three required disclosures (what changed, roles added/removed, prior findings superseded). V-02 has no AMEND provision.

4. **Named-role sign-off in examples** — V-01's Step 6 examples show the exact pattern ("requires security-architect sign-off after fix"), which trains the model output on what GO WITH CONDITIONS should look like. V-02's table schema for GO/NO-GO omits this column entirely.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia-first sequencing creates structural divergence baseline before technical roles respond", "AMEND mode as a named first-class section with three-part disclosure schema", "explicit anti-pattern prohibition in instructions (not just \"different perspectives\") forces structural root-cause"]}
```
