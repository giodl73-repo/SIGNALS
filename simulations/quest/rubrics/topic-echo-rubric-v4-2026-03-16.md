Written to `simulations/quest/rubrics/topic-echo-rubric-v4-2026-03-16.md`.

---

**Two new criteria extracted from Round 3 scoring differentials:**

**C-15 — Pre-commitment enforcement mechanism declaration** (correctness, applicability gate: C-11)

The Round 3 scorecard revealed that C-13 splits cleanly on *what type of boundary* governed PBI production. V-01/V-04 scored PARTIAL because a phase gate creates temporal separation but doesn't prevent the model from drawing on prior reasoning across phases. V-03/V-05 scored PASS because a role boundary creates structural impossibility — the PBI-writing stage literally cannot see signal content. C-15 captures this: the artifact must declare which mechanism was used. Without that declaration, a reviewer cannot calibrate their trust in C-13's independence claim — they must re-derive it from content analysis. A freeze declaration ("PBI frozen at [step]. Signal artifacts opened after.") provides temporal provenance; a role-scope declaration provides structural provenance. The rubric notes that temporal < structural, and artifacts may indicate which applies.

**C-16 — Production-time per-entry verification attestation** (behavior, applicability gate: C-14)

The Round 3 scorecard revealed that C-14 splits on whether the entry carries an *explicit verification statement* or just three pointers. V-01 scored PARTIAL (bullet list, no schema, no self-check — "omission risk under model drift: moderate"). V-02/V-04/V-05 scored PASS when they included labeled schema plus an explicit self-check. V-05's strongest form enumerated each verification path individually. C-16 captures the second tier: the entry must include a production-time attestation that each pointer was verified — not just present. Audit burden shifts from reviewer obligation (C-14) to producer evidence (C-16).

**Score model:** Aspirational 30 pts (6 criteria) → 40 pts (8 criteria, 5 pts each). Max composite: 120 → 130.
ified before writing. The
direction of audit burden shifts: C-14 asks reviewers to check the chain; C-16 requires
producers to attest the chain before handing it off. Applicability gate: C-14 must pass.

**Score model update:** Aspirational: 30 pts (6 criteria) -> 40 pts (8 criteria, 5 pts each).
Max composite: 120 -> 130. Golden threshold unchanged (all essential pass AND composite >= 80).
Example calculations and golden path examples updated to reflect 8 aspirational criteria.

**New relationship entries:**
- C-11 / C-15: C-15 extends C-11 by requiring the enforcement mechanism to be declared, not
  just that a PBI section exists.
- C-13 / C-15: C-15 provides the provenance that allows a reviewer to trust C-13 independence
  without performing full content analysis.
- C-14 / C-16: C-16 extends C-14 from pointer presence to production-time attestation.
  C-14 is the structural minimum; C-16 is the evidence that the structure was verified.

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

## Aspirational Criteria (weight: 40 points total, 5 pts each)

Raise the bar once essential and recommended criteria are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Surprise hierarchy by design impact** | depth | The surprises are ranked by design impact, with an explicit rationale for the ranking. The ranking is argued ("this surprise outranks the others because it affects the X decision which is load-bearing for the architecture") not asserted. A ranked list without argument is insufficient -- the hierarchy must be defensible to a reader who disagrees with it. |
| C-10 | **Riskiest surprise flagged** | behavior | The single surprise most likely to invalidate a core assumption is explicitly flagged with a warning. The flag names the assumption at risk, the signal that revealed it, and what would need to be true for the assumption to hold despite the surprise. An artifact that surfaces surprises without escalating the most dangerous one misses its highest-value contribution to the next team. |
| C-11 | **Pre-committed prior belief inventory** | correctness | The artifact contains a Prior Belief Inventory produced before signal reading -- evidenced by its existence as a discrete, numbered or labeled section that predates the surprise entries. Each surprise entry references a specific PB entry by identifier (number, label, or verbatim quote). This prevents post-hoc rationalization of the "expected" state and makes every departure claim auditable: a reviewer can verify that the prior belief was genuinely prior, not constructed to fit the finding. An artifact where "expected X" appears only within surprise entries, with no independent PBI section, satisfies C-06 but not C-11. The minimum bar: (a) a discrete PBI section exists, (b) entries are addressable by identifier, (c) each surprise cites a specific PBI entry by that identifier. |
| C-12 | **Named surprise handles** | behavior | Each surprise carries a short named handle (2-5 words) specific enough to be cited by future signal artifacts or team members without re-reading the echo. The handle must distinguish this surprise from every other in the same investigation and from generic observations. Test: could a teammate say "remember the [handle] surprise?" and be unambiguously understood by the full team? "API complexity surprise" fails -- it is universal. "competitor-treated-X-as-solved" passes -- it is unique to this investigation. Named handles make the echo surprises into first-class citable artifacts rather than prose-embedded findings; they are the unit of institutional memory that flows forward into later namespaces. |
| C-13 | **Dual phase-locked pre-commitment integrity** | correctness | The PBI and Handle Ledger are demonstrably independent pre-commitments -- evidenced by content that could not have been co-constructed. PBI entries describe domain beliefs in belief language (what the team expected before seeing signals). Handle Ledger titles name specific investigation findings in finding language (what was discovered by reading signals). Independence fails if: (a) a PBI entry names a handle label by its final form (the handle was predictable at PBI time), or (b) a Handle Ledger title echoes PBI entry language verbatim (the handle was constructed by inverting a prediction rather than naming a finding). The test is content-based: does PBI content demonstrate pre-signal ignorance of the specific findings? Do handle names demonstrate post-signal, post-gate specificity that PBI entries could not have anticipated? C-13 is only applicable when both C-11 and C-12 are satisfied. |
| C-14 | **Single-entry audit trail completeness** | behavior | Each surprise entry contains all three pointers required to verify its full provenance chain without consulting other sections: (1) its Handle Ledger title, (2) its PBI identifier, (3) its source signal artifact. A reviewer reading one entry can verify: handle exists in Handle Ledger, prior belief exists in PBI, finding exists in named signal artifact -- all three checks possible from the entry alone. An entry that requires navigating to the PBI section to find the prior belief, or to the Handle Ledger to confirm the title, or that names only "the signals" as its source, fails. This is the composition criterion for C-11 and C-12: they combine cleanly when each entry carries all three pointers, not merely when the two sections exist separately. C-14 is only applicable when both C-11 and C-12 are satisfied. |
| C-15 | **Pre-commitment enforcement mechanism declaration** | correctness | The artifact declares how its PBI was isolated from signal knowledge, not merely that a PBI section exists. A timestamped freeze declaration ("PBI frozen at [step]. Signal artifacts opened after.") provides temporal provenance. A role-scope declaration ("PBI produced by Archivist role with no access to signal artifacts") provides structural provenance. Without a mechanism declaration, a reviewer must infer pre-commitment quality from content analysis alone -- making C-13 independence unverifiable without re-deriving it from scratch. The mechanism declaration is the difference between a PBI that could have been pre-committed (C-11) and a PBI whose provenance is traceable (C-15). Note: temporal provenance (phase gate with freeze timestamp) is weaker than structural provenance (role scope exclusion) because a phase gate sequences but does not block cross-phase reasoning; an artifact may indicate which type was used, allowing reviewers to calibrate accordingly. C-15 is only applicable when C-11 is satisfied. |
| C-16 | **Production-time per-entry verification attestation** | behavior | Each surprise entry includes an explicit statement confirming that all three audit pointers were verified at production time: (1) handle was confirmed to exist in the Handle Ledger at the named title, (2) PBI-Ref entry was confirmed to exist at the cited identifier, (3) source artifact was confirmed to appear in the signal set by name. A verification attestation converts the audit chain from reviewer obligation into producer evidence. An entry that carries three pointers (C-14) but no attestation requires a reviewer to perform the three checks; an entry with a production-time attestation shifts the burden to the producer, who verified the chain before the artifact was finalized. An attestation that names each check explicitly is a pass; a generic "verified" statement without naming what was verified fails -- reviewers must be able to see which checks were performed. C-16 is only applicable when C-14 is satisfied. |

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
- Aspirational: 40 points total (8 criteria, 5 points each)
- Max composite: 130

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/8 pass -> 1/8 * 40 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/8 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 8/8 -> 40
- **Composite = 130** -- maximum

---

## Criterion Relationships

**C-01 / C-04 relationship**: C-01 requires at least one named surprise with departure framing.
C-04 requires that the artifact contains *only* surprises -- no unsegregated summary content.
Both must pass together: an artifact can have named surprises (C-01) while burying them in a
summary (C-04 fail), or can contain only surprise entries but without departure framing (C-01 fail).

**C-02 / C-05 relationship**: C-02 requires tracing to a named source artifact. C-05 requires
specificity to this investigation. Both are independently verifiable: an artifact can cite a
specific source (C-02 pass) but describe a generic observation not derived from that source
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
departure framing. C-12 requires each surprise to also carry a short reusable handle citable
by future artifacts. C-01 can be satisfied by a well-framed paragraph with no handle. C-12
requires the handle as a separate named artifact. The test for C-12 is forward-facing: does
the handle travel? Can it be cited in a scout:story or program:plan artifact without re-reading
the echo? C-05 (specificity) and C-12 (named handle) reinforce each other -- a specific
surprise is easier to name concisely; a well-named handle signals that specificity was achieved.

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

**C-11 / C-15 relationship**: C-11 establishes that a PBI exists and is addressable. C-15
requires the artifact to additionally declare *how* the PBI was isolated from signal knowledge.
C-11 is the structural minimum (the section exists); C-15 is the provenance layer (the
mechanism that made it genuinely prior is legible to a reviewer). An artifact can satisfy
C-11 (PBI section present, identifiers present, citations present) while failing C-15 (no
declaration of whether a phase gate or role boundary governed PBI production). The mechanism
declaration matters because it changes what a reviewer must do to trust C-13: with C-15
satisfied, the enforcement mechanism is stated; without it, the reviewer must infer quality
from content analysis alone.

**C-13 / C-15 relationship**: C-13 tests independence from content evidence (language analysis).
C-15 tests independence from mechanism evidence (provenance declaration). Both target the same
property -- genuine pre-commitment -- through different lenses. C-13 can be satisfied without
C-15 (content analysis shows independence but no mechanism is declared). C-15 can be satisfied
without C-13 passing (mechanism declared but content shows contamination). The strongest
artifacts satisfy both: the mechanism was sound (C-15) and the content confirms it (C-13).
A declared information boundary (role scope) is stronger provenance than a declared workflow
boundary (phase gate) because the former is structurally enforced; artifacts may indicate
which applies, allowing reviewers to weight accordingly.

**C-14 / C-16 relationship**: C-14 requires each entry to carry three pointers. C-16 requires
each entry to include a production-time attestation that those pointers were verified before
writing. C-14 is the structural requirement (pointers present). C-16 is the evidence layer
(pointers were checked, not just present). An artifact can satisfy C-14 (all three pointers
appear) while failing C-16 (no per-entry attestation that they were verified). Satisfying
both establishes the full chain: the pointers are present (C-14) and the producer confirmed
each one at production time (C-16), shifting audit burden from reviewer to producer. An
attestation that names each check explicitly ("Handle confirmed in Ledger; PBI-04 confirmed
at that identifier; scout:competitors artifact confirmed in signal set") is stronger than a
generic confirmation; reviewers should be able to distinguish which checks were performed.
