---
skill: quest-rubric
skill_target: topic-achievements
date: 2026-03-16
version: 1
---

# Scoring Rubric — topic-achievements

Evaluates output from `/topic-achievements` (or the achievements section within `/topic-status`).
The skill scans signal artifacts for a topic and classifies achievements as earned, in-progress, or locked.

---

## Criteria

### Essential (60 pts total — all must pass)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Achievement state classification** — every achievement in the output must be assigned exactly one state: earned, in-progress, or locked. No achievement may be left unclassified or assigned multiple states. | correctness | All achievements carry one of {earned, in-progress, locked}; zero unclassified entries. |
| C-02 | **Falsified achievement treated distinctly** — the Falsified achievement must appear in its own named entry and be distinguished from other achievements, reflecting that it rewards intellectual honesty rather than artifact volume. | correctness | A named "Falsified" entry exists and its description or framing distinguishes it (e.g., notes it rewards honesty, surfaces when a hypothesis was retracted/amended). |
| C-03 | **Artifact-grounded output** — earned and in-progress states must cite evidence from actual signal artifacts (namespace, skill, or artifact name), not invented placeholders. Locked achievements may reference artifact count targets. | correctness | At least one earned or in-progress achievement cites a specific artifact, namespace, or artifact count derived from the scan. |
| C-04 | **In-progress achievements show quantified progress** — any achievement classified as in-progress must include a numeric or ratio indicator of how close (e.g., "3 of 5 namespaces covered", "2 of 3 required"). | depth | Every in-progress entry contains a numeric progress indicator; "almost there" or similar vague language alone fails. |
| C-05 | **Next recommended action present** — the output concludes with at least one concrete recommended next action that would advance the topic's achievement state. | behavior | A clearly labeled "next action" (or equivalent heading) is present and actionable (names a specific skill, artifact type, or step). |

---

### Recommended (30 pts total — output is better with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **All 7 categories represented** — the output organizes achievements under all seven named categories: exploration, depth, coverage, quality, chain, discovery, corps/crew. Missing categories must be explicitly noted as "no achievements yet" rather than silently omitted. | coverage | All 7 category labels appear in the output; absent-category sections say so explicitly. |
| C-07 | **Earned achievements carry dates** — every earned achievement includes the date it was earned, enabling traceability to the artifact scan. | format | All earned entries include a date (ISO or relative); entries without dates fail this criterion. |
| C-08 | **Locked achievements state unlock conditions** — each locked achievement specifies what still needs to happen (artifact type, count, or action) rather than just showing a lock symbol. | depth | Every locked entry includes at least one concrete unlock condition. |

---

### Aspirational (10 pts total — raise the bar once essential/recommended are stable)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Achievement narrative coherence** — the output concludes with or opens with a 1–3 sentence synthesis of what the achievement picture says about topic maturity (e.g., "Strong on exploration, weak on chain — no hypothesis has been falsified yet"). A flat checklist without narrative fails. | depth | A summary sentence or paragraph interpreting the overall achievement state is present and specific to the topic. |
| C-10 | **Falsified framed as positive signal** — the Falsified achievement description explicitly frames falsification as intellectual honesty and a sign of rigorous investigation, not as a failure or negative outcome. | behavior | The Falsified entry uses positive framing (e.g., "rewarded for retracting…", "signals honest inquiry") rather than neutral or negative language. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential | Output is trustworthy and complete |
| Silver | >= 60, all essential | Usable but missing recommended polish |
| Bronze | >= 40, some essential | Partial — achievement scan present but gaps |
| Fail | any essential fails | Output cannot be trusted as-is |

---

## Usage Notes

- Run against the full `/topic-achievements` output for a topic that has at least 3 signal artifacts.
- If no artifacts exist for the topic, only C-05 (next action) and C-02 (Falsified entry) are scoreable; defer full rubric scoring until artifacts exist.
- The Falsified achievement (C-02, C-10) has two criteria touching it because it is the most important signal of intellectual honesty in the plugin — it warrants extra scrutiny.
