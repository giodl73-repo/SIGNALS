Now I have everything needed to score. Let me evaluate each variation systematically against the 9 rubric criteria.

---

## Scorecard — `file-issue` Round 1

**Rubric version**: v1 | **Date**: 2026-03-17 | **Variations evaluated**: V-01 through V-05

---

### V-01 — Phrasing Register: Conversational / Ask-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All four required fields captured | PASS | Ask-first design explicitly collects skill, expected, actual, severity one at a time; hypothesis claims no sacrifice of C-01 |
| C-02 Severity uses valid enum | PASS | Inferred from hypothesis ("without sacrificing C-01/C-02") and five-step structure; implementation less visible due to truncated body |
| C-03 GitHub issue format present | PASS | "Draft issue" step 3 produces GitHub-formatted output with title and labeled sections (tail shows title template) |
| C-04 Local artifact written to simulations/feedback/ | PASS | "Write artifact" step 4 with path visible in tail end of body |
| C-05 Actionable, specific title | PASS | Title template includes `{skill-name}` and symptom (fragment visible in body tail) |
| C-06 Sufficient reproducibility context | PASS | Enrichment step (step 2) specifically surfaces topic, invocation chain, context that templates miss |
| C-07 Repo open offer presented | PASS | Step 5 is explicit offer: "Would you like me to open this as a GitHub issue? I can run: `gh issue create`" |
| C-08 Severity-appropriate framing | **FAIL** | Differentiator table shows only "tone note" — weakest C-08 implementation across all variations; no inline rules or structural enforcement |
| C-09 Skill context enrichment | PASS | Enrichment step (step 2) explicitly asks for topic, invocation chain, related artifacts |

**Essential pass**: 4/4 ✓ | **Recommended pass**: 3/3 | **Aspirational pass**: 1/2

```
composite = (4/4 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = 95
```

**Verdict**: Acceptable (95, all essential pass) — falls short of aspirational ceiling due to weak C-08.

---

### V-02 — Output Format: Table-Driven Intake

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All four required fields captured | PASS | Table has explicit rows for Skill, Expected, Actual, Severity; "If the user has not supplied any field, ask for it before proceeding" |
| C-02 Severity uses valid enum | PASS | Inline in table: "crash / wrong-output / missing-feature / improvement — pick one"; "reject any other value and ask again" — explicit enforcement |
| C-03 GitHub issue format present | PASS | Title `[{severity}] {skill}: {symptom}` + Expected, Actual, Steps to reproduce, Context sections all required |
| C-04 Local artifact written to simulations/feedback/ | PASS | Path `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` + full frontmatter spec (skill, topic, item, date, severity, target_skill) |
| C-05 Actionable, specific title | PASS | Title derived from "Expected vs Actual delta" — names skill and observable symptom explicitly |
| C-06 Sufficient reproducibility context | PASS | Table captures Invocation and Related; issue body has "Steps to reproduce" with Invocation, Topic, Related required |
| C-07 Repo open offer presented | PASS | "Repo offer" block with `gh issue create --title ... --body-file {artifact-path}` |
| C-08 Severity-appropriate framing | PASS | Four explicit tone rules inline: crash = "Immediate triage needed", improvement = "enhancement would increase quality", etc. |
| C-09 Skill context enrichment | PASS | Table has Topic and Related rows; issue body has Context section for "version, date, chain, or artifact context" |

**Essential pass**: 4/4 ✓ | **Recommended pass**: 3/3 | **Aspirational pass**: 2/2

```
composite = (4/4 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100
```

**Verdict**: Golden (100, all essential pass).

---

### V-03 — Lifecycle Emphasis: Explicit 4-Phase Boundaries

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All four required fields captured | PASS | PHASE 1 (SETUP) will not proceed to Phase 2 until all four fields are present; each absence is flagged individually |
| C-02 Severity uses valid enum | PASS | SETUP requires severity "exactly one of: crash, wrong-output, missing-feature, improvement" — invalid value blocks progression |
| C-03 GitHub issue format present | PASS | PHASE 2 (EXECUTE) produces title + six required body sections |
| C-04 Local artifact written to simulations/feedback/ | PASS | PHASE 4 (AMEND) writes to `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` with full frontmatter |
| C-05 Actionable, specific title | PASS | EXECUTE: "title must name the skill and the observable symptom; reject generic titles" — explicit rejection rule |
| C-06 Sufficient reproducibility context | PASS | EXECUTE requires "Steps to reproduce" section; PHASE 3 check 4 asks "Is there enough detail for a maintainer to reproduce?" before artifact write |
| C-07 Repo open offer presented | PASS | PHASE 4 ends with "Would you like to open this as a GitHub issue?" + full `gh issue create` command |
| C-08 Severity-appropriate framing | PASS | Tone guidance for all 4 severities in EXECUTE; PHASE 3 check 5 explicitly validates tone match before proceeding |
| C-09 Skill context enrichment | PASS | SETUP notes enriching context already provided; EXECUTE requires a "Context" section for "topic, related skills, version/date, or linked artifacts" |

**Essential pass**: 4/4 ✓ | **Recommended pass**: 3/3 | **Aspirational pass**: 2/2

```
composite = (4/4 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100
```

**Verdict**: Golden (100, all essential pass). FINDINGS phase as pre-write quality gate is a standout structural choice.

---

### V-04 — Role Sequence + Output Format: Reporter / Maintainer Handoff

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All four required fields captured | PASS | Reporter table with all four required fields; "all must be present before handing off" is blocking |
| C-02 Severity uses valid enum | PASS | Reporter table: "Exactly one of: crash, wrong-output, missing-feature, improvement"; Maintainer check catches enum errors |
| C-03 GitHub issue format present | PASS | Final issue format has Title + Expected, Actual, Steps to reproduce, Context — all labeled sections required |
| C-04 Local artifact written to simulations/feedback/ | PASS | LOG section: `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` with frontmatter specified |
| C-05 Actionable, specific title | PASS | Maintainer check "Title specificity: Names skill + symptom, not generic" with explicit corrective action "Rewrite title" |
| C-06 Sufficient reproducibility context | PASS | Maintainer check "Reproducibility: Enough to reproduce or investigate" with corrective action "Add steps or ask user" |
| C-07 Repo open offer presented | PASS | OFFER section with `gh issue create` command |
| C-08 Severity-appropriate framing | PASS | Maintainer check "Severity tone: Matches the enum value" with corrective action "Reframe body tone" |
| C-09 Skill context enrichment | PASS | Maintainer check "Context: At least one item beyond the 4 fields" with corrective action "Add topic/date/chain/artifact" — only variation that makes C-09 an explicit gated check |

**Essential pass**: 4/4 ✓ | **Recommended pass**: 3/3 | **Aspirational pass**: 2/2

```
composite = (4/4 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100
```

**Verdict**: Golden (100, all essential pass). Strongest C-09 enforcement of any variation via Maintainer check-with-corrective-action.

---

### V-05 — Inertia Framing + Phrasing Register: Severity-Led Triage

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All four required fields captured | PASS | Severity first via triage; "collect the three remaining required fields" then covers Skill, Expected, Actual |
| C-02 Severity uses valid enum | PASS | Triage presents exact numbered list of four valid values; "Once severity is confirmed" implies validation gate |
| C-03 GitHub issue format present | PASS | Four per-severity templates each produce GitHub format with title + multiple labeled sections |
| C-04 Local artifact written to simulations/feedback/ | PASS | Explicit path + full frontmatter matching V-02/V-03 spec |
| C-05 Actionable, specific title | PASS | Per-severity titles are the most specific across all variations: crash = "unhandled error -- {one-line description}", wrong-output = "{field} -- expected {X}, got {Y}" |
| C-06 Sufficient reproducibility context | PASS | Every severity template has a dedicated reproduction section: crash has "Reproduction: Invocation, Input, Env"; wrong-output has "Reproduction: {invocation, input, topic}"; missing-feature has "Scope" |
| C-07 Repo open offer presented | PASS | Offer section includes `gh issue create` with `--label "{severity}"` — only variation to include label flag |
| C-08 Severity-appropriate framing | PASS | Strongest C-08 implementation: per-severity templates make tone mismatch structurally impossible. Crash has "Priority: HIGH — skill non-functional"; improvement has "Rationale" + "Acceptance condition" framing |
| C-09 Skill context enrichment | PASS | Per-severity enrichment fields: crash has "Env: {topic, date, chain}", wrong-output has "Delta", missing-feature has "References: {any spec, rubric, or related skill}", improvement has "Acceptance condition" |

**Essential pass**: 4/4 ✓ | **Recommended pass**: 3/3 | **Aspirational pass**: 2/2

```
composite = (4/4 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100
```

**Verdict**: Golden (100, all essential pass). Strongest C-08 implementation of any variation; per-severity templates also deliver the richest C-09 enrichment.

---

## Rankings

| Rank | Variation | Composite | All Essential | Verdict |
|------|-----------|-----------|---------------|---------|
| 1 | V-05 Severity-Led Triage | 100 | ✓ | Golden |
| 2 | V-03 Lifecycle Phases | 100 | ✓ | Golden |
| 3 | V-04 Reporter/Maintainer | 100 | ✓ | Golden |
| 4 | V-02 Table-Driven Intake | 100 | ✓ | Golden |
| 5 | V-01 Ask-First | 95 | ✓ | Acceptable |

**Tiebreaker rationale at 100**: V-05 edges V-03 because structural enforcement of C-08 (hardest criterion to satisfy robustly) is a higher-value achievement than a quality gate; once a skill has structural tone enforcement, a separate gate phase is a nice-to-have. V-03 edges V-04 because FINDINGS phase catches any failure before artifact write, while the Reporter/Maintainer split adds interaction overhead for the same coverage. V-02 scores last at 100 because it is the most fragile structurally — a model could fill the table correctly but still write a generic title if the symptom derivation step is lazy.

---

## Excellence Signals

Three patterns in the top-scoring variations that made them better:

**1. Severity-gated body templates** (V-05)
Each severity value maps to a distinct issue schema with different field names and tone instructions built in. A crash template cannot produce casual improvement framing because the fields themselves are different. This is architectural enforcement, not a reminder note — the strongest possible defense of C-08.

**2. Pre-write quality gate** (V-03 FINDINGS phase)
A mandatory self-evaluation phase placed *between* drafting and artifact write. The skill must answer five explicit yes/no checks and revise before proceeding. This catches C-01, C-02, C-05, C-06, and C-08 failures before they become logged artifacts — turning the skill into a two-pass system without requiring a second role.

**3. Maintainer check-with-corrective-action** (V-04)
The Maintainer role table lists not just the check but the corrective action if it fails ("Rewrite title", "Add steps or ask user", "Add topic/date/chain/artifact"). This makes C-09 gated rather than aspirational — the skill will not finalize until at least one enriching context item is present. The only variation that treats C-09 as a blocking criterion rather than a recommendation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["severity-gated body templates", "pre-write quality gate", "maintainer check-with-corrective-action"]}
```
