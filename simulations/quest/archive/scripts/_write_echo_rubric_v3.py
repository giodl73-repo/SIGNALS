OUT = r'C:\src\sim\simulations\quest\rubrics\topic-echo-rubric-v3-2026-03-16.md'

v3 = """---
skill: quest-rubric
skill_target: topic-echo
date: 2026-03-16
version: 3
prior_version: topic-echo-rubric-v2-2026-03-16.md
---

# topic-echo -- Scoring Rubric v3

## Skill Definition

`topic:echo` synthesizes unexpected findings after all essential signals are gathered.
It asks exactly one question: **"What did we learn that we did not expect?"**

It is not a summary of findings. It is a synthesis of surprises. Each surprise must be
named, traced to its source signal, and assessed for impact on the design direction.
The artifact is institutional memory -- written for the next team that walks this path,
not a retrospective for the team that just finished.

---

## What changed from v2

**Two new aspirational criteria (C-13, C-14):**

**C-13 -- Dual phase-locked pre-commitment integrity** (correctness)
Derived from V-05 Excellence Signal Pattern 1: "dual pre-commitment at structurally separate
lifecycle moments." C-11 tests that a PBI section exists and is addressable. C-12 tests that a
Handle Ledger exists and carries a portability test. C-13 tests that the two pre-commitments
are demonstrably independent -- that they were made with genuinely different information and
could not have been co-constructed. The evidence is in the content: PBI entries describe prior
domain beliefs using belief language; Handle Ledger titles name specific investigation findings
using finding language. Independence fails in two directions: (a) a PBI entry names a handle
label by its final form (the handle was predictable at PBI time, so both pre-commitments share
the same information); (b) a Handle Ledger title echoes PBI entry language verbatim (the handle
was constructed by inverting a prediction rather than naming a finding). C-13 is satisfiable
only if both C-11 and C-12 are satisfied first.

**C-14 -- Single-entry audit trail completeness** (behavior)
Derived from V-05 Excellence Signal Pattern 2: "C-11 and C-12 are structurally non-competing."
Because both C-11 (PBI citation per entry) and C-12 (Handle Ledger membership per entry) are
required, each surprise entry must point to three distinct artifacts: its handle in the Handle
Ledger, its prior belief in the PBI, and its source signal artifact. C-14 tests that all three
pointers appear in a single entry, making each surprise a fully self-contained citable unit. A
reviewer reading one entry should be able to verify the full chain -- handle in ledger, prior
belief in PBI, finding in signal set -- without navigating to other sections. An entry that
requires cross-referencing to reconstruct any pointer fails. This is the composition criterion:
C-11 and C-12 compose cleanly if and only if each entry carries all three pointers.

**Score model update:** Aspirational rises from 20 pts (4 criteria, 5 pts each) to 30 pts
(6 criteria, 5 pts each). Max composite rises from 110 to 120. Golden threshold unchanged
(all essential pass AND composite >= 80). Example calculations and golden path examples
updated to reflect 6 aspirational criteria.

**New relationship entries:** C-11 + C-12 -> C-13 (C-13 requires both; tests their
independence); C-13 + C-14 (C-14 is the composition test -- verifies that C-11 and C-12
combine into a per-entry audit chain, not just co-exist as separate sections).

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. If any essential criterion fails, the output is not useful.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Named surprises present** | correctness | At least one surprise is named as a discrete item. A surprise is not a finding -- it must be framed as something unexpected: the output must make clear what was anticipated and why the actual result departed from it. A list of findings without surprise framing fails this criterion entirely. NOT: "We found that X matters" (finding). PASS: "We expected X to be negligible; it turned out to dominate" (surprise). |
| C-02 | **Signal tracing per surprise** | correctness | Every named surprise is traced to a specific source signal or artifact by name. Generic attribution ("the evidence showed") is insufficient. Each surprise must name the artifact that produced it (e.g., a specific namespace output, interview result, prototype run). A surprise without a traceable source cannot be audited by the next team and fails. |
| C-03 | **Design impact assessed per surprise** | depth | Every named surprise carries an explicit assessment of its impact on design direction. Impact may be confirming (validates current direction), redirecting (changes a decision), or destabilizing (opens a previously closed question). An impact statement that does not identify which design decision is affected fails. "This changes things" without naming what changes is insufficient. |
| C-04 | **Synthesis not summary** | behavior | The artifact does not summarize all findings. It contains only surprises and their analysis. If expected findings appear, they are either absent or explicitly marked as context-only (not presented as output items). An artifact that enumerates findings and labels some "interesting" does not satisfy this criterion -- the surprise/expected partition must be explicit and structural. NOT: a summary section followed by a "highlights" section. PASS: a document whose every entry is framed as a surprise with a departure-from-expectation statement. |
| C-05 | **Surprise specificity** | correctness | Each surprise is specific to this topic's signal set, not a generic observation that could appear in any investigation. "APIs are harder to design than expected" fails -- it applies universally. "The scout:competitors signal revealed that all three competitors treat X as a solved problem, contrary to our assumption that the space was unsolved" passes -- it is falsifiable against this investigation's artifacts. |

---

## Recommended Criteria (weight: 30 points total, 10 pts each)

Output is better with these. Golden typically requires at least 2 of 3.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Expectation counterfactual** | depth | Each surprise explicitly names what was expected versus what was found. The counterfactual structure ("We expected X; we found Y") is stated, not implied. A reader new to the topic can reconstruct the prior assumption from the surprise entry alone, without consulting the underlying signal artifacts. Surprises that omit the expected-state half are incomplete -- they describe the finding but not the departure. |
| C-07 | **Institutional framing** | behavior | The artifact is explicitly addressed to a future team, not the current one. At least one element signals forward-facing intent: the surprises are framed as "things you would not predict from the artifacts alone," a closing note names what the next team should investigate first given these surprises, or the opening declares the institutional purpose. An artifact that reads as a personal retrospective without forward framing fails this criterion. |
| C-08 | **Cross-signal pattern identification** | coverage | If two or more surprises share an underlying cause or implication, that relationship is named. The pattern identification goes beyond listing -- it states what the surprises have in common and what that pattern implies for the design. If all surprises are genuinely independent, the output explicitly states this. Omitting pattern analysis when multiple surprises exist is a fail; "these surprises are unrelated" with a brief rationale is a pass. |

---

## Aspirational Criteria (weight: 30 points total, 5 pts each)

Raise the bar once essential and recommended criteria are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Surprise hierarchy by design impact** | depth | The surprises are ranked by design impact, with an explicit rationale for the ranking. The ranking is argued ("this surprise outranks the others because it affects the X decision which is load-bearing for the architecture") not asserted. A ranked list without argument is insufficient -- the hierarchy must be defensible to a reader who disagrees with it. |
| C-10 | **Riskiest surprise flagged** | behavior | The single surprise most likely to invalidate a core assumption is explicitly flagged with a warning. The flag names the assumption at risk, the signal that revealed it, and what would need to be true for the assumption to hold despite the surprise. An artifact that surfaces surprises without escalating the most dangerous one misses its highest-value contribution to the next team. |
| C-11 | **Pre-committed prior belief inventory** | correctness | The artifact contains a Prior Belief Inventory produced before signal reading -- evidenced by its existence as a discrete, numbered or labeled section that predates the surprise entries. Each surprise entry references a specific PB entry by identifier (number, label, or verbatim quote). This prevents post-hoc rationalization of the "expected" state and makes every departure claim auditable: a reviewer can verify that the prior belief was genuinely prior, not constructed to fit the finding. An artifact where "expected X" appears only within surprise entries, with no independent PBI section, satisfies C-06 but not C-11. The minimum bar: (a) a discrete PBI section exists, (b) entries are addressable by identifier, (c) each surprise cites a specific PBI entry by that identifier. |
| C-12 | **Named surprise handles** | behavior | Each surprise carries a short named handle (2-5 words) specific enough to be cited by future signal artifacts or team members without re-reading the echo. The handle must distinguish this surprise from every other in the same investigation and from generic observations. Test: could a teammate say "remember the [handle] surprise?" and be unambiguously understood by the full team? "API complexity surprise" fails -- it is universal. "competitor-treated-X-as-solved" passes -- it is unique to this investigation. Named handles make the echo surprises into first-class citable artifacts rather than prose-embedded findings; they are the unit of institutional memory that flows forward into later namespaces. |
| C-13 | **Dual phase-locked pre-commitment integrity** | correctness | The PBI and Handle Ledger are demonstrably independent pre-commitments -- evidenced by content that could not have been co-constructed. PBI entries describe domain beliefs in belief language (what the team expected before seeing signals). Handle Ledger titles name specific investigation findings in finding language (what was discovered by reading signals). Independence fails if: (a) a PBI entry names a handle label by its final form (the handle was predictable at PBI time), or (b) a Handle Ledger title echoes PBI entry language verbatim (the handle was constructed by inverting a prediction rather than naming a finding). The test is content-based: does PBI content demonstrate pre-signal ignorance of the specific findings? Do handle names demonstrate post-signal, post-gate specificity that PBI entries could not have anticipated? C-13 is only applicable when both C-11 and C-12 are satisfied. |
| C-14 | **Single-entry audit trail completeness** | behavior | Each surprise entry contains all three pointers required to verify its full provenance chain without consulting other sections: (1) its Handle Ledger title, (2) its PBI identifier, (3) its source signal artifact. A reviewer reading one entry can verify: handle exists in Handle Ledger, prior belief exists in PBI, finding exists in named signal artifact -- all three checks possible from the entry alone. An entry that requires navigating to the PBI section to find the prior belief, or to the Handle Ledger to confirm the title, or that names only "the signals" as its source, fails. This is the composition criterion for C-11 and C-12: they combine cleanly when each entry carries all three pointers, not merely when the two sections exist separately. C-14 is only applicable when both C-11 and C-12 are satisfied. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 30 points total (6 criteria, 5 points each)
- Max composite: 120

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/6 pass -> 1/6 * 30 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/6 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 6/6 -> 30
- **Composite = 120** -- maximum

---

## Criterion Relationships

**C-01 / C-04 relationship**: C-01 requires at least one named surprise with departure framing.
C-04 requires that the artifact contains *only* surprises -- no unsegregated summary content.
Both must pass together: an artifact can have named surprises (C-01) while burying them in a
summary (C-04 fail), or can contain only surprise entries but without departure framing (C-01 fail).

**C-02 / C-05 relationship**: C-02 requires tracing to a named source artifact. C-05 requires
specificity to this investigation. Both are independently verifiable: an artifact can cite a
specific source (C-02 pass) but describe a generic observation not derived from that source's
content (C-05 fail). The highest-quality surprises satisfy both.

**C-06 / C-07 tension**: C-06 (expectation counterfactual) is oriented backward -- reconstructing
the prior state. C-07 (institutional framing) is oriented forward -- addressing the next team.
An artifact that does both anchors the surprise in history and projects it into the future.
An artifact that does only one is still useful but not fully realized.

**C-09 / C-10 relationship**: C-09 requires ranking all surprises. C-10 requires flagging the
most dangerous one. C-09 can be satisfied without C-10 (all surprises ranked but none escalated
as risk). C-10 requires identifying the riskiest surprise but does not require ranking the others.
The highest-quality artifacts satisfy both.

**C-06 / C-11 relationship**: C-06 requires the "expected X; found Y" structure to be present
per surprise entry. C-11 requires the expected state to have been *committed before signal
reading*, evidenced by a discrete Prior Belief Inventory with addressable entries. C-06 can
be satisfied by priors reconstructed during writing (post-hoc); C-11 cannot. An artifact that
satisfies C-11 automatically satisfies C-06 (the PBI supplies the counterfactual half
structurally), but the reverse is not true. C-11 is the structural enforcement of what C-06
asks for rhetorically.

**C-01 / C-12 relationship**: C-01 requires each surprise to be named as a discrete item with
departure framing. C-12 requires each surprise to also carry a short reusable handle that is
citable by future artifacts. C-01 can be satisfied by a well-framed paragraph with no handle.
C-12 requires the handle as a separate named artifact. The test for C-12 is forward-facing:
does the handle travel? Can it be cited in a scout:story or program:plan artifact without
re-reading the echo? C-05 (specificity) and C-12 (named handle) reinforce each other --
a specific surprise is easier to name concisely; a well-named handle signals that specificity
was achieved.

**C-11 + C-12 / C-13 relationship**: C-13 requires both C-11 and C-12 to be satisfied first --
it is inapplicable if either is absent. Given both, C-13 tests whether the two pre-commitments
are genuinely independent or were co-constructed. The independence evidence is content-based:
PBI entries use belief language about domain expectations; Handle Ledger titles use finding
language specific to what signals revealed. An artifact can satisfy C-11 and C-12 (both
sections exist, both carry required structure) while failing C-13 (PBI entries anticipate
handle names, indicating the two sections were written together rather than at separate
lifecycle moments).

**C-13 + C-14 relationship**: C-14 tests the composition of C-11 and C-12 at the entry level
rather than the section level. C-13 tests independence between sections (are the two
pre-commitments genuinely separate?). C-14 tests integration within entries (does each entry
carry all three pointers?). An artifact can satisfy C-13 (sections are independent) while
failing C-14 (individual entries omit one or more pointers). Satisfying both establishes that
the pre-commitments are independent at the macro level and composable at the micro level --
the full audit chain is both genuine and legible.
"""

with open(OUT, 'w') as f:
    f.write(v3)
print("written ok")
