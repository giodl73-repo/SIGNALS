**`simulations/quest/rubrics/signal-check-rubric-2026-03-18.md`** — written.

---

## Rubric Summary

**5 Essential** — all must pass for the output to be a usable health report:

| ID | Criterion |
|----|-----------|
| C-01 | All four dimensions present (SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP) |
| C-02 | SEQUENCE grounded in artifact dates, not assumed ordering |
| C-03 | COHERENCE names specific signal pairs — not generic "seems aligned" |
| C-04 | CAUSAL GAP states mechanism evidence or explicitly names the absence |
| C-05 | Advisory/coaching register throughout — no blocking verdicts |

**3 Recommended** — meaningfully better with all three:

| ID | Criterion |
|----|-----------|
| C-06 | STALENESS applies a named, concrete age threshold |
| C-07 | Every flagged issue includes a next action |
| C-08 | Report opens with a readiness summary before dimension analysis |

**2 Aspirational** — raise the bar once essentials are stable:

| ID | Criterion |
|----|-----------|
| C-09 | Cross-dimension patterns named when a shared root cause exists |
| C-10 | Missing signals identified by namespace + specific skill |

**Golden threshold**: all 5 essential pass + composite ≥ 80.
exist, SEQUENCE section names this explicitly as an open gap rather than asserting an order. |
| C-03 | COHERENCE names specific agreements and contradictions | correctness | COHERENCE section names at least one specific signal pair that agrees or contradicts — with artifact names or signal types identified. Generic statements ("signals seem aligned") without named evidence = FAIL. |
| C-04 | CAUSAL GAP states mechanism evidence or absence | correctness | CAUSAL GAP section either (a) names the mechanism linking the feature to the claimed outcome and cites the signal that establishes it, or (b) explicitly names the gap ("no mechanism evidence found") as an open issue. Silence on mechanism = FAIL. |
| C-05 | Output register is coaching, not punitive | behavior | Each flagged issue is framed as something the team can decide to address — not as a blocking verdict or disqualifying failure. No dimension produces a pass/fail gate that prevents the user from proceeding. Advisory language throughout. |

---

### Recommended (C-06 to C-08)

Output is meaningfully better with all three. Absence degrades actionability.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | STALENESS applies a concrete threshold | depth | STALENESS analysis names a specific age cutoff (e.g., "signals older than 30 days in a fast-moving market") and applies it to the artifact inventory rather than describing staleness in relative or vague terms ("some signals may be dated"). Threshold may be calibrated from the inventory itself — but it must be named explicitly. |
| C-07 | Each flagged issue includes a next action | behavior | Every issue surfaced across all four dimensions includes a concrete next step the team can take (e.g., "run /discover-causal to establish mechanism evidence" or "refresh competitors signal — current one is 45 days old"). Issues without next actions = FAIL for this criterion. |
| C-08 | Report opens with a readiness summary | format | The first substantive section of the output is a readiness summary that states the overall signal health posture before any per-dimension analysis begins. Summary may be brief (2-4 sentences) but must precede the dimension breakdown. |

---

### Aspirational (C-09 to C-10)

These raise the bar once essential and recommended are stable. Neither is required for gold.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimension patterns named when present | depth | When two or more dimensions share a common root cause (e.g., a SEQUENCE gap in discovery also explains a CAUSAL GAP — the team specified before gathering mechanism evidence), the output names this as a pattern rather than reporting each dimension independently. Pattern naming is optional when no cross-dimension link exists. |
| C-10 | Missing signal types identified by namespace | coverage | For each gap identified, the output names the specific signal skill that would close it (e.g., "CAUSAL GAP: run /discover-causal; STALENESS on competitors: run /discover-competitors"). Identification is by namespace and skill, not just by dimension name. |

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

| Tier | Weight | Max contribution |
|------|--------|-----------------|
| Essential (5 criteria) | 60 pts | 12 pts each |
| Recommended (3 criteria) | 30 pts | 10 pts each |
| Aspirational (2 criteria) | 10 pts | 5 pts each |

### Score Examples

| Essential | Recommended | Aspirational | Composite | Gold? |
|-----------|-------------|--------------|-----------|-------|
| 5/5 | 3/3 | 2/2 | 100 | YES |
| 5/5 | 3/3 | 0/2 | 90 | YES |
| 5/5 | 2/3 | 2/2 | 80 | YES (boundary) |
| 5/5 | 1/3 | 2/2 | 80 | YES (boundary) |
| 4/5 | 3/3 | 2/2 | 88 | NO (essential fail) |
| 5/5 | 0/3 | 0/2 | 60 | NO |

---

## Design Notes

**Why SEQUENCE requires artifact dates (C-02):** A model that claims discovery preceded
specification without citing dated artifacts is asserting order from inference. The value
of SEQUENCE is catching cases where the dates *don't* support the claimed order. Date-free
SEQUENCE analysis cannot catch this.

**Why CAUSAL GAP requires naming mechanism or gap explicitly (C-04):** The causal mechanism
is the hardest thing to surface because it is never in a single artifact — it must be
assembled across signals. Silence means the dimension was skipped, not that the mechanism
was established.

**Why register matters (C-05):** Signal-check is explicitly described as "not punitive."
A health report that blocks decisions or issues verdicts defeats the coaching intent. The
skill is positioned as something to run *before* committing — the team should leave with
a clear view of what they know and what they are deciding to do despite gaps, not a
gatekeeper that overrides their judgment.

**Why C-09/C-10 are aspirational:** Cross-dimension pattern naming requires synthesis
beyond per-dimension analysis. Namespace-specific gap identification requires knowing the
skill catalog. Both are high-value outputs but impose overhead that is not essential for a
correct, actionable report.
