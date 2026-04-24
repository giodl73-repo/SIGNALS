## file-issue — Round 2 Scoring (Rubric v2)

---

### V-01 — Lifecycle Emphasis: Minimal Blocking Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Required fields captured | **PASS** | Step 1 collects skill, expected, actual, severity; body template has all four sections |
| C-02 | Severity vocabulary enforcement | **PASS** | "Severity must be exactly one of the four enum values. Reject any other value and ask again." |
| C-03 | GitHub issue format | **PASS** | Title `[{severity}] {skill}: {symptom}` + Expected / Actual / Steps / Context sections |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` — skill name + date, unambiguous |
| C-05 | Actionable, specific issue title | **PASS** | Title template requires skill name + symptom derived from expected/actual delta |
| C-06 | Sufficient reproducibility context | **PASS** | Steps section includes invocation + topic + related; gate check #4 explicitly enforces this |
| C-07 | Repo open offer presented | **PASS** | Step 5 prints `gh issue create` command with title and body-file |
| C-08 | Severity-appropriate framing | **PASS** | Four-line severity tone guidance; crash=urgent/immediate steps; improvement=constructive/proposal |
| C-09 | Skill context enrichment | **PASS** | "Collect any available enriching context without extra prompting: topic, invocation, related skills, version or date" |
| C-10 | Pre-write validation gate | **PASS** | "Step 3 — Pre-Write Gate" is a named phase, separate from Step 2 Draft, with "DO NOT write the artifact until all checks below pass" |
| C-11 | Corrective actions per validation check | **FAIL** | Checks 1–5 are a numbered list with no prescribed remedies on failure. "If any check fails, revise the draft and re-check" is a general instruction, not per-check corrective actions |

**Score:**
- Essential: 4/4 → 60
- Recommended: 3/3 → 30
- Aspirational: 3/4 (C-08, C-09, C-10) → 7.5
- **Composite: 97.5 — Golden**

---

### V-02 — Output Format: Corrective-Action Validation Table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Required fields captured | **PASS** | Intake table shows Skill/Expected/Actual/Severity required; body template complete |
| C-02 | Severity vocabulary enforcement | **PASS** | Four-value enum in intake; validation table row enforces "Exactly one of the four values" |
| C-03 | GitHub issue format | **PASS** | Title format + all required body sections present |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |
| C-05 | Actionable, specific issue title | **PASS** | Title specificity check in validation table; correction: "Rewrite: '[{severity}] {skill}: {specific symptom}'" |
| C-06 | Sufficient reproducibility context | **PASS** | Reproducibility row in validation table: "Add Invocation and Topic...; ask user if still absent" |
| C-07 | Repo open offer presented | **PASS** | Offer section with `gh issue create` command |
| C-08 | Severity-appropriate framing | **PASS** | Four-severity tone section; validation table has "Tone match" row with remedy "Rewrite body using the tone guidance for this severity" |
| C-09 | Skill context enrichment | **PASS** | Optional intake fields (topic, invocation, related); "Context enrichment" validation row |
| C-10 | Pre-write validation gate | **PASS** | "**Validation — apply remedies before writing**" is a named section, separate from Draft, preceding Write, with explicit blocking: "After all checks show pass, write the artifact." Covers reproducibility, tone, and completeness. Note: the variation hypothesis predicted this would fail C-10 by calling it "embedded in the flow" — but the named heading + explicit blocking instruction constitute a structural gate. |
| C-11 | Corrective actions per validation check | **PASS** | Three-column table: Check \| Pass condition \| Action on fail. Every row has prescribed remedy: "Ask: 'Which skill ran?'", "Rewrite: ...", "Rewrite body using the tone guidance", etc. |

**Score:**
- Essential: 4/4 → 60
- Recommended: 3/3 → 30
- Aspirational: 4/4 → 10
- **Composite: 100 — Golden**

**Experiment finding:** The single-axis C-11 variation accidentally also passed C-10. A corrective-action table with a blocking instruction necessarily creates a structural gate — C-10 and C-11 are structurally co-dependent at the table level. The single-axis isolation hypothesis was falsified.

---

### V-03 — Lifecycle + Format: Phase Gate with Corrective-Action Table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Required fields captured | **PASS** | PHASE 1 collects all four; PHASE 2 body template complete |
| C-02 | Severity vocabulary enforcement | **PASS** | "severity is exactly one of: crash, wrong-output, missing-feature, improvement" in PHASE 1 |
| C-03 | GitHub issue format | **PASS** | Title template + full body sections in PHASE 2 |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in PHASE 4 |
| C-05 | Actionable, specific issue title | **PASS** | PHASE 3 "Title specificity" check with correction "Rewrite: '[{severity}] {skill}: {specific symptom}'" |
| C-06 | Sufficient reproducibility context | **PASS** | Steps section in PHASE 2; PHASE 3 Reproducibility row |
| C-07 | Repo open offer presented | **PASS** | PHASE 4 offer with `gh issue create` |
| C-08 | Severity-appropriate framing | **PASS** | PHASE 2 severity tone for all four values; PHASE 3 "Tone match" row |
| C-09 | Skill context enrichment | **PASS** | PHASE 1 "Note any enriching context"; Context section in PHASE 2; PHASE 3 enrichment row |
| C-10 | Pre-write validation gate | **PASS** | "PHASE 3 — VALIDATE" is an explicitly numbered phase, separate from PHASE 2 EXECUTE, with "DO NOT advance to Phase 4 until all checks pass." Verifies reproducibility, tone, completeness. Strongest C-10 implementation in Round 2. |
| C-11 | Corrective actions per validation check | **PASS** | PHASE 3 table: Check \| Pass condition \| Correction on fail. All six rows have prescribed corrections: "Ask user...", "Ask user to choose from enum list", "Rewrite: ...", "Add invocation...; ask user if absent", etc. |

**Score:**
- Essential: 4/4 → 60
- Recommended: 3/3 → 30
- Aspirational: 4/4 → 10
- **Composite: 100 — Golden**

---

### V-04 — Full Synthesis: Severity Templates + Enrichment + Phase Gate + Corrective Actions

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Required fields captured | **PASS** | STEP 1 collects severity + skill + expected + actual; per-severity templates have all body sections |
| C-02 | Severity vocabulary enforcement | **PASS** | Four-value numbered list in STEP 1; STEP 3 "Severity enum" check |
| C-03 | GitHub issue format | **PASS** | Per-severity title formats + severity-specific body sections |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in STEP 4 |
| C-05 | Actionable, specific issue title | **PASS** | Each template has severity-specific title format naming skill + symptom; STEP 3 "Title specificity" check |
| C-06 | Sufficient reproducibility context | **PASS** | Each template has reproduction section; STEP 3 Reproducibility check |
| C-07 | Repo open offer presented | **PASS** | STEP 4 offer with `gh issue create --label "{severity}"` |
| C-08 | Severity-appropriate framing | **PASS** | Strongest C-08 in the round: four distinct per-severity templates enforce tone architecturally. Crash includes "Priority: HIGH — skill non-functional" + Impact section. Improvement requires "Acceptance condition". Tone can't be wrong without choosing the wrong template. |
| C-09 | Skill context enrichment | **PASS** | STEP 1 explicit collect: "Topic name, Invocation string, Related skills/rubrics/artifacts, Skill version or date." Each template has Context section. STEP 3 enrichment check. |
| C-10 | Pre-write validation gate | **PASS** | "STEP 3 — PRE-WRITE GATE" explicitly named, "DO NOT write the artifact until all checks pass." Separate from STEP 2 DRAFT. Verifies reproducibility, tone, completeness. |
| C-11 | Corrective actions per validation check | **PASS** | STEP 3 table with "Correction on fail" column. All rows have prescribed actions, including severity-specific: "Rewrite using the severity-gated template tone for this severity." |

**Score:**
- Essential: 4/4 → 60
- Recommended: 3/3 → 30
- Aspirational: 4/4 → 10
- **Composite: 100 — Golden**

---

### V-05 — Phrasing Register: Compressed Inline Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Required fields captured | **PASS** | INTAKE collects four required fields; DRAFT body has Expected/Actual/Steps/Context |
| C-02 | Severity vocabulary enforcement | **PASS** | "Severity (required): crash / wrong-output / missing-feature / improvement"; check #2 enforces enum |
| C-03 | GitHub issue format | **PASS** | Title format + all body sections |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |
| C-05 | Actionable, specific issue title | **PASS** | Check #3 "Title names skill + symptom; No generic text ('Bug report', 'Issue') in title" |
| C-06 | Sufficient reproducibility context | **PASS** | Check #4 "Body is reproducible \| Invocation, input, or event sequence present" |
| C-07 | Repo open offer presented | **PASS** | OFFER section with `gh issue create` command |
| C-08 | Severity-appropriate framing | **PASS** | Four-line severity framing guidance; check #5 "Tone matches severity \| Language fits crash/wrong-output/missing-feature/improvement framing" |
| C-09 | Skill context enrichment | **PASS** | INTAKE: "Collect without extra prompting — use whatever is already in the user message: Topic, invocation string, related skills or artifacts, version or date"; check #6 enforces enrichment |
| C-10 | Pre-write validation gate | **PASS** | "**PRE-WRITE CHECKS — all must pass before writing; apply remedy on each failure and re-check**" is a bold all-caps named section between DRAFT and WRITE. "Do not proceed to WRITE until all six checks show pass." Covers completeness (#1), enum (#2), title (#3), reproducibility (#4), tone (#5), enrichment (#6). Criterion met without a numbered phase structure. |
| C-11 | Corrective actions per validation check | **PASS** | Four-column table: # \| Check \| Pass \| Remedy on fail. All six rows have prescribed remedies: "Ask user for the missing field(s)", "Ask: 'Choose from: ...'", "Rewrite: ...", "Add Topic and Invocation; ask user if both are absent", "Rewrite tone using the severity framing guidance above", "Add any available item to Context section" |

**Score:**
- Essential: 4/4 → 60
- Recommended: 3/3 → 30
- Aspirational: 4/4 → 10
- **Composite: 100 — Golden**

---

## Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|-----------|---------------|-----------------|-------------------|-----------|---------|
| V-01 | 60 | 30 | 7.5 (C-08, C-09, C-10) | **97.5** | Golden |
| V-02 | 60 | 30 | 10 (all four) | **100** | Golden |
| V-03 | 60 | 30 | 10 (all four) | **100** | Golden |
| V-04 | 60 | 30 | 10 (all four) | **100** | Golden |
| V-05 | 60 | 30 | 10 (all four) | **100** | Golden |

**Ranking (tie-broken by C-10/C-11 implementation strength):**

1. **V-04** — strongest overall: per-severity templates enforce C-08 architecturally; most explicit enrichment collection; named STEP 3 PRE-WRITE GATE; severity-gated corrective action in C-11 table
2. **V-03** — clearest phase structure: VALIDATE phase is the canonical gate pattern; table corrections are complete; ties V-05 on most criteria
3. **V-05** — compactness wins: compressed inline gate proves the phase apparatus is not load-bearing; all criteria satisfied with minimum prose
4. **V-02** — experiment falsified its own hypothesis: designed to test C-11 only, but named section + blocking instruction also satisfied C-10
5. **V-01** — C-11 gap: only variation with a checklist but no prescribed remedies; correctly isolated as the single failing criterion

---

## Excellence Signals

**From V-02 (experiment falsification):**
C-10 and C-11 are structurally co-dependent. A corrective-action table with a blocking instruction in its section header necessarily creates a structural gate. The single-axis isolation between "gate structure" and "corrective actions" was not achievable — any table designed for C-11 that sits before Write with a blocking instruction also satisfies C-10.

**From V-04 (per-severity templates):**
Severity-appropriate tone (C-08) is most robustly enforced by template architecture, not prose guidance. When each severity value branches to a structurally different template — with severity-specific sections like `Impact`, `Delta`, `Acceptance condition` — tone violation requires choosing the wrong template, which is a different (and far more visible) error class than ignoring prose guidance.

**From V-05 (minimal gate structure):**
The minimum structure that satisfies C-10 is: a named section (bold or heading) + an explicit blocking statement + coverage of completeness, reproducibility, and tone. A numbered phase label is not required. This confirms that the gate pattern is about the blocking instruction and coverage, not the lifecycle scaffolding.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-10 and C-11 are structurally co-dependent: a corrective-action table with a blocking instruction in its section header satisfies both simultaneously; single-axis isolation between gate structure and corrective actions is not achievable at the table level", "Per-severity templates enforce severity-appropriate tone architecturally rather than as prose guidance: each severity branch is a structurally different template, making tone violation a template-selection error rather than an ignored note", "Minimum gate structure for C-10 is: named section plus explicit blocking statement plus coverage of completeness, reproducibility, and tone — numbered phase labels are not load-bearing"]}
```
