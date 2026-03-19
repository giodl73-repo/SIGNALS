---
skill: validate-customers
topic: ai-code-review
date: 2026-03-18
weighted_score: 3.2
verdict: REVISE
---

# Customer Validation: ai-code-review

---

## PHASE 1 -- SIGNAL ACQUISITION

| Signal file | Skill | Date | Key finding |
|-------------|-------|------|-------------|
| signals/discover/inertia/ai-code-review-inertia-2026-03-18.md | discover-inertia | 2026-03-18 | Ad-hoc paste-to-LLM + human PR review costs ~$70K/year for 5-dev team; inertia MEDIUM; GitHub Copilot Code Review (GA 2025) is the primary competitive forcing function |
| signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md | discover-hypothesis | 2026-03-18 | Hypothesis OPEN at 72% confidence: structured review beats unstructured on defect detection; key tension is coverage quality vs. artifact permanence/audit trail |
| signals/specify/proposal/ai-code-review-proposal-2026-03-18.md | specify-proposal | 2026-03-18 | Primary differentiator is artifact permanence + topic-scoped cross-PR pattern detection vs. Copilot's inline comment model; veto holders are Tech Lead and Security/Compliance |
| signals/validate/design/ai-code-review-design-2026-03-19.md | validate-design | 2026-03-19 | NEEDS-WORK verdict; 3 P1 blockers (auto-selection algorithm, golden test, reproducibility spec) and 20 P2 conditions including secrets-in-artifacts and user-facing output format |

Feature summary: Signal's `/review:code` skill runs structured AI code review against a named topic, producing a permanent artifact in `signals/review/code/` with severity-classified findings (P1/P2/P3), a coverage surface map, and cross-PR pattern history. Primary differentiator over GitHub Copilot Code Review: artifact permanence, topic-scoped history, cross-PR pattern detection. Current state: design review is NEEDS-WORK with unresolved gaps in secrets handling, user-facing output format, and skill identity.

---

## PHASE 2 -- 12-PERSONA EVALUATION

```
[C-01] Maria Chen -- Maker / indie developer
Usefulness:   3  Why: Structural review is useful as a pre-commit sanity check, but the core value prop (compressing human reviewer time) does not apply to solo work.
Clarity:      3  Why: "Topic-scoped" and "artifact permanence" require Signal ecosystem context that an indie dev is unlikely to have on first encounter.
Would adopt:  2  Why: The overhead of Signal onboarding vs. pasting to Claude directly is a real friction barrier with no team-level payoff.
Audience:     secondary
Top concern:  Zero-friction alternative (Copilot or paste-to-Claude) already exists; Signal adds onboarding cost for a benefit that only materializes at team scale.
Delight:      None -- if a "quick mode" existed (single-file, no topic required), she might use it.
```

```
[C-02] James Park -- Enterprise PM
Usefulness:   4  Why: Cross-PR artifact history gives him evidence for post-mortems and feature quality discussions with stakeholders.
Clarity:      4  Why: The $70K/year cost framing and "how did this get through review?" narrative directly match his vocabulary.
Would adopt:  4  Why: If the team is using it, he will require it -- the audit trail answers his hardest post-ship accountability questions.
Audience:     primary
Top concern:  If the artifact format is inconsistent or the AMEND cycle is unpredictable, evidence quality degrades and the artifact loses its stakeholder credibility.
Delight:      Cross-PR pattern detection -- recurring defect classes surfaced automatically is exactly the kind of systemic intelligence he cannot get from individual PR reviews.
```

```
[C-03] Sofia Rodriguez -- UX designer
Usefulness:   2  Why: Code diff analysis is not her workflow; she has no reason to invoke a code review skill.
Clarity:      3  Why: The concept is understandable but entirely outside her domain.
Would adopt:  1  Why: No use case for a UX designer unless the skill is extended to review front-end accessibility or interaction patterns.
Audience:     non-target
Top concern:  "AI review" as a phrase may attract her attention when the feature is announced, creating misaligned expectations about what it actually reviews.
Delight:      None.
```

```
[C-04] Amir Hassan -- DevOps engineer
Usefulness:   4  Why: MERGE-READY/CONDITIONAL/BLOCKED verdict system maps directly to CI gate logic; pre-triage before human review reduces bottleneck.
Clarity:      3  Why: The CI/CD integration path is conceptually clear but the design leaves override mechanism and large-diff handling unspecified.
Would adopt:  3  Why: Will integrate into CI pipeline IF the override mechanism (needed for emergency deploys) and large-diff threshold are defined; without those, he cannot reliably operationalize it.
Audience:     secondary
Top concern:  No verdict override with audit trail means a BLOCKED verdict could halt an emergency hotfix with no sanctioned escape hatch.
Delight:      The structured verdict (not just findings) -- CI gates can consume MERGE-READY/BLOCKED without parsing Markdown.
```

```
[C-05] Priya Patel -- Data scientist
Usefulness:   3  Why: She writes Python data pipelines and would use code review; the audit trail for data code changes is genuinely useful.
Clarity:      3  Why: The Markdown artifact is clear but lacks the machine-readable output she needs to integrate findings into her tooling.
Would adopt:  3  Why: Would adopt if a JSON sidecar shipped; hesitant on Markdown-only output that cannot be queried or aggregated.
Audience:     secondary
Top concern:  No structured output format means she cannot build downstream dashboards or track finding trends over time without parsing Markdown.
Delight:      Cross-PR pattern detection -- recurring data handling anti-patterns (missing null checks, unvalidated DataFrame inputs) surfaced automatically across a project.
```

```
[C-06] Tom Mueller -- Security architect
Usefulness:   4  Why: Structured security review with P1/P2/P3 taxonomy and named threat categories (injection, auth, secrets, input validation) is directly applicable to his workflow.
Clarity:      3  Why: The security reviewer discipline is defined but the unresolved gap -- review artifacts may capture credentials from code under review -- creates a credibility problem before he even evaluates coverage quality.
Would adopt:  2  Why: Cannot recommend a tool that persists diff content to a repository file until secrets-in-artifacts is resolved; one accidental credential capture and the tool is permanently banned from the security team's approved list.
Audience:     primary
Top concern:  Secrets-in-artifacts (design Security #3): if a reviewed diff contains an API key in a test fixture, the review artifact captures and persists it to the repo. This is a P0 security incident waiting to happen.
Delight:      None until secrets handling is resolved. After resolution: the supply-chain threat category (currently missing) would be the highest-value addition for his team.
```

```
[C-07] Lin Wei -- Startup founder
Usefulness:   4  Why: The cost reduction story ($70K/year for 5-dev team) is compelling; faster PR cycles directly affect her shipping velocity.
Clarity:      3  Why: Signal ecosystem onboarding (install, topic registry, reviewer config) vs. Copilot's zero-setup model is a real clarity gap at the decision moment.
Would adopt:  3  Why: Would adopt over Copilot IF a single one-sentence differentiator can be articulated and the onboarding is under 30 minutes; currently neither is clearly defined.
Audience:     primary
Top concern:  Copilot is already in her GitHub subscription. The switching-cost analysis (2-3 days direct + 3-4 weeks habit formation) needs a visible payoff story at week 1, not week 12.
Delight:      The $70K/year quantification -- she can put this in her team retrospective immediately as a "what this replaced" metric.
```

```
[C-08] Diana Brooks -- Enterprise buyer
Usefulness:   4  Why: ROI calculation + audit trail = clear business case; the $70K/year figure and post-mortem accountability story translate directly to a procurement justification.
Clarity:      4  Why: The problem statement and Copilot comparison are articulated; she can explain the purchase decision to finance and legal.
Would adopt:  3  Why: Needs a vendor support SLA, enterprise deployment guide, and legal clearance on artifact liability before signing; the proposal identifies the legal question as open.
Audience:     secondary
Top concern:  The open legal question (can a dated artifact stating "no security issues found" be cited in an audit?) must be resolved before any regulated enterprise deploys this.
Delight:      The artifact audit trail -- enterprise buyers currently have zero documentation of what AI tools checked in a PR; this fills that gap structurally.
```

```
[C-09] Carlos Mendez -- Support engineer
Usefulness:   2  Why: Code review is not his workflow; he evaluates this as a ticket predictor, not a tool he would use.
Clarity:      2  Why: The validate-code vs. review-code skill identity confusion and the undefined AMEND termination condition will generate a predictable support queue.
Would adopt:  2  Why: He won't choose to adopt it; he will be required to support it and he already sees the friction points.
Audience:     non-target
Top concern:  Three known ticket generators before launch: (1) "Which skill do I use -- validate-code or review-code?", (2) "My AMEND loop isn't converging -- what do I do?", (3) "The artifact captured a credential from my test file."
Delight:      None -- his job gets harder if the skill ships with current gaps unresolved.
```

```
[C-10] Yuki Tanaka -- Junior developer
Usefulness:   4  Why: Severity-classified findings (P1/P2/P3) with actionable recommendations are a structured learning tool -- better than freeform LLM feedback.
Clarity:      2  Why: No user-facing output description means she cannot predict what she will receive; validate-code vs. review-code confusion makes the first invocation a guessing game.
Would adopt:  2  Why: High motivation but low confidence in the first-run experience; without a "here is what you will see" preview, junior developers will not retry after a confusing first result.
Audience:     primary
Top concern:  Time-to-first-value is undefined. She needs a "run this, get this" moment within 5 minutes. Current design requires ecosystem onboarding before any output appears.
Delight:      P1/P2/P3 classification with per-finding fix recommendations -- the structured output is far more actionable for a junior developer than the free-form suggestions she gets from ad-hoc LLM paste.
```

```
[C-11] Elena Kovacs -- PM, regulated industry
Usefulness:   5  Why: Dated, topic-scoped, repository-persisted AI review artifacts that cross-reference prior findings are exactly what regulated teams need and cannot get from Copilot's inline comment model.
Clarity:      4  Why: The audit trail value prop is clearly articulated; the legal disclaimer gap is flagged but does not obscure the core proposition.
Would adopt:  3  Why: Adoption blocked in regulated contexts until secrets-in-artifacts (Security #3) and security spec compliance severity (Security #4) are resolved; she cannot allow a tool that might embed credentials in commit history.
Audience:     primary
Top concern:  Secrets-in-artifacts + undefined security severity for spec compliance violations are both blockers for regulated deployment, even though the core value prop is exactly right.
Delight:      Artifact permanence + cross-PR pattern detection -- "This is the exact thing compliance teams have been waiting for: a dated, auditable AI review record that survives the PR and connects findings across the project timeline."
```

```
[C-12] Frank Hoffmann -- Regulator / compliance officer
Usefulness:   3  Why: A dated, topic-scoped review artifact could form part of a compliance evidence package, but only if liability language is resolved.
Clarity:      3  Why: The concept is understandable; the open question of whether "no issues found" artifacts create legal exposure is the central clarity blocker.
Would adopt:  1  Why: He does not adopt software; he evaluates it. He would not recommend these artifacts as admissible evidence without legal review of the disclaimer language.
Audience:     non-target
Top concern:  An artifact stating "no security findings" could be cited defensively by a company during a breach investigation, potentially creating false assurance documentation.
Delight:      None -- pending legal review of artifact disclaimer language.
```

---

## PHASE 3 -- WEIGHTED SCORING

| Persona | Audience | Weight | Usefulness | Clarity | Would-Adopt | Persona avg | Weighted |
|---------|----------|--------|------------|---------|-------------|-------------|----------|
| C-01 Maria Chen | Secondary | 2 | 3 | 3 | 2 | 2.67 | 5.34 |
| C-02 James Park | Primary | 3 | 4 | 4 | 4 | 4.00 | 12.00 |
| C-03 Sofia Rodriguez | Non-target | 1 | 2 | 3 | 1 | 2.00 | 2.00 |
| C-04 Amir Hassan | Secondary | 2 | 4 | 3 | 3 | 3.33 | 6.66 |
| C-05 Priya Patel | Secondary | 2 | 3 | 3 | 3 | 3.00 | 6.00 |
| C-06 Tom Mueller | Primary | 3 | 4 | 3 | 2 | 3.00 | 9.00 |
| C-07 Lin Wei | Primary | 3 | 4 | 3 | 3 | 3.33 | 9.99 |
| C-08 Diana Brooks | Secondary | 2 | 4 | 4 | 3 | 3.67 | 7.34 |
| C-09 Carlos Mendez | Non-target | 1 | 2 | 2 | 2 | 2.00 | 2.00 |
| C-10 Yuki Tanaka | Primary | 3 | 4 | 2 | 2 | 2.67 | 8.01 |
| C-11 Elena Kovacs | Primary | 3 | 5 | 4 | 3 | 4.00 | 12.00 |
| C-12 Frank Hoffmann | Non-target | 1 | 3 | 3 | 1 | 2.33 | 2.33 |

Sum of weighted scores: 82.67
Sum of weights: 26
Weighted aggregate: 3.18 / 5.00
Threshold: 3.5 (ship-ready)
Result: BELOW THRESHOLD

---

## PHASE 4 -- SIGNAL EXTRACTION

**Adoption blockers (primary persona would-adopt < 3):**

- [C-06] Tom Mueller (Security architect) -- Secrets-in-artifacts: the skill persists review output (including diff content) to a repository file; if the reviewed code contains credentials, API keys, or tokens in test fixtures or config files, the artifact captures and commits them. A single incident of this type permanently disqualifies the tool from security-conscious teams.
- [C-10] Yuki Tanaka (Junior developer) -- No user-facing output description + validate-code/review-code skill identity confusion makes the first-run experience unpredictable. Junior developers who cannot predict what they will receive will not retry after one confusing invocation. Time-to-first-value is undefined, which kills adoption at the entry-level audience.

**Positioning leaks (non-target confused about who this is for):**

- [C-03] Sofia Rodriguez (UX designer) -- "AI review" as a launch phrase will attract UX practitioners expecting a user experience or accessibility audit tool. The feature is strictly a code diff analyzer; the positioning does not clarify scope.
- [C-09] Carlos Mendez (Support engineer) -- The validate-code vs. review-code skill identity confusion and undefined AMEND termination are not positioning confusion but will generate predictable support escalations. He reads the feature as a ticket generator in its current state.

**Delight signals (any persona usefulness = 5):**

- [C-11] Elena Kovacs (regulated PM) -- Artifact permanence + cross-PR pattern detection: "This is the exact thing compliance teams have been waiting for: a dated, auditable AI review record that survives the PR and connects findings across the project timeline." The audit trail differentiator is not just preferred -- it is the specific capability that regulated teams cannot get from any current alternative.

**Verdict: REVISE**

Weighted aggregate 3.18 is below the 3.5 ship-ready threshold. Two primary personas (C-06, C-10) score would-adopt < 3. The C-11 delight signal confirms the core value proposition is correct. The revisions are targeted: resolve secrets-in-artifacts and define the first-run experience. The product does not need a redesign -- it needs two specific gaps closed before it can reach the audience it was built for.

---

## PHASE 5 -- AMEND

**1. Resolve the highest-severity adoption blocker: secrets-in-artifacts (C-06 Tom Mueller)**

Add a mandatory pre-write step to the `/review:code` skill specification that scans the accumulated artifact content for credential patterns (API key formats, private key headers, connection strings, bearer token patterns) before writing to disk. Any detected credential pattern causes the artifact to substitute a redaction marker (`[REDACTED: credential pattern detected]`) and appends a `secrets_redacted: true` flag to frontmatter. This step must execute before `fs.writeFile` or equivalent -- a post-write scan is not sufficient because the artifact may already have been committed. Document this behavior explicitly in the "User-Facing Output" section so security teams can verify the mechanism.

Why this amendment unlocks adoption: Tom Mueller (primary, would-adopt 2) and Elena Kovacs (primary, would-adopt 3) are both blocked by this gap. Resolving it converts C-06 from a veto to a conditional approval (would-adopt 3-4) and removes the primary blocker for regulated deployment. The design review already flagged this as Security Architect #3 (P2); this amendment closes it at the customer validation layer with explicit redaction mechanics.

**2. Fix the most common positioning leak: first-run experience and skill identity (C-10 Yuki Tanaka)**

Add a "User-Facing Output" section to the skill specification (the design review's Documentation #1 recommendation) that shows a concrete example of what the user sees: the verdict line first ("MERGE-READY -- 0 P1, 3 P2"), then the P1 summary, then the top finding, then the full block structure. This section should appear before any technical spec content so that a developer invoking the skill for the first time can predict their output before running. Separately, explicitly deprecate `review-code` with a one-line redirect to `validate-code` in the skill catalog and docs/guides/review.md.

Why this amendment unlocks adoption: Yuki Tanaka (primary, would-adopt 2) scores usefulness 4 but clarity 2 -- the problem is not that the feature is unwanted, it is that the first-run experience is undefined. Closing the output-format gap and removing the skill identity confusion converts C-10 from adoption blocker to a likely adopter (would-adopt 3-4).

**3. Amplify the strongest delight signal: audit trail as the lead value proposition (C-11 Elena Kovacs)**

Reorder the feature's primary positioning from "compresses human reviewer time" (the inertia signal's cost framing) to "creates a dated, topic-scoped, repository-persisted AI review record that survives the PR." The $70K/year cost reduction should remain as a secondary supporting point, but the regulated-industry and compliance audience -- the only audience that scores usefulness 5 -- is not motivated by cost alone. They need the artifact permanence story as the headline. Update the problem statement's opening paragraph, the success criteria framing, and any one-pager or announcement copy to lead with: "When a bug ships and the post-mortem question is 'what was checked?' -- Signal answers it with a dated artifact." The cost story is the business case; the audit trail is the adoption hook for the highest-value audience segment.

---

QUALITY: 4
CLAUDE_COMPATIBLE: Y
NOTES: Multi-signal synthesis worked cleanly -- proposal, design review, and inertia artifacts provided sufficient context for all 12 persona evaluations without gaps. One structural note: C-06 (Security architect) appears both as a customer persona here and as a domain expert in the design review; the findings align, which confirms the secrets-in-artifacts blocker is real and not an artifact of persona framing. The weighted aggregate (3.18) is pulled down primarily by two primary personas (C-06: 3.00, C-10: 2.67) -- if both amendment items are resolved, the projected score rises to approximately 3.7-3.8, above the ship-ready threshold.
