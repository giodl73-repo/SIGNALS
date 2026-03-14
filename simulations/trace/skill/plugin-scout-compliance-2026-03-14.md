---
skill: trace-skill
topic: plugin
item: scout-compliance
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-compliance

**Invocation**: `/scout-compliance "Signal plugin -- CLI tool distributed as SKILL.md files, runs in Claude Code, produces Markdown artifacts in git repos"`
**Scenario**: Compliance officer at regulated financial services firm

## Phase 1: Setup

7 frameworks inferred: SOC 2, GLBA, FFIEC, SR 11-7, FINRA BCP, PCI DSS (conditional), GDPR/CCPA (conditional). No user prompting needed.

## Phase 2: Execute

**Key finding**: The primary compliance risk surface is Claude Code sending repo content to the Anthropic API. Signal does not expand this surface -- it exists for any Claude Code usage.

- SOC 2 / FFIEC: vendor assessment scope = Claude Code, not Signal
- SR 11-7: applies to Claude (the model), not Signal (the methodology). Signal's documented roles IMPROVE SR 11-7 posture.
- GLBA: applies to artifacts in git, not to Signal itself. Git access controls are the control.
- BCP: artifacts persist without Claude Code. Stronger posture than SaaS.

## Phase 3: Findings

### Requirements Matrix

| Requirement | Status |
|-------------|--------|
| Vendor assessment | Scope = Claude Code, not Signal |
| Data access controls | SATISFIED -- git repo controls |
| Audit trail | SATISFIED -- git commit history |
| Data residency | SATISFIED -- local git |
| Model risk documentation | ACTION -- add Claude Code to inventory |
| NPI handling policy | ACTION -- policy update required (1-2 weeks) |

**Blocking requirements**: 0 (for teams where Claude Code is already approved)

### Already Satisfied by Design

Git-native artifacts, no server/SaaS, no user data persistence, SKILL.md is plain text, methodology documented, artifacts survive without AI. All compliance-favorable by design.

## Phase 4: Amend

1. Clarify SR 11-7 scope -- Signal is a methodology, not the model
2. Add data-sensitivity tiering (GREEN/YELLOW/RED) to NPI policy
3. Verify Anthropic API zero-retention terms in existing vendor agreement

## Verdict

**Result**: USEFUL. Signal is adoption-ready for teams where Claude Code is already approved. Key message for compliance officers: "Approving Signal is approving a process, not a vendor."

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | Vendor assessment scope = Claude Code, not Signal | P1 (informational) |
| SF-02 | SR 11-7 applies to Claude, not Signal -- misclassification risk | P1 (informational) |
| SF-03 | Git history satisfies SOC 2 / FFIEC / SR 11-7 audit trail | P2 (document as control) |
| SF-04 | NPI policy gap -- no restriction on artifact content | P2 (policy action) |
| SF-05 | Anthropic API data retention terms require one-time verification | P2 |
| SF-06 | Signal's structured methodology improves SR 11-7 posture | P2 (document as benefit) |
| SF-07 | PCI DSS scope conditional on team behavior, not Signal design | P3 |
