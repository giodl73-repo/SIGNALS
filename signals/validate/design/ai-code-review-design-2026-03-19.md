---
skill: validate-design
topic: ai-code-review
date: 2026-03-19
reviewer_count: 8
p1_count: 3
p2_count: 20
p3_count: 9
domain_roles_active:
  - Security Architect
  - DevOps Engineer
---

# Design Review: ai-code-review

**Design documents reviewed:**
- `signals/validate-code.md` — full skill specification (216 lines)
- `simulations/draft/specs/signal-review-2026-03-14.md` §review:code — detailed spec
- `signals/review-code.md` — skill description (7 lines)
- `docs/guides/review.md` — review namespace guide (125 lines)
- `signals/discover/inertia/ai-code-review-inertia-2026-03-18.md` — market context

---

## BLOCK 0 -- CONTENT SIGNAL CATALOGUE

| Signal phrase | Domain category |
|---------------|-----------------|
| Injection, auth, secrets exposure, input validation, unsafe deserialization | security |
| auto-selected domain experts from language/framework context | AI/automation |
| PR diff, diff range, MERGE-READY/CONDITIONAL/BLOCKED verdicts | platform (VCS/CI) |
| Spec compliance checks as cross-cutting reviewer lens | compliance |

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
| Injection, auth, secrets exposure, input validation, unsafe deserialization | Security Architect | The design hard-codes security review patterns and threat categories as a first-class reviewer discipline; a security architect must evaluate whether the threat model is complete and the attack surface coverage is adequate. |
| PR diff, diff range, MERGE-READY/CONDITIONAL/BLOCKED verdicts | DevOps Engineer | The design produces merge-gate verdicts and accepts PR diffs as input; a DevOps/platform engineer must evaluate whether the CI/CD integration points and workflow assumptions are correctly specified. |
| auto-selected domain experts from language/framework context | No expert needed | Auto-selection of reviewers is a design decision within the Architect discipline's purview and does not require a dedicated AI/ML specialist for this review scope. |
| Spec compliance checks as cross-cutting reviewer lens | No expert needed | Spec compliance is a cross-cutting methodology lens adequately covered by the Testing and Process stock disciplines without requiring a dedicated compliance specialist. |

BLOCK 1 domain count = 2

---

## BLOCK 1.5 -- ROSTER COMMITMENT TABLE

| Reviewer | Role | Source |
|----------|------|--------|
| Security Architect | Domain expert | Domain |
| DevOps Engineer | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate:
1. Domain row count = 2. BLOCK 1 domain count = 2. ✓ F-09 passes.
2. "Security Architect" matches BLOCK 1 Expert added. "DevOps Engineer" matches BLOCK 1 Expert added. ✓ F-10 passes.

Total reviewers: 8

---

## BLOCK 2 -- PER-REVIEWER FINDINGS

### Security Architect (Domain expert / Domain)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The Security reviewer focus lists 5 threat categories (injection, auth, secrets, input validation, unsafe deserialization) but omits supply-chain threats (dependency vulnerabilities, malicious packages) — among the top code-level attack vectors in 2025-2026 ecosystems | P2 | BLOCK 1 — REVIEWER ROSTER / Security focus | Add "dependency vulnerability scanning" and "supply-chain integrity" to the Security reviewer's focus description |
| 2 | All findings share the same P1/P2/P3 severity scale regardless of domain — a secrets-exposure P2 has fundamentally different risk characteristics than a naming-clarity P2, but the design provides no way to distinguish them in triage | P2 | BLOCK 3 — Severity definitions | Add a risk-weight modifier for security findings, or define security-specific severity criteria that account for blast radius and exploitability |
| 3 | No guidance on handling sensitive content encountered during review (credentials in config, API keys in test fixtures) — the design assumes reviewers analyze code but does not address what happens when the review artifact itself captures secrets | P2 | BLOCK 2 — PER-REVIEWER FINDINGS / Security | Add a pre-scan step that detects and redacts secrets from review output before the artifact is persisted to the repository |
| 4 | The Spec compliance check does not specify whether security requirements in the spec are treated as hard P1 constraints or soft P2 suggestions — a spec stating "all inputs must be validated" should produce P1 findings when violated | P2 | BLOCK 3 — Spec compliance summary | Specify that security-related spec compliance violations default to P1 severity unless the spec explicitly marks them as advisory |

### DevOps Engineer (Domain expert / Domain)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The verdict system (MERGE-READY / CONDITIONAL / BLOCKED) has no override or exception mechanism — in practice, CI/CD gates need an escape hatch for emergency deployments or known-acceptable risk | P2 | BLOCK 3 — Verdict | Add an override mechanism with a required justification field and audit trail that records who overrode, when, and why |
| 2 | The design accepts "PR diff" as input but does not specify how large diffs are handled — a 500-file PR will produce an unwieldy artifact that is harder to act on than the PR itself | P2 | Input type / Files | Define a file-count or token-budget threshold that triggers chunked review or requires explicit scope narrowing before proceeding |
| 3 | The AMEND mode re-runs "affected disciplines on changed files only" but does not specify how the system determines which files changed — this requires integration with the VCS diff mechanism that is never described | P3 | AMEND | Specify the change-detection mechanism: git diff against the prior review's commit SHA, with the SHA stored in artifact frontmatter for traceability |
| 4 | No guidance on how review artifacts integrate with existing PR platforms (GitHub PR comments, Azure DevOps work items) — the artifact is standalone Markdown but teams expect review feedback inline in their PR tool | P3 | Artifact output | Add a section on output format extensibility: Markdown as canonical, with optional structured JSON sidecar for tool integration per P-09 |

### Architect (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The domain expert auto-selection uses a signal table (Language, Framework, Auth pattern, Data persistence, Public API) but the selection algorithm is underspecified — which signal combinations trigger which expert, what happens when signals conflict, and how confidence is determined are all undefined | P1 | BLOCK 0 — DOMAIN SIGNAL SCAN | Define an explicit signal-to-expert mapping with precedence rules, confidence thresholds, and conflict-resolution behavior |
| 2 | The reviewer disciplines are hard-coded (Security, Performance, Maintainability, Testing, Documentation, Architecture) with no extension point — organizations needing Accessibility, Internationalization, or domain-specific disciplines cannot customize the stock set | P2 | BLOCK 1 — REVIEWER ROSTER | Allow the stock discipline list to be configurable via simulate.yaml while preserving the current 6 as defaults |
| 3 | No dependency or interaction model between reviewers — if Security and Architecture both notice the same pattern, both produce separate findings with no deduplication in the synthesis | P2 | BLOCK 3 — Cross-cutting patterns | Add an explicit deduplication step that merges same-file, same-line findings from different reviewers into a single finding with multiple reviewer attributions |
| 4 | The per-reviewer finding tables use different column structures across the review namespace: validate-code uses (ID, File:Line, Finding, Severity, Fix) while validate-design uses (Finding, Sev, Section, Recommendation) — this inconsistency creates cognitive load for users who use both skills | P3 | BLOCK 2 — PER-REVIEWER FINDINGS | Standardize finding table columns across all review skills in the namespace, or document the rationale for structural divergence |

### Code-Quality (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | Severity semantics differ between validate-code ("P1 = blocks merge") and validate-design ("P1 = blocks delivery") — same labels with different meanings across skills in the same namespace will confuse users and tools that consume findings | P2 | BLOCK 2 / Severity definitions | Unify severity semantics across the review namespace, or use distinct label sets to make the difference visible (e.g., M1/M2/M3 for merge-blocking) |
| 2 | The frontmatter schema (skill, topic, date, reviewer_count, p1-p3 counts) omits what was reviewed — two reviews of different code on the same topic on the same day produce indistinguishable frontmatter | P2 | Frontmatter specification | Add `input_path`, `input_sha`, and `signal_name` to frontmatter to uniquely identify the review subject |
| 3 | The skill specification is 216 lines with no table of contents, no section numbering, and no anchor points — navigating to a specific block requires scanning the full document | P3 | General structure | Add a TOC with anchor links and consistent block numbering |
| 4 | The "Patterns identified" field after each reviewer section is free-text with one example but no format constraint — two runs of the same skill will produce incomparable pattern descriptions | P3 | BLOCK 2 — Patterns identified | Define a structured pattern format: "[pattern name] — [count] of [total] [unit] — [implication]" |

### Documentation (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The design specifies internal block structure but never describes what the user actually sees — there is no user-facing output format, no summary section, and no guidance on how to read the artifact | P2 | General | Add a "User-facing output" section describing the summary a user reads first: verdict, P1 count, top finding, then full block structure |
| 2 | The AMEND section says "re-run affected disciplines on changed files only" but provides no example of what an AMEND artifact looks like — does it produce a diff, a full re-review, or an amendment appended to the original? | P2 | AMEND | Add a concrete AMEND output example showing resolved findings, new findings, and updated verdict |
| 3 | The relationship between validate-code and review-code is confusing — the skill catalog lists both with nearly identical descriptions and the user has no guidance on which to invoke | P2 | Skill identity | If validate-code supersedes review-code, deprecate review-code explicitly with a redirect. If they coexist, document the distinction with a comparison table. |
| 4 | The spec examples (in signal-review-2026-03-14.md) reference Dataverse, TypeScript, and compiler domains — users reviewing Python, Go, or Rust codebases will find every example irrelevant to their context | P3 | Examples | Add at least one domain-neutral example (e.g., a Python web API review) alongside the existing platform-specific examples |

### Testing (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | No specification for how to validate that the skill produces correct results — there is no golden test, no acceptance criteria, and no expected-output definition for the skill itself | P1 | General / Skill testability | Define a golden input/output pair: a known code sample with planted issues and the expected finding set, usable as the acceptance test per P-11 |
| 2 | No inter-run reproducibility specification — running the same review twice on identical input may produce different findings, severities, and verdicts, undermining the audit-trail value proposition identified in the inertia analysis | P1 | General / Determinism | Define a reproducibility target (e.g., 80% finding overlap on identical inputs) and document the parameters that affect output variance |
| 3 | The design does not specify behavior when input is empty, contains only comments, or is a binary file — these edge cases will occur in real PR diffs | P2 | Input type / BLOCK 0 | Add input validation rules: reject binary files with a clear message, handle empty/comment-only files with "no findings" and an explanatory note |
| 4 | The cross-cutting pattern analysis requires cross-file reasoning but the design specifies no maximum file count or token budget — at scale, pattern analysis will either silently truncate or produce shallow results | P2 | BLOCK 3 / Cross-cutting patterns | Define the scaling model: full analysis up to N files, sampled analysis with coverage disclosure beyond N |

### Process (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The design provides no workflow for disagreement resolution — when a developer disputes a P1 finding, the only option is AMEND (re-run the reviewer), with no appeal, escalation, or rationale-capture mechanism | P2 | AMEND / Dispute resolution | Add a dispute mechanism: developer marks a finding as "disputed" with rationale, triggering a re-review with the dispute context included |
| 2 | No positioning guidance for when to use validate-code vs. human review vs. both — the inertia analysis warns that "parallel reviews create comment duplication" but the skill design does not address this transition risk | P2 | General / Adoption | Add a "When to use" section positioning this skill: pre-triage (before human review), replacement (low-risk changes), or complement (high-risk changes alongside human review) |
| 3 | No time or cost estimates — teams planning sprint work cannot predict how long a validate-code run takes or what token budget it consumes | P3 | General / Lifecycle | Add estimated duration ranges (quick: 1-2 min, standard: 3-5 min, deep: 8-15 min) and approximate token budgets |
| 4 | The AMEND cycle has no termination condition — "iterate until all disciplines pass" could loop indefinitely if a finding cannot be resolved at the code level | P3 | AMEND | Add a maximum iteration count (e.g., 3) with guidance: if findings persist, escalate to human review or accept with documented rationale |

### Implementation (Stock discipline / Stock)

| # | Finding | Sev | Section | Recommendation |
|---|---------|-----|---------|----------------|
| 1 | The design says "Group findings by file" in the synthesis but per-reviewer tables are organized by reviewer — this requires a transformation from reviewer-grouped to file-grouped findings that is never specified | P2 | BLOCK 3 — Cross-cutting patterns | Specify the grouping algorithm: collect all findings, sort by file path, then by severity within file, preserving reviewer attribution |
| 2 | The auto-detection heuristics for domain expert selection are undefined — a TypeScript file importing React vs. Vue should select different framework experts, but the detection logic (file extension, import analysis, pattern matching) is not specified | P2 | BLOCK 0 — DOMAIN SIGNAL SCAN | Define detection heuristics: file extension → language, import/require statements → framework, API pattern matching → domain signals |
| 3 | The verdict mapping (P1=0 → MERGE-READY, P1=0 + P2>0 → CONDITIONAL, P1>0 → BLOCKED) does not account for P2 accumulation — 20 P2 findings arguably represents a worse state than 1 P1 finding, but the design calls both "not blocked" | P2 | BLOCK 3 — Verdict | Add a P2 accumulation threshold (e.g., P2 count > 10 escalates to BLOCKED) or a weighted severity score that prevents P2 floods from being dismissed |
| 4 | The design produces Markdown artifacts but the frontmatter lacks structured data for programmatic consumption — no findings array, no machine-readable verdict, no field for downstream tooling | P3 | Frontmatter / Artifact format | Support `--json` output per PRINCIPLES.md P-09: produce a structured JSON sidecar with findings array, verdict, and metadata suitable for CI/CD and dashboard consumption |

---

## BLOCK 3 -- SYNTHESIS

```
Overall verdict: NEEDS-WORK

P1 blockers (must resolve before implementation):
  - Architect #1 — Auto-selection algorithm for domain experts is underspecified; implementation cannot proceed without defined signal-to-expert mappings
  - Testing #1 — No golden test or acceptance criteria exist for the skill; cannot verify correctness
  - Testing #2 — No reproducibility specification; undermines the audit-trail value proposition that differentiates Signal from ad-hoc LLM review

P2 conditions (must resolve before sign-off):
  - Security Architect #1 — Missing supply-chain threat coverage
  - Security Architect #2 — No risk-weight distinction for security findings
  - Security Architect #3 — Secrets in review artifacts unaddressed
  - Security Architect #4 — Security spec compliance severity undefined
  - DevOps Engineer #1 — No verdict override mechanism
  - DevOps Engineer #2 — Large-diff handling unspecified
  - Architect #2 — Hard-coded disciplines with no extension point
  - Architect #3 — No finding deduplication across reviewers
  - Code-Quality #1 — Severity semantics inconsistent across namespace
  - Code-Quality #2 — Frontmatter insufficient for unique identification
  - Documentation #1 — No user-facing output summary
  - Documentation #2 — AMEND output format undefined
  - Documentation #3 — validate-code vs review-code relationship unclear
  - Testing #3 — Edge case input handling missing
  - Testing #4 — Scaling model for pattern analysis undefined
  - Process #1 — No dispute/escalation mechanism
  - Process #2 — No positioning vs human review
  - Implementation #1 — File-grouped synthesis unspecified
  - Implementation #2 — Auto-detection heuristics undefined
  - Implementation #3 — P2 accumulation not reflected in verdict

Cross-reviewer consensus:
  Architect #1 and Implementation #2 both flag the underspecified auto-selection
  algorithm as a design gap that blocks implementation. Documentation #1 and
  Code-Quality #2 both identify insufficient output metadata as a usability
  problem. Testing #2 and Process #2 both flag the gap between the inertia
  analysis's value proposition (artifact permanence, audit trail) and the
  design's actual specification of those properties.

Strongest signal:
  Testing #2 (reproducibility). The inertia analysis identifies "audit trail"
  and "cross-PR pattern detection" as the key differentiators over ad-hoc LLM
  review and Copilot. An unreproducible review that yields different findings
  on identical input undermines this differentiator at the foundation. Without
  a reproducibility target, the skill cannot credibly claim to produce an
  auditable record.
```

---

## AMEND

1. **Add a reproducibility and testing specification** — Insert a new section "Skill Validation" after BLOCK 3 in `signals/validate-code.md`. Define a golden test pair (known code sample with planted defects + expected finding set), a reproducibility target (≥80% finding overlap on identical inputs across runs), and the parameters that affect variance (model, temperature, reviewer order). Why: Testing #1 and #2 are both P1 blockers. The inertia analysis positions artifact permanence as the core differentiator — that claim requires a testable, reproducible output.

2. **Specify the auto-selection algorithm** — Expand BLOCK 0 in `signals/validate-code.md` with an explicit signal-to-expert mapping table, detection heuristics (file extension → language, import analysis → framework, pattern matching → security/data/API domains), precedence rules when signals conflict, and a confidence threshold below which auto-selection is skipped. Why: Architect #1 (P1) and Implementation #2 (P2) both flag this as underspecified. Without defined mappings, every implementation will invent its own heuristics, producing inconsistent reviewer rosters.

3. **Add user-facing output format and AMEND example** — Insert a "User-Facing Output" section before BLOCK 0 in `signals/validate-code.md` that describes the summary users see first (verdict line, P1 count, top finding, then full block output). Expand the AMEND section with a concrete before/after example showing which findings were resolved, which are new, and how the verdict changed. Why: Documentation #1 and #2 (both P2) flag that users cannot predict what they will receive or how iteration works.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: GitHub Copilot produced this artifact successfully. The multi-block gating protocol (F-01 through F-21) executed without conformance failures. One Copilot-specific observation: the BLOCK 0 pre-scan requires reading multiple files before any table is populated — in Copilot's tool-calling model this maps naturally to parallel file reads, which is an efficiency advantage over sequential approaches. No Copilot-incompatible patterns detected.
