## Quest Score — corps-rob R1

### Scoring Model

- Essential (C-01–C-05): 12 pts each, max 60 — all must pass for golden
- Recommended (C-06–C-08): 10 pts each, max 30
- Aspirational (C-09–C-10): 5 pts each, max 10
- PASS = full, PARTIAL = half, FAIL = 0
- Golden threshold: all essential pass + composite >= 80

---

### V-01 — Role Sequence: Risk-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage labeling | PASS | `## Stage: [stage-name]` required per stage |
| C-02 Role-loaded perspective | PASS | Finding template explicitly says "specific concern from this role's lens — not a category" |
| C-03 ROB format compliance | PASS | Stage header, ROLE line, numbered findings with severity, VERDICT present |
| C-04 Actionable findings | PASS | Minimum 2 per stage, inline Owner and Resolution required |
| C-05 Go/No-Go in TPM | PASS | Explicit "GO / NO-GO / GO WITH CONDITIONS" section with finding/risk ID citation |
| C-06 Cross-stage coherence | PARTIAL | SEQUENCE NOTE instructs later stages to cite tpm risk IDs, but it is a trailing note rather than a structural per-stage step — likely inconsistent compliance |
| C-07 Structured risk register | PASS | Table with ID, Risk, Severity, Likelihood, Mitigation; min 3 rows, 1 HIGH |
| C-08 Exec-office cascade tracing | FAIL | No exec-office cascade requirement; exec-office uses the generic stage template only |
| C-09 Blocker detection | FAIL | No blocker check mechanism |
| C-10 Cross-cutting themes | FAIL | No themes section |

**Score:** 60 + 5 + 10 + 0 + 0 = **75**
All essential pass: YES — Not golden (75 < 80)

---

### V-02 — Output Format: Table-Centric

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage labeling | PASS | `## Stage: [stage-name]` in template |
| C-02 Role-loaded perspective | PARTIAL | ORIENTATION line in stage header but finding template cell says only "[specific concern]" — no explicit tie to role's lens inside the finding row |
| C-03 ROB format compliance | PASS | Stage header, ROLE+ORIENTATION, severity column in table, verdict row |
| C-04 Actionable findings | PASS | Table structure forces Owner and Resolution into columns; min 2 rows enforced |
| C-05 Go/No-Go in TPM | PASS | Decision table with "GO / NO-GO / GO WITH CONDITIONS" single-row, no ambiguity |
| C-06 Cross-stage coherence | FAIL | No cross-stage referencing mechanism |
| C-07 Structured risk register | PASS | Table with Status column; min 3 rows, 1 HIGH, Status: OPEN/WATCH/MITIGATED |
| C-08 Exec-office cascade tracing | PASS | Mission Cascade table with named mission, program, artifact, alignment; "strategic goals" explicitly fails |
| C-09 Blocker detection | FAIL | No blocker mechanism |
| C-10 Cross-cutting themes | FAIL | No themes section |

**Score:** 54 + 0 + 10 + 10 + 0 = **74**
All essential pass: NO (C-02 partial) — Not golden

---

### V-03 — Phrasing Register: Descriptive / Role-Oriented

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage labeling | PASS | `## Stage: [stage-name]` in template |
| C-02 Role-loaded perspective | PASS | "Let the loaded orientation shape what each stage finds — not a generic list of concerns, but this role's specific anxieties about this specific topic" — strongest C-02 language of any variation |
| C-03 ROB format compliance | PASS | Stage header, ROLE line, findings with severity, verdict |
| C-04 Actionable findings | PASS | Minimum 2 findings, each requires Owner and Resolution |
| C-05 Go/No-Go in TPM | PASS | Labeled "GO / NO-GO / GO WITH CONDITIONS" line citing primary risk or finding |
| C-06 Cross-stage coherence | FAIL | No structural mechanism for cross-stage referencing |
| C-07 Structured risk register | PASS | Pipe-delimited structured list (R-01 | name | Severity | Likelihood | Mitigation) satisfies "structured list" condition; 3+ entries, 1 HIGH |
| C-08 Exec-office cascade tracing | PASS | Explicit requirement: "traces at least one named executive-level mission... the mission must be named and the alignment or gap must be specific" |
| C-09 Blocker detection | FAIL | No blocker mechanism |
| C-10 Cross-cutting themes | FAIL | No themes section |

**Score:** 60 + 0 + 10 + 10 + 0 = **80**
All essential pass: YES — Golden (80 = threshold exactly)

---

### V-04 — Lifecycle Emphasis + Cross-Stage Coherence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage labeling | PASS | `## Stage: [stage-name]` required |
| C-02 Role-loaded perspective | PARTIAL | ROLE+orientation loaded and stated in header; but finding template says "specific concern — not a category" without tying it to the role's documented lens in the finding cell — weaker than V-01/V-03/V-05 |
| C-03 ROB format compliance | PASS | Stage header, ROLE, labeled VERDICT, findings with severity |
| C-04 Actionable findings | PASS | Min 2 per stage with Owner and Resolution in finding format |
| C-05 Go/No-Go in TPM | PASS | Bold `**GO / NO-GO / GO WITH CONDITIONS**` with cited finding/risk IDs and conditions |
| C-06 Cross-stage coherence | PASS | STEP 3 is a required structural step at every stage; "at least 2 cross-stage references must appear across the full run" with fallback Cross-Stage Summary enforcement |
| C-07 Structured risk register | PASS | Risk register table in TPM, min 3 rows, 1 HIGH |
| C-08 Exec-office cascade tracing | PASS | Exec-office finding must name an S-office mission and trace alignment or gap to the artifact, with example format provided |
| C-09 Blocker detection | PASS | BLOCKER CHECK is a required section after every verdict; explicit "BLOCKS [stage-name] — F-[N] — [reason]" format |
| C-10 Cross-cutting themes | FAIL | Cross-Stage Summary fallback is about reference count enforcement, not cross-cutting theme elevation |

**Score:** 54 + 10 + 10 + 10 + 5 + 0 = **89**
All essential pass: NO (C-02 partial) — Not golden despite high composite

---

### V-05 — Full Integration

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Stage labeling | PASS | `## Stage: [stage-name]` required in template |
| C-02 Role-loaded perspective | PASS | Finding table row template explicitly says "specific concern grounded in this role's lens" and "second specific concern from this role's domain" — role anchor is inside the finding cell |
| C-03 ROB format compliance | PASS | Stage header, ROLE+LENS, severity column in table, labeled VERDICT |
| C-04 Actionable findings | PASS | Table columns force Owner and Resolution; min 2 rows; severity must vary |
| C-05 Go/No-Go in TPM | PASS | Go/No-Go Ritual as a blockquote with bold decision label, rationale citing risk IDs, conditions, named Owner — most structured C-05 of any variation |
| C-06 Cross-stage coherence | PARTIAL | Cross-Stage References section present at every stage; no numeric minimum per-stage and "cite any" language means zero references could satisfy the structural requirement — weaker enforcement than V-04 |
| C-07 Structured risk register | PASS | Table with Source Stage column (stronger than rubric requires); min 3 rows, 1 HIGH |
| C-08 Exec-office cascade tracing | PASS | Mission Cascade table with named mission, program, artifact, alignment; "strategic priorities" explicitly called out as failing |
| C-09 Blocker detection | FAIL | Cross-stage references use confirm/escalate/contradict vocabulary but no explicit BLOCKS mechanism targeting a downstream stage |
| C-10 Cross-cutting themes | PASS | Cross-Cutting Themes table required for `--stage all`; theme must name recurrence pattern across 2+ stages and be distinct from individual findings; copying one finding explicitly ruled out |

**Score:** 60 + 5 + 10 + 10 + 0 + 5 = **90**
All essential pass: YES — Golden (90 > 80)

---

### Final Rankings

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-05 Full Integration | 90 | YES |
| 2 | V-04 Lifecycle + Coherence | 89 | NO (C-02 partial) |
| 3 | V-03 Descriptive / Role-Oriented | 80 | YES (at threshold) |
| 4 | V-01 Risk-First Sequence | 75 | NO |
| 5 | V-02 Table-Centric | 74 | NO (C-02 partial) |

---

### Excellence Signals from V-05

**1. Role-lens anchor inside the finding cell.**
Placing "grounded in this role's lens" and "from this role's domain" directly in the finding table row template anchors C-02 at the point of production. Every earlier variation either stated it in a header (easy to ignore) or a prose instruction (easy to drift). V-05 makes it structurally unavoidable.

**2. Inertia Anchor as a persistent per-stage check.**
A named Inertia Baseline written before Stage 1, referenced briefly at every stage, forces each role to engage with the status-quo alternative from their specific perspective. This differentiates role-loaded findings more reliably than instructions alone — a PM's inertia concern is adoption friction; a TPM's is schedule disruption; an architect's is migration debt.

**3. Source Stage column in risk register.**
Adding Source Stage to the risk register table costs zero tokens but creates a provenance chain from individual stage findings up to the TPM risk register — a partial implementation of C-06 embedded in C-07.

**4. Go/No-Go Ritual with Owner field.**
Formatting the go/no-go as a blockquote declaration with an Owner field transforms the decision from a verdict line into an accountable record. The Owner field is the key addition — it forces the model to name who is responsible for tracking conditions, which signals organizational reality rather than just structural compliance.

**5. Cross-Cutting Themes table with recurrence-pattern requirement.**
The table structure is standard, but the constraint "the theme must name the pattern of recurrence — why the same concern appearing in multiple stages is more serious than it was in any one stage alone" prevents the most common C-10 failure: copying one finding and relabeling it a theme.

---

### Weakness in V-05 to address in R2

**C-06 / C-09 gap**: V-05 has Cross-Stage References at every stage but no numeric minimum and no explicit blocker detection. V-04 solved both with the 4-step gate protocol (STEP 3 with minimum count enforcement + BLOCKER CHECK). Merging V-04's gate protocol into V-05's full-integration frame would close both gaps and likely push composite to 95+.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["role-lens anchor inside the finding cell template (not just the stage header) prevents C-02 drift at the point of production", "persistent Inertia Anchor before Stage 1 forces per-stage role differentiation without counting references — each role's status-quo anxiety is distinct", "Source Stage column in risk register embeds cross-stage provenance in C-07 at zero structural cost", "Go/No-Go Ritual blockquote with Owner field converts a verdict line into an accountable decision record"]}
```
