---
skill: simulate-state
topic: ai-code-review
date: 2026-03-18
---

# State Simulation: AI Code Review

## Domain Summary

An AI code review system receives pull requests (PRs), enqueues them for analysis, runs static
and semantic checks via AI reviewer agents, returns findings, and gates merge on approval.
Three role perspectives are applied throughout:

- **Sales**: Wants fast-path reviews for demo branches; loops block customer commitments.
- **Customer Service (CS)**: Needs urgent bug fixes to skip queue during incidents; latency
  in QUEUED state is an SLA risk.
- **Finance**: Requires every change to pass through APPROVED with full audit trail;
  any bypass of state gates is a compliance violation.

---

## State Inventory

| ID | State              | Description                                              |
|----|--------------------|----------------------------------------------------------|
| S0 | DRAFT              | PR created, not yet submitted for review                 |
| S1 | SUBMITTED          | PR submitted; awaiting queue admission                   |
| S2 | QUEUED             | Admitted to review queue; waiting for AI slot            |
| S3 | ANALYZING          | AI reviewer agent actively processing the diff           |
| S4 | REVIEWED           | Analysis complete; findings available, verdict pending   |
| S5 | CHANGES_REQUESTED  | One or more blocking findings; author must revise        |
| S6 | REVISION_SUBMITTED | Author pushed fix commits; re-review needed              |
| S7 | APPROVED           | No blocking findings; merge gate open                    |
| S8 | MERGED             | Code integrated into target branch (terminal)            |
| S9 | CLOSED             | PR closed without merge (terminal)                       |

---

## Operation Catalog

| Op | Operation            | Trigger                              |
|----|----------------------|--------------------------------------|
| O1 | submit(pr)           | Author clicks "Submit for Review"    |
| O2 | enqueue(pr)          | System admission controller runs     |
| O3 | start_analysis(pr)   | AI scheduler claims an idle slot     |
| O4 | complete_review(pr, verdict) | AI agent publishes findings  |
| O5 | request_changes(pr)  | Verdict contains blocking findings   |
| O6 | approve(pr)          | Verdict contains zero blocking items |
| O7 | update_code(pr)      | Author pushes new commits            |
| O8 | merge(pr)            | Author or CI triggers merge          |
| O9 | close(pr)            | Author or admin discards PR          |
| O10| reopen(pr)           | Author re-activates a closed PR      |
| O11| escalate(pr)         | CS urgency override — bumps queue    |

---

## Hand-Compiled State Transitions

### Transition T1: DRAFT -> SUBMITTED via submit(pr)

**Starting state**: S0 (DRAFT)
**Operation**: O1 submit(pr)

Preconditions:
- pr.diff is non-empty (at least one changed file)
- pr.target_branch exists and is accessible
- pr.author is authenticated
- pr is not already in S1..S9

State changes:
- pr.state: DRAFT -> SUBMITTED
- pr.submitted_at = now()
- pr.review_attempts = 0

Postconditions:
- pr.state == SUBMITTED
- pr.submitted_at is set
- Admission controller is notified (event emitted)

Invariants that must hold:
- pr.author != null
- pr.diff.file_count > 0
- pr.target_branch is writeable by merge system

**Finding F-01**: No check that pr.diff is non-empty before submit. A zero-diff PR can
enter SUBMITTED and propagate through the entire pipeline, wasting an AI slot and
producing a vacuous "approved" result. Precondition must be enforced at O1, not assumed.

---

### Transition T2: SUBMITTED -> QUEUED via enqueue(pr)

**Starting state**: S1 (SUBMITTED)
**Operation**: O2 enqueue(pr)

Preconditions:
- pr.state == SUBMITTED
- Admission policy check passes (size limits, token budget, org quota)
- pr has not been closed (pr.closed_at == null)

State changes:
- pr.state: SUBMITTED -> QUEUED
- pr.queued_at = now()
- pr.queue_position assigned by scheduler

Postconditions:
- pr.state == QUEUED
- pr.queue_position > 0
- pr visible in queue dashboard

Invariants:
- queue_position is unique across all QUEUED PRs
- pr.queued_at >= pr.submitted_at

**Finding F-02** (CS role): The admission controller has no urgency lane. During an
incident, a CS bug-fix PR enters the same queue as a low-priority feature branch. No
precondition supports escalate(pr) at this stage. Recommend: O11 escalate(pr) must be
available in S1/S2 and must mutate queue_position to 1 with cs_escalated flag set.

---

### Transition T3: QUEUED -> ANALYZING via start_analysis(pr)

**Starting state**: S2 (QUEUED)
**Operation**: O3 start_analysis(pr)

Preconditions:
- pr.state == QUEUED
- An AI reviewer slot is available (slot.idle == true)
- pr.diff has not changed since enqueue (diff_hash matches)

State changes:
- pr.state: QUEUED -> ANALYZING
- pr.analysis_started_at = now()
- slot.pr_id = pr.id; slot.idle = false
- pr.reviewer_session_id = slot.session_id

Postconditions:
- pr.state == ANALYZING
- pr.reviewer_session_id != null
- slot.idle == false

Invariants:
- Exactly one slot is assigned per PR in ANALYZING
- pr.diff_hash captured at enqueue time equals pr.diff_hash now

**Finding F-03** (Race condition — critical): Two scheduler threads can concurrently
read the same slot as idle and both invoke start_analysis on the same PR. No compare-and-
swap or optimistic lock guards the slot claim. Result: two AI sessions analyze the same
PR; first to complete_review wins; second produces orphaned results with no PR to attach
to. Fix: slot assignment must be atomic (SELECT FOR UPDATE or CAS on slot.idle).

**Finding F-04** (Sales role): If author pushes a commit while pr.state == QUEUED,
diff_hash changes but T3 precondition does not re-validate. Analysis starts on stale diff.
Verdict will not reflect latest changes. Precondition must check diff_hash at start_analysis
time, not just at enqueue time. If mismatch: abort T3, reset to SUBMITTED, re-enqueue.

---

### Transition T4a: ANALYZING -> APPROVED via complete_review(pr, PASS)

**Starting state**: S3 (ANALYZING)
**Operation**: O4 complete_review(pr, verdict=PASS) then O6 approve(pr)

Preconditions:
- pr.state == ANALYZING
- pr.reviewer_session_id matches calling session
- verdict.blocking_findings.count == 0
- verdict.warnings_acknowledged == true (if any warnings exist)

State changes:
- pr.state: ANALYZING -> APPROVED
- pr.review_completed_at = now()
- pr.review_result = verdict
- slot.idle = true (slot released)
- pr.approved_by = [reviewer_session_id]
- pr.review_attempts += 1

Postconditions:
- pr.state == APPROVED
- pr.merge_gate_open == true
- pr.approved_by is non-empty
- slot is released back to pool

Invariants:
- pr.approved_by cannot contain pr.author (self-approval invariant)
- pr.review_attempts >= 1
- If pr.review_attempts > threshold, alert fired (potential looping)

**Finding F-05** (Finance role): The self-approval invariant is not checked at complete_review
time — it is only checked at merge time. This creates a window where an AI session whose
session_id was spoofed to match the author's identity produces an APPROVED state that
passes Finance audit queries. Invariant must be checked at T4a postcondition, not deferred.

---

### Transition T4b: ANALYZING -> CHANGES_REQUESTED via complete_review(pr, FAIL)

**Starting state**: S3 (ANALYZING)
**Operation**: O4 complete_review(pr, verdict=FAIL) then O5 request_changes(pr)

Preconditions:
- pr.state == ANALYZING
- pr.reviewer_session_id matches calling session
- verdict.blocking_findings.count > 0

State changes:
- pr.state: ANALYZING -> CHANGES_REQUESTED
- pr.review_completed_at = now()
- pr.review_result = verdict
- slot.idle = true
- pr.review_attempts += 1
- findings written to pr.findings[]

Postconditions:
- pr.state == CHANGES_REQUESTED
- pr.findings.count > 0
- pr.merge_gate_open == false
- Author notified (event emitted)

Invariants:
- pr.findings.count == verdict.blocking_findings.count
- pr.merge_gate_open == false whenever state is CHANGES_REQUESTED

**Finding F-06**: No maximum review_attempts cap is enforced. A PR that repeatedly fails
(e.g., auto-generated code the AI consistently rejects) will loop S5->S6->S2->S3->S5
indefinitely. Each loop consumes an AI slot. Add invariant: if pr.review_attempts >= MAX,
auto-close with status REVIEW_LOOP_EXCEEDED and notify author + manager.

---

### Transition T5: CHANGES_REQUESTED -> REVISION_SUBMITTED via update_code(pr)

**Starting state**: S5 (CHANGES_REQUESTED)
**Operation**: O7 update_code(pr)

Preconditions:
- pr.state == CHANGES_REQUESTED
- pr.author is authenticated and is the PR owner
- new commits address at least one finding in pr.findings[]
- pr.target_branch has not diverged more than staleness_threshold commits

State changes:
- pr.state: CHANGES_REQUESTED -> REVISION_SUBMITTED
- pr.diff_hash updated to new diff
- pr.revision_count += 1
- pr.last_revision_at = now()
- findings marked as PENDING_RE_REVIEW

Postconditions:
- pr.state == REVISION_SUBMITTED
- pr.diff_hash reflects new commits
- pr.revision_count >= 1

Invariants:
- pr.revision_count increments monotonically
- pr.diff_hash after update != pr.diff_hash before update (real change occurred)

**Finding F-07** (Sales role): No check that new commits actually address any finding.
Author can push a trivial whitespace commit to escape CHANGES_REQUESTED and get re-queued
without fixing the blocking issue. Precondition should require at minimum one finding
transitioned to PENDING_RE_REVIEW based on file overlap heuristic.

**Finding F-08** (invalid transition): update_code is not blocked in ANALYZING state.
If author pushes while AI is active (S3), the operation succeeds silently. pr.diff_hash
changes but pr.state stays ANALYZING. AI completes on old diff; verdict is invalidated.
This is the same failure path as F-04 but from the update_code side. O7 must check that
pr.state NOT IN {ANALYZING, QUEUED} and reject if so (or auto-abort analysis, reset, re-enqueue).

---

### Transition T6: REVISION_SUBMITTED -> QUEUED via enqueue(pr)

**Starting state**: S6 (REVISION_SUBMITTED)
**Operation**: O2 enqueue(pr)

Preconditions:
- pr.state == REVISION_SUBMITTED
- Admission policy allows re-review (quota not exhausted)
- pr.review_attempts < MAX_REVIEW_ATTEMPTS

State changes:
- pr.state: REVISION_SUBMITTED -> QUEUED
- pr.queued_at = now() (updated)
- prior findings retained in pr.findings[] as PENDING_RE_REVIEW

Postconditions:
- pr.state == QUEUED
- Prior findings visible to AI agent on next analysis pass

Invariants:
- pr.findings from prior rounds must be passed to AI context on next analysis
- Quota check applies identically to first-time and re-review enqueues

**Finding F-09**: Prior findings are not injected into AI context on re-review. AI re-analyzes
from scratch, may re-surface same findings already acknowledged, or miss regressions.
The enqueue operation must attach prior_findings to the analysis job context.

---

### Transition T7: APPROVED -> MERGED via merge(pr)

**Starting state**: S7 (APPROVED)
**Operation**: O8 merge(pr)

Preconditions:
- pr.state == APPROVED
- pr.merge_gate_open == true
- pr.target_branch has not diverged since approval (within rebase_tolerance)
- No concurrent merge in progress (merge_lock not held)
- CI status checks all green (if required)
- pr.approved_by does not contain only pr.author

State changes:
- pr.state: APPROVED -> MERGED
- pr.merged_at = now()
- pr.merged_by = caller_identity
- target_branch HEAD updated to include PR commits
- merge_lock released

Postconditions:
- pr.state == MERGED (terminal)
- target_branch.head contains pr.commits
- Audit log entry written with: pr.id, pr.merged_by, pr.approved_by, pr.merged_at

Invariants:
- MERGED is terminal: no further state transitions permitted
- Audit log entry is mandatory (Finance invariant — must not be skipped on failure path)

**Finding F-10** (Race condition — critical): Two concurrent callers invoke merge(pr) while
pr.state == APPROVED. Both pass the "state == APPROVED" precondition check. Both acquire
partial merge state. Target branch receives duplicate commits or corrupted HEAD. Fix: merge
operation must acquire merge_lock with TAS/CAS before reading pr.state.

**Finding F-11** (Finance role): On merge failure (e.g., git conflict mid-merge), pr.state
may remain APPROVED but target_branch is in a partial state. Audit log entry is only written
on success path. Finance requires audit entries for failures too. Postcondition must write
audit log unconditionally in a finally block, with status MERGE_FAILED if applicable.

---

### Transition T8: APPROVED -> CLOSED via close(pr)

**Starting state**: S7 (APPROVED)
**Operation**: O9 close(pr)

Preconditions:
- pr.state == APPROVED
- caller is pr.author or admin
- pr.merged_at == null (not already merged)

State changes:
- pr.state: APPROVED -> CLOSED
- pr.closed_at = now()
- pr.merge_gate_open = false

Postconditions:
- pr.state == CLOSED (terminal)
- pr.merge_gate_open == false

Invariants:
- CLOSED PRs cannot be merged (merge_gate_open must be false)
- CLOSED is terminal

---

### Transition T9: CLOSED -> SUBMITTED via reopen(pr)

**Starting state**: S9 (CLOSED)
**Operation**: O10 reopen(pr)

Preconditions:
- pr.state == CLOSED
- pr.merged_at == null (MERGED is terminal and cannot be reopened)
- caller is pr.author or admin
- pr.target_branch still exists

State changes:
- pr.state: CLOSED -> SUBMITTED
- pr.closed_at = null
- pr.reopened_at = now()
- pr.reopened_by = caller_identity

Postconditions:
- pr.state == SUBMITTED
- Prior findings retained from before close

Invariants:
- reopen is only valid from CLOSED (not MERGED)
- pr.review_attempts carries over (does not reset to 0)

**Finding F-12** (invalid transition): reopen does not validate that pr.diff is still non-empty
and that pr.target_branch still exists. If target_branch was deleted after close, reopen
succeeds and PR enters SUBMITTED pointing at a non-existent branch. O10 must re-validate all
submit(pr) preconditions.

---

## Invalid Transition Table

| From              | Operation       | Why Invalid                                              |
|-------------------|-----------------|----------------------------------------------------------|
| DRAFT             | merge(pr)       | Skips all review gates — Finance violation               |
| DRAFT             | approve(pr)     | No analysis has occurred                                 |
| QUEUED            | merge(pr)       | Bypasses ANALYZING and APPROVED gates                    |
| QUEUED            | approve(pr)     | No analysis result exists                                |
| ANALYZING         | merge(pr)       | Analysis incomplete; verdict unknown                     |
| CHANGES_REQUESTED | merge(pr)       | Blocking findings unresolved — Finance violation         |
| CHANGES_REQUESTED | approve(pr)     | Approval requires zero blocking findings                 |
| REVISION_SUBMITTED| merge(pr)       | Re-analysis not yet run                                  |
| REVISION_SUBMITTED| approve(pr)     | Re-analysis not yet run                                  |
| MERGED            | any             | Terminal state; all operations must be rejected          |
| CLOSED            | merge(pr)       | merge_gate_open is false; merge must be rejected         |
| any               | start_analysis  | Only valid from QUEUED; other states have no queue slot  |

---

## Race Condition Register

| RC-ID | Scenario                                    | Severity | Fix                                           |
|-------|---------------------------------------------|----------|-----------------------------------------------|
| RC-01 | Concurrent start_analysis on same QUEUED PR | Critical | CAS on slot.idle; one winner, one rejected    |
| RC-02 | Author update_code during ANALYZING         | High     | Block O7 in S3; or abort analysis, re-enqueue |
| RC-03 | Concurrent merge(pr) on APPROVED PR         | Critical | merge_lock TAS before state read              |
| RC-04 | enqueue called twice on SUBMITTED PR        | Medium   | Idempotent enqueue: check state == SUBMITTED  |
| RC-05 | close + merge concurrent on APPROVED        | High     | Serialize via merge_lock; close checks lock   |
| RC-06 | reopen + enqueue concurrent on CLOSED       | Low      | State check under lock in both operations     |

---

## Invariant Register

| INV-ID | Invariant                                                         | Checked At         |
|--------|-------------------------------------------------------------------|--------------------|
| INV-01 | pr.author != approved_by member (no self-approval)               | T4a postcondition  |
| INV-02 | MERGED is terminal; no transitions out                            | All operations     |
| INV-03 | pr.merge_gate_open == false whenever state != APPROVED            | T4b, T8, T9        |
| INV-04 | pr.findings.count == verdict.blocking_findings.count             | T4b postcondition  |
| INV-05 | pr.review_attempts increments monotonically; never decrements     | T4a, T4b           |
| INV-06 | Exactly one AI slot per ANALYZING PR                              | T3 via CAS         |
| INV-07 | Audit log entry written on every merge attempt (pass or fail)     | T7 finally block   |
| INV-08 | pr.diff_hash at analysis time must match diff_hash at enqueue time| T3 precondition    |
| INV-09 | pr.review_attempts < MAX_REVIEW_ATTEMPTS before re-enqueue        | T6 precondition    |
| INV-10 | queue_position is unique across all QUEUED PRs                    | T2 postcondition   |

---

## Role Perspective Summary

### Sales
Key risk: Review loop (F-06) and stale-diff analysis (F-04/F-08) extend cycle time for demo
branches. A PR that loops 3+ times before a demo blocks the sales motion. Recommend:
priority lane configurable per branch pattern (e.g., `demo/*`) that bypasses quota checks
and gets queue_position = 1 on first enqueue.

### Customer Service
Key risk: No urgency path (F-02). During a P0 incident, a CS bug fix waits behind feature
PRs with no mechanism to escalate. O11 escalate(pr) must be a first-class operation, not a
manual workaround. Also: loop cap (F-06) can auto-close an in-flight incident fix. MAX
should be configurable and CS-escalated PRs should have a higher cap.

### Finance
Key risk: Three bypass paths to MERGED without full approval trail:
(1) Self-approval window (F-05) — invariant checked too late.
(2) Missing audit log on merge failure (F-11) — compliance gap.
(3) Invalid transitions to MERGED from non-APPROVED states (table above) — must be
    enforced at the operation layer, not just UI layer.
Finance requires: all three gaps closed, audit log non-optional, and change_history table
recording every state transition with caller identity and timestamp.

---

## Findings Summary

| ID   | Type                    | Severity | Description                                      |
|------|-------------------------|----------|--------------------------------------------------|
| F-01 | Missing precondition    | Medium   | No empty-diff guard at submit                    |
| F-02 | Missing operation       | High     | No urgency escalate lane (CS risk)               |
| F-03 | Race condition          | Critical | Concurrent slot claim in start_analysis          |
| F-04 | Stale-state analysis    | High     | Author commit during QUEUED invalidates diff     |
| F-05 | Invariant checked late  | High     | Self-approval not blocked at complete_review     |
| F-06 | Missing loop cap        | High     | Unbounded review_attempts drains AI quota        |
| F-07 | Weak revision guard     | Medium   | Trivial commit escapes CHANGES_REQUESTED         |
| F-08 | Invalid transition      | High     | update_code allowed during ANALYZING             |
| F-09 | Context missing         | Medium   | Prior findings not passed to re-review           |
| F-10 | Race condition          | Critical | Concurrent merge on APPROVED corrupts branch     |
| F-11 | Audit gap               | High     | Merge failure omits audit log (Finance)          |
| F-12 | Missing re-validation   | Medium   | reopen does not validate target_branch exists    |

---

QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: Clean run. State machine is self-consistent across all 12 findings. Race conditions RC-01 and RC-03 are the highest-priority items for implementation. Finance findings (F-05, F-11) are compliance-blockers that should gate any production deployment.
