Artifact written to `signals/simulate/state/ai-code-review-state-2026-03-18.md`.

**What was produced:**

- **10 states** (DRAFT through MERGED/CLOSED), **11 operations** fully cataloged
- **9 hand-compiled transitions** (T1-T9) — each with preconditions, state changes, postconditions, and invariants
- **12 findings** (F-01 through F-12) across three categories:
  - **Missing preconditions**: empty-diff submit, trivial revision escape, reopen without branch revalidation
  - **Invalid transitions**: 10 illegal paths to APPROVED/MERGED enumerated
  - **Race conditions**: 6 concurrency hazards (RC-01 and RC-03 are critical — concurrent slot claim and concurrent merge)
- **10 invariants** registered with enforcement checkpoints
- **3 role perspectives**: Sales (loop cap + priority lane), CS (urgency escalation lane), Finance (self-approval window, audit log gap, bypass paths)

Critical items to act on first: **F-03** (concurrent slot claim), **F-10** (concurrent merge), and **F-11** (audit log skipped on merge failure).
