---
skill: quest-golden
skill_target: trace-deployment
date: 2026-03-14
rounds: 20
rubric_final: trace-deployment-rubric-v17-2026-03-14.md
score: 205
status: GOLDEN
---

# trace-deployment — Golden Prompt

**Score:** 205/260 (v16 rubric) | **All-essential pass** | **Simplification:** PASS (27% reduction)

---

## Golden Prompt Body

You are running a deployment trace signal for: {{topic}}

---

**FINDINGS — do not fill this now. Return here after Stage 2.**

| Phase | Gap | Domain | Severity | Why it ranks here |
|-------|-----|--------|----------|-------------------|

Return to this table after completing Stage 2. Add one row per gap found. Before assigning severity, compare each gap against the others across both domains — Operations and Commerce — and rank by deployment blast radius, not by phase order.

---

## ROLE — STAGE 1: OPERATIONS DEPLOYMENT EXPERT

You are a senior Operations/SRE engineer with production authority across infrastructure provisioning, pipeline gates, and incident response.

**Stage 1 vocabulary** (use throughout): health endpoint · pipeline gate · deployment lock · canary threshold · alert baseline · secrets rotation · config drift · blue-green swap · runbook trigger · SLA window · circuit breaker

Trace the full deployment lifecycle for {{topic}} across four phases. Name the specific artifact, actor, and failure mode for each item. Do not generalize.

**what needs to be true before we touch this?**

List every pre-deploy check. "Verify the environment is stable" names no artifact and does not qualify; "confirm health endpoint /ready returns 200 on all service replicas" qualifies.

**what order do the pieces go in?**

List every deployment step in exact execution order. Each step names the artifact, the prior step it depends on (or NONE), and the out-of-order failure.

**how do we know it landed?**

List every post-deploy validation. Each validation names what is checked, the method, and what a failed validation triggers. A validation that asks "did everything land correctly?" names no probe and does not qualify.

**what do we do if it didn't?**

List every rollback trigger and the full rollback execution sequence. Each entry names the trigger condition, the rollback artifact, the rollback execution order, and the minimum data-integrity guarantee after rollback completes.

---

## ROLE — STAGE 2: COMMERCE DEPLOYMENT EXPERT (Review and Extend)

You are a senior Commerce platform deployment specialist. Review the Operations trace above and extend it — do not restate it. You surface Commerce-specific gaps that an infrastructure expert misses.

**Stage 2 vocabulary** (use throughout): deployment manifest · feature flag gate · catalog sync boundary · order pipeline drain · pricing cache invalidation · entitlement snapshot · rollback window · dark-launch guard · cutover window · cart-session baseline

Answer each sub-question explicitly. Name Commerce artifacts — do not generalize.

**1a (Commerce / PRE-DEPLOY):** Which Commerce-specific pre-deploy check is absent from Stage 1's trace? Name the Commerce artifact being missed and the failure mode if the check is absent.

**1b (Commerce / DEPLOY-SEQUENCE):** Which Commerce artifact promotion step is missing from or incorrectly sequenced in Stage 1's deployment order? Name the artifact and the out-of-order consequence.

**1c (Commerce / POST-VALIDATE):** Which Commerce business metric or entitlement verification is absent from Stage 1's post-deploy validation? Name the metric or check and what silent failure its absence allows.

**1d (Commerce / ROLLBACK):** Which Commerce artifact state is not restored in Stage 1's rollback path? Name the Commerce artifact and the state abandoned on rollback.

**AUTOMATION HOOKS — at least one per domain:**

For each domain (Operations · Commerce), name at least one automation hook: a specific tool, pipeline gate, or named check that enforces a currently manual or absent validation. For each hook, state the domain, the hook name, the phase it runs in (PRE-DEPLOY · DEPLOY-SEQUENCE · POST-VALIDATE · ROLLBACK-DETECT), and what failure it catches. "Add monitoring" does not name a hook.

Now return to the FINDINGS table above and fill it in.

---

## What Made It Golden

**1. Operations-first role sequence (C-14 / C-37)**
Placing SRE as Stage 1 front-loads infrastructure pre-conditions — the phase where silent deployment failures originate. Commerce Stage 2 then fills gaps the infrastructure expert cannot see. This ordering matches how real deployment failures cascade: infra gaps first, then Commerce-state gaps that only surface hours later.

**2. Prose structural-adoption path (C-14 / C-21 / C-26 / C-33 / C-34)**
Colloquial interrogative headers ("what needs to be true before we touch this?") paired with prose instructions — not tables or formal section headers — activates the five structural-adoption criteria as a unit. V-02's formal headers (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE) blocked C-21/C-26/C-33/C-34 and lost 40 points, confirming this path is not interchangeable with table-anchored formats.

**3. Front-loaded empty FINDINGS skeleton (C-30)**
Placing the FINDINGS table before Stage 1 content — with an explicit "do not fill this now" instruction — forces the model to anchor its output structure before generating trace content. The empty skeleton at top creates a contract the model must satisfy at the end; omitting it loses the blast-radius ranking and cross-domain comparison.

**4. `(Domain / Phase)` pair notation on all Stage 2 sub-questions (C-41)**
R19 used domain-only labels (`1a (Commerce):`) and systematically dropped POST-VALIDATE and ROLLBACK phases. R20 uses `(Commerce / PRE-DEPLOY)`, `(Commerce / DEPLOY-SEQUENCE)`, `(Commerce / POST-VALIDATE)`, `(Commerce / ROLLBACK)` — pair labels on every sub-question header. C-41 confirmed: all four phases receive Commerce coverage with zero systematic drops.

**5. Stage 2 explicit non-restatement + vocabulary compartmentalization (C-38 / C-40)**
"Review the Operations trace above and extend it — do not restate it" is a hard boundary that prevents Stage 2 from duplicating Stage 1 content. Separate vocabulary blocks per stage (11 terms each, zero overlap) enforce domain compartmentalization without role-conflict. Stage 2 surfaces Commerce artifact gaps; Stage 1 is not revisited.

---

## Final Rubric Criteria Summary (v17)

| Criterion | Fires in Golden | Notes |
|-----------|----------------|-------|
| C-14 | YES | Prose structural-adoption: colloquial headers + prose instructions |
| C-21 | YES | No formal section headers blocking criteria group |
| C-26 | YES | Interrogative phase headers activate questioning register |
| C-29 | YES | Declarative disqualifier present in PRE-DEPLOY phase body |
| C-31 | YES | Disqualifier confirmed inside named phase section (not general instructions) |
| C-32 | YES | Single-paragraph density maintained per phase |
| C-33 | YES | Vocabulary block in role header, not scattered |
| C-34 | YES | Per-phase instruction is singular focused clause |
| C-37 | YES | Two-stage structure present |
| C-38 | YES | Stage 2 extend-not-restate boundary explicit |
| C-39 | YES | Separate vocabulary blocks per stage |
| C-40 | YES | Stage 2 sub-questions cover all four phases |
| C-41 | YES | `(Domain / Phase)` pair notation on all Stage 2 sub-questions |
| C-42 | BLOCKED | Two-stage-only ceiling diagnostic — V-03 fires this at 160/260 |
| C-43 | CANDIDATE | Stage 2 intra-domain quality review — not yet in this golden; R21 target |
| C-44 | CANDIDATE | Declarative disqualifier in phase section confirmed — scores in R21 |

**v17 ceiling for this path:** 215/270 (C-43 + C-44 not yet written into prompt)
**R21 target:** Add Stage 2 sub-questions 2a–2d targeting Stage 1 intra-domain quality defects (C-43), verify declarative disqualifier is inside `**what needs to be true...?**` section body not above it (C-44).
