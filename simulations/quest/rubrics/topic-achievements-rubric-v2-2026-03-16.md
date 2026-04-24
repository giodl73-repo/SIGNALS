Written to `simulations/quest/rubrics/topic-achievements-rubric-v2-2026-03-16.md`.

---

**What changed from v1 to v2:**

Three new aspirational criteria extracted from V-04's 100-point performance:

**C-11 — Synthesis precedes category detail** (`architecture`)
V-01 and V-03 got PARTIAL on C-09 not because synthesis was absent but because it was fragmented into per-category sentences. V-04 put a single integrated synthesis *before* the enumeration. C-09 and C-11 are now deliberately separate: C-09 tests *existence*, C-11 tests *position*.

**C-12 — Rules enforced by consequence** (`rigor`)
V-04 was the only variation to say "no date = not earned" and "no ratio = rewrite as LOCKED." Advisory wording ("include a date") can be silently ignored; consequence-backed wording cannot. This criterion rewards prompt designs that make compliance structurally difficult to violate.

**C-13 — Falsified structurally isolated from the category loop** (`architecture`)
V-04 gave Falsified its own dedicated step outside the general 7-category iteration. All other variations embedded it within the chain category. Structural isolation means it cannot be skipped or abbreviated when the model is in enumeration mode.

**Scoring formula updated:** aspirational denominator changes from `/2` to `/5` (total stays 10 pts). Falsified now has three criteria total (C-02, C-10, C-13) — presence, framing, isolation.
namespace, skill, or artifact name), not invented placeholders. Locked achievements may reference artifact count targets. | correctness | At least one earned or in-progress achievement cites a specific artifact, namespace, or artifact count derived from the scan. |
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
| C-09 | **Achievement narrative coherence** — the output contains a 1-3 sentence synthesis of what the achievement picture says about topic maturity (e.g., "Strong on exploration, weak on chain — no hypothesis has been falsified yet"). A flat checklist without narrative fails. | depth | A summary sentence or paragraph interpreting the overall achievement state is present and specific to the topic. |
| C-10 | **Falsified framed as positive signal** — the Falsified achievement description explicitly frames falsification as intellectual honesty and a sign of rigorous investigation, not as a failure or negative outcome. | behavior | The Falsified entry uses positive framing (e.g., "rewarded for retracting...", "signals honest inquiry") rather than neutral or negative language. |
| C-11 | **Synthesis precedes category detail** — the maturity synthesis (C-09) appears as an *opening* interpretive frame before the per-category enumeration, not as a closing afterthought. Per-category sentences do not substitute for this: they may supplement it but cannot replace a prior integrated read. | architecture | A synthesis paragraph or block appears before the first category section; per-category interpretation alone fails this criterion even if C-09 passes. |
| C-12 | **Rules enforced by consequence** — state classification rules are backed by explicit consequences stating what to do when a rule is broken (e.g., "no artifact citation = demote to locked", "no ratio = rewrite as locked"), not just positive requirements. Self-enforcing rules prevent silent omissions. | rigor | At least two classification rules carry an explicit "if not present, then..." or equivalent enforcement clause; advisory-only wording fails. |
| C-13 | **Falsified structurally isolated from the category loop** — the Falsified achievement is handled in its own dedicated section or step, separate from the general per-category enumeration, so it cannot be skipped, abbreviated, or absorbed when iterating through the 7 categories. | architecture | Falsified appears under its own heading or in a section explicitly labeled for it, outside the general category table or loop; appearing only as one row within the chain category block fails. |

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
| Gold | >= 80, all essential | Output is trustworthy and complete |
| Silver | >= 60, all essential | Usable but missing recommended polish |
| Bronze | >= 40, some essential | Partial — achievement scan present but gaps |
| Fail | any essential fails | Output cannot be trusted as-is |

---

## Criterion Lineage

| ID | Source | Round introduced |
|----|--------|-----------------|
| C-01 through C-10 | v1 rubric | — |
| C-11 | V-04 excellence signal: synthesis-first ordering | R1 |
| C-12 | V-04 excellence signal: enforcement via consequence | R1 |
| C-13 | V-04 excellence signal: Falsified dedicated step | R1 |

---

## Usage Notes

- Run against the full `/topic-achievements` output for a topic that has at least 3 signal artifacts.
- If no artifacts exist for the topic, only C-05 (next action) and C-02 (Falsified entry) are scoreable; defer full rubric scoring until artifacts exist.
- The Falsified achievement (C-02, C-10, C-13) now has three criteria touching it because it is the most important signal of intellectual honesty in the plugin — presence, framing, and structural isolation each warrant independent scrutiny.
- C-11 and C-09 are related but distinct: C-09 asks whether synthesis exists; C-11 asks whether it leads. A variation can pass C-09 and fail C-11 (synthesis present but buried at the end).
- C-12 rewards prompt designs that make correctness structurally difficult to violate, not just instructed. Advisory-only wording ("include a date") passes C-07; consequence-backed wording ("no date = not earned") is needed for C-12.
