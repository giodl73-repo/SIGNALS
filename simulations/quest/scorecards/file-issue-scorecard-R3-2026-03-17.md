## file-issue — Round 3 Scoring (Rubric v3)

### Criterion-by-Criterion Evaluation

---

#### V-01 — Phrasing Register: Conversational First-Person Imperative

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | **PASS** | "Do not draft until all four are answered." All four fields explicitly listed and blocked. |
| C-02 | Severity vocabulary enforcement | **PASS** | "If the user gives a severity value that is not one of these four, tell them: 'Choose from: crash, wrong-output, missing-feature, improvement -- no other values are accepted.'" |
| C-03 | GitHub issue format | **PASS** | Four titled templates with `[{severity}] {skill}: {description}` title pattern and Expected/Actual/Steps/Context section structure. |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` explicit. |
| C-05 | Actionable, specific issue title | **PASS** | Each title template contains `{skill}` + specific symptom description; no generic text allowed. |
| C-06 | Sufficient reproducibility context | **PASS** | All four templates include Steps to reproduce with Invocation + Topic + Chain; note-while-collecting instruction covers context. |
| C-07 | Repo open offer presented | **PASS** | `gh issue create` command block presented after write step. |
| C-08 | Severity-appropriate framing | **PASS** | crash: "Priority: HIGH -- skill non-functional"; improvement: Rationale + Acceptance condition sections. Tone calibrated per template. |
| C-09 | Skill context enrichment | **PASS** | "While collecting, also note anything...topic name, invocation string, related skills, version or date." Context section in every template. |
| C-10 | Pre-write validation gate | **PASS** | "Before writing the artifact, check all of the following...do not write until every check passes." Numbered six-check gate blocks write. |
| C-11 | Corrective actions per validation check | **PASS** | Each numbered check has explicit "If not:" remedy: ask user, ask user, rewrite title, add Topic+Invocation, rewrite body, add enrichment. |
| C-12 | Per-severity body templates | **PASS** | Four named `If {severity}:` blocks. crash has Priority+Impact fields; improvement has Acceptance condition; wrong-output has Delta; missing-feature has References. Template selection determines structure. |
| C-13 | Severity-labeled issue creation | **PASS** | `--label "{severity}"` present in gh command. |

**Score**: 4/4 essential (60) + 3/3 recommended (30) + 6/6 aspirational (10) = **100**

---

#### V-02 — Role Sequence: Template-First (Severity Selects Template; Template Drives Collection)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | **PASS** | Four severity-gated forms each mark `[required]` fields; STEP 2 instructs fields "must be non-empty before you proceed." |
| C-02 | Severity vocabulary enforcement | **PASS** | "Severity must be exactly one of these four values. Reject any other input and re-prompt. Do not collect any other field until severity is confirmed." |
| C-03 | GitHub issue format | **PASS** | Four STEP 3 issue templates with title + Expected/Actual/Steps/Context structure per severity. |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in STEP 5. |
| C-05 | Actionable, specific issue title | **PASS** | Title patterns all contain `{skill}` + severity-specific symptom tokens; no generic text. |
| C-06 | Sufficient reproducibility context | **PASS** | Each severity form includes Invocation, Topic, Chain fields; templates have Steps sections. |
| C-07 | Repo open offer presented | **PASS** | `gh issue create` command in STEP 5 Offer block. |
| C-08 | Severity-appropriate framing | **PASS** | crash form includes Priority+Impact; improvement form requires Acceptance condition; templates carry matching tone. |
| C-09 | Skill context enrichment | **PASS** | Every form includes Related/Version/date fields; Context section in all templates. |
| C-10 | Pre-write validation gate | **PASS** | "STEP 4 -- PRE-WRITE GATE: DO NOT write the artifact until all rows below show PASS." Explicit blocking before STEP 5. |
| C-11 | Corrective actions per validation check | **PASS** | "Correction on fail" column with explicit prescribed remedy for each of six rows. |
| C-12 | Per-severity body templates | **PASS** | Architecturally strongest: four forms (input schema) + four issue templates (output schema), each severity-distinct. crash form requires Impact/Priority; improvement form marks Acceptance condition `[required for improvement]`; template selection governs both collection and output. |
| C-13 | Severity-labeled issue creation | **PASS** | `--label "{severity}"` present in STEP 5 gh command. |

**Score**: 4/4 essential (60) + 3/3 recommended (30) + 6/6 aspirational (10) = **100**

**Architectural note**: Only variation where the template is simultaneously an input schema and output schema — severity-first means template selection gates collection, not just formatting.

---

#### V-03 — Inertia Framing: Workflow Blockage as Organizing Metaphor

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | **PASS** | TRIAGE section: "Collect the four required fields. For each absent field, ask before proceeding." All four listed. |
| C-02 | Severity vocabulary enforcement | **PASS** | "Reject any severity value not in this exact list. Ask again until one of the four is chosen." |
| C-03 | GitHub issue format | **PASS** | Four DRAFT templates each have `[{severity}] {skill}: {workflow-phrase} -- {description}` title + Expected/Actual/Steps/Context sections. |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in WRITE section. |
| C-05 | Actionable, specific issue title | **PASS** | Titles include `{skill}` + specific symptom (e.g. "workflow blocked -- {one-line description}", "workflow degraded -- {field} incorrect"). Workflow prefix does not genericize — specific problem still named. |
| C-06 | Sufficient reproducibility context | **PASS** | "Collect without prompting: topic, invocation string, related skills...These tell the maintainer where in the workflow this occurred." Steps sections in all templates. |
| C-07 | Repo open offer presented | **PASS** | `gh issue create` command in OFFER section. |
| C-08 | Severity-appropriate framing | **PASS** | crash: "Priority: HIGH -- workflow non-resumable" + Workflow impact section; improvement: "Acceptance condition" section with specific verification description. |
| C-09 | Skill context enrichment | **PASS** | Context section in all templates; workflow-framing sections (Workflow step blocked, Workflow impact, Current workflow) add enrichment intrinsically. |
| C-10 | Pre-write validation gate | **PASS** | "VALIDATE -- DO NOT write the artifact until all checks pass." Named VALIDATE phase with explicit blocking before WRITE. |
| C-11 | Corrective actions per validation check | **PASS** | Table with "Correction on fail" column; all seven rows have explicit prescribed remedies. |
| C-12 | Per-severity body templates | **PASS** | Four workflow-framed templates. crash includes Priority + Workflow impact; improvement includes Acceptance condition. Template selection determines presence of workflow-blockage section. |
| C-13 | Severity-labeled issue creation | **PASS** | `--label "{severity}"` in OFFER section gh command. |

**Score**: 4/4 essential (60) + 3/3 recommended (30) + 6/6 aspirational (10) = **100**

**Architectural note**: V-03 adds a seventh check row (Workflow frame present) in VALIDATE, producing a richer validation gate than other variations. Excess relative to rubric minimum, but not penalized.

---

#### V-04 — Lifecycle Compression: Two Macro-Phases (COLLECT+DRAFT / VALIDATE+WRITE)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | **PASS** | Form field table marks required per severity; "Ask the user to fill in all required fields before drafting." |
| C-02 | Severity vocabulary enforcement | **PASS** | "Severity must be exactly one of these four. Reject any other value and re-prompt." |
| C-03 | GitHub issue format | **PASS** | Four A2 templates with title pattern + Expected/Actual/Steps/Context structure. |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in B2. |
| C-05 | Actionable, specific issue title | **PASS** | Title patterns contain `{skill}` + specific symptom. |
| C-06 | Sufficient reproducibility context | **PASS** | Topic + Invocation in optional form row; templates include Steps to reproduce. B1 check row "Add Topic and Invocation; ask user if both absent" forces coverage. |
| C-07 | Repo open offer presented | **PASS** | `gh issue create` command in B3. |
| C-08 | Severity-appropriate framing | **PASS** | crash: Priority+Impact; improvement: Rationale+Acceptance condition. Form table makes severity-specific required fields explicit (e.g. Acceptance condition required only for improvement). |
| C-09 | Skill context enrichment | **PASS** | Optional fields (topic, invocation, chain, version) in form table; Context in all templates; B1 "Context enriched" check enforces at least one item. |
| C-10 | Pre-write validation gate | **PASS** | "**DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE**" at phase boundary + "Do not proceed to B2 until every row shows PASS" in B1. Dual blocking — phase level and row level. |
| C-11 | Corrective actions per validation check | **PASS** | "Correction on fail" column with explicit remedies for all six B1 rows. |
| C-12 | Per-severity body templates | **PASS** | Four named templates in A2; form field table makes per-severity required fields explicit. crash has Priority/Impact; improvement has Acceptance condition. |
| C-13 | Severity-labeled issue creation | **PASS** | `--label "{severity}"` in B3 gh command. |

**Score**: 4/4 essential (60) + 3/3 recommended (30) + 6/6 aspirational (10) = **100**

**Architectural note**: Phase boundary produces the clearest gate signal. "DO NOT BEGIN PHASE B" is structurally harder to skip than a pre-write checklist — phase structure makes the gate location explicit.

---

#### V-05 — Minimal-Token Density: All 13 Criteria, Densest Form

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | **PASS** | "Collect all four required fields. For any absent field, ask before drafting." All four marked `[required]`. |
| C-02 | Severity vocabulary enforcement | **PASS** | "Severity [required]: crash / wrong-output / missing-feature / improvement only; reject all other values and re-prompt." |
| C-03 | GitHub issue format | **PASS** | Four template blocks each with title line + Expected/Actual/Reproduce/Context sections. |
| C-04 | Artifact path under simulations/feedback/ | **PASS** | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in WRITE. |
| C-05 | Actionable, specific issue title | **PASS** | All title patterns contain `{skill}` + specific symptom token. |
| C-06 | Sufficient reproducibility context | **PASS** | "Reproduce: Invocation: `{invocation}` | Topic: {topic}" in all templates; "Also collect without prompting: topic, invocation..." |
| C-07 | Repo open offer presented | **PASS** | `gh issue create` command in OFFER. |
| C-08 | Severity-appropriate framing | **PASS** | crash: "Priority: HIGH -- skill non-functional" in title block; improvement: "Acceptance condition: {how you confirm it is done -- required for improvement}". "Template determines structure; do not merge or substitute." |
| C-09 | Skill context enrichment | **PASS** | Context field in all templates; "Also collect without prompting: topic, invocation, related skills, version or date." |
| C-10 | Pre-write validation gate | **PASS** | "**PRE-WRITE GATE -- STOP. Do not write until all rows pass. Apply remedy on each failure; re-check.**" Unambiguous blocking instruction. |
| C-11 | Corrective actions per validation check | **PASS** | "Remedy on fail" column with explicit prescribed remedy for each of six rows. |
| C-12 | Per-severity body templates | **PASS** | Four `*severity:*` template blocks with structurally distinct required fields. crash has Priority+Impact; improvement has Acceptance condition marked "required for improvement". "Template determines structure; do not merge or substitute" is explicit. |
| C-13 | Severity-labeled issue creation | **PASS** | `--label "{severity}"` in OFFER gh command. |

**Score**: 4/4 essential (60) + 3/3 recommended (30) + 6/6 aspirational (10) = **100**

**Architectural note**: V-05 is the hypothesis falsification proof — minimum token count achieves maximum score. The structural apparatus (four templates, blocking instruction, remedy column) is load-bearing; the prose elaboration in other variations is explanatory, not compliance-generating.

---

### Round 3 Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Verdict |
|-----------|---------------|-----------------|-------------------|-----------|---------|
| **V-01** | 60 (4/4) | 30 (3/3) | 10 (6/6) | **100** | Golden |
| **V-02** | 60 (4/4) | 30 (3/3) | 10 (6/6) | **100** | Golden |
| **V-03** | 60 (4/4) | 30 (3/3) | 10 (6/6) | **100** | Golden |
| **V-04** | 60 (4/4) | 30 (3/3) | 10 (6/6) | **100** | Golden |
| **V-05** | 60 (4/4) | 30 (3/3) | 10 (6/6) | **100** | Golden |

---

### Excellence Signals

All five variations scored 100. The axes were correctly isolated — no variation failed a criterion because of its structural choice. Three new patterns emerged:

**From V-02 (template-first)**: When severity is selected before other fields are collected, the template functions as an input schema. This is architecturally stronger than collect-then-apply: the template determines what to ask, not what to do with answers. C-12 compliance is structural, not behavioral — a user cannot supply fields the wrong-severity template doesn't have.

**From V-05 (minimal density)**: The falsification result. V-05 achieves 100 at minimum token count, confirming that the load-bearing structural elements are the four named template blocks, the explicit STOP/blocking instruction, and the remedy column. Prose elaboration, conversational framing, workflow metaphors, and phase structures are UX improvements — not compliance generators.

**From V-04 (phase boundary as gate)**: "DO NOT BEGIN PHASE B" places the gate at a location that is structurally visible and hard to skip. Compared to a numbered checklist prefixed with "before writing," a phase boundary makes the gate the architectural dividing line rather than a step within a phase.

---

### Round 3 Hypotheses — Verdicts

| Hypothesis | Result |
|------------|--------|
| Conversational register is neutral to compliance (V-01) | **Confirmed** — V-01 = 100; register does not affect any criterion. |
| Template-first ordering produces architecturally tighter C-12 (V-02) | **Confirmed** — V-02 passes C-12 with the strongest architecture, though other variations also pass; ordering is superior not uniquely necessary. |
| Workflow-blockage framing drives richer C-06/C-09 (V-03) | **Confirmed in structure** — V-03 naturally surfaces reproducibility context through workflow framing; scoring parity means rubric captures this under C-06/C-09 check rows, not exclusive to V-03. |
| Lifecycle compression preserves gate property (V-04) | **Confirmed** — Two macro-phases achieves 100; the gate is in the blocking instruction, not the four-phase count. |
| Minimum token count is irrelevant to score (V-05) | **Confirmed** — V-05 = 100; structural apparatus is load-bearing, prose is not. |

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["severity-first ordering turns the template into an input schema — template selection governs collection, not just formatting", "phase boundary as gate is structurally harder to skip than a pre-write checklist embedded within a phase", "minimum token density achieves maximum score — structural apparatus (4 templates, STOP instruction, remedy column) is load-bearing; prose elaboration is not"]}
```
