# /quest:score — org-committee — Round 1

## Evaluation

---

### V-01 — Challenger-First Order

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | "Identify the committee type: ROB, shiproom, or arch-board" — explicit in Step 1 |
| C-02 | PASS | "Read the charter files from `.roles/`. Load every participant named in the charter." Graceful fallback with disclosure. |
| C-03 | PASS | Fixed sequence with role orientations defined: inertia-advocate (status-quo/switching cost), architect (structure/risk), PM (evidence/responds to concerns already raised). Role-blind statements explicitly excluded. |
| C-04 | PASS | Step 4 names exactly three sections with explicit headings: Decisions, Action Items, Dissenting Opinions |
| C-05 | PASS | "At least one participant must raise a challenge, block, or condition. A simulation where everyone approves without friction is a failed simulation." |
| C-06 | PASS | "Every statement must reference the specific agenda item, not generic committee boilerplate. Role-blind statements ('this needs more work') fail." |
| C-07 | PASS | "Each item must name the responsible role and describe a concrete deliverable — not 'investigate further.'" |
| C-08 | PASS | "For each dissent, include the condition under which the dissenter would change their position." |
| C-09 | PARTIAL | Challenger-first ordering structurally prevents optimistic anchoring — a process mechanism for surprise, but no explicit instruction to surface something the user hadn't anticipated. |
| C-10 | PASS | Explicit Verdict line with re-entry path required for non-approved outcomes. |

**Score**: essential 5/5 → 60, recommended 3/3 → 30, aspirational 1.5/2 → 7.5
**Composite: 97.5**

---

### V-02 — Scorecard Table First

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | "committee type the user has requested (ROB, shiproom, or arch-board)" |
| C-02 | PASS | "Read `.roles/`... Load every named participant. If no charter exists, fall back to default Signal roles and disclose the fallback." |
| C-03 | PASS | "Run each participant through their role lens... apply their documented role orientation (PM = evidence/adoption, architect = structure/risk, inertia-advocate = status-quo defense)." |
| C-04 | PASS | Part 3 has Decisions, Action Items, Dissenting Opinions as named sections |
| C-05 | PASS | "At least one participant must raise a challenge, block, or condition. A simulation where everyone approves without friction is a failed simulation." |
| C-06 | PASS | Scorecard table forces per-participant position declaration anchored to the agenda item before prose begins; "no new positions should appear in prose that weren't telegraphed in the scorecard." |
| C-07 | PASS | "Each item: owner (by role name) + concrete deliverable. No unowned items. No vague items." |
| C-08 | PASS | "Each dissent: what the dissenter said, and what condition would resolve it." |
| C-09 | PARTIAL | Scorecard-first format enforces upfront stance commitment and prevents softening in prose — a discipline mechanism, not a content-seeking mechanism. No explicit instruction to find non-obvious concerns. |
| C-10 | PASS | Explicit `**Re-entry path**` field required when verdict is not Approved. |

**Score**: essential 5/5 → 60, recommended 3/3 → 30, aspirational 1.5/2 → 7.5
**Composite: 97.5**

---

### V-03 — Inertia Framing (Status-Quo as Named Antagonist)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | "charter matching the requested committee type (ROB, shiproom, arch-board)" |
| C-02 | PASS | "Load named participants. Fall back to default Signal roles if no charter is found, and disclose that you did." |
| C-03 | PASS | Each role defined with concrete lens: inertia-advocate from Current System Brief, architect checks contracts/namespace, PM responds to inertia-advocate's specific concerns — not a clean room. |
| C-04 | PASS | Decisions, Action Items, Dissenting Opinions, Verdict — all four sections present and named. |
| C-05 | PASS | "At least one participant must challenge, block, or condition their approval. A rubber-stamp simulation failed to simulate." |
| C-06 | PASS | Current System Brief step forces the simulation to ground switching-cost claims in the specific agenda item. Inertia-advocate must use "specific switching costs, not generic resistance." |
| C-07 | PASS | "Owner (by name from charter) + concrete deliverable. No vague items." |
| C-08 | PASS | "Every block or condition, with the resolution path: what would have to be true for the dissenter to approve?" |
| C-09 | **PASS** | Step 1 explicitly asks "What workflows, habits, or integrations depend on the current behavior? What is the switching cost?" — this is a content-seeking mechanism aimed at uncovering concerns the proposer has not yet articulated. Quality bar note seals it: "A good simulation of this kind leaves the user with at least one concern they had not already identified." |
| C-10 | PASS | Verdict + Re-entry path explicitly required and templated. |

**Score**: essential 5/5 → 60, recommended 3/3 → 30, aspirational 2/2 → 10
**Composite: 100**

---

### V-04 — Conversational + Phase Markers (Incomplete)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | PHASE 0 identifies committee type explicitly |
| C-02 | PASS | "open `.roles/` and load the charter... If the charter doesn't exist, use Signal's default roles and say so." |
| C-03 | FAIL | Prompt is truncated before the simulation phase — no role lens enforcement visible |
| C-04 | FAIL | Truncated — three required sections cannot be confirmed |
| C-05 | FAIL | Truncated — anti-rubber-stamp constraint cannot be confirmed |
| C-06 | FAIL | Truncated |
| C-07 | FAIL | Truncated |
| C-08 | FAIL | Truncated |
| C-09 | FAIL | Truncated |
| C-10 | FAIL | Truncated |

**Score**: essential 2/5 → 24, recommended 0/3 → 0, aspirational 0/2 → 0
**Composite: 24 — FAILING**

Note: PHASE 0 setup is well-structured and the conversational register reads cleanly. The approach has merit — the failure is submission quality, not concept quality.

---

## Rankings

| Rank | Variation | Score | Essential | Band |
|------|-----------|-------|-----------|------|
| 1 | V-03 Inertia Framing | 100 | 5/5 | Golden |
| 2 | V-01 Challenger-First | 97.5 | 5/5 | Golden |
| 3 | V-02 Scorecard Table | 97.5 | 5/5 | Golden |
| 4 | V-04 Phase Markers | 24 | 2/5 | Failing |

V-01 and V-02 are tied at 97.5. The tiebreaker favors V-01 slightly — challenger-first ordering is a process mechanism with direct consequences on what gets surfaced (anchoring effects), whereas the scorecard format in V-02 is a discipline mechanism that prevents drift but doesn't change what the simulation discovers.

---

## Excellence Signals from V-03

Three patterns made V-03 the only variation to achieve C-09:

1. **Pre-simulation context anchoring**: The "Current System Brief" step forces the model to characterize the current system before any participant speaks. This makes all subsequent discussion grounded in concrete stakes rather than abstract risk.

2. **Named-harm requirement for blocks**: "The inertia-advocate's block or condition must name the concrete harm that would occur if the current system is displaced." This converts generic resistance into falsifiable claims — and falsifiable claims surface surprises.

3. **Explicit simulation-failure definition**: The quality bar paragraph names what a bad simulation looks like ("If the minutes read like a pre-written approval, the simulation did not work"). This is a behavioral instruction, not just a rubric note — it trains the model to self-audit before finishing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-simulation-current-system-brief", "named-harm-requirement-for-blocks", "explicit-simulation-failure-definition"]}
```
