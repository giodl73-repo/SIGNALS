---
skill: validate-design
topic: ai-code-review
date: 2026-03-18
reviewer_count: 10
p1_count: 6
p2_count: 28
p3_count: 6
domain_roles_active: Security Reviewer, Legal/Compliance Reviewer, UX/DX Reviewer, Data/Analytics Reviewer
---

# validate-design: ai-code-review

Source document: `signals/specify/proposal/ai-code-review-proposal-2026-03-18.md`

---

## BLOCK 0 -- CONTENT SIGNAL CATALOGUE

| Signal phrase | Domain category |
|---------------|-----------------|
| "skill transmits code to an external LLM API; diff contains secrets that would be transmitted" | security |
| "AI-generated review artifacts may create records with legal or compliance implications" | compliance |
| "dated artifact stating 'no security issues found' could be cited in audit" | compliance/audit |
| "liability or compliance exposure in regulated development contexts" | legal |
| "developer-facing UX for invoking the skill and viewing the artifact that fits inside the PR workflow" | UX/developer-experience |
| "CLI output that maps to GitHub PR comment format" | platform/integration |
| "cross-PR pattern detection surfaces at least one recurring finding class" | data/analytics |
| "average human reviewer comment count drops by 30%+ on signal-reviewed PRs vs. control PRs" | data/measurement |

Gate F-13 check: all 8 signals recorded before BLOCK 1 opens. BLOCK 0 closed.

---

## BLOCK 1 -- EXPERT ROSTER

Stock table (fixed):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| "skill transmits code to an external LLM API; diff contains secrets that would be transmitted" | Security Reviewer | Diff transmission to external LLM introduces data exfiltration and secrets exposure risk that requires a dedicated security lens beyond what stock reviewers cover. |
| "AI-generated review artifacts may create records with legal or compliance implications" | Legal/Compliance Reviewer | Artifacts that assert findings (or their absence) in a dated, permanent record create potential liability and compliance exposure that requires dedicated legal-domain analysis. |
| "dated artifact stating 'no security issues found' could be cited in audit" | No expert needed | Covered by the Legal/Compliance Reviewer whose charter includes audit-citation liability -- a separate compliance auditor would be redundant. |
| "liability or compliance exposure in regulated development contexts" | No expert needed | Subsumed by Legal/Compliance Reviewer already added for the compliance signal above. |
| "developer-facing UX for invoking the skill and viewing the artifact that fits inside the PR workflow" | UX/DX Reviewer | Developer experience and friction design for CLI-to-PR workflow integration is outside stock discipline coverage and requires a dedicated UX/DX lens. |
| "CLI output that maps to GitHub PR comment format" | No expert needed | Covered by UX/DX Reviewer already added; GitHub format mapping is an implementation detail within the same DX concern. |
| "cross-PR pattern detection surfaces at least one recurring finding class" | Data/Analytics Reviewer | Cross-PR aggregation and pattern detection requires data model, query mechanism, and statistical validity analysis not covered by any stock discipline. |
| "average human reviewer comment count drops by 30%+ on signal-reviewed PRs vs. control PRs" | No expert needed | Covered by Data/Analytics Reviewer; measurement validity and baseline protocol are within the same data domain. |

Signal disposition gate (F-18 + F-21): all 8 BLOCK 0 signals have either a domain expert row or a populated disposition row. Gate satisfied.

BLOCK 1 domain count = 4

---

## BLOCK 1.5 -- ROSTER COMMITMENT TABLE

| Reviewer | Role | Source |
|----------|------|--------|
| Security Reviewer | Domain expert | Domain |
| Legal/Compliance Reviewer | Domain expert | Domain |
| UX/DX Reviewer | Domain expert | Domain |
| Data/Analytics Reviewer | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate:
1. Domain row count = 4. BLOCK 1 domain count = 4. Match. F-09 satisfied.
2. Domain Reviewer names (Security Reviewer, Legal/Compliance Reviewer, UX/DX Reviewer, Data/Analytics Reviewer) exactly match Expert added values in BLOCK 1. F-10 satisfied.

---

## BLOCK 2 -- PER-REVIEWER FINDINGS

---

### Security Reviewer

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | Diff content is transmitted to an external LLM API with no stated data classification controls -- there is no defined upper bound on sensitivity level of code that may be submitted | P1 | Proposed Solution; Alignment Checklist > Security | Define a data classification gate before transmission: state which classification levels (e.g., Public, Internal) are permitted; require opt-in for Confidential or higher; add this as a hard requirement in the proposed solution, not deferred to alignment |
| 2 | The proposal does not address LLM API key management: how keys are stored, rotated, or scoped to prevent unauthorized use | P2 | Alignment Checklist > Security | Add an explicit key management requirement to the security alignment question: key storage location, rotation cadence, and minimum permission scope |
| 3 | No requirement exists to negotiate or verify the LLM provider's data retention policy -- submitted diffs may be retained and used for model training by default | P2 | Alignment Checklist > Security | Add a retention policy verification requirement: zero-retention API contract or explicit provider confirmation that submitted content is not retained; document this as a prerequisite before any real PR diffs are reviewed |
| 4 | No pre-transmission secret scanning is proposed -- if a diff contains API tokens, passwords, or private keys, they will be sent to the external LLM without detection | P1 | Proposed Solution | Require a pre-transmission secret scan step (e.g., using a pattern-matching tool against common secret formats) as a mandatory gate; if secrets are detected, abort and alert the developer rather than transmitting |

---

### Legal/Compliance Reviewer

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The proposal describes artifacts that may state "no security issues found" -- a dated, permanent record making this assertion creates actionable liability if a subsequent security defect ships from a reviewed PR | P1 | Stakeholders > Security/Compliance; Proposed Solution | Mandate disclaimer language on every artifact: "This artifact represents AI-assisted review coverage only. It does not constitute a certification of security, correctness, or completeness. Human review remains the authoritative record." This language must appear in the artifact schema, not just in documentation. |
| 2 | Legal alignment is marked "Not started" with no timeline, owner, or gate -- yet the proposal permits dogfood on real PRs before legal sign-off; this creates exposure in any regulated or enterprise context | P2 | Alignment Checklist > Legal | Elevate Legal to the minimum viable alignment tier alongside Engineering and Security; the alignment checklist must explicitly block dogfood start until Legal sign-off is obtained or a scope limitation (e.g., internal-only, non-regulated repos) is formally documented |
| 3 | No artifact retention or deletion policy is defined -- dated artifacts accumulate indefinitely with no stated ownership, disposal schedule, or right-to-erasure mechanism | P2 | Proposed Solution | Define artifact lifecycle policy in the proposed solution: retention period, who owns artifacts, and whether they fall under any data governance obligation |
| 4 | If code diffs contain PII (e.g., test data with real names, email addresses in log samples), transmission to an external LLM may trigger GDPR, CCPA, or equivalent obligations not acknowledged in the proposal | P2 | Alignment Checklist > Security | Add a PII detection check to the pre-transmission gate (alongside secret scanning); document the legal basis for any PII transmission or prohibit PII-containing diffs from AI review |

---

### UX/DX Reviewer

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | "Fits inside the PR workflow" and "CLI output that maps to GitHub PR comment format" are stated as design goals but deferred entirely to the alignment checklist -- no solution is proposed for how the artifact surfaces in the developer's actual PR context | P2 | Proposed Solution; Alignment Checklist > Design | Define the artifact delivery path in the proposed solution: is it CLI stdout, a file the developer pastes, an automated PR comment via GitHub API, or a link? This is not a design detail to defer -- it is the primary adoption driver for the developer persona |
| 2 | The 2-3 minute invocation ceiling is stated but the diff input mechanism is unspecified: does the developer manually copy-paste a diff, pipe from `git diff`, provide a file path, or use a PR URL? Each mechanism has dramatically different friction and security implications | P2 | Proposed Solution | Specify the diff input mechanism in the proposed solution section; this single decision determines whether the invocation ceiling is achievable and how secrets scanning is implemented |
| 3 | The 30-day success criterion ("3 artifacts, 2+ developers") has no onboarding or documentation path -- developers cannot produce artifacts if they do not know how to invoke the skill | P3 | Success Criteria > 30 days | Add a 30-day criterion for documentation completeness: the skill must have a quickstart guide and example invocation available before the 30-day measurement window opens |
| 4 | No error or degradation states are defined: if the LLM API is unavailable, rate-limited, returns a malformed response, or times out, the skill has no stated behavior -- developers may silently lose work | P2 | Proposed Solution | Define graceful degradation behavior: on API failure, emit a structured error artifact (not a blank file) with a timestamp, error code, and retry guidance so the developer knows the review did not complete |

---

### Data/Analytics Reviewer

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The 60-day success criterion requires "average human reviewer comment count drops by 30%+" but no baseline measurement protocol is established before dogfood begins -- without a pre-dogfood baseline, this criterion cannot be evaluated | P1 | Success Criteria > 60 days | Define and execute a baseline measurement protocol before the first dogfood PR: collect human reviewer comment counts per PR for the same team over a 2-week pre-dogfood window; record reviewer identity, PR size, and sprint to enable matched comparison |
| 2 | The 90-day criterion requires "artifact search" to surface recurring findings but no search mechanism, index structure, or query interface is defined -- artifacts in flat files are not searchable without tooling | P2 | Success Criteria > 90 days | Specify the artifact search mechanism required to satisfy the 90-day criterion: whether it is a structured index file, a grep-based convention, or a dedicated query skill; this is a prerequisite for the criterion, not a post-ship enhancement |
| 3 | The north star metric compares "artifact-reviewed PRs vs. PRs without" but no control group selection methodology is defined -- self-selection bias (developers choosing which PRs to skill-review) will invalidate the comparison | P2 | Success Criteria > North Star | Add a control group protocol: matched PRs selected by the same developer, same size band (lines changed), and same sprint; document the matching criteria before dogfood to avoid post-hoc rationalization |
| 4 | Finding severity classification (HIGH/MED/LOW in the risk mitigation text) has no stated calibration protocol -- without inter-rater reliability measurement, the same diff reviewed twice may produce inconsistent severity outputs that corrupt cross-PR pattern data | P3 | Proposed Solution; Risks > Risk 2 | Define a calibration step: review at least two PRs with two independent LLM invocations (or two human evaluators scoring the AI output) before declaring the severity taxonomy stable enough for cross-PR comparison |

---

### Architect

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The full artifact schema is not defined -- the proposed solution describes the artifact's value but not its structure: required sections, finding entry format (title, severity, file reference, line reference, recommendation), coverage flags format, or frontmatter fields | P2 | Proposed Solution | Define the artifact schema before spec writing; at minimum: frontmatter fields (topic, date, diff-hash, reviewer-model), a findings table schema, and a coverage flags section with defined granularity (per-file, per-concern category) |
| 2 | The storage path `signals/review/code/` is stated without verification against Signal's 9-namespace model (scout, draft, review, flow, trace, prove, listen, program, topic) -- `review` is a valid namespace but `code` as a sub-path has no stated justification or namespace doc reference | P2 | Proposed Solution | Verify the storage path against Signal's namespace specification; if `review/code/` is the intended path, add a note explaining the sub-path convention; if not, correct the path to align with the namespace model |
| 3 | Cross-PR pattern detection is a 90-day success criterion but no architectural component supports it -- there is no index file, tag system, or query mechanism in Signal's design that would enable finding-class aggregation across artifact files | P1 | Proposed Solution; Success Criteria > 90 days | Before committing to the 90-day criterion, design the cross-PR query mechanism: an explicit index file updated on each review, a convention-based search protocol, or a dedicated `/review:patterns` skill; this is architecture that must exist before the criterion is valid |
| 4 | No versioning or amendment model exists for re-reviews: if a developer revises a PR and re-runs the skill, it is unclear whether a new artifact is created (cluttering the namespace) or the existing artifact is amended (requiring a defined amendment protocol) | P2 | Proposed Solution | Define re-review behavior: specify whether the skill creates a new artifact per invocation (with a version suffix or diff-hash identifier) or appends to an existing artifact; align this decision with Signal's finding lifecycle conventions |

---

### Code-Quality

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | Two severity taxonomies coexist in the proposal ecosystem: HIGH/MED/LOW (Risk 2 mitigation) and P1/P2/P3 (validate-design skill); the artifact must use one taxonomy, but the proposal does not specify which | P2 | Risks > Risk 2; Proposed Solution | Standardize on one severity taxonomy throughout the proposal and artifact schema; state the chosen taxonomy explicitly in the proposed solution section |
| 2 | The "cap at 10 findings, filter to HIGH+MED by default" rule is stated in the risk mitigation section (Risk 2) but does not appear in the proposed solution as a design constraint -- it will be missed during implementation | P2 | Risks > Risk 2; Proposed Solution | Move the 10-finding cap, severity filter default, and coverage summary requirement from the risk section into the proposed solution as explicit design constraints on the artifact output format |
| 3 | "Explicit coverage flags for unchecked areas" is stated as a solution feature but its format, granularity, and definition of "unchecked" are not specified -- implementers have no guidance on what constitutes a valid coverage record | P2 | Proposed Solution | Define coverage flag format: at minimum, specify granularity (per-file, per-function, per-concern category), the vocabulary for flag values (e.g., checked / partially-checked / skipped), and what triggers a "skipped" classification |
| 4 | The `/review:code` skill invocation signature is referenced but never defined -- parameters, required vs. optional arguments, output contract, and preconditions (e.g., must be invoked within a git repo) are all absent | P2 | Proposed Solution | Add a skill interface definition block to the proposed solution: skill name, parameter list (topic, diff-source, output-path), output type (artifact path), and preconditions; or reference the Signal plugin-plan.md section where this will be defined |

---

### Documentation

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The storage path `signals/review/code/` is referenced as the artifact destination but does not appear in the directory structure defined in CLAUDE.md -- the path will be undiscoverable unless the index is updated before the skill ships | P2 | Proposed Solution | Update CLAUDE.md and `signals/TOPICS.md` to include the `review/` namespace path as a known storage location before the skill ships |
| 2 | All five alignment checklist items are marked "Not started" with no assigned owners or target dates -- the checklist has no operational weight and will not drive action | P3 | Alignment Checklist | Add an owner (role or team name) and a target date to each alignment checklist item; without these, the checklist is documentation, not a gate |
| 3 | The Why Now table has two "NO" rows (User data, Platform change) with no explanation of why the absence of these triggers does not delay the initiative -- a reader unfamiliar with the context may question whether the initiative is premature | P3 | Why Now | Add one sentence per NO row explaining why the absence of that trigger is not a blocker (e.g., "User data: absence of telemetry does not delay build; cost estimate from inertia signal is sufficient for decision") |
| 4 | The proposal's Phase 1 explicitly notes "No discover-competitors signal exists" as a gap, but this gap does not appear in the Risks section -- a reader reviewing only the Risks section would be unaware of incomplete competitive intelligence | P2 | Risks | Add a Risk row for the missing competitors signal: "Competitive landscape is incomplete -- Copilot may not be the only or primary threat; risk increases if another entrant (JetBrains AI, Cursor) closes the artifact-permanence gap first" |

---

### Testing

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | No test plan or testability criteria exist for the `/review:code` skill itself -- the proposal defines success metrics for the product but not for validating that the skill produces correct, consistent output | P2 | Missing section | Add a testing strategy section: define what "correct" output means (finding accuracy vs. a human gold standard), how consistency across invocations will be measured, and what regression testing looks like after LLM model updates |
| 2 | The 30-day success criterion ("3 artifacts, 2+ developers, 5+ findings each") has no quality gate -- an artifact with 5 boilerplate or trivially incorrect findings satisfies the criterion equally to one with 5 high-value findings | P2 | Success Criteria > 30 days | Add a quality gate to the 30-day criterion: at least 3 of 5 findings per artifact must be confirmed actionable by the developer who ran the review (simple self-report, recorded in a follow-up artifact or PR comment) |
| 3 | The hypothesis is OPEN at 72% confidence and the proposal acknowledges a falsification condition, but no falsification test schedule is defined -- if the hypothesis is never tested, Risk 3 ("hypothesis falsifies") cannot be monitored or mitigated | P2 | Risks > Risk 3 | Add a falsification test schedule to Risk 3: the three tests defined in the hypothesis signal (benchmark, coverage audit, literature search) must be completed within the 60-day window; if not, Risk 3 escalates to P1 |
| 4 | Coverage flag completeness has no acceptance criteria -- the proposal states that coverage flags will show "what was checked even when findings are minimal" but does not define when a coverage record is considered complete vs. partial | P3 | Proposed Solution | Define coverage completeness acceptance criteria: a coverage record is complete when every file in the diff has a flag (checked/skipped), and every skipped file has a stated reason |

---

### Process

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The alignment checklist lists all five teams in flat order, but the proposal text (Phase 3) states Engineering + Security are minimum viable before spec writing -- this ordering is not enforced in the checklist structure | P2 | Alignment Checklist; Phase 3 | Restructure the alignment checklist into two explicit tiers: "Gate 1: before spec writing" (Engineering, Security) and "Gate 2: before ship" (Design, Legal, Support); mark Gate 1 items as blocking |
| 2 | The Tech Lead is identified as a veto holder over the review process but is absent from the alignment checklist -- they could veto post-build if the artifact format does not match their workflow expectations | P2 | Stakeholders; Alignment Checklist | Add Tech Lead to the alignment checklist with a specific question: "Does the proposed artifact format and invocation model fit into the team's existing PR workflow without adding overhead?" |
| 3 | The "critical alignment path" section states "Tech Lead first" but Phase 3 elevates Security to minimum viable alongside Engineering -- these two sections give conflicting guidance on sequencing | P2 | Critical alignment path; Phase 3 minimum viable | Resolve the contradiction: decide whether Security or Tech Lead is the first gate and state the sequence explicitly in one authoritative location; delete the redundant guidance from the other section |
| 4 | "Dogfood" is referenced in Risk 1 mitigation ("ship a working dogfood version within 30 days on Signal's own codebase") but no dogfood scope is defined: which team, which repo, which PR size range, minimum number of PRs required | P3 | Risks > Risk 1 | Define the dogfood scope as a formal milestone: team (Signal developers), repo (C:\src\sim), PR size range (e.g., 50-500 lines changed), minimum PRs (3), and review completion criteria |

---

### Implementation

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The diff input mechanism is not defined anywhere in the proposal -- "passing the diff context" could mean manual paste, `git diff` pipe, file path argument, PR URL, or GitHub API pull -- this is the primary implementation decision and shapes everything downstream (secret scanning, invocation friction, API payload size) | P1 | Proposed Solution | Define the diff input mechanism before spec writing; recommended: `git diff HEAD~1` piped to stdin as the primary path, with a `--file` fallback for reviewing a saved diff; document this as a required design decision in the proposed solution section |
| 2 | The LLM prompt structure is not defined -- "structured AI code review" is the stated outcome but what categories of issues the LLM is instructed to look for, what it is told to skip, and how findings are formatted in the response are all absent | P2 | Proposed Solution | Define the reviewer prompt structure in the proposed solution: at minimum, the review categories (correctness, security, style, test coverage), the output format template the LLM is asked to follow, and the explicit scope limitations ("do not flag style issues below P2") |
| 3 | The 60-day and 90-day success criteria require comparing signal-reviewed PRs to control PRs, but no mechanism exists for tracking which PRs received a skill review -- without this, the comparison dataset cannot be assembled | P2 | Success Criteria | Define the PR tracking mechanism before dogfood begins: a PR label applied when the skill is invoked, a log entry in a tracking file, or a field in the artifact frontmatter that records the PR identifier |
| 4 | The 30-day dogfood target ("ship a working dogfood version within 30 days") appears only in Risk 1 mitigation -- it is not a formal implementation milestone with defined deliverables, dependencies, or a blocking status | P2 | Risks > Risk 1 | Promote the 30-day dogfood target to a formal implementation milestone in the proposed solution or a new "Implementation Plan" section: defined deliverables (working CLI invocation, at least one artifact produced), dependencies (Engineering alignment complete, secret scanning gate in place), and a clear blocking criteria |

---

## BLOCK 3 -- SYNTHESIS

```
Overall verdict: NEEDS-WORK

P1 blockers (must resolve before implementation):
  - Security-1   Security Reviewer      -- Diff classification controls absent; no upper bound on data sensitivity permitted in LLM payloads
  - Security-4   Security Reviewer      -- No pre-transmission secret scanning gate; secrets will be sent to external LLM without detection
  - Legal-1      Legal/Compliance Reviewer -- Artifact language creates liability; "no security issues found" assertion requires mandatory disclaimer in schema
  - Data-1       Data/Analytics Reviewer   -- No baseline measurement protocol; 60-day 30% reduction criterion is unvalidatable without pre-dogfood baseline
  - Architect-3  Architect              -- Cross-PR query mechanism not designed; 90-day pattern detection criterion depends on non-existent infrastructure
  - Impl-1       Implementation         -- Diff input mechanism undefined; primary implementation decision shapes secret scanning, friction, and API payload design

P2 conditions (must resolve before sign-off):
  - Security-2, Security-3     LLM API key management and provider data retention policy not addressed
  - Legal-2, Legal-3, Legal-4  Legal alignment has no gate; artifact retention policy absent; PII detection not required
  - UX-1, UX-2, UX-4          PR workflow integration deferred; diff input mechanism unspecified; no error state handling
  - Data-2, Data-3             Artifact search mechanism undefined; control group methodology absent for north star metric
  - Architect-1, Architect-2, Architect-4  Artifact schema undefined; storage path unverified; re-review versioning absent
  - CQ-1 through CQ-4          Severity taxonomy inconsistency; 10-finding cap not in solution; coverage flags undefined; skill interface absent
  - Docs-1, Docs-4             Storage path absent from CLAUDE.md; missing competitors gap not surfaced as risk
  - Testing-1, Testing-2, Testing-3  No skill test plan; 30-day criterion has no quality gate; falsification test unscheduled
  - Process-1 through Process-3  Alignment checklist unsequenced; Tech Lead absent from checklist; alignment path contradicts Phase 3
  - Impl-2, Impl-3, Impl-4    LLM prompt structure undefined; PR tracking mechanism absent; dogfood target not a formal milestone

Cross-reviewer consensus:
  Four independent reviewers (Architect, Code-Quality, Implementation, UX/DX) identified the same root gap: the proposal
  describes outcomes and value but defers all structural decisions -- artifact schema, diff input model, skill interface,
  coverage flag format -- to later phases without specifying where those decisions will be made. This is a proposal that
  knows what it wants to achieve but has not yet committed to how any of it works. Security and Legal reviewers
  independently identified that data transmission to an external LLM is treated as a detail in the alignment checklist
  when it is actually a P1 design constraint that must be resolved before any real PR diffs are reviewed.

Strongest signal:
  Data-1 (Data/Analytics Reviewer, P1): No baseline measurement protocol exists for the primary success criterion.
  The 60-day "30% reduction in human reviewer comments" metric is the proposal's core validation gate, but without
  a pre-dogfood baseline collection window, the criterion cannot be evaluated regardless of how well the skill
  performs. This is not a documentation gap -- it is a measurement design gap that must be resolved before the
  first dogfood PR is reviewed.
```

---

## AMEND

Three targeted amendments based on the highest-severity findings:

**Amendment 1 -- Data security constraints section (new, in Proposed Solution)**

What changes: Add a dedicated "Data Security Constraints" subsection to the Proposed Solution.
Where: After the solution description paragraph, before the Why Now section.
Why: P1 findings Security-1 and Security-4 establish that the absence of data classification controls and pre-transmission secret scanning are blockers to implementation -- these are not alignment questions, they are design requirements that must appear in the solution spec.

Content to add:
> **Data Security Constraints (required, not deferred)**
> 1. Pre-transmission secret scan: the skill MUST run a pattern-matching scan for common secret formats (API tokens, private keys, connection strings) before transmitting any diff content to the LLM API. If secrets are detected, the skill aborts and emits a structured error artifact -- it does not transmit.
> 2. Data classification gate: the skill MUST document which data classification levels are permitted for AI review. Default: Internal and below. Confidential-classified repositories require an explicit opt-in flag.
> 3. PII detection: the skill SHOULD run a PII pattern check alongside the secret scan; if PII is detected, log a warning in the artifact header.
> 4. LLM provider data retention: before any real PR reviews, the team MUST obtain and document confirmation from the LLM provider that submitted content is not retained for training.

**Amendment 2 -- Artifact schema definition block (new, in Proposed Solution)**

What changes: Add a formal artifact schema definition to the Proposed Solution.
Where: Append to the Proposed Solution section as a "Artifact Schema" subsection.
Why: P2 findings Architect-1, Code-Quality-1, Code-Quality-3, and Code-Quality-4 all trace back to the same gap: no schema exists for the review artifact, creating ambiguity in severity taxonomy, coverage flags, and finding structure that will result in inconsistent artifacts across reviewers and PRs.

Content to add:
> **Artifact Schema (required fields)**
> Frontmatter: `skill`, `topic`, `date`, `diff-hash`, `reviewer-model`, `finding-count`, `coverage-pct`
> Findings table: `| # | Finding | Sev | File | Line | Recommendation |` -- severity values: P1/P2/P3 (P1 = blocks merge, P2 = must fix before review sign-off, P3 = should fix before ship).
> Coverage flags: one row per file in the diff: `| file-path | checked / partially-checked / skipped | reason-if-skipped |`
> Output cap: maximum 10 findings per artifact; filter to P1+P2 by default; P3 findings appear in a collapsible "additional findings" section.
> Disclaimer (required, first line of artifact body): "AI-assisted review only. Not a certification of security, correctness, or completeness."

**Amendment 3 -- Baseline measurement protocol (new, in Success Criteria)**

What changes: Add a "Baseline Protocol" subsection to the Success Criteria section, before the 30-day horizon row.
Where: Success Criteria section, as a prerequisite gate before the measurement window opens.
Why: P1 finding Data-1 establishes that the 60-day "30% reduction" criterion is unvalidatable without a pre-dogfood baseline; this is not optional and must be treated as a prerequisite step, not a measurement taken after the fact.

Content to add:
> **Baseline Protocol (prerequisite before dogfood begins)**
> Before the first dogfood PR is reviewed with `/review:code`:
> 1. Collect human reviewer comment counts for the target team over a 2-week baseline window on PRs that were NOT skill-reviewed.
> 2. Record per-PR: developer identity, lines changed, sprint number, human reviewer comment count, and time-to-approval.
> 3. Store baseline in `signals/review/baselines/ai-code-review-baseline-{date}.md`.
> 4. The 60-day criterion is evaluated by comparing post-dogfood PRs (matched by developer + size band + sprint) against this baseline. Self-selected PRs are excluded from the comparison if they differ materially in size or complexity from the baseline sample.
```

---

QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: All 6 blocks complete. 10 reviewers (4 domain + 6 stock). 6 P1 blockers, 28 P2 conditions, 6 P3 items. Gate checks F-01 through F-21 satisfied. Strongest finding: absence of baseline measurement protocol makes the primary success criterion unvalidatable -- this must be resolved before dogfood begins, not during.
