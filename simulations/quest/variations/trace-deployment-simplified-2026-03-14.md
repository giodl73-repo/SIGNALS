## Simplification Pass — V-01 (trace-deployment)

### What I'm working with

The file contains V-01 through V-05. Only V-01 is the winning variation (lines 30–92). I simplify that body only.

---

## Step 1 — Identify dead weight

| Cut | Words | Reason |
|-----|-------|--------|
| "You own the infrastructure pre-conditions that Commerce deployments routinely skip..." | 33 | Flavor, no criterion mapping in V-01 |
| **"Current practice:"** paragraph entirely | 43 | Background color; NOT C-23 inertia (that's V-04/V-05). V-01 never claimed C-23. |
| Stage 1 role domain elaboration list (trimmed) | 9 | "alert baseline management, secrets rotation, and incident response" → pruned to core |
| General trace instruction (condensed) | 17 | "For each item, name the specific artifact, the actor responsible, and the failure mode if the item is absent or executed out of order. Name every artifact — do not generalize." → "Name the specific artifact, actor, and failure mode for each item. Do not generalize." |
| Phase 1 per-item re-statement | 16 | "Each check names the specific artifact being verified, who runs it, and what breaks if it is skipped." fully repeats the general instruction above |
| Phase 2 per-item re-statement | 10 | "Each step names the artifact being deployed or configured, identifies the prior step it depends on..." → keep only the dependency-chain clause (not in general instruction) |
| Phase 3 method parenthetical | 8 | "(probe name, alert threshold, metric, health endpoint)" — already established by disqualifier example |
| Stage 2 domain detail list | 15 | "with production delivery history across catalog management, pricing engine, promotions pipeline, order management, and entitlement services" → cut entirely |
| Stage 2 "You catch what an infrastructure expert misses:" enumeration | 20 | Sub-questions already enumerate these exactly; reduce to "You surface Commerce-specific gaps that an infrastructure expert misses." |
| Final return trailing clause | 9 | "comparing each gap across both domains before assigning severity" — exact repeat of FINDINGS table instruction |

---

## Step 2 — Simplified prompt body

---

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

## Step 3 — Criteria verification

| Criterion | Status | Why |
|-----------|--------|-----|
| C-14 front-loaded-empty-skeleton | PASS | Table + "do not fill now" + return instruction intact |
| C-21 colloquial-interrogative-headers | PASS | All four phase headers unchanged |
| C-37 extend-not-restate | PASS | "extend it — do not restate it" kept |
| C-38 cross-domain gap coverage | PASS | FINDINGS comparison + four sub-questions covering both domains |
| C-39 four-phase coverage | PASS | All four phases in Stage 1 and Stage 2 |
| C-40 Commerce cross-domain extension | PASS | Four Stage 2 sub-questions intact |
| C-41 phase-domain-pair notation | PASS | All four `(Commerce / PHASE)` labels unchanged |
| C-42 two-stage-only ceiling | BLOCKED | Correct — C-14 and C-21 both pass, same as original |
| C-23 inertia | N/A | V-01 never had it — "Current practice" paragraph was NOT C-23 |
| C-19/C-29 declarative disqualifier | PASS | Negative examples kept in pre-deploy and post-validate |
| Vocabulary criterion | PASS | Both vocabulary lists intact |
| Automation hooks | PASS | Full hooks instruction with domain/phase/failure fields kept |

**All essential criteria: YES**

---

## Simplification report

**Removed (180 words across 10 cuts):**
- Role flavor sentences 2 (33w) and Current Practice paragraph (43w): zero criterion mapping, pure background color
- Stage 1 general instruction: condensed redundant elaboration (17w)
- Phase 1 per-item re-statement: exact repeat of general instruction (16w)
- Phase 2 per-item re-statement: partial repeat; kept dependency-chain clause (10w)
- Phase 3 method parenthetical: established by example already (8w)
- Stage 2 domain detail list in role description (15w)
- Stage 2 "You catch..." enumeration: sub-questions already enumerate (20w)
- Final return trailing clause: repeat of FINDINGS table instruction (9w)
- Stage 1 role domain list: trimmed to core (9w)

```json
{"simplified_word_count": 581, "original_word_count": 793, "all_essential_still_pass": true}
```
