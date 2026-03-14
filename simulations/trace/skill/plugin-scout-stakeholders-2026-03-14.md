---
skill: trace-skill
topic: plugin
item: scout-stakeholders
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md
---

# /trace-skill -- scout-stakeholders

**Invocation**: `/scout-stakeholders "launching Signal plugin at a 5,000-person Microsoft all-hands"`
**Scenario**: Lead planning all-hands launch, bottom-up opt-in rollout

## Phase 1: Setup

No CODEOWNERS in repo. Skill falls back to invocation-string inference (correct behavior -- invocation contains rich org context: "5,000-person Microsoft all-hands"). Roles: PM, Strategy, UX.

**SF-01-A (P2)**: CODEOWNERS fallback is implicit in spec. Must be made explicit: "If org signals are absent, extract from invocation. If invocation is also insufficient, ask one question: What org is this for?"

## Phase 2: Execute

### Power/Interest Grid

| Stakeholder | Power | Interest | Category |
|-------------|-------|----------|----------|
| CVP / VP Engineering | 5 | 2 | Gatekeeper (keep satisfied) |
| Security Review Board | 5 | 1 | Gatekeeper (CRITICAL path) |
| Principal/Partner Engineers | 4 | 4 | Influencer (engage pre-event) |
| Architects | 4 | 4 | Influencer (win before all-hands) |
| PM Director | 4 | 3 | Influencer |
| Compliance / Privacy | 4 | 1 | Gatekeeper |
| Agenda Coordinator | 3 | 2 | Gatekeeper (owns slot) |
| Dev Lead (early adopter) | 3 | 5 | Champion (give demo slot) |
| Developers (5,000) | 2 | 3 | User (inform) |

### Key conflicts

1. **Security Review Board**: power 5, interest 1. Will not self-initiate. If review not started before slot is confirmed, it blocks the launch.
2. **CVP vs. developer audience**: exec wants cost/risk framing; developers want the tool itself. Two audiences, one stage.
3. **Architects skeptic cluster**: applies "production-ready or demo toy?" filter. Too late to address at the all-hands.

## Phase 3: Findings

**Veto risks**:
1. Security Review Board -- P=HIGH, I=CRITICAL. Start review now, target 2 weeks before event.
2. Architects (skeptic subset) -- P=MEDIUM, I=HIGH. Private demo 1 week before.
3. CVP low engagement -- P=MEDIUM, I=MEDIUM. Brief with cost-reduction frame 2 days before.

**Communication strategy**:
| Quadrant | Who | Timing | Message |
|----------|-----|--------|---------|
| Keep satisfied | CVP, Security, Compliance | 3 weeks before | Risk profile + security model |
| Engage | Principals, Architects, PM Director | 2 weeks before | Private demo, collect objections |
| Champion | Dev Lead | Now | Give them the live demo slot |
| Inform | All developers | All-hands day | One tool, one link, 5 minutes to install |

## Phase 4: Amend

1. Add Agenda Coordinator to critical path explicitly (owns the slot, 2 months lead time)
2. Distinguish "all developers" (interest 2, inform) from "early adopter segment" (interest 5, engage within 48h post-event)
3. Add "what we are NOT doing" data flow summary for Compliance/Security gatekeepers

## Verdict

**Result**: USEFUL. Power/interest grid, veto risks, and communication strategy produced concrete, urgent actions.

### Findings Register

| ID | Finding | Severity |
|----|---------|----------|
| SF-01-A | CODEOWNERS fallback rule is implicit -- must be made explicit | P2 |
| SF-01-B | Architect skeptic cluster must be addressed pre-event, not at the all-hands | P1 |
| SF-01-C | Security review must start before slot is confirmed, not after | P1 |
| SF-01-D | Developer audience needs post-event follow-on path within 48h | P2 |
