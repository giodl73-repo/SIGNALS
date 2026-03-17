Now I have the full R14 and R15 scorecards. Key state before writing:

- **Template ceiling**: 165/210 (stable, C-31/C-32 structurally inaccessible via template)
- **Best prose ceiling**: 160/210 (V-03/V-05 in R15: compressed + dual disqualifiers + C-17 + C-32)
- **Gap to close**: 5 pts — the template path uniquely holds C-14, C-21, C-26, C-27, C-28 on criteria that have never been tested for prose activation
- **R15 conclusion**: "Rubric v12 is stable. No candidates for C-33."

R16 priority question: **can any template-exclusive criterion activate on the prose path?** Three candidates: C-14 (front-loaded gap skeleton), C-21/C-26 (interrogative headers), C-27 (three-field rollback).

---

# /quest:variate — `trace:deployment` — Round 16

**Rubric**: v12 (210 pts, 32 criteria) | **Date**: 2026-03-15
**R15 prose ceiling**: 160/210 (V-03, V-05) | **Template ceiling**: 165/210 (V-02, stable)
**R16 focus**: probe three template-exclusive criteria (C-14, C-21/C-26, C-27) for prose-path activation

**Single-axis variations**: V-01 (C-14 probe), V-02 (C-21/C-26 probe), V-03 (C-27 probe)
**Combined variations**: V-04 (C-14 + C-21/C-26 joint), V-05 (C-21/C-26 embedded + C-27 + compression tradeoff)

---

## V-01

**Axis**: Lifecycle emphasis — front-loaded gap table in prose before Phase 1 (no template field architecture)
**Hypothesis**: Placing a gap table skeleton instruction *before* the phase trace in a prose prompt activates C-14; the test resolves whether C-14 and C-15 are mutually exclusive on the prose path. If a prose gap table is not "template apparatus" in C-15's sense, both can activate simultaneously (+5 pts over R15 ceiling). If they are mutually exclusive, C-14 PASS forces C-15 FAIL and the score stays at 150/210.
**Predicted delta if C-14 ∩ C-15 coexist**: 160 → 165 (ties template ceiling)
**Predicted delta if mutually exclusive**: 160 → 150 (C-15 drops out, net –10)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [describe what this team currently does — their shared runbook,
manual approval gates, and deployment sequence as practiced].
Known failure mode: [describe the recurring failure this team has encountered — the
check or step that gets skipped and what it costs when it does].

Before tracing any phase, create your gap table now. Write a table with four columns:
Phase | Gap | Severity (critical / moderate / low) | Why. Print the header row; leave
every data row blank. Do not pre-fill any row. You will return to fill this table only
after completing all four phases. When you return, compare every gap against every
other before assigning Severity.

PRE-DEPLOY CHECKS

List at least 3 checks. For each, name what is being verified and what failure looks
like. "'Confirm the environment is healthy' names no specific condition and does not
qualify."

DEPLOYMENT SEQUENCE

List at least 4 steps in execution order. Call out at least one ordering dependency
explicitly — the step that must complete before the next can begin, and what breaks
if it does not.

POST-DEPLOY VALIDATION

List at least 2 validation actions. Each must name a probe, threshold, or
data-integrity assertion. "A validation that asks 'did the deployment succeed?' names
no probe or threshold and does not qualify."

ROLLBACK

State the rollback trigger, at least one undo step, and how to verify rollback
succeeded.

Return to the gap table above. Fill one row per phase. State what should be added or
changed — naming a gap without prescribing a remedy does not qualify. Identify at
least one automation hook in the deployment lifecycle.
```

---

## V-02

**Axis**: Phrasing register — bare colloquial interrogative phase headers in a prose prompt (no template field architecture, no per-phase template fields)
**Hypothesis**: Interrogative headers identical to the template path's ("what needs to be true before we touch this?", etc.) inside a prose prompt test whether C-21 and C-26 are surface-form signals (activate on the header text regardless of surrounding context) or template-apparatus signals (only activate when accompanied by field labels). If C-21/C-26 activate in prose: +10 pts over prose baseline at standard density. If they are template-exclusive: no gain, confirms these two criteria are path-locked.
**Predicted delta if C-21 ∩ C-26 activate in prose**: 150 → 160 (matches R15 prose ceiling by a different path)
**Predicted delta if template-exclusive**: 150 → 150 (confirms path-lock, useful as negative evidence)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [describe what this team currently does — their checklist,
deployment sequence, and approval gates as practiced].
Known failure mode: [describe the recurring failure pattern].

Trace the deployment of {{TOPIC}} in prose across four phases. Each phase begins with
the bare header shown below — answer it in full prose sentences.

what needs to be true before we touch this?
List at least 3 pre-deploy checks. For each, name the specific condition being
verified and what failure looks like. "'Verify the system is ready' names no specific
condition and does not qualify."

what's the deployment order?
List at least 4 steps in execution order. Call out at least one ordering dependency
explicitly — the step that must complete before the next can begin, and what breaks
if it does not.

did it land?
List at least 2 post-deploy validation actions. Each must name a probe, threshold, or
data-integrity assertion. "A validation that asks 'is the deployment healthy?' names
no probe or threshold and does not qualify."

what do we do if it didn't?
State the rollback trigger, at least one undo step, and how to verify rollback
succeeded.

After all four phases, produce a cross-phase gap summary table: Phase | Gap | Severity
(critical / moderate / low) | Why. Identify at least one gap per phase; state what
should be added or changed — naming a gap without a remedy does not qualify. Compare
all gaps before assigning Severity. Identify at least one automation hook.
```

---

## V-03

**Axis**: Output format — three-field rollback structure explicitly labeled in prose, at compressed single-paragraph density, with dual disqualifiers
**Hypothesis**: Naming the rollback instruction as exactly three bare-labeled components ("trigger", "steps", "verify") in a prose prompt tests whether C-27 is a template-exclusive criterion (requires colon-notation fields like `trigger:`, `rollback-1:`, `verify-rollback:`) or a semantic criterion (requires exactly three named rollback components regardless of notation). Combined with compression, this activates C-17/C-31/C-32 simultaneously. If C-27 activates in prose: 160 → 165 (ties template ceiling via a different path). If template-exclusive: 160 → 160 (no change, useful negative evidence for C-27 path-lock).
**Predicted delta if C-27 activates in prose**: +5 pts — prose ceiling reaches 165/210
**Predicted delta if template-exclusive**: 0 pts — confirms C-27 is path-locked

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [what this team currently does — checklist, sequence, approval gates
as practiced].
Known failure mode: [the recurring failure — what gets skipped and what it costs].

Trace the deployment of {{TOPIC}} in a single instruction: for pre-deploy list 3+
checks, each naming the specific condition verified and what failure looks like
("ensure services are available" names no condition and does not qualify); for
sequence list 4+ ordered steps and call out one ordering dependency explicitly — the
step that must complete before the next begins; for validation list 2+ probes or
thresholds (a validation that asks "did the deployment succeed?" names no probe or
threshold and does not qualify); for rollback cover exactly three labeled components
in order — trigger (what condition initiates rollback), steps (what you undo and in
what order), verify (how you confirm rollback succeeded). Per phase name one gap and
its remedy. Close with a cross-phase gap table (Phase, Gap, Severity, Why) — compare
each gap against the others before assigning Severity; name at least one automation
hook.
```

---

## V-04

**Axes combined**: Front-loaded gap table (C-14 probe) + bare interrogative phase headers (C-21/C-26 probe), standard density, dual disqualifiers
**Hypothesis**: Combining V-01's front-loaded gap table with V-02's interrogative headers in a single prose prompt probes C-14, C-21, and C-26 jointly. If all three activate alongside C-15, prose ceiling rises by 15 pts; the key interaction risk is that the front-loaded gap table may block C-15 (apparatus exclusion), which would cap the gain at C-21 + C-26 only. This is the maximum-ambition standard-density test for the prose path toward the template ceiling.
**Predicted score range**: 150 (no new criteria activate) → 160 (C-21 + C-26 activate, C-15 survives) → 155 (C-14 activates, C-15 drops)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [what this team currently does — shared runbook, approval gates,
and deployment sequence as practiced].
Known failure mode: [the recurring failure — the check or step that gets skipped and
what it costs].

Before tracing any phase, write your gap table now. Four columns: Phase | Gap |
Severity (critical / moderate / low) | Why. Print the header row; leave all data rows
blank. Do not pre-fill. Return to fill it only after all four phases are complete;
compare every gap against the others before assigning Severity.

what needs to be true before we touch this?
List at least 3 pre-deploy checks. For each, name the specific condition being
verified and what failure looks like. "'Verify the environment is stable' names no
specific condition and does not qualify."

what's the deployment order?
List at least 4 steps in execution order. Call out at least one ordering dependency —
the step that must complete before the next can begin and what breaks if it does not.

did it land?
List at least 2 post-deploy validation actions. Each must name a probe, threshold, or
data-integrity assertion. "A validation that asks 'is the catalog sync current?' names
no probe or threshold and does not qualify."

what do we do if it didn't?
State the rollback trigger, at least one undo step, and how to verify rollback
succeeded.

Return to the gap table. Fill one row per phase. State what should be added or
changed — naming a gap without a remedy does not qualify. Identify at least one
automation hook.
```

---

## V-05

**Axes combined**: Interrogative phase prompts embedded in compressed paragraph (C-17/C-32 path) + three-field rollback (C-27 probe) + dual disqualifiers
**Hypothesis**: Embedding interrogative phase anchors *inline* within a compressed instruction paragraph (not as standalone headers) tests the exact boundary of C-21/C-26: if the header text must appear as a standalone line, inline embedding fails C-21/C-26 but preserves C-17; if any interrogative phase phrasing activates C-21/C-26 regardless of line position, the prose-compressed path gains +10. Combined with the three-field rollback probe, maximum possible score is 175/210 — though the compression/standalone-header incompatibility is the expected discriminator between V-05 and V-02.
**Predicted score if inline embedding fails C-21/C-26**: 160 + C-27-delta (same as R15 V-03 ± 5)
**Predicted score if inline embedding passes C-21/C-26**: 175/210 (new prose ceiling)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [what this team currently does — checklist, sequence, approval gates
as practiced].
Known failure mode: [the recurring failure — what gets skipped and what it costs].

Trace {{TOPIC}}'s deployment by answering four phase prompts in sequence — each answer
in prose: "what needs to be true before we touch this?" — list 3+ checks, each naming
the specific condition and failure mode ("ensure services are available" names no
condition; does not qualify); "what's the deployment order?" — list 4+ ordered steps
and name one ordering dependency explicitly; "did it land?" — list 2+ probes or
thresholds (a validation that asks "did the deployment succeed?" names no probe; does
not qualify); "what do we do if it didn't?" — cover exactly three labeled components:
trigger (what initiates rollback), steps (what you undo and in what order), verify
(how you confirm rollback succeeded). Per phase name one gap and its remedy. Close
with a cross-phase gap table (Phase, Gap, Severity, Why) — compare before assigning
Severity; name at least one automation hook.
```

---

## R16 discriminating questions

| Question | Test | Verdict available from |
|----------|------|------------------------|
| Is C-14 mutually exclusive with C-15 on the prose path? | V-01 | C-14 result in V-01 |
| Do interrogative headers activate C-21/C-26 on the prose path? | V-02 | C-21/C-26 result in V-02 |
| Is C-27 template-exclusive or semantic? | V-03 | C-27 result in V-03 |
| Do C-14 + C-21/C-26 compound or interfere in prose? | V-04 | C-14 × C-21/C-26 interaction |
| Are standalone headers required for C-21/C-26, or does inline suffice? | V-02 vs V-05 | Δ between V-02 and V-05 on C-21/C-26 |

**Prose ceiling sensitivity** (if all probes succeed):

| New criteria | Added pts | Projected ceiling |
|---|---|---|
| C-27 only | +5 | 165/210 — ties template |
| C-21 + C-26 only | +10 | 170/210 — exceeds template |
| C-14 + C-15 intact | +5 | 165/210 |
| C-27 + C-21 + C-26 (compressed) | +15 | 175/210 |
