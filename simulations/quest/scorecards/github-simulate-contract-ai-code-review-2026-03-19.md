● List directory .
  └ 13 files found

● List directory signals
  └ 5 files found

● List directory signals\simulate
  └ 2 files found

● List directory signals\discover
  └ 4 files found

● List directory signals\draft
  └ 1 file found

● List directory signals\specify
  └ 3 files found

● List directory signals\specify
  └ 3 files found

● List directory signals\draft\specs
  └ 1 file found

● List directory signals\simulate\lifecycle
  └ 1 file found

● List directory simulations
  └ 1 file found

● List directory signals\simulate\request
  └ 1 file found

● Read ai-code-review-request-2026-03-19.md
  │ signals\simulate\request\ai-code-review-request-2026-03-19.md
  └ 1 line read

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ 1 line read

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ 1 line read

Let me read the spec and simulation artifacts in sections to understand the contract and actual output.

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-request-2026-03-19.md
  │ signals\simulate\request\ai-code-review-request-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L120:280 (161 lines read)

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ L120:280 (161 lines read)

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ L280:450 (59 lines read)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L280:450 (171 lines read)

● Read ai-code-review-request-2026-03-19.md
  │ signals\simulate\request\ai-code-review-request-2026-03-19.md
  └ L120:300 (181 lines read)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L450:600 (25 lines read)

● Read ai-code-review-request-2026-03-19.md
  │ signals\simulate\request\ai-code-review-request-2026-03-19.md
  └ L300:500 (201 lines read)

● List directory signals\specify
  └ 3 files found

● Read ai-code-review-request-2026-03-19.md
  │ signals\simulate\request\ai-code-review-request-2026-03-19.md
  └ L500:700 (68 lines read)

● List directory signals\specify\commitment
  └ 1 file found

● List directory signals\specify\pitch
  └ 1 file found

● List directory signals\specify\proposal
  └ 1 file found

● Read ai-code-review-commitment-2026-03-19.md
  │ signals\specify\commitment\ai-code-review-commitment-2026-03-19.md
  └ L1:80 (80 lines read)

Now I have a thorough understanding of the artifacts. Let me read a bit more of the commitment plan and then build the contract simulation artifact.

● Read ai-code-review-commitment-2026-03-19.md
  │ signals\specify\commitment\ai-code-review-commitment-2026-03-19.md
  └ L80:200 (121 lines read)

● List directory signals\roles
  └ 3 files found

● Create contract output directory (shell)
  │ if (!(Test-Path "sim-test\signals\simulate\contract")) { New-Item -ItemType Directory
  │ -Path "sim-test\signals\simulate\contract" -Force }
  └ 4 lines...

Now I have a comprehensive understanding of all three artifacts. Let me build the contract simulation artifact. The key sources are:

1. **Spec** (`draft/specs/ai-code-review-spec-2026-03-19.md`) — the contract/expected behavior
2. **Lifecycle simulation** (`simulate/lifecycle/ai-code-review-lifecycle-2026-03-19.md`) — actual behavioral output
3. **Request trace simulation** (`simulate/request/ai-code-review-request-2026-03-19.md`) — actual request-level output

I need to perform a structured comparison using the GateTokenSchema, identify mismatches, and produce a GO/NO-GO gate result.

● Create ai-code-review-contract-2026-03-19.md +243
  └ signals\simulate\contract\ai-code-review-contract-2026-03-19.md

● Verify artifact written (shell)
  │ Get-Content "sim-test\signals\simulate\contract\ai-code-review-contract-2026-03-19.md" |
  │ Select-Object -First 5
  └ 6 lines...

Contract simulation complete. Artifact written to `signals/simulate/contract/ai-code-review-contract-2026-03-19.md`.

**Gate result: FAIL (NO-GO)**

**Summary:**
- **Schema sweep:** PASS — all 7 GateTokenSchema fields validated
- **Element diff:** 3 CRITICAL, 3 HIGH, 9 MEDIUM, 3 LOW mismatches

**Critical blockers:**
1. **CF-01:** JWT scope `inference:analyze` ≠ required `inference:analyze:security` — blocks all AI inference
2. **CF-02:** Installation token has `pull_requests:read` but needs `write` — blocks review posting
3. **CF-03:** 5 of 12 spec requirements untestable due to upstream auth failures

**High findings:** No `.ai-review.yml` config fetch; shallow context assembly (missing blame, imports, README, prior feedback)

**Remediation:** Fix both auth gaps → re-run `/simulate-request` → fix config/context gaps → re-gate.


Total usage est:        6 Premium requests
API time spent:         4m 5s
Total session time:     4m 24s
Total code changes:     +243 -0
Breakdown by AI model:
 claude-opus-4.6-1m       875.7k in, 9.2k out, 813.0k cached (Est. 6 Premium requests)
