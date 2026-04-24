Done. Here is the complete updated rubric:

---

# signal-check Rubric — v3 (2026-03-18)

Evaluates the output of `/signal:check` against quality criteria derived from iterative design experiments. Three tiers: Essential (gate), Recommended (depth), Aspirational (excellence). Gold requires all essential passing and composite >= 80.

---

## Criterion Summary

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

**8 Aspirational** — raise the bar once essentials are stable. C-09 and C-10 retained from v1; C-11 through C-13 added from R1 excellence signals; C-14 through C-16 added from R2 excellence signals:

| ID | Criterion | Source |
|----|-----------|--------|
| C-09 | Cross-dimension patterns named when a shared root cause exists | v1 |
| C-10 | Missing signals identified by namespace + specific skill | v1 |
| C-11 | All skill references use `/namespace:skill` format consistently | EX-01 |
| C-12 | A terminal MISSING SIGNAL GUIDE section collates all gaps | EX-02 |
| C-13 | Absent evidence is declared explicitly — no dimension silently omits | EX-03 |
| C-14 | A named STANDING RULES block precedes all inventory and analysis | EX-04 |
| C-15 | Each dimension specifies required verbatim absence phrases | EX-05 |
| C-16 | Every constraint explicitly enumerates all output locations it governs | EX-06 |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Criterion Detail

### Essential (C-01 to C-05)

*(unchanged from v2)*

### Recommended (C-06 to C-08)

*(unchanged from v2)*

### Aspirational (C-09 to C-16)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09–C-13 | *(unchanged from v2)* | | |
| C-14 | Named STANDING RULES block precedes all inventory and analysis | structure | The output opens with a named STANDING RULES block (or equivalent heading) that declares system-wide enforcement constraints before any inventory or dimension analysis begins. The block must enumerate obligations that apply across the entire output — not guidance scoped to one section. Per-section reminders alone do not satisfy this criterion. Derived from EX-04: a named STANDING RULES block is the structural mechanism that separates composite 100 from 98. |
| C-15 | Each dimension specifies required verbatim absence phrases | correctness | For each of the four dimensions, the rubric or skill instruction names at least one required verbatim phrase to use when relevant evidence is absent (e.g., "no artifact dates available — ordering cannot be established" for SEQUENCE; "no mechanism evidence found — the causal gap is open" for CAUSAL GAP). Structural guidance ("state the absence") without exact wording does not satisfy this criterion. Derived from EX-05: verbatim forms prevent analysis drift more reliably than structural instructions alone. |
| C-16 | Every constraint enumerates all output locations it governs | format | Any constraint declared in the rubric or instruction explicitly names every output location where it applies (e.g., "applies to readiness summary, all action fields, cross-dimension patterns, and MISSING SIGNAL GUIDE. No exceptions."). Generic scope ("throughout the output") does not satisfy this criterion. Derived from EX-06: V-01 and V-03 failed C-11 and C-13 because constraints named one section but not the others. A constraint scoped to one location is effectively restricted to that location in practice. |

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

| Tier | Criteria | Weight | Points each |
|------|----------|--------|-------------|
| Essential | 5 | 60 pts | 12 pts |
| Recommended | 3 | 30 pts | 10 pts |
| Aspirational | 8 | 10 pts | 1.25 pts |

| Essential | Recommended | Aspirational | Composite | Gold? |
|-----------|-------------|--------------|-----------|-------|
| 5/5 | 3/3 | 8/8 | 100 | YES |
| 5/5 | 3/3 | 6/8 | 97.5 | YES |
| 5/5 | 3/3 | 0/8 | 90 | YES |
| 5/5 | 1/3 | 8/8 | 80 | YES (boundary) |
| 5/5 | 0/3 | 8/8 | 70 | NO |
| 4/5 | 3/3 | 8/8 | 88 | NO (essential fail) |

---

**What changed from v2:**
- Aspirational tier: 5 → 8 criteria; denominator in formula updated to `/8 * 10`
- C-14 (EX-04): named STANDING RULES preamble block — structure criterion
- C-15 (EX-05): required verbatim absence phrases per dimension — correctness criterion
- C-16 (EX-06): constraint scope must enumerate every output location — format criterion
- Score examples updated; v2 100-scorers (V-04, V-05) remain 100 under v3
tegory | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimension patterns named when present | depth | When two or more dimensions share a common root cause (e.g., a SEQUENCE gap in discovery also explains a CAUSAL GAP — the team specified before gathering mechanism evidence), the output names this as a pattern rather than reporting each dimension independently. Pattern naming is optional when no cross-dimension link exists. |
| C-10 | Missing signals identified by namespace + skill | coverage | For each gap identified, the output names the specific signal skill that would close it (e.g., "CAUSAL GAP: run /discover:causal; STALENESS on competitors: run /discover:competitors"). Identification is by namespace and skill, not just by dimension name. |
| C-11 | All skill references use `/namespace:skill` format | format | Every skill reference in the output — whether in action fields, next steps, or a closing guide — uses the explicit `/namespace:skill` format. Bare skill names (e.g., "discover-causal" without the slash and namespace) or vague prompts ("run the relevant discover skill") = FAIL. Derived from EX-01: C-10 is a format threshold, not a depth threshold. Skill awareness without format enforcement does not satisfy the criterion. |
| C-12 | Terminal MISSING SIGNAL GUIDE collates all gaps | structure | The output includes a dedicated final section — a MISSING SIGNAL GUIDE or equivalent — that collates every flagged gap across all four dimensions into a single terminal list. Each line specifies one gap and the `/namespace:skill` to close it. This section provides structural redundancy over per-dimension action fields: both must be present for C-12 to pass. Derived from EX-02: the guide simultaneously satisfies C-07 (next action present) and C-10 (namespace + skill named) for every gap, making omission of either a visible structural failure. |
| C-13 | Absent evidence declared explicitly — no silent omissions | correctness | For every dimension where the relevant evidence is absent or unavailable, the output uses explicit absence language (e.g., "no mechanism evidence found — the causal gap is open", "no artifact dates available — ordering cannot be established"). A dimension that returns no finding when evidence is missing — without stating the absence — = FAIL. Derived from EX-03: explicit prohibition patterns ("silence does not pass") prevent analysis drift under minimal-inventory conditions. Absence must be named, not left blank. |
| C-14 | Named STANDING RULES block precedes all inventory and analysis | structure | The output opens with a named STANDING RULES block (or equivalent heading) that declares system-wide enforcement constraints before any inventory or dimension analysis begins. The block must enumerate obligations that apply across the entire output — not guidance scoped to one section. Per-section reminders alone do not satisfy this criterion; a preamble-level named block is required. Derived from EX-04: a named STANDING RULES block is the structural mechanism that separates composite 100 from 98. Constraints embedded inside per-section guidance do not propagate system-wide with the same force as a named preamble block. |
| C-15 | Each dimension specifies required verbatim absence phrases | correctness | For each of the four dimensions, the rubric or skill instruction names at least one required verbatim phrase to use when relevant evidence is absent (e.g., "no artifact dates available — ordering cannot be established" for SEQUENCE; "no mechanism evidence found — the causal gap is open" for CAUSAL GAP). Structural guidance ("state the absence") without specifying exact wording does not satisfy this criterion. Derived from EX-05: verbatim forms prevent analysis drift under minimal-inventory conditions more reliably than structural instructions alone. A model given exact required phrases produces consistent explicit absence declarations; a model given only structural guidance drifts toward hedging or omission. |
| C-16 | Every constraint enumerates all output locations it governs | format | Any constraint declared in the rubric or instruction — skill reference format, absence declaration requirement, verbatim form obligation — explicitly names every output location where it applies (e.g., "applies to readiness summary, all action fields, cross-dimension patterns, and MISSING SIGNAL GUIDE. No exceptions."). Generic scope ("throughout the output", "in all sections") does not satisfy this criterion. Derived from EX-06: V-01 and V-03 failed C-11 and C-13 because constraints were named in one section but not propagated to others. A constraint that names only one location is effectively scoped to that location in practice. Location enumeration is the mechanism that closes the propagation gap. |

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

| Tier | Criteria | Weight | Points each |
|------|----------|--------|-------------|
| Essential | 5 | 60 pts total | 12 pts |
| Recommended | 3 | 30 pts total | 10 pts |
| Aspirational | 8 | 10 pts total | 1.25 pts |

### Score Examples

| Essential | Recommended | Aspirational | Composite | Gold? |
|-----------|-------------|--------------|-----------|-------|
| 5/5 | 3/3 | 8/8 | 100 | YES |
| 5/5 | 3/3 | 6/8 | 97.5 | YES |
| 5/5 | 3/3 | 0/8 | 90 | YES |
| 5/5 | 2/3 | 8/8 | 90 | YES |
| 5/5 | 1/3 | 8/8 | 80 | YES (boundary) |
| 5/5 | 0/3 | 8/8 | 70 | NO |
| 4/5 | 3/3 | 8/8 | 88 | NO (essential fail) |

**Note on R2 scores under v3**: V-04 and V-05 scored 100 under v2 (all 13 criteria
passing). Under v3 the aspirational denominator expands from /5 to /8 and C-14
through C-16 are added. V-04/V-05 passed C-14 (STANDING RULES block present), C-15
(verbatim forms per dimension), and C-16 (constraint scope enumerated explicitly) —
so their composite remains 100. V-01/V-02/V-03, which previously failed C-11 or
C-13 due to constraint propagation gaps, predictably also fail C-15 and C-16 under
v3, since the same structural deficiency that caused those essential-adjacent failures
is exactly what C-15 and C-16 are designed to diagnose.

---

## Design Notes

**Why SEQUENCE requires artifact dates (C-02):** A model that claims discovery
preceded specification without citing dated artifacts is asserting order from
inference. The value of SEQUENCE is catching cases where the dates *don't* support
the claimed order. Date-free SEQUENCE analysis cannot catch this.

**Why CAUSAL GAP requires naming mechanism or gap explicitly (C-04):** The causal
mechanism is the hardest thing to surface because it is never in a single artifact
— it must be assembled across signals. Silence means the dimension was skipped,
not that the mechanism was established.

**Why register matters (C-05):** Signal-check is explicitly described as "not
punitive." A health report that blocks decisions or issues verdicts defeats the
coaching intent. The skill is positioned as something to run *before* committing —
the team should leave with a clear view of what they know and what they are
deciding to do despite gaps, not a gatekeeper that overrides their judgment.

**Why C-09/C-10 are aspirational:** Cross-dimension pattern naming requires
synthesis beyond per-dimension analysis. Namespace-specific gap identification
requires knowing the skill catalog. Both are high-value outputs but impose overhead
that is not essential for a correct, actionable report.

**Why C-11 is separate from C-10 (v2):** C-10 tests whether namespace + skill are
*present* in the output. C-11 tests whether every skill reference uses the
`/namespace:skill` *format* consistently — including in places outside the dedicated
gap guide (action fields, readiness summary, inline recommendations). A report can
pass C-10 (guide exists with correct format) while failing C-11 (inline references
use bare skill names). The distinction is precision of format enforcement across
the full output.

**Why C-12 adds value over C-07 (v2):** C-07 requires a next action per flagged
issue. C-12 requires a *collated terminal section* that lists all gaps in one place.
The terminal guide provides structural redundancy: if a per-dimension action field
is missing, the guide makes the omission visible. Both must be present for C-12
to pass.

**Why C-13 is aspirational rather than essential (v2):** Explicit absence
declarations are already partially covered by C-04 (CAUSAL GAP must name "no
mechanism evidence found") and C-02 (SEQUENCE must name "ordering cannot be
established" when dates are absent). C-13 generalizes this pattern across all four
dimensions — a broader contract than the essential criteria impose.

**Why C-14 is separate from C-08 (v3):** C-08 requires a readiness summary at the
top of the output — a health verdict. C-14 requires a named STANDING RULES block
that declares system-wide enforcement constraints before any analysis — an
enforcement frame. These are structurally distinct: the readiness summary tells the
user what the signal health looks like; the STANDING RULES block governs how the
remainder of the output is produced. A report can pass C-08 (summary present) while
failing C-14 (no named rules block, or rules embedded per-section rather than
declared preamble-level). EX-04 showed this is what distinguishes 100 from 98 in
practice: without a named preamble block, constraints must be re-declared in every
section and omissions are invisible.

**Why C-15 is separate from C-13 (v3):** C-13 is an output criterion — did the
generated report state absence explicitly? C-15 is a design criterion — does the
rubric or instruction specify *exact required phrases* for each dimension's absence
case? These operate at different layers. A rubric can produce C-13-passing outputs
through structural guidance alone, but EX-05 demonstrates that verbatim forms
produce more consistent compliance than structural guidance. C-15 makes the
verbatim-form design practice a scorable property of the rubric itself, not just
the output it produces.

**Why C-16 is separate from C-11 and C-13 (v3):** C-11 and C-13 are output
criteria — skill format consistency and explicit absence declarations in the
generated report. C-16 is a rubric-design criterion — do the constraint declarations
themselves enumerate every location they govern? EX-06 showed that V-01 failed
C-11 at readiness summary and cross-dimension patterns because the constraint never
named those locations. A constraint that names only one section is effectively
scoped to that section, regardless of authorial intent. C-16 makes location
enumeration a scorable requirement so that implicit propagation assumptions do not
survive into deployed rubrics.
