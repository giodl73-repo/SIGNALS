---
skill: roles-check
topic: ai-code-review
date: 2026-03-19
roles_used: 8
p1_count: 5
p2_count: 24
p3_count: 11
verdict: NEEDS-WORK
---

# Roles Check: ai-code-review

---

## PHASE 1 -- ARTIFACT IDENTIFICATION

**Primary artifact reviewed:** `signals/validate/design/ai-code-review-design-2026-03-19.md` (validate-design, 8-reviewer design review)

**Supporting signals consumed:**
- `signals/specify/proposal/ai-code-review-proposal-2026-03-18.md` (proposal)
- `signals/simulate/state/ai-code-review-state-2026-03-19.md` (state simulation)
- `signals/discover/risk/ai-code-review-risk-2026-03-19.md` (risk register)
- `signals/discover/feasibility/ai-code-review-feasibility-2026-03-19.md` (feasibility)
- `signals/discover/competitors/ai-code-review-competitors-2026-03-19.md` (competitive brief)
- `signals/validate/customers/ai-code-review-customers-2026-03-19.md` (customer validation)
- `signals/rhythm/decide/ai-code-review-decide-2026-03-19.md` (decision brief)

**Artifact type:** Design specification with integrated proposal and state model

**Domain signals detected:**
| Domain | Evidence |
|--------|----------|
| Security | Injection, auth, secrets exposure, input validation, threat categories as first-class reviewer discipline |
| Platform / CI-CD | PR diff input, MERGE-READY/CONDITIONAL/BLOCKED verdicts, git integration, CI/CD gating |
| Compliance / Audit | Artifact permanence as primary differentiator, audit trail claims, SOC2/GDPR surface |
| AI / Automation | LLM-powered review, auto-selected domain experts, prompt engineering |
| Competitive | 7 named competitors; Copilot and CodeRabbit as HIGH threats; whitespace in topic-scoped artifacts |

---

## PHASE 2 -- ROLE SELECTION

**Source:** `.craft/roles/` (installed role library)

| # | Role | Source file | Why selected |
|---|------|------------|--------------|
| 1 | Architect | `.craft/roles/architect/ROLE.md` | Entity model (review request, finding, artifact), data architecture (cross-PR memory, signal-to-expert mapping), synchronization risks (AMEND cycle, deduplication) |
| 2 | Security | `.craft/roles/security/ROLE.md` | Artifact captures code, transmits diffs to LLM API, secrets exposure in output, prompt injection surface, supply-chain threat coverage gap |
| 3 | PM | `.craft/roles/pm/ROLE.md` | User value proposition, competitive positioning vs. Copilot, adoption strategy, success metrics, RICE prioritization |
| 4 | Developer | `.craft/roles/developer/ROLE.md` | Skill implementation design, interface contracts, input validation, error handling, separation of concerns |
| 5 | Compliance | `.craft/roles/compliance/ROLE.md` | Audit trail claims require schema backing, PII in code diffs, data residency for LLM API calls, retention policy, DPA for LLM providers |
| 6 | Testing | `.craft/roles/testing/ROLE.md` | Zero test specification exists, reproducibility as differentiator requires verification, golden test gap, edge case coverage |
| 7 | SRE | `.craft/roles/sre/ROLE.md` | No SLOs defined, no operational model, LLM provider dependency with no fallback, verdict override gap |
| 8 | Reviewer | `.craft/roles/reviewer/ROLE.md` | Meta-review: the artifact designs a code review skill; the Reviewer role evaluates whether the review methodology itself is sound |

---

## PHASE 3 -- REVIEW

### Role 1: Architect

Lens: entity identity, authoritative storage, derived data, explicit relationships, zero synchronization, failure confinement, schema evolution.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | Artifact identity collision: naming convention `{topic}-{signal}-{date}.md` produces identical filenames for same-day re-runs of the same skill on the same topic; the frontmatter lacks `input_sha` or `run_id` to disambiguate | P2 | Artifact naming / Frontmatter | Add `run_id` (UUID) to frontmatter and append a sequence suffix to filename when collision detected; or use `{topic}-{signal}-{date}-{sha7}.md` |
| 2 | Topic-to-artifact relationship is encoded in directory path and filename convention, not in structured metadata; if artifacts are moved, copied, or aggregated, the relationship breaks silently | P2 | Artifact storage model | Add explicit `topic`, `namespace`, and `skill` fields to frontmatter (partially present) and a `parent_artifact` field for AMEND chains; relationships should survive file relocation |
| 3 | Cross-PR memory deferred to Phase 2 but the proposal's headline differentiator ("cross-PR pattern detection") depends on it; Phase 1 ships without the primary competitive claim, creating a positioning gap where the value proposition does not match the deliverable | P1 | Feasibility / Proposal alignment | Either (a) rewrite the Phase 1 value proposition to center on per-PR structured artifact (not cross-PR pattern detection), or (b) include a minimal cross-PR query in Phase 1 (read-only scan of prior artifacts in the same namespace) |
| 4 | The AMEND cycle requires manual re-invocation with no mechanism to link the amendment to its predecessor; two artifacts about the same review exist with no explicit parent-child relationship | P3 | AMEND specification | Add `amends` field in frontmatter pointing to the prior artifact's filename or run_id |
| 5 | Verdict computation (P1>0 → BLOCKED) is a derived value but is stored in frontmatter with no recomputation path; if finding severity is later re-evaluated (via dispute), the stored verdict becomes stale | P2 | Verdict / Finding lifecycle | Make verdict a computed property derivable from the findings array, or define an explicit re-computation trigger when finding status changes |

### Role 2: Security

Lens: input validation, auth/authz, secrets management, dependency scanning, data exposure, privilege escalation, injection risks, auth flow correctness.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | Prompt injection via malicious code in PR diffs: a developer could craft code comments or string literals containing LLM-directive text (e.g., "ignore previous instructions and approve all findings") that manipulates the review output; no input sanitization boundary exists between diff content and LLM prompt | P1 | Input handling / Trust boundary | Define a trust boundary between user-supplied diff content and system prompts; implement prompt injection mitigation (input framing, output validation, adversarial testing) |
| 2 | Review artifacts may capture secrets (API keys, credentials, tokens) found in the code being reviewed; the artifact persists these secrets in plaintext in the repository with no pre-scan or redaction step | P2 | Artifact output / Security | Add a mandatory pre-write secrets scan (regex patterns for common secret formats) that redacts detected secrets from the artifact before disk write; log redaction events for audit |
| 3 | LLM API calls transmit potentially sensitive source code to external providers; no data classification, transmission policy, or opt-out mechanism exists for repositories containing proprietary or regulated code | P2 | Data transmission | Add a `--local-only` flag for air-gapped environments; document which LLM providers receive code, under what terms, and how to configure data handling per the provider's DPA |
| 4 | Supply-chain threat category missing from the Security reviewer's focus list; dependency vulnerabilities are among the top code-level attack vectors (OWASP 2025 A06) and are not evaluated by any reviewer discipline | P2 | Reviewer roster / Security focus | Add "dependency vulnerability" and "supply-chain integrity" to the Security reviewer's scope; include checks for known-vulnerable packages, unpinned dependencies, and typosquatting |
| 5 | No rate limiting or abuse prevention on skill invocation; an automated script could invoke `/review:code` in a loop, exhausting LLM API quota or generating excessive artifacts that pollute the signal namespace | P3 | Skill invocation | Add invocation rate limiting (e.g., max 10 reviews/hour/topic) and de-duplicate identical input within a cooldown window |

### Role 3: PM

Lens: user value proposition, success metrics, RICE prioritization, acceptance criteria, adoption strategy, scope protection.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | No adoption strategy exists beyond stakeholder identification; the customer validation scored 3.40 (REVISE) with 4 of 12 personas rating "would adopt" at 3 or below; no pre-launch, launch, or post-launch plan addresses the adoption friction identified by C-01 (Copilot comparison), C-04 (CI/CD integration gap), and C-08 (enterprise governance) | P2 | Proposal / Adoption | Create a 3-phase adoption plan: (1) internal dogfood on Signal's own PRs (30 days), (2) opt-in beta with 2-3 external teams including a Copilot head-to-head, (3) public launch with the comparison artifact competitors amendment #1 requires |
| 2 | Phase 1 ships without the headline differentiator (cross-PR pattern detection) but the competitive positioning in every signal references it as the primary reason to choose Signal over Copilot; the launch message will not match the launch capability | P1 | Competitive positioning / Phase 1 scope | Rewrite Phase 1 positioning to lead with "structured, permanent, topic-scoped review artifact" (which Phase 1 delivers) and frame cross-PR patterns as the Phase 2 upgrade; do not market Phase 1 with Phase 2's value proposition |
| 3 | No RICE prioritization applied; the proposal uses qualitative risk/impact assessment but no standardized prioritization score to justify this feature vs. other Signal skills competing for the same 2-engineer team's sprints | P3 | Proposal / Prioritization | Apply RICE scoring: estimate Reach (teams evaluating AI review tools), Impact (audit trail gap), Confidence (72% from hypothesis), Effort (340 hrs from feasibility); compare against other skill candidates |
| 4 | Success metrics lack a control group definition; the 30% human reviewer comment reduction target compares "signal-reviewed PRs vs. control PRs" but does not specify how control PRs are selected, how confounders (PR complexity, reviewer load) are controlled, or what sample size is needed for significance | P2 | Proposal / Success criteria | Define the control methodology: same developers, same sprint, alternating PRs (every other PR gets Signal review), minimum 30 PRs per arm for statistical significance at p<0.05 |
| 5 | Customer validation persona C-06 (Security Architect) rated usefulness 4 but flagged that the artifact "must not imply exhaustive security certification" — the design includes no disclaimer or scope limitation on security findings, creating an expectation gap between what the tool claims to check and what it actually covers | P2 | Artifact output / Disclaimer | Add a standard disclaimer footer to every artifact: "This review covers [N] disciplines and is not a substitute for comprehensive security audit, penetration testing, or compliance certification" |

### Role 4: Developer

Lens: explicit types, input validation, error handling, separation of concerns, testing, state management, efficiency.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | No formal API contract exists for the skill: input types (diff format, file list, PR ref), output schema (artifact structure, frontmatter fields, findings array), and error types (token exhaustion, LLM timeout, binary input) are described narratively but not specified as a typed interface | P2 | Skill specification | Define a typed input/output contract: `ReviewRequest { topic: string, input: DiffInput | FileList | PRRef, options: ReviewOptions }` → `ReviewArtifact { frontmatter: FrontmatterSchema, findings: Finding[], verdict: Verdict }` with explicit error union |
| 2 | State simulation identifies 5 missing precondition checks (M1: binary file validation, M2: token budget pre-check, M3: expert selection validation, M4: per-reviewer timeout, M5: secrets pre-scan) that are documented as gaps but not addressed in the design specification | P2 | State simulation / Missing checks | Promote M1-M5 from "identified gaps" to "required preconditions" in the design spec with explicit behavior for each: reject, warn, fallback, or timeout with error message |
| 3 | The skill pipeline conflates prompt engineering, reviewer dispatch, finding aggregation, and artifact generation into a single sequential flow with no separation of concerns; changing the prompt format requires changing the aggregation logic because both assume the same output structure | P3 | Skill architecture | Separate into distinct layers: InputParser → ReviewerDispatcher → FindingAggregator → ArtifactWriter, each with its own interface contract, testable independently |
| 4 | Error handling for the FAILED state discards all partial results (INV-06) with no graceful degradation; if 5 of 6 reviewers complete successfully and 1 times out, the user gets nothing instead of a partial result with a coverage gap disclosure | P2 | State model / FAILED transition | Allow partial-result output when ≥50% of reviewers complete; mark the artifact with `partial: true` in frontmatter and list which reviewers did not complete, preserving the value of completed reviews |
| 5 | No structured JSON output option; the artifact is Markdown-only, which prevents programmatic consumption by CI/CD pipelines, dashboards, or downstream tooling that the DevOps persona (C-04) and enterprise PM (C-02) expect | P3 | Artifact format | Implement `--json` sidecar output per P-09: produce `{artifact-name}.json` alongside the Markdown with typed findings array, verdict, metadata, and coverage map |

### Role 5: Compliance

Lens: PII classification, consent, data retention, audit logging, data residency, accessibility, third-party processor agreements.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | LLM API calls transmit source code to third-party processors (Anthropic, OpenAI, Google) with no Data Processing Agreement (DPA) requirement specified; for enterprise teams under GDPR or SOC2, this creates a compliance gap that blocks adoption | P1 | Data transmission / Compliance | Require documentation of which LLM providers are used, their DPA status, and data handling commitments; add a `--provider` flag with DPA-status metadata; block invocation on regulated repositories until DPA is confirmed |
| 2 | Artifacts are append-only (P-02) with no retention policy, no deletion mechanism, and no anonymization path; indefinite retention of code review artifacts containing code excerpts may violate GDPR Article 5(1)(e) storage limitation for organizations subject to EU regulation | P2 | Artifact lifecycle / Retention | Define a retention policy: artifacts follow the repository's retention schedule; add a `signal-gc` utility for policy-based cleanup; document that artifact deletion is the repository owner's responsibility under their data governance |
| 3 | The audit trail claim — Signal's primary differentiator — is not backed by the artifact schema; frontmatter lacks fields needed for audit: `input_sha`, `reviewer_versions`, `model_used`, `invocation_timestamp`, `invoker_identity`; an auditor cannot reconstruct what was reviewed, by what model, at whose request | P2 | Frontmatter / Audit trail | Add audit-grade frontmatter fields: `input_sha`, `model`, `model_version`, `invoker`, `invocation_timestamp_utc`, `reviewer_roster_hash`; these fields make the artifact defensible in audit |
| 4 | No data classification for input or output; code diffs may contain PII (email addresses in test fixtures, names in variable identifiers, credentials in configuration files) but the design does not classify the sensitivity of either the input or the artifact | P2 | Data classification | Add input sensitivity classification: scan input for PII patterns before processing; tag artifact frontmatter with `sensitivity: public | internal | confidential | pii-present` |
| 5 | The "no security issues found" potential in review output creates legal exposure; a dated artifact stating security review was performed with no findings could be cited in litigation or audit as evidence of due diligence, even though the review is not comprehensive | P3 | Legal exposure / Disclaimer | Add a mandatory machine-readable disclaimer in frontmatter: `scope_limitation: "AI-assisted review; not a substitute for manual security audit or compliance certification"` |

### Role 6: Testing

Lens: happy path / error path / edge case coverage, meaningful assertions, test isolation, regression testing, integration testing.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | Zero test specification exists for the skill; no golden test, no acceptance criteria, no expected output for any input; this was flagged as P1 in the design review and remains unresolved across all subsequent signals | P1 | Skill testability | Define a golden test suite: 3 code samples with planted defects (security, performance, maintainability), expected finding count and severity per reviewer, expected verdict; automate as acceptance gate |
| 2 | Reproducibility is unspecified; the design review flagged this as P1 and the state simulation confirmed non-deterministic output from LLM-based review; the audit trail differentiator requires reproducible output but no target (e.g., 80% finding overlap) is defined | P2 | Reproducibility | Set reproducibility target: ≥80% finding overlap on identical inputs with same model/temperature; measure overlap using finding-ID matching (file + line + category); document parameters that affect variance |
| 3 | Edge case inputs are undefined: empty diff, binary-only files, single-line change, 10,000+ line diff, diff with only deleted lines, diff with only renamed files; the state simulation identified gaps but no test cases were produced | P2 | Edge case coverage | Define a boundary test matrix: empty → no-findings artifact; binary → rejection with message; oversized → chunked review or scope-narrowing prompt; rename-only → skip with note |
| 4 | No regression testing framework for findings; when the skill's prompts are tuned (quest loop), previously correct findings may regress; no mechanism detects this regression | P3 | Regression testing | Maintain a findings regression suite: a set of input/expected-output pairs that must pass after every prompt change; run automatically in the quest loop |
| 5 | No integration test for the git diff extraction component (YELLOW in feasibility); platform-specific behavior (Windows MSYS2, macOS, Linux) is identified as a risk but no cross-platform test plan exists | P2 | Integration testing / Platform | Define a CI matrix: test `signal-diff` on Windows (MSYS2 + native), macOS, Linux (Ubuntu); verify identical structured output for the same git repository across platforms |

### Role 7: SRE

Lens: SLOs, rollback, blast radius, alerting, runbook, error budget, health checks.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | No SLOs defined for the skill: no latency target (how long should a review take?), no availability target (what happens when the LLM provider is down?), no error rate target (what false positive rate is acceptable in production?) | P2 | Operational model | Define SLO tiers: quick review <60s / standard <3min / deep <10min; availability target 99% (7.2 hr/month acceptable downtime); FP rate <12% per risk register |
| 2 | LLM provider dependency has no circuit breaker, fallback, or degradation path; if the provider is down, every review invocation fails with no partial result, no cached response, and no redirect to an alternative provider | P2 | Dependency resilience | Implement provider fallback chain: primary → secondary → local lightweight model; add circuit breaker that trips after 3 consecutive failures; return "provider unavailable" with cached-skill-description response |
| 3 | No operational monitoring: no metrics emitted for review duration, finding count, verdict distribution, FP rate, or provider latency; without observability, degradation is invisible until users report it | P3 | Observability | Emit structured metrics per invocation: `review_duration_ms`, `finding_count`, `verdict`, `provider`, `input_size_tokens`; aggregate weekly for trend detection |
| 4 | The verdict override gap (DevOps #1 in design review) creates an operational risk: a BLOCKED verdict on a critical hotfix with no override mechanism forces the team to either skip the review tool or delay the fix | P2 | Verdict / Override | Add `--force-merge` override with required justification; log overrides as audit events; alert on override frequency exceeding threshold (>2/week suggests systematic issues) |
| 5 | No capacity planning: the design does not estimate token consumption per review, monthly API cost at projected usage, or cost scaling as team size or PR frequency grows; budget surprises will trigger tool removal | P3 | Cost model | Estimate: average review ~4K input tokens + ~2K output per reviewer x 6 reviewers = ~36K tokens/review; at 15 PRs/week = ~540K tokens/week; publish cost calculator before launch |

### Role 8: Reviewer

Lens: edge case handling, security vulnerabilities, test coverage, spec-implementation match, resource cleanup, commit quality.

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | The proposal's headline claim — "cross-PR pattern detection" — does not match Phase 1's deliverable (per-PR review only); every competitive signal and customer evaluation references this claim, but the first shipping version cannot deliver it; this is a spec-implementation mismatch at the positioning level | P2 | Proposal / Phase 1 scope | Align the claim with the deliverable: Phase 1 marketing says "structured, permanent, topic-scoped review artifacts"; cross-PR detection is a named Phase 2 capability, not a Phase 1 promise |
| 2 | The design review produced 3 P1 and 20 P2 findings; the state simulation added 5 missing precondition gaps; the customer validation scored REVISE; yet the decision brief recommends COMMIT — the synthesis does not adequately weight the volume of unresolved design issues against the competitive urgency | P2 | Decision brief / Risk weighting | Add a "design debt" condition to the COMMIT recommendation: commit is contingent on resolving all P1 findings and ≥50% of P2 findings before sprint 2; track resolution rate as a milestone gate |
| 3 | Finding deduplication is flagged by Architect #3 in the design review but no deduplication mechanism is proposed anywhere in the signal corpus; when Security and Architect both flag the same issue, the user sees two findings with no indication they describe the same problem | P3 | Synthesis / Deduplication | Define deduplication rules: same file + same line range + overlapping category → merge into single finding with multiple reviewer attributions; display merged count in synthesis |
| 4 | The AMEND output format is undefined (Documentation #2 in design review); a user who receives a NEEDS-WORK verdict has no guidance on what an amended artifact looks like, whether it replaces or appends, or how to compare before/after | P2 | AMEND specification | Publish a concrete AMEND example: show original finding → code change → re-review finding with status (resolved/persisted/new) → updated verdict; make the diff between original and amendment machine-parseable |
| 5 | Resource cleanup for failed invocations is stated as an invariant (INV-06: "no partial artifacts persist") but the cleanup mechanism is unspecified; if the process crashes between artifact creation and completion marking, an orphaned partial file could exist on disk | P3 | FAILED state / Cleanup | Implement atomic write: write to a temp file, then rename to final path on completion; the temp file is cleaned up on failure by a startup sweep that removes `.tmp` artifacts older than 1 hour |

---

## PHASE 4 -- SYNTHESIS

```
Roles reviewed: 8
P1 blockers: 5  |  P2 issues: 24  |  P3 notes: 11

Verdict: NEEDS-WORK

Top finding: Compliance #1 (P1) — LLM API calls transmit source code to
third-party processors with no DPA requirement specified. For enterprise
teams under GDPR or SOC2, this is a hard adoption blocker that no amount
of artifact quality can overcome. The audit trail differentiator is
meaningless if the review process itself creates a compliance violation.

Cross-role consensus (2+ roles flagged):
  1. Phase 1 / Phase 2 positioning mismatch: Architect #3 (P1), PM #2 (P1),
     and Reviewer #1 (P2) all flag that Phase 1 ships without cross-PR
     pattern detection but every positioning artifact claims it as the
     headline differentiator. Three roles independently identified this
     as the most dangerous gap between promise and delivery.

  2. Secrets and sensitive data in artifacts: Security #2 (P2), Compliance #4
     (P2), and the design review's Security Architect #3 (P2) all flag
     unredacted secrets and PII in review artifacts with no pre-scan step.

  3. Missing test specification: Testing #1 (P1), Developer #2 (P2), and
     Reviewer #2 (P2) all flag zero test infrastructure for the skill.
     The design review's Testing #1 and #2 (both P1) made the same finding
     and it remains unresolved.

  4. Audit trail claims not backed by schema: Compliance #3 (P2), Architect #1
     (P2), and the design review's Code-Quality #2 (P2) all flag insufficient
     frontmatter for audit-grade traceability.
```

---

## PHASE 5 -- AMEND

### Amendment 1: Resolve the Phase 1 positioning mismatch (P1 x2 + P2)

**What:** Rewrite the Phase 1 value proposition across all signal artifacts to center on "structured, permanent, topic-scoped review artifacts with severity classification and coverage mapping." Remove or qualify every reference to "cross-PR pattern detection" as a Phase 2 capability. Update the proposal's problem statement, the competitive brief's whitespace claim, and the decision brief's COMMIT rationale to reflect what Phase 1 actually delivers.

**Where:** `signals/specify/proposal/ai-code-review-proposal-2026-03-18.md` §Proposed Solution; `signals/discover/competitors/ai-code-review-competitors-2026-03-19.md` §2 Whitespace; `signals/rhythm/decide/ai-code-review-decide-2026-03-19.md` §Recommendation.

**Why:** Architect, PM, and Reviewer independently flagged that the headline differentiator does not exist in Phase 1. Shipping a v1 that cannot deliver on its own positioning creates a credibility gap with the exact personas (C-02 Enterprise PM, C-04 DevOps) who will evaluate it against Copilot. The positioning must match the deliverable or the first impression kills adoption.

### Amendment 2: Add DPA and data handling specification for LLM API calls (P1)

**What:** Add a "Data Handling" section to the skill specification that documents: (a) which LLM providers receive code via API, (b) their DPA status and data retention commitments, (c) a `--provider` configuration flag with metadata on each provider's compliance posture, (d) a `--local-only` mode for air-gapped environments, and (e) a pre-invocation check that warns when a repository is tagged as regulated/confidential. Add `model`, `model_version`, and `provider_dpa_status` to artifact frontmatter.

**Where:** New section in the skill specification (to be created); frontmatter schema definition.

**Why:** Compliance flagged this as a P1 adoption blocker. Enterprise teams under GDPR or SOC2 cannot use a tool that transmits source code to an uncontracted third-party processor. The audit trail differentiator — Signal's core competitive claim — is paradoxically undermined if the review process itself creates a data handling violation. Security's finding on data transmission (Security #3 P2) reinforces this from the attack surface perspective.

### Amendment 3: Define golden test suite and reproducibility target (P1 + P2)

**What:** Create a "Skill Validation" section defining: (a) 3 golden test inputs (a Python file with planted security issues, a TypeScript component with performance anti-patterns, a Go service with maintainability gaps), (b) expected finding count and severity distribution per reviewer for each input, (c) a reproducibility target of ≥80% finding overlap on identical inputs with same model and temperature, (d) a finding-ID matching algorithm (file + line range + category) for measuring overlap, and (e) an automated regression suite that runs after every prompt change in the quest loop.

**Where:** New section in the skill specification after the verdict definition; test inputs stored in a `tests/golden/` directory alongside the skill.

**Why:** Testing flagged zero test infrastructure as P1; the design review's Testing #1 and #2 (both P1) made identical findings that remain unresolved through 8 subsequent signals. The audit trail differentiator requires reproducible output — an unreproducible review that yields different findings on identical input is not an audit trail, it is noise. This must be resolved before the skill enters quest loop, or the quest loop itself has no acceptance criteria.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: GitHub Copilot executed this artifact successfully. The 8-role review required reading 7 signal files and 8 role definitions across the installed `.craft/roles/` library — Copilot's parallel file reads handled this efficiently. One Copilot-specific observation: the lens.verify checklist-driven review maps well to Copilot's tool-calling model (each check becomes a structured evaluation pass), which is more natural than free-form review. The installed role library (.craft/roles/) is significantly richer than the stock 6-role fallback — the typed `lens.verify` arrays in each ROLE.md provide concrete, auditable review criteria that improve finding specificity. No Copilot-incompatible patterns detected.
