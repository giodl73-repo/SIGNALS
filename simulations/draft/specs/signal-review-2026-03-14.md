# Review Specification

**Topic**: sim
**Namespace**: /review:
**Skills**: 4
**Default mode**: Full
**Audience**: Architects, tech leads, PMs, and domain experts who need multi-perspective validation before committing to a design direction

## Purpose

Does the design hold up when examined by disciplined reviewers, persona advocates, domain experts, and real customer archetypes? /review: answers "Is the design right?" by running the same artifact through independent, role-specific lenses and synthesizing consensus findings.

## Skills

### /review:design

**What**: Multi-expert review of a design artifact (spec, proposal, ADR) through auto-selected domain experts and the 6 standard disciplines.
**Stock roles**: 6 disciplines (architect, code quality, documentation, testing, process, implementation), domain experts (auto-selected from content — e.g., a spec mentioning RBAC selects a security architect, a spec mentioning Dataverse selects a platform engineer)
**Input**: Path to a design artifact (spec, proposal, ADR, or design document). Optionally, explicit expert names to include.
**Output**: Per-reviewer findings with severity (P1 blocking, P2 major, P3 minor), consensus analysis, split opinions, and a synthesized review summary.
**Lifecycle**:
- Setup: Read the artifact, extract key topics (security, data model, API surface, etc.), auto-select 3-5 expert roles from content signals, confirm selection with user. Identify which of the 6 disciplines are relevant.
- Execute: Each expert and discipline reviews independently. Experts score against their domain criteria. Disciplines score against their standard rubric. All findings tagged with severity and specific line/section references.
- Findings: Cross-reviewer synthesis — identify consensus issues (2+ reviewers flag the same thing), split opinions (reviewers disagree), and unique catches (one reviewer found something others missed). Rank by severity. Produce a single summary document.
- Amend: Author addresses findings one by one (accept, reject with rationale, or defer). Re-run specific reviewers on changed sections only. Iterate until no P1 findings remain.
**Lightweight**: `--quick` auto-selects disciplines from content, merges Execute + Findings into a single review document, skips Amend.
**Artifact**: `review/design/sim-{slug}-{date}.md`
**Example**:
User runs `/review:design design/auth/SPEC-AUTH-01.md`. Setup reads the spec, detects topics: OAuth, token refresh, RBAC, Dataverse security roles. Auto-selects: Security Architect, API Designer, Dataverse Platform Engineer. Confirms with user. Execute produces 3 expert reviews + 4 discipline reviews (architecture, code quality, testing, implementation — documentation and process skipped as not relevant). Expert "Security Architect" flags P1: "Token refresh window of 5 minutes creates a replay attack surface — reduce to 30 seconds or add jti claim." Expert "API Designer" flags P2: "No rate limiting specified for token endpoint." Discipline "Testing" flags P2: "No scenario covers expired-token-during-batch-operation." Findings synthesis: 1 P1 (consensus — security architect and code quality both flagged token window), 3 P2, 2 P3. Amend: author reduces refresh window to 30 seconds, adds rate limiting section, adds batch-expiry scenario. Re-runs Security Architect on changed sections — P1 resolved.

### /review:code

**What**: Multi-discipline code review of implementation artifacts (source files, PRs, diffs) against the 6 standard disciplines.
**Stock roles**: 6 disciplines (architect, code quality, documentation, testing, process, implementation), domain experts (auto-selected from codebase context — language, framework, platform)
**Input**: Path to source files, a PR number, or a git diff range. Optionally, the spec the code implements (for contract validation).
**Output**: Per-discipline findings with severity, code-level annotations (file:line references), and a synthesized review with pass/fail per discipline.
**Lifecycle**:
- Setup: Read the code, identify language/framework/platform context, auto-select domain experts (e.g., TypeScript code selects a Node.js expert, Dataverse plugin code selects a Dataverse platform engineer). If a spec is provided, load it as the contract baseline.
- Execute: Each discipline reviews independently. Architecture checks layering and dependency direction. Code quality checks conventions and maintainability. Testing checks coverage and edge cases. Implementation checks correctness and performance. If a spec was provided, each reviewer also checks spec compliance.
- Findings: Synthesize across disciplines. Group by file. Identify patterns (e.g., "error handling is inconsistent across 4 files" rather than 4 separate findings). Pass/fail per discipline with rationale.
- Amend: Author fixes code issues, re-runs affected disciplines on changed files only. Iterate until all disciplines pass.
**Lightweight**: `--quick` runs only code quality + implementation disciplines, produces inline annotations, skips Amend.
**Artifact**: `review/code/sim-{slug}-{date}.md`
**Example**:
User runs `/review:code craft-cli/src/astro/compiler.ts --spec design/astro/SPEC-ASTRO-01.md`. Setup detects TypeScript, Node.js, compiler domain. Auto-selects: Compiler Expert, TypeScript Specialist. Execute: Architecture flags P2: "Parser and lexer in same file — spec says separate compilation units." Code Quality flags P3: "3 functions exceed 50 lines." Testing flags P1: "No test covers malformed input — spec section 4.2 requires graceful degradation." Implementation passes. Findings synthesis: 1 P1 (testing gap against spec), 1 P2, 1 P3. Author adds malformed-input tests, splits parser/lexer, refactors long functions. Re-run: all disciplines pass.

### /review:users

**What**: 5 persona advocates walk through a design or feature from their specific user perspective, identifying confusion, friction, fear, jargon, and missing context.
**Stock roles**: 5 persona advocates (maker, developer, compliance officer, supervisor, operator)
**Input**: Path to a design artifact, feature spec, or CLI help output. Optionally, a specific user journey to walk through.
**Output**: Per-persona walkthrough report with friction points, confusion moments, fear triggers, jargon flags, and a per-persona usability score (1-5).
**Lifecycle**:
- Setup: Read the artifact, identify the user-facing surface (CLI commands, configuration files, error messages, documentation). For each persona, determine their typical entry point and journey through the feature. Confirm scope with user.
- Execute: Each persona walks through the artifact independently, narrating their experience in first person. Maker asks "Can I do this without reading a manual?" Developer asks "Are outputs machine-parseable?" Compliance asks "Would an auditor accept this?" Supervisor asks "Can I intervene in 30 seconds?" Operator asks "Would a Terraform user be confused?" Each persona flags specific moments of confusion, friction, or delight with exact quotes from the artifact.
- Findings: Cross-persona synthesis — identify universal friction (all personas struggle), role-specific friction (only one persona struggles), and persona conflicts (what helps one persona hurts another). Rank findings by how many personas are affected. Compute aggregate usability score.
- Amend: Author addresses universal friction first, then role-specific issues. Re-walks affected personas through changed sections. Iterate until no persona scores below 3/5.
**Lightweight**: `--quick` runs maker + developer personas only, produces a single combined walkthrough, skips Amend.
**Artifact**: `review/users/sim-{slug}-{date}.md`
**Example**:
User runs `/review:users design/admin/SPEC-AD-02.md --journey "create a new solution and deploy it"`. Setup identifies CLI surface: `craft solution new`, `craft solution pack`, `craft deploy`. Determines each persona's entry point. Execute: Maker walks through — "I typed `craft solution new` and it asked me 6 questions. By question 3 I don't know what 'managed vs unmanaged' means. I would stop here." (Score: 2/5, friction at terminology). Developer walks through — "JSON output from `craft solution pack` is clean. But `--dry-run` doesn't show the actual payload, just 'would deploy'. I need the payload for CI." (Score: 3/5, friction at CI integration). Compliance officer walks through — "Where is the audit log? I deployed a solution but there's no record of who approved it or when." (Score: 1/5, blocking — no audit trail). Supervisor walks through — "`craft deploy --status` shows current state but I can't cancel a running deployment." (Score: 3/5). Operator walks through — "This feels like Terraform plan/apply. Good. But `craft deploy` doesn't show a diff of what changes." (Score: 3/5). Findings: P1 (universal): no deployment diff. P1 (compliance-specific): no audit trail. P2: terminology barrier for makers. P2: no payload preview for CI. Amend: author adds audit logging, deployment diff, glossary tooltip system. Re-walk: compliance scores 4/5, maker scores 3/5.

### /review:customers

**What**: 12 customer personas (C-01 through C-12) evaluate a feature, naming decision, UX pattern, or pricing model from their industry and role perspective, producing quantified scores and verbatim reactions.
**Stock roles**: 12 customer personas — C-01 Maria Chen (Maker/Retail), C-02 James Okafor (Developer/SaaS), C-03 Priya Sharma (Architect/Finance), C-04 David Kim (PM/Healthcare), C-05 Elena Vasquez (Compliance/Insurance), C-06 Robert Tanaka (Auditor/Government), C-07 Catherine Moore (Executive/Consulting), C-08 Ahmad Al-Rashid (Partner/Energy), C-09 Lisa Johansson (SRE/Telecom), C-10 Marcus Rivera (Data Scientist/Education), C-11 Tomoko Watanabe (Team Lead/Manufacturing), C-12 Frank Hoffmann (Regulator/Legal)
**Input**: The feature, name, UX pattern, or pricing model to evaluate. Context about what it does and who it's for.
**Output**: Per-persona evaluation with scores (usefulness 1-5, clarity 1-5, would-adopt 1-5), verbatim reactions, and a persona-weighted aggregate score.
**Lifecycle**:
- Setup: Present the feature to all 12 personas. For each persona, establish their industry context, budget constraints, technical depth, and primary concern. Identify which personas are primary audience vs. secondary vs. not-target.
- Execute: Each persona evaluates independently. They score on 3 dimensions: usefulness ("does this solve my problem?"), clarity ("do I understand what this does?"), would-adopt ("would I actually use this?"). They provide verbatim first reactions, concerns, and dealbreakers. Non-target personas still evaluate — their reactions reveal positioning leaks.
- Findings: Persona-weighted synthesis. Primary-audience personas weighted 3x, secondary 2x, non-target 1x. Identify adoption blockers (any primary persona scores would-adopt < 3), positioning leaks (non-target personas are confused about who this is for), and delight signals (scores of 5). Compute weighted aggregate across all dimensions.
- Amend: Author addresses adoption blockers first, then positioning leaks. Re-evaluates affected personas on changes. Iterate until no primary persona has would-adopt < 3.
**Lightweight**: `--quick` runs 4 representative personas (C-01 maker, C-02 developer, C-05 compliance, C-07 executive), produces a single scorecard, skips Amend.
**Artifact**: `review/customers/sim-{slug}-{date}.md`
**Example**:
User runs `/review:customers "New feature: AI-assisted deployment validation — scans your solution for common deployment failures before you ship"`. Setup: primary audience = C-02 (developer), C-03 (architect), C-09 (SRE), C-11 (team lead). Secondary = C-04 (PM), C-08 (partner). Non-target = C-01 (maker), C-06 (auditor), C-07 (executive), C-10 (data scientist), C-12 (regulator). Execute: C-02 James (developer) scores usefulness 5, clarity 4, would-adopt 5 — "Finally. I've shipped broken solutions 3 times this quarter. If this catches managed-component collisions, I'm in." C-01 Maria (maker) scores usefulness 2, clarity 2, would-adopt 1 — "What's a 'solution'? I just want my workflow to work. This sounds like something my IT team would use, not me." C-05 Elena (compliance) scores usefulness 4, clarity 3, would-adopt 4 — "If it produces a validation report I can attach to the change request, yes. Without evidence artifacts, it's just another tool." C-07 Catherine (executive) scores usefulness 3, clarity 2, would-adopt 2 — "How much does this save us per deployment? I need an ROI number, not a feature description." Findings: Weighted aggregate 3.8/5. No adoption blockers in primary audience. Positioning leak: C-01 confused — feature name uses jargon ("solution", "deployment validation") that excludes makers. Delight: C-02 and C-09 both score 5 on usefulness. Recommendation: add plain-language subtitle ("Catch problems before you ship"), add ROI estimator for executive audience.

## Roles

### Stock roles

| Role | What It Does | Used By |
|------|-------------|---------|
| Architect (discipline) | Reviews system structure, layering, dependency direction, separation of concerns | design, code |
| Code Quality (discipline) | Reviews conventions, naming, maintainability, complexity, duplication | design, code |
| Documentation (discipline) | Reviews accuracy, completeness, audience-appropriateness of docs and comments | design, code |
| Testing (discipline) | Reviews test coverage, edge cases, scenario completeness, validation strategy | design, code |
| Process (discipline) | Reviews workflow, gates, progress tracking, team coordination patterns | design |
| Implementation (discipline) | Reviews correctness, performance, security, error handling, resource management | design, code |
| Maker (persona) | Non-technical user who builds without code — tests for jargon, complexity barriers | users |
| Developer (persona) | Technical user who extends and automates — tests for machine-parseability, CI integration | users |
| Compliance (persona) | Governance-focused user — tests for audit trails, evidence, regulatory acceptability | users |
| Supervisor (persona) | Management user who oversees and intervenes — tests for visibility, control, response time | users |
| Operator (persona) | Infrastructure user who deploys and monitors — tests for operational patterns, health checks | users |
| C-01 through C-12 (customers) | 12 industry-specific personas spanning maker to regulator — tests for adoption, clarity, positioning | customers |
| Domain experts (auto-selected) | Named experts selected from content signals — compiler theorists, security architects, platform engineers, etc. | design, code |

### Custom roles (optional)

`/review:design` and `/review:code` benefit most from custom expert roles. If your domain has specific experts not covered by auto-selection (e.g., a medical informaticist for healthcare data models, a NERC CIP specialist for energy compliance), create them as role files in `.roles/{name}/ROLE.md` with expertise description, evaluation criteria, and typical findings. Custom roles participate in the same lifecycle as stock roles.

`/review:customers` supports adding personas C-13+ for industry-specific testing. Create persona files following the C-01 template in `design/admin/focus/Q07/data/customer-personas.md`.

## Artifacts

```
review/
├── design/
│   ├── sim-auth-spec-2026-03-14.md         # Expert + discipline review of auth spec
│   ├── sim-admin-proposal-2026-03-15.md     # Review of admin proposal
│   └── sim-flash-adr-2026-03-16.md          # Review of Flash ADR
├── code/
│   ├── sim-compiler-pr-387-2026-03-14.md    # Code review of PR #387
│   └── sim-sdk-refactor-2026-03-15.md       # Code review of SDK refactor
├── users/
│   ├── sim-deploy-journey-2026-03-14.md     # 5-persona walkthrough of deployment
│   └── sim-onboarding-flow-2026-03-15.md    # 5-persona walkthrough of onboarding
└── customers/
    ├── sim-ai-validation-2026-03-14.md      # 12-persona evaluation of AI validation feature
    └── sim-pricing-model-2026-03-15.md      # 12-persona evaluation of pricing
```

All artifact filenames use the pattern `sim-{slug}-{date}.md` where `sim` is the topic prefix. The topic prefix ensures all artifacts for a single initiative are discoverable via glob: `review/**/sim-*.md`.

## Technique Heritage

| Skill | Technique | What It Contributes |
|-------|-----------|-------------------|
| design | 05 Expert Review | Named-expert AI reviewers with domain-specific lenses (Aho, Lattner, etc.). Auto-selection from content signals. Independent review + synthesis pattern. |
| design | 06 Discipline Review | 6-discipline standardized rubric. 5-tier resolution chain for discipline matching. Finding format with severity (P1/P2/P3). |
| code | 06 Discipline Review | Same 6 disciplines applied to code rather than design. Per-file annotation pattern. Pass/fail per discipline. |
| users | 04 Persona Walkthrough | 5 persona advocates with distinct journeys. First-person narration. Friction/confusion/fear taxonomy. Per-persona scoring. |
| customers | 07 Customer Persona | 12 personas (C-01 through C-12) with industry context, blind spots, mental models. Quantified scoring with persona-weighted aggregation. Content prediction rates. |

## Cross-Namespace Integration

**Inputs from other namespaces**:
- `/draft:spec` and `/draft:proposal` produce the design artifacts that `/review:design` evaluates
- `/prove:synthesize` produces investigation reports that may need `/review:design` validation
- `/program:plan` sequences `/review:` skills after `/draft:` skills and before implementation

**Outputs to other namespaces**:
- `/review:design` P1 findings feed back to `/draft:` for revision
- `/review:users` friction findings feed into `/listen:feedback` as pre-ship predictions (did the friction we predicted actually manifest?)
- `/review:customers` adoption scores feed into `/prove:hypothesis` as evidence (hypothesis: "customers will adopt feature X" — review scores are the evidence)
- `/review:code` pass/fail gates are used by `/program:plan` as stage gates before deployment

**Self-referential**: `/review:` skills can review each other's outputs. A `/review:design` of the /review: spec itself is the first dogfood test.
