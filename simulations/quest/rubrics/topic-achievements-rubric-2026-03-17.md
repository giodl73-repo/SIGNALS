# Rubric — topic-achievements v2 (2026-03-17)

Evaluates the output of a `/topic-achievements` skill invocation. Score each criterion PASS or FAIL, then apply the scoring formula.

---

## Criteria

### Essential (60 pts total — output cannot be trusted without these)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **One state per achievement** — every achievement in the output carries exactly one state: EARNED, IN-PROGRESS, or LOCKED. Dual states, ambiguous states ("EARNED/IN-PROGRESS"), or missing states fail this criterion. | essential | correctness | Every achievement entry has exactly one state value; no entry is missing a state or carries two. |
| C-02 | **Falsified is named as an honesty signal** — a named "Falsified" entry exists in the output and its text distinguishes it as an intellectual-honesty signal, not merely a volume or count signal. An entry that says only "hypothesis not proven" without framing it as an honesty achievement fails. | essential | correctness | A named "Falsified" entry exists in the output; its text references honesty, retraction, or belief update — not just artifact count. |
| C-03 | **Artifact-grounded classification** — EARNED and IN-PROGRESS states must cite evidence from actual signal artifacts (namespace, skill name, or artifact name) found during the glob scan, not invented placeholders. LOCKED entries may reference targets without existing artifacts. | essential | correctness | At least one EARNED or IN-PROGRESS entry cites a specific artifact, namespace, or scan-derived artifact count. No invented artifact names appear. |
| C-04 | **In-progress achievements show numeric progress** — any IN-PROGRESS entry must include a ratio or count indicator (e.g., "3 of 5 namespaces covered"). Vague qualifiers ("almost there", "partially done") alone fail this criterion. | essential | depth | Every IN-PROGRESS entry contains a numeric ratio or count; vague-only language fails. |
| C-05 | **Next recommended action is present and specific** — the output includes at least one concrete next-action recommendation that names a skill to invoke, an artifact type it would produce, or a step to take. A generic "add more artifacts" instruction fails. | essential | behavior | A labeled next-action block exists and names a specific skill, artifact type, or action step. |

---

### Recommended (30 pts total — output is better with these)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **All 7 categories represented** — the output classifies achievements under all seven named categories: exploration, depth, coverage, quality, chain, discovery, corps/crew. Categories with nothing to show must appear with an explicit "no achievements yet" note rather than being silently omitted. | recommended | coverage | All 7 category labels appear in the output; any category without achievements states so explicitly. |
| C-07 | **Earned achievements carry dates** — every EARNED entry includes the date it was earned, enabling traceability back to the artifact scan. An EARNED entry without a date is evidence of an unverified claim. | recommended | format | Every EARNED entry includes a date (ISO or relative); entries without dates fail this criterion. |
| C-08 | **Locked achievements state unlock conditions** — each LOCKED entry specifies what must happen to unlock it: which artifact type, what count, or what action. A bare lock symbol or "not yet earned" with no path forward fails. | recommended | depth | Every LOCKED entry includes at least one concrete unlock condition. |

---

### Aspirational (10 pts total — raise the bar once essential/recommended are stable)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Maturity synthesis before classification** — the output opens with or precedes all per-category detail with a 1-3 sentence interpretation of what the overall achievement picture says about topic maturity (e.g., "Strong on exploration, no chain signal yet, Falsified not earned — investigation is broad but shallow"). A flat list without framing narrative fails. | aspirational | depth | A summary paragraph interpreting the overall achievement state is present and appears before (or at the opening of) the per-category detail. |
| C-10 | **Falsified framed as a positive signal** — the Falsified entry explicitly uses positive framing: earning it is a mark of rigorous inquiry, not a mark of failure. Neutral language ("hypothesis not confirmed") or negative framing ("failed hypothesis") fails. If Falsified is LOCKED, the entry frames it as an open invitation rather than a deficit. | aspirational | behavior | The Falsified entry uses explicitly positive language (e.g., "intellectual honesty", "followed the evidence", "rewarded for retracting", "open invitation"); neutral or negative framing fails. |
| C-11 | **State-column isolation** — state values appear in a dedicated structural position (table column, labeled field, or equivalent) that makes one-state-per-achievement verifiable by scanning a single axis without parsing prose sentences. An output that embeds state in running text (e.g., "this achievement is EARNED based on…") passes C-01 but fails C-11. Structural placement does the validation work so the reader does not have to. | aspirational | format | State values occupy a dedicated column, field label, or structural slot; prose-embedded states fail regardless of C-01 status. |
| C-12 | **Synthesis placement boundary** — the maturity synthesis paragraph is positioned strictly before the per-category classification begins — not after, not as a closing reflection. "Before the first category entry" is the only acceptable position. A synthesis that appears after the per-category detail, even if it is substantive and passes C-09, fails C-12. A placement rule is stronger than a presence rule: it prevents the most common degradation (synthesis becoming an afterthought). | aspirational | depth | The maturity synthesis paragraph appears before the first category entry; placement after per-category detail fails. |
| C-13 | **Hallucination-safe evidence fallback** — when artifact evidence is uncertain, the output degrades gracefully to namespace-level citation rather than fabricating artifact names. The output never invents artifact names to satisfy citation requirements; uncertain evidence is expressed as "namespace: flow" or equivalent rather than a specific but non-existent artifact. This is a stricter complement to C-03: C-03 catches fabricated names that appear; C-13 rewards the positive behavior of graceful degradation when the model is unsure. | aspirational | correctness | No invented artifact names appear under uncertainty; uncertain evidence uses namespace or skill as the safe floor citation. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Output is trustworthy and complete |
| Silver | >= 60, all essential pass | Usable but missing recommended polish |
| Bronze | >= 40, some essential pass | Achievement scan present but gaps |
| Fail | any essential fails | Output cannot be trusted as-is |

---

## Usage Notes

- Run against a `/topic-achievements` output for a topic with at least 3 signal artifacts. If fewer than 3 artifacts exist, only C-02, C-05, and C-10 are fully scoreable — defer complete rubric scoring until artifacts exist.
- C-02 and C-10 both target Falsified. This is intentional: Falsified is the most important achievement in the plugin and warrants two independent checks (presence/naming and framing quality).
- C-03 guards against hallucination: if an output earns achievements citing artifacts that do not exist in the glob result, C-03 fails regardless of structural quality.
- C-11, C-12, and C-13 were promoted to aspirational in v2 based on excellence signals from the R1 quest cycle (2026-03-17). C-11 rewards structural state isolation (validated by V-02's table-column pattern scoring 100). C-12 strengthens C-09 with a placement boundary rather than mere presence (V-01 failed C-09 by placing synthesis after classification; V-02 passed by specifying "before or immediately after — not buried at the end"). C-13 rewards graceful evidence degradation (V-02's "cite namespace only if unsure" escape hatch prevents forced hallucination without silencing the model).
- **Known growth criteria** (candidates for v3): (a) consequence-backed classification rules — every rule should carry a demotion clause so advisory instructions cannot be silently ignored; (b) Falsified structural isolation as an essential criterion — Falsified should appear as a dedicated step outside the 7-category enumeration loop to prevent compression when the model is in list-completion mode. Both patterns were validated in R1/R2 quest cycles on 2026-03-16.
