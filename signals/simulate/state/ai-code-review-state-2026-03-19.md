---
skill: simulate-state
topic: ai-code-review
date: 2026-03-19
---

# State Simulation: ai-code-review

Hand-compiled state transitions for the `/review:code` skill applied to the `ai-code-review` topic. Each entity's lifecycle is traced from initial state through all operations, with preconditions, postconditions, and invariants at every step. Stock domain experts (Sales, Customer Service, Finance) evaluate transitions from their perspective.

**Source signals consumed:**
- `signals/specify/proposal/ai-code-review-proposal-2026-03-18.md`
- `signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md`
- `signals/discover/inertia/ai-code-review-inertia-2026-03-18.md`
- `signals/validate/design/ai-code-review-design-2026-03-19.md`
- `signals/validate/customers/ai-code-review-customers-2026-03-19.md`

---

## ENTITY 1: REVIEW REQUEST

The review request is the primary lifecycle object. A developer invokes `/review:code topic:ai-code-review` and the system progresses through a deterministic pipeline.

### State Diagram

```
IDLE --> PENDING --> SCANNING --> REVIEWING --> SYNTHESIZING --> COMPLETE
                        |             |              |
                        v             v              v
                     FAILED        FAILED         FAILED
```

### Transition Table

| # | From | Operation | To | Preconditions | State Changes | Postconditions | Invariants |
|---|------|-----------|-----|---------------|---------------|----------------|------------|
| T1 | IDLE | Developer invokes `/review:code topic:ai-code-review` with input (diff, files, or PR ref) | PENDING | (a) Topic name is non-empty; (b) Input is provided and non-empty; (c) Input is not a binary file | Request object created with: request_id, topic, input_ref, timestamp, status=PENDING | Request exists in system; no artifact created yet; no findings exist | INV-01: Exactly one request per invocation; no shared mutable state between concurrent requests |
| T2 | PENDING | System runs DOMAIN SIGNAL SCAN on input files | SCANNING | (a) Request status == PENDING; (b) Input files are readable; (c) Token budget has not been exhausted | Signal table populated: language, framework, auth patterns, data persistence, public API flags detected; domain experts selected | Signal table is non-empty; expert roster is finalized (stock 6 + domain experts); roster is immutable for remainder of this request | INV-02: Expert roster, once committed, cannot change during a single review run |
| T3 | SCANNING | System dispatches input to each reviewer discipline in parallel | REVIEWING | (a) Request status == SCANNING; (b) Expert roster is committed and non-empty; (c) Input size is within token budget per reviewer | Per-reviewer finding tables are being populated; each reviewer operates independently on the same input snapshot | At least one reviewer has produced findings or an explicit "no findings" result | INV-03: All reviewers operate on the same input snapshot; input is immutable during review |
| T4 | REVIEWING | All reviewers complete; system aggregates findings | SYNTHESIZING | (a) Request status == REVIEWING; (b) Every reviewer in the committed roster has returned a result (findings or "no findings"); (c) No reviewer has timed out without a result | Findings merged into a single table; cross-cutting patterns identified; file-grouped view generated; verdict computed from severity counts | Synthesis section exists; verdict is one of {MERGE-READY, CONDITIONAL, BLOCKED}; finding count per severity (P1, P2, P3) is finalized | INV-04: Verdict is deterministic given the same severity counts -- P1>0 always produces BLOCKED |
| T5 | SYNTHESIZING | System writes artifact to `signals/review/code/{topic}-{signal}-{date}.md` | COMPLETE | (a) Request status == SYNTHESIZING; (b) Synthesis is finalized; (c) Artifact path does not collide with an existing file (or signal name differentiates) | Artifact written to disk with frontmatter (skill, topic, date, reviewer_count, severity counts, verdict); request status set to COMPLETE | Artifact file exists on disk; artifact is immutable (P-02); frontmatter is parseable YAML | INV-05: Artifact, once written, is never modified by the system; only AMEND produces new files |
| T6 | PENDING / SCANNING / REVIEWING / SYNTHESIZING | Unrecoverable error (token exhaustion, file read failure, LLM timeout) | FAILED | Error condition detected at any active stage | Request status set to FAILED; partial results discarded; no artifact written | No artifact exists for a FAILED request; system returns error message to developer | INV-06: A FAILED request never produces an artifact; no partial artifacts persist |

### Invalid State Transitions

| # | From | Attempted Operation | Why Invalid | Risk If Allowed |
|---|------|---------------------|-------------|-----------------|
| X1 | COMPLETE | Re-run review on same input | COMPLETE is a terminal state; re-running produces a new request (P-02 append-only), not a state change on the existing request | Violates P-02; overwrites the audit trail that is the primary differentiator vs. Copilot |
| X2 | SCANNING | Developer adds additional files to input | Input is frozen at PENDING -> SCANNING transition (INV-03); mid-scan input mutation invalidates signal detection results | Domain experts selected based on original input would be wrong for the expanded input; findings would be inconsistent |
| X3 | REVIEWING | Remove a reviewer from the roster | Roster is committed at SCANNING -> REVIEWING transition (INV-02); removing a reviewer mid-run produces incomplete coverage | Coverage map claims "6 disciplines checked" but only 5 ran; audit trail is false |
| X4 | FAILED | Resume from failure point | No checkpoint mechanism exists; partial reviewer results are discarded at failure | Resuming with stale partial results could mix findings from two different input states if the code changed between failure and resume |
| X5 | IDLE | Invoke without input (no diff, no files) | Precondition (b) of T1 violated; the system has nothing to review | Produces an artifact with zero findings and a MERGE-READY verdict, which is misleading -- the user may interpret "no findings" as "code is clean" rather than "nothing was reviewed" |

### Missing Precondition Checks (Design Gaps)

| # | Transition | Missing Check | Impact |
|---|------------|---------------|--------|
| M1 | T1 (IDLE -> PENDING) | No validation that input is not exclusively binary files | Binary file input produces garbage findings or silent failure; design review DevOps #3 flagged this |
| M2 | T2 (PENDING -> SCANNING) | No token budget pre-check before dispatching to scan | Large diffs (500+ files) exhaust the token budget during scanning, failing at T3 instead of T2; user waits for scan completion only to get a late failure |
| M3 | T3 (SCANNING -> REVIEWING) | No check that the auto-selected domain experts are valid for the detected signals | Architect #1 flagged: signal-to-expert mapping is underspecified; conflicting signals could select contradictory experts |
| M4 | T4 (REVIEWING -> SYNTHESIZING) | No timeout enforcement per reviewer | A single slow reviewer blocks synthesis for all other completed reviewers; no partial-result fallback |
| M5 | T5 (SYNTHESIZING -> COMPLETE) | No secrets scan on artifact content before writing to disk | Security Architect #3 flagged: review artifact may capture secrets found in code; artifact persists secrets in plaintext in the repository |

---

## ENTITY 2: REVIEW FINDING

Individual findings are the atomic unit of review output. Each finding has its own lifecycle within the request.

### State Diagram

```
                               +--> ACCEPTED (developer agrees)
                               |
DETECTED --> TRIAGED --> DISPUTED --> RE-EVALUATED --> ACCEPTED / WAIVED
                    |                                     
                    +--> ACCEPTED (no dispute)            
```

### Transition Table

| # | From | Operation | To | Preconditions | State Changes | Postconditions | Invariants |
|---|------|-----------|-----|---------------|---------------|----------------|------------|
| F1 | (none) | Reviewer identifies an issue at a file:line location | DETECTED | (a) Reviewer is in the committed roster; (b) File:line is within the input scope; (c) Finding is not a duplicate of an already-detected finding from the same reviewer | Finding record created: id, reviewer, file, line, description, raw_severity | Finding exists with a raw severity assigned by the reviewer | INV-07: Every finding has exactly one originating reviewer; attribution is immutable |
| F2 | DETECTED | System applies severity mapping (P1/P2/P3) based on reviewer assessment and domain rules | TRIAGED | (a) Finding status == DETECTED; (b) Severity mapping rules are defined for this finding type | Severity finalized to P1, P2, or P3; finding is included in the synthesis aggregation | Finding has a final severity; finding contributes to verdict calculation | INV-08: Severity, once triaged, does not change within the same review run |
| F3 | TRIAGED | Developer marks finding as "disputed" with rationale | DISPUTED | (a) Finding status == TRIAGED; (b) Developer provides a non-empty rationale; (c) Review is in COMPLETE state (disputes happen post-artifact) | Finding flagged as disputed; rationale recorded; original severity preserved alongside dispute | Disputed finding is visible in the artifact; original severity still contributes to verdict of the original run | INV-09: Disputes do not retroactively change the verdict of the completed review; they feed into the AMEND cycle |
| F4 | DISPUTED | AMEND cycle re-evaluates the disputed finding with dispute context | RE-EVALUATED | (a) Finding status == DISPUTED; (b) AMEND cycle is active; (c) Disputed rationale is included in re-review context | Finding re-assessed: severity may change, finding may be withdrawn, or finding may be confirmed | Re-evaluated finding has a resolution: ACCEPTED (confirmed), WAIVED (withdrawn with rationale), or DOWNGRADED (severity reduced) | INV-10: Re-evaluation rationale is recorded; the chain of (original finding -> dispute -> re-evaluation) is traceable |
| F5 | TRIAGED | Developer accepts finding (no dispute) | ACCEPTED | (a) Finding status == TRIAGED; (b) Developer has reviewed the finding | Finding marked as accepted; no further state changes | Accepted finding remains in the artifact record permanently | INV-07 holds: attribution unchanged |

### Invalid State Transitions

| # | From | Attempted Operation | Why Invalid |
|---|------|---------------------|-------------|
| XF1 | ACCEPTED | Re-open as DISPUTED | Once accepted, the finding is part of the historical record; re-opening it violates P-02 append-only -- create a new finding or amend |
| XF2 | DETECTED | Developer disputes before triage | Severity is not yet assigned; disputing an un-triaged finding has no target severity to contest |
| XF3 | WAIVED | Escalate to P1 | A waived finding was explicitly withdrawn; escalating it requires a new finding in a new review run, not a resurrection of the old one |

### Missing Precondition Checks

| # | Transition | Missing Check | Impact |
|---|------------|---------------|--------|
| MF1 | F1 (DETECTED) | No deduplication across reviewers | Architect #3 flagged: Security and Architecture may both flag the same file:line issue; two findings on the same code with no merge step inflates finding counts and misleads the verdict |
| MF2 | F2 (TRIAGED) | No risk-weight modifier for security findings | Security Architect #2 flagged: a security P2 (secrets exposure) has fundamentally different blast radius than a naming-clarity P2; same label, different risk |
| MF3 | F3 (DISPUTED) | No mechanism exists in current design | Process #1 flagged: the design has no dispute workflow; findings are take-it-or-leave-it |

---

## ENTITY 3: REVIEW VERDICT

The verdict is a derived state computed from the aggregated findings. It serves as a merge gate.

### State Diagram

```
UNDETERMINED --> MERGE-READY    (P1 == 0, P2 <= threshold)
             |-> CONDITIONAL    (P1 == 0, P2 > 0 but <= threshold)
             |-> BLOCKED        (P1 > 0 OR P2 > accumulation threshold)
```

### Transition Table

| # | From | Operation | To | Preconditions | State Changes | Postconditions | Invariants |
|---|------|-----------|-----|---------------|---------------|----------------|------------|
| V1 | UNDETERMINED | Synthesis completes with P1 == 0 and P2 == 0 | MERGE-READY | (a) All reviewers reported; (b) Severity counts finalized | Verdict = MERGE-READY; artifact frontmatter records verdict | Artifact is actionable: developer can proceed to merge | INV-11: MERGE-READY requires P1 == 0; no exception |
| V2 | UNDETERMINED | Synthesis completes with P1 == 0 and 0 < P2 <= 10 | CONDITIONAL | (a) All reviewers reported; (b) P2 threshold defined (currently implicit) | Verdict = CONDITIONAL; artifact lists P2 findings as conditions | Developer may merge after addressing P2 conditions or accepting them with rationale | INV-11 holds |
| V3 | UNDETERMINED | Synthesis completes with P1 > 0 | BLOCKED | (a) All reviewers reported; (b) At least one P1 finding exists | Verdict = BLOCKED; artifact lists P1 blockers | Developer must resolve P1 findings before merging; AMEND cycle is the resolution path | INV-12: BLOCKED cannot transition to MERGE-READY without a new review run (AMEND or fresh) |
| V4 | UNDETERMINED | Synthesis completes with P1 == 0 and P2 > accumulation threshold | BLOCKED | (a) All reviewers reported; (b) P2 accumulation threshold exceeded | Verdict = BLOCKED due to P2 flood | Same as V3; P2 accumulation is treated as a blocking condition | INV-13: P2 accumulation threshold must be defined and documented |

### Invalid State Transitions

| # | From | Attempted Operation | Why Invalid |
|---|------|---------------------|-------------|
| XV1 | BLOCKED | Developer overrides to MERGE-READY without AMEND | No override mechanism exists (DevOps #1 flagged); the verdict is immutable on the artifact |
| XV2 | MERGE-READY | Finding added post-synthesis | Findings are frozen at synthesis; new findings require a new review run |
| XV3 | CONDITIONAL | Auto-promote to MERGE-READY after timeout | No time-based state change exists; conditions must be explicitly resolved |

### Missing Precondition Checks

| # | Transition | Missing Check | Impact |
|---|------------|---------------|--------|
| MV1 | V2 (CONDITIONAL) | No P2 accumulation threshold defined | Implementation #3 flagged: 20 P2 findings all individually "non-blocking" but collectively indicating a deeply flawed change; current design allows CONDITIONAL with any number of P2s |
| MV2 | V1-V4 (all) | No check that coverage is sufficient before computing verdict | A review that only examined 3 of 50 changed files and found no P1s produces MERGE-READY, but coverage was 6%; the verdict is technically correct but practically misleading |
| MV3 | V3 (BLOCKED) | No override/exception mechanism | DevOps #1 flagged: emergency deployments and known-acceptable risks have no escape hatch; the only path is AMEND, which requires a full re-review cycle |

---

## ENTITY 4: AMEND CYCLE

The AMEND cycle is the re-review lifecycle triggered when a developer makes changes to address findings.

### State Diagram

```
NOT_STARTED --> CHANGE_DETECTED --> SCOPE_DETERMINED --> RE-REVIEWING --> AMENDED
                                                              |
                                                              v
                                                           FAILED
```

### Transition Table

| # | From | Operation | To | Preconditions | State Changes | Postconditions | Invariants |
|---|------|-----------|-----|---------------|---------------|----------------|------------|
| A1 | NOT_STARTED | Developer invokes AMEND on a COMPLETE review, providing changed files | CHANGE_DETECTED | (a) A prior COMPLETE review artifact exists for this topic; (b) Changed files are a subset of the original review scope; (c) Prior artifact's commit SHA is available for diff computation | Changed file set identified; prior artifact referenced by path and date | System knows which files changed and which reviewers originally flagged those files | INV-14: AMEND always references a specific prior artifact; it is not a standalone review |
| A2 | CHANGE_DETECTED | System determines which reviewer disciplines are affected by the changes | SCOPE_DETERMINED | (a) Change set is non-empty; (b) Original reviewer-to-file mappings are recoverable from the prior artifact | Affected disciplines identified; unaffected disciplines are skipped | Scope is a strict subset of the original reviewer roster; at least one discipline is in scope | INV-15: AMEND never expands scope beyond the original review; new files require a fresh review |
| A3 | SCOPE_DETERMINED | Affected disciplines re-review changed files with prior findings as context | RE-REVIEWING | (a) Scope is determined; (b) Prior findings for affected disciplines are available as context; (c) Changed files are readable at current state | Re-review produces: resolved findings (prior finding no longer applies), new findings (new issues in changed code), persistent findings (prior finding still applies) | Every prior finding for affected disciplines has a resolution status: RESOLVED, PERSISTENT, or SUPERSEDED | INV-16: Prior findings are not deleted; they are marked with a resolution status in the AMEND artifact |
| A4 | RE-REVIEWING | System writes AMEND artifact with updated verdict | AMENDED | (a) All affected disciplines have completed re-review; (b) New synthesis computed from: (original unaffected findings) + (AMEND findings) | New artifact written: `{topic}-{signal}-amend-{date}.md`; new verdict computed from combined finding set | AMEND artifact exists alongside (not replacing) the original; cross-reference links both artifacts | INV-05 holds: original artifact is untouched |

### Invalid State Transitions

| # | From | Attempted Operation | Why Invalid |
|---|------|---------------------|-------------|
| XA1 | NOT_STARTED | AMEND invoked without a prior COMPLETE review | No reference artifact exists; AMEND requires a baseline to diff against |
| XA2 | RE-REVIEWING | Developer changes code again during re-review | Input is frozen at CHANGE_DETECTED (INV-03 applies); mid-AMEND input mutation invalidates re-review context |
| XA3 | AMENDED | AMEND the AMEND (recursive) beyond iteration limit | Process #4 flagged: no termination condition; could loop indefinitely |

### Missing Precondition Checks

| # | Transition | Missing Check | Impact |
|---|------------|---------------|--------|
| MA1 | A1 (CHANGE_DETECTED) | No mechanism to retrieve prior artifact's commit SHA | DevOps #3 flagged: AMEND change detection requires git diff against a baseline, but the baseline SHA is not stored in artifact frontmatter |
| MA2 | A2 (SCOPE_DETERMINED) | No mapping from file changes to reviewer disciplines | The original artifact records findings per reviewer, but which reviewer "owns" which file is not explicit; scope determination is guesswork |
| MA3 | A3 (RE-REVIEWING) | No iteration counter or maximum | Process #4 flagged: AMEND cycles can repeat without bound; no escalation trigger after N iterations |

---

## ENTITY 5: CONCURRENT REVIEW (RACE CONDITIONS)

Per P-01 (Concurrent by Default), multiple developers may run `/review:code` on the same topic simultaneously. This entity models the interaction.

### Scenario Table

| # | Scenario | Actors | Race Condition | Invariant at Risk | Mitigation |
|---|----------|--------|----------------|-------------------|------------|
| R1 | Two developers review different PRs on the same topic simultaneously | Dev A runs `/review:code topic:ai-code-review` on PR #42; Dev B runs `/review:code topic:ai-code-review` on PR #43 | **No race**: per P-01, each produces a separate dated artifact with a different signal name; file naming includes enough uniqueness to prevent collision | INV-01 (one request per invocation) | P-07 naming contract: `ai-code-review-pr42-2026-03-19.md` and `ai-code-review-pr43-2026-03-19.md` are distinct files |
| R2 | Same developer reviews the same PR twice on the same day | Dev A runs `/review:code` on PR #42 at 9am and again at 3pm after code changes | **Potential collision**: both runs produce `ai-code-review-{signal}-2026-03-19.md`; if the signal name is identical, the second run attempts to write a file that already exists | INV-05 (artifact immutability) | Signal name must encode enough distinctness (e.g., include commit SHA prefix or run counter); current naming convention does not guarantee uniqueness for same-day same-signal runs |
| R3 | Developer runs AMEND while another developer starts a fresh review on the same PR | Dev A AMENDs the 9am review; Dev B starts a fresh review on the same PR with new commits | **Logical race**: AMEND operates on the original snapshot; fresh review operates on the current snapshot; both produce artifacts that may contradict each other on the same topic | INV-14 (AMEND references prior artifact) | Both artifacts are valid within their scope; synthesis requires human judgment to reconcile. The system should warn when an AMEND references a stale baseline. |
| R4 | Review running while developer pushes new commits to the PR branch | Dev A invokes review; while REVIEWING phase is active, Dev B pushes commits to the same branch | **Input drift**: INV-03 (input immutability during review) is only enforced if the system snapshots input at PENDING; if it reads files from the live branch, input may change mid-review | INV-03 (input snapshot) | System must snapshot the input (diff content or file content) at PENDING -> SCANNING transition and operate on the snapshot, not the live branch |
| R5 | Two developers dispute different findings on the same review artifact concurrently | Dev A disputes finding #3; Dev B disputes finding #7 on the same artifact | **Write contention on artifact**: if disputes are written to the original artifact, concurrent writes corrupt the file | INV-05 (artifact immutability); P-02 (append-only) | Disputes must produce separate records (e.g., a dispute sidecar file or a new AMEND artifact), not modify the original review artifact |

---

## STOCK ROLE DOMAIN EXPERT EVALUATION

### Sales Domain Expert

**Perspective:** How do these state transitions affect the ability to sell, demonstrate, and position `ai-code-review` against competitors (primarily GitHub Copilot Code Review)?

| # | State Area | Finding | Severity | Recommendation |
|---|------------|---------|----------|----------------|
| S1 | Verdict states (V1-V4) | The BLOCKED verdict has no override mechanism. In a sales demo, a prospect will ask: "What happens in an emergency? Can we override?" The answer is currently "no," which is a deal-breaker for enterprise buyers who need exception handling in any gating tool. | HIGH | Add an override-with-audit mechanism. Sales cannot demo a merge gate without an escape hatch. Every competing CI/CD gate tool (SonarQube, Snyk, etc.) has one. |
| S2 | Concurrent review (R1) | The naming convention produces unique artifacts per PR, which is a positive demo story: "Show your auditor that every PR was independently reviewed." This is Signal's primary differentiator vs. Copilot's ephemeral inline comments. | POSITIVE | Emphasize artifact permanence in sales materials. The state model inherently supports the audit trail narrative. |
| S3 | AMEND cycle (A1-A4) | The AMEND cycle requires a prior COMPLETE review. Prospects will ask: "What if I just want to re-run the review?" The current model forces a distinction between "fresh review" and "AMEND" that is confusing to explain in a 30-minute demo. | MED | Simplify the user-facing model: "re-run" always produces a new artifact; "amend" is an advanced mode for finding-resolution tracking. Don't force the distinction on first contact. |
| S4 | Finding lifecycle (F1-F5) | No dispute mechanism exists. Enterprise buyers will ask: "Can developers push back on false positives?" The answer is currently "no structured way," which signals an immature tool. | HIGH | Dispute workflow is table-stakes for enterprise sales. Implement it before the first enterprise demo. |

### Customer Service Domain Expert

**Perspective:** What support cases will these state transitions generate? Where will users get stuck, confused, or frustrated?

| # | State Area | Finding | Severity | Recommendation |
|---|------------|---------|----------|----------------|
| CS1 | T6 (FAILED state) | FAILED discards all partial results. A user who waited 5 minutes for a large review and hits a timeout on the last reviewer loses everything. Support ticket: "I ran the review, it said 'failed,' and now I have nothing." Expected volume: HIGH for users with large PRs. | HIGH | Implement partial-result preservation: if 5 of 6 reviewers completed, write a partial artifact marked as INCOMPLETE with the available findings, and note which reviewer failed. |
| CS2 | X5 (invoke without input) | If a user invokes `/review:code` without providing a diff or file path, the missing precondition check means the system either crashes or produces a vacuous MERGE-READY artifact. Support ticket: "I ran the review and it says everything is fine but I didn't give it any code." | HIGH | Validate input at T1 with a clear error message: "No input provided. Please specify a diff, file path, or PR reference." |
| CS3 | R2 (same-day collision) | If a user runs the same review twice on the same day with the same signal name, the second run may fail silently or overwrite the first. Support ticket: "I ran the review twice and my first results disappeared." | MED | Generate a unique artifact filename that includes a run counter or timestamp suffix. Warn the user if a same-signal artifact already exists for today. |
| CS4 | MV2 (low-coverage verdict) | A review that examined 3 of 50 files and found no P1s produces MERGE-READY. User merges, bug ships from file #47 that was never reviewed. Post-mortem: "Signal said it was MERGE-READY." Support ticket becomes a trust-destroying event. | CRITICAL | Include coverage percentage in the verdict. A MERGE-READY with <50% coverage must be flagged as LOW-CONFIDENCE or downgraded to CONDITIONAL. |
| CS5 | A3 (AMEND without iteration limit) | User enters an AMEND loop: fix code, AMEND, new findings, fix code, AMEND, new findings. After 5 cycles the user is frustrated and files a ticket: "The review keeps finding new things no matter what I fix." | MED | Cap AMEND iterations at 3. After 3, produce a summary of persistent findings and recommend human review escalation. |

### Finance Domain Expert

**Perspective:** What are the cost implications of each state transition? Where does resource consumption spike? Where are hidden costs?

| # | State Area | Finding | Severity | Recommendation |
|---|------------|---------|----------|----------------|
| FN1 | T3 (REVIEWING - parallel dispatch) | Each reviewer discipline consumes a separate LLM call. 6 stock disciplines + 2 domain experts = 8 parallel LLM calls per review. At ~$0.03-0.10 per call (depending on model and token count), a single review costs $0.24-$0.80. At 15 PRs/week (5 devs x 3 PRs), weekly cost is $3.60-$12.00; annual cost is ~$190-$625. | LOW | Cost is well within budget for the $70K/year human review labor it partially replaces. Document the per-review cost estimate so teams can budget. |
| FN2 | T6 (FAILED - wasted spend) | A FAILED review at the SYNTHESIZING stage means 8 LLM calls were paid for but produced no usable artifact. If failure rate is 10% (large diffs, timeouts), annual waste is ~$19-$63. Small in absolute terms, but user-perceived cost is "I paid for nothing." | LOW | Log failed reviews with cost attribution. Even small waste erodes trust if invisible. |
| FN3 | AMEND cycle (A3) | Each AMEND cycle re-runs affected disciplines. If 4 of 6 disciplines are affected, that is 4 LLM calls per AMEND. An unbounded AMEND loop (MA3) at 4 calls per iteration could consume 5x the cost of the original review before the user gives up. | MED | Enforce iteration cap (3 AMENDs). Display cumulative cost after each AMEND: "This review has consumed $X across N iterations." |
| FN4 | M2 (large diff, no pre-check) | A 500-file PR dispatched to 8 reviewers may hit token limits and produce 8 FAILED calls. The user pays for 8 full-context LLM calls that all fail. Estimated worst-case: $2-$6 per failed mega-review. | MED | Pre-check token budget at PENDING -> SCANNING. Reject or chunk oversized inputs before dispatching to reviewers. Surface estimated cost before proceeding: "This review will cost approximately $X. Proceed?" |
| FN5 | R1 (concurrent reviews) | Two developers reviewing different PRs independently is correct behavior but doubles the cost. No cost-sharing mechanism for overlapping file reviews across PRs. | LOW | Not a bug -- this is the expected cost model. Document it: "Each review is independent; reviewing the same file in two different PRs costs two reviews." |

---

## INVARIANT REGISTRY

All invariants identified across entities, consolidated for verification.

| ID | Invariant | Entity | Verified By |
|----|-----------|--------|-------------|
| INV-01 | Exactly one request per invocation; no shared mutable state | Review Request | T1 preconditions; P-01 concurrent-by-default |
| INV-02 | Expert roster is immutable once committed for a review run | Review Request | T2 postconditions; X3 invalid transition |
| INV-03 | All reviewers operate on the same input snapshot; input is immutable during review | Review Request | T3 preconditions; R4 race condition |
| INV-04 | Verdict is deterministic given the same severity counts | Verdict | V1-V4 transition rules |
| INV-05 | Artifact, once written, is never modified by the system | Review Request / AMEND | T5 postconditions; P-02 append-only |
| INV-06 | A FAILED request never produces an artifact | Review Request | T6 postconditions |
| INV-07 | Every finding has exactly one originating reviewer; attribution is immutable | Finding | F1 postconditions |
| INV-08 | Severity, once triaged, does not change within the same review run | Finding | F2 postconditions |
| INV-09 | Disputes do not retroactively change the verdict of the completed review | Finding | F3 postconditions |
| INV-10 | Re-evaluation rationale is recorded; full chain is traceable | Finding | F4 postconditions |
| INV-11 | MERGE-READY requires P1 == 0; no exception | Verdict | V1 preconditions |
| INV-12 | BLOCKED cannot transition to MERGE-READY without a new review run | Verdict | XV1 invalid transition |
| INV-13 | P2 accumulation threshold must be defined and documented | Verdict | V4; MV1 missing check |
| INV-14 | AMEND always references a specific prior artifact | AMEND Cycle | A1 preconditions |
| INV-15 | AMEND never expands scope beyond the original review | AMEND Cycle | A2 postconditions |
| INV-16 | Prior findings are not deleted; they are marked with resolution status | AMEND Cycle | A3 postconditions |

---

## CRITICAL FINDINGS SUMMARY

Ranked by blast radius (highest first):

| Rank | Finding | Source | Blast Radius | Design Gap |
|------|---------|--------|--------------|------------|
| 1 | Low-coverage MERGE-READY verdict (MV2, CS4) | Verdict Entity / Customer Service | A user merges confidently based on MERGE-READY; bug ships from unreviewed file; post-mortem destroys trust in the tool and the audit trail narrative | No coverage threshold in verdict computation; coverage percentage is not surfaced |
| 2 | FAILED request discards all partial results (T6, CS1) | Review Request / Customer Service | User loses 5 minutes of compute and all findings when one reviewer times out; repeated failures on large PRs will drive abandonment | No partial-result preservation; no graceful degradation |
| 3 | No dispute mechanism (MF3, S4) | Finding Entity / Sales | Enterprise buyers reject tools without false-positive handling; developers with no pushback path either ignore findings or stop using the tool | Design omits the dispute lifecycle entirely |
| 4 | No verdict override (XV1, MV3, S1) | Verdict Entity / Sales | Emergency deployments are blocked with no escape hatch; teams will route around the tool rather than be blocked by it | No override-with-audit mechanism |
| 5 | Secrets persisted in review artifacts (M5) | Review Request | Review artifact captures a hardcoded API key found in code; artifact is committed to repo; secret is now in two places instead of one | No pre-write secrets scan on artifact content |
| 6 | P2 accumulation not reflected in verdict (MV1) | Verdict Entity | 20 P2 findings produce CONDITIONAL instead of BLOCKED; developer treats each P2 as individually ignorable; collectively they represent a deeply flawed change | No P2 accumulation threshold defined |
| 7 | Same-day artifact collision (R2, CS3) | Concurrent Review | Second review overwrites or fails against first; user loses data or is confused by silent failure | Naming convention does not guarantee within-day uniqueness |
| 8 | Unbounded AMEND loop (MA3, CS5, FN3) | AMEND Cycle / Finance | User iterates indefinitely; cost accumulates; frustration grows; no escalation path | No iteration cap; no cumulative cost visibility |
| 9 | Input snapshot not enforced (R4) | Concurrent Review | Mid-review code push changes the input; findings reference code that no longer exists at review completion | No explicit snapshot mechanism described in design |
| 10 | Cross-reviewer finding deduplication missing (MF1) | Finding Entity | Same issue flagged by 2+ reviewers inflates finding count; CONDITIONAL becomes BLOCKED due to duplicate P2s | No dedup step in synthesis |

---

## RECOMMENDATIONS

1. **Add coverage percentage to verdict computation.** A MERGE-READY verdict with <50% file coverage must be flagged LOW-CONFIDENCE or downgraded to CONDITIONAL. This is the single highest-trust issue.

2. **Implement partial-result preservation on failure.** If N-1 of N reviewers complete, write a PARTIAL artifact with available findings and a clear INCOMPLETE flag. Do not discard hours of compute.

3. **Design the dispute lifecycle.** Findings need DISPUTED -> RE-EVALUATED states with rationale capture. This is table-stakes for enterprise adoption and false-positive management.

4. **Add override-with-audit to verdicts.** BLOCKED verdicts need an escape hatch that records who overrode, when, and why. Every CI/CD gate tool has this.

5. **Scan artifacts for secrets before writing to disk.** A pre-write scan that redacts detected secrets prevents the review tool from amplifying the very security issues it is designed to catch.

6. **Define and enforce the P2 accumulation threshold.** Suggested: P2 > 10 escalates verdict to BLOCKED. Document the threshold in the skill specification.

7. **Guarantee artifact filename uniqueness within a day.** Append a short hash or run counter to the signal name for same-topic same-day runs.

8. **Cap AMEND iterations at 3.** After 3 cycles, recommend human review escalation and display cumulative cost.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: No Copilot-specific issues encountered. Parallel file reads and directory exploration worked correctly. The skill ran end-to-end without requiring interactive user input. Frontmatter and artifact naming followed conventions. One minor observation: Copilot's tool-calling model handled the multi-entity state decomposition well, though the lack of a persistent scratchpad meant all state modeling was done in a single pass rather than iteratively refined.
