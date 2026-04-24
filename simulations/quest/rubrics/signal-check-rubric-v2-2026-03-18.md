The background check is stale — the file was empty when I read it, so I wrote it fresh. The v2 rubric is already in place at `simulations/quest/rubrics/signal-check-rubric-v2-2026-03-18.md`.
 Essential** — all must pass for the output to be a usable health report:

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

**5 Aspirational** — raise the bar once essentials are stable. C-09 and C-10 retained from v1; C-11 through C-13 added from R1 excellence signals:

| ID | Criterion | Source |
|----|-----------|--------|
| C-09 | Cross-dimension patterns named when a shared root cause exists | v1 |
| C-10 | Missing signals identified by namespace + specific skill | v1 |
| C-11 | All skill references use `/namespace:skill` format consistently | EX-01 |
| C-12 | A terminal MISSING SIGNAL GUIDE section collates all gaps | EX-02 |
| C-13 | Absent evidence is declared explicitly — no dimension silently omits | EX-03 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

All five must pass. A single essential failure disqualifies the output from gold regardless of composite score.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | All four dimensions present | completeness | Output contains all four named sections: SEQUENCE, COHERENCE, STALENESS, CAUSAL GAP — by name or equivalent heading. A report that omits any dimension entirely = FAIL. |
| C-02 | SEQUENCE grounded in artifact dates | correctness | SEQUENCE analysis either (a) cites specific artifact names and dates to establish the order, or (b) names this as an open gap when dates are unavailable or absent. Asserting an ordering without citing dates = FAIL. |
| C-03 | COHERENCE names specific agreements and contradictions | correctness | COHERENCE section names at least one specific signal pair that agrees or contradicts — with artifact names or signal types identified. Generic statements ("signals seem aligned") without named evidence = FAIL. |
| C-04 | CAUSAL GAP states mechanism evidence or absence | correctness | CAUSAL GAP section either (a) names the mechanism linking the feature to the claimed outcome and cites the signal that establishes it, or (b) explicitly names the gap ("no mechanism evidence found") as an open issue. Silence on mechanism = FAIL. |
| C-05 | Output register is coaching, not punitive | behavior | Each flagged issue is framed as something the team can decide to address — not as a blocking verdict or disqualifying failure. No dimension produces a pass/fail gate that prevents the user from proceeding. Advisory language throughout. |

---

### Recommended (C-06 to C-08)

Output is meaningfully better with all three. Absence degrades actionability.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | STALENESS applies a concrete threshold | depth | STALENESS analysis names a specific age cutoff (e.g., "signals older than 30 days in a fast-moving market") and applies it to the artifact inventory rather than describing staleness in relative or vague terms ("some signals may be dated"). Threshold may be calibrated from the inventory itself — but it must be named explicitly. |
| C-07 | Each flagged issue includes a next action | behavior | Every issue surfaced across all four dimensions includes a concrete next step the team can take (e.g., "run /discover:causal to establish mechanism evidence" or "refresh competitors signal — current one is 45 days old"). Issues without next actions = FAIL for this criterion. |
| C-08 | Report opens with a readiness summary | format | The first substantive section of the output is a readiness summary that states the overall signal health posture before any per-dimension analysis begins. Summary may be brief (2-4 sentences) but must precede the dimension breakdown. |

---

### Aspirational (C-09 to C-13)

These raise the bar once essential and recommended are stable. None are required for gold. C-09 and C-10 are retained from v1. C-11 through C-13 are new in v2, derived from R1 excellence signals.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimension patterns named when present | depth | When two or more dimensions share a common root cause (e.g., a SEQUENCE gap in discovery also explains a CAUSAL GAP — the team specified before gathering mechanism evidence), the output names this as a pattern rather than reporting each dimension independently. Pattern naming is optional when no cross-dimension link exists. |
| C-10 | Missing signals identified by namespace + skill | coverage | For each gap identified, the output names the specific signal skill that would close it (e.g., "CAUSAL GAP: run /discover:causal; STALENESS on competitors: run /discover:competitors"). Identification is by namespace and skill, not just by dimension name. |
| C-11 | All skill references use `/namespace:skill` format | format | Every skill reference in the output — whether in action fields, next steps, or a closing guide — uses the explicit `/namespace:skill` format. Bare skill names (e.g., "discover-causal" without the slash and namespace) or vague prompts ("run the relevant discover skill") = FAIL. Derived from EX-01: C-10 is a format threshold, not a depth threshold. Skill awareness without format enforcement does not satisfy the criterion. |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | structure | The output includes a dedicated final section — a MISSING SIGNAL GUIDE or equivalent — that collates every flagged gap across all four dimensions into a single terminal list. Each line specifies one gap and the `/namespace:skill` to close it. This section provides structural redundancy over per-dimension action fields: both must be present for C-12 to pass. Derived from EX-02: the guide simultaneously satisfies C-07 (next action present) and C-10 (namespace + skill named) for every gap, making omission of either a visible structural failure. |
| C-13 | Absent evidence declared explicitly — no silent omissions | correctness | For every dimension where the relevant evidence is absent or unavailable, the output uses explicit absence language (e.g., "no mechanism evidence found — the causal gap is open", "no artifact dates available — ordering cannot be established"). A dimension that returns no finding when evidence is missing — without stating the absence — = FAIL. Derived from EX-03: single-axis scores exceeded design estimates because explicit prohibition patterns ("silence does not pass", "do not assert order without dates") prevent analysis drift under minimal-inventory conditions. The output criterion mirrors the design principle: absence must be named, not left blank. |

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

| Tier | Criteria | Weight | Points each |
|------|----------|--------|-------------|
| Essential | 5 | 60 pts total | 12 pts |
| Recommended | 3 | 30 pts total | 10 pts |
| Aspirational | 5 | 10 pts total | 2 pts |

### Score Examples

| Essential | Recommended | Aspirational | Composite | Gold? |
|-----------|-------------|--------------|-----------|-------|
| 5/5 | 3/3 | 5/5 | 100 | YES |
| 5/5 | 3/3 | 3/5 | 96 | YES |
| 5/5 | 3/3 | 0/5 | 90 | YES |
| 5/5 | 2/3 | 5/5 | 90 | YES |
| 5/5 | 1/3 | 5/5 | 80 | YES (boundary) |
| 5/5 | 0/3 | 5/5 | 70 | NO |
| 4/5 | 3/3 | 5/5 | 88 | NO (essential fail) |

**Note on R1 scores under v2**: V-01/V-02/V-03 scored 95 under v1 (5/5 essential, 3/3 recommended, 1/2 aspirational). Under v2 the denominator changes from /2 to /5 and C-11 through C-13 add new criteria. V-04/V-05 (which had MISSING SIGNAL GUIDE sections with explicit /namespace:skill format) gain partial credit on C-11 and C-12; C-13 requires runtime evidence. The expanded aspirational tier creates headroom that design-level scoring alone cannot fill.

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

**Why C-11 is separate from C-10 (v2):** C-10 tests whether namespace + skill are
*present* in the output. C-11 tests whether every skill reference uses the
`/namespace:skill` *format* consistently — including in places outside the dedicated
gap guide (action fields, readiness summary, inline recommendations). A report can pass
C-10 (guide exists with correct format) while failing C-11 (inline references use bare
skill names). The distinction is precision of format enforcement across the full output.

**Why C-12 adds value over C-07 (v2):** C-07 requires a next action per flagged issue.
C-12 requires a *collated terminal section* that lists all gaps in one place. The terminal
guide provides structural redundancy: if a per-dimension action field is missing, the guide
makes the omission visible. If the guide is missing, per-dimension fields are still required
by C-07. Both must be present for C-12 to pass. This mirrors the EX-02 finding: the guide
upgrades C-07 compliance from instructed to structurally enforced.

**Why C-13 is aspirational rather than essential (v2):** Explicit absence declarations are
already partially covered by C-04 (CAUSAL GAP must name "no mechanism evidence found") and
C-02 (SEQUENCE must name "ordering cannot be established" when dates are absent). C-13
generalizes this pattern across all four dimensions and to all evidence types — a broader
contract than the essential criteria impose. At the aspirational tier it rewards outputs
that apply the explicit-absence discipline system-wide without requiring it as a gate.
