Looking at the R2 scorecard, two new patterns emerge from V-04's combined-rule evidence that aren't yet criteria:

1. **V-04 C-06 evidence**: "Three rules compound to strongly differentiate descriptions" — when rules stack, descriptions carry multiple specificity dimensions simultaneously (mechanism + deliverable, not just one). This is distinct from C-13 (quantified artifacts) and C-06 (differentiating) — it's about *bi-directional* description structure.

2. **V-04 C-07 evidence**: "Hierarchy unchanged; tagline rule may even strengthen it" — taglines that are *mutually distinguishable* across namespaces reinforce visual hierarchy because each namespace header carries a unique identity. C-11 requires a tagline; C-15 requires each tagline to be namespace-specific (not interchangeable).

These become C-14 and C-15. Aspirational denominator updates from `/5` to `/7`.

---

```markdown
# Signal Rubric — v3
**Updated**: 2026-03-16
**Scope**: `/signal` skill — full index, filtered, and bare modes
**Previous**: v2 (2026-03-16)
**Changes**: Added C-14, C-15 from R2 excellence signals (V-04 compound-rule analysis);
updated aspirational scoring denominator from /5 to /7.

---

## Criteria Table

| ID | Weight | Category | Criterion |
|----|--------|----------|-----------|
| C-01 | essential | correctness | All 12 namespaces present |
| C-02 | essential | correctness | Sub-skill counts match canonical registry |
| C-03 | essential | coverage | Every sub-skill has a one-line description in non-bare mode |
| C-04 | essential | behavior | `/signal <namespace>` filters to that namespace only |
| C-05 | essential | behavior | `/signal --bare` produces only command names, one per line, no headers or descriptions |
| C-06 | recommended | depth | Descriptions are specific and differentiating — no two feel interchangeable |
| C-07 | recommended | format | Visual hierarchy — sub-skills are visually subordinate to namespace headers |
| C-08 | recommended | behavior | Routing hint present per namespace ("describe your need") |
| C-09 | aspirational | format | Skill count embedded in namespace header line |
| C-10 | aspirational | depth | T3 tier annotations on T3-only skills |
| C-11 | aspirational | format | Namespace purpose tagline appended to the count header (e.g., `-- discover what's true before you design`) |
| C-12 | aspirational | format | Routing hints formatted as Markdown blockquote (`>`) rather than inline prose |
| C-13 | aspirational | depth | Descriptions reference quantified output artifacts — specific counts, named deliverables, or rated outputs (e.g., "5-8 named competitors with threat ratings", "per-persona scoring") |
| C-14 | aspirational | depth | Descriptions are bi-directional — each specifies both the mechanism (what the skill does) AND the deliverable (what you receive), not one or the other alone |
| C-15 | aspirational | format | Namespace taglines are mutually distinguishable — no two taglines are interchangeable across namespaces; each captures what is unique about that namespace's purpose |

---

## Scoring Formula

```
score = (essential_pass / 5 × 60)
      + (recommended_pass / 3 × 30)
      + (aspirational_pass / 7 × 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (~1.43 pts each)
- PARTIAL on a recommended criterion = 0.5 criterion credit

**Golden threshold**: all 5 essential PASS **and** composite ≥ 80

---

## Criterion Definitions

### C-01 — All 12 namespaces present (essential / correctness)

The output must include sections for all 12 canonical namespaces:
`scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`, `quest`, `mock`, `org`.

FAIL if any namespace is absent or misspelled.

---

### C-02 — Sub-skill counts match canonical registry (essential / correctness)

Each namespace header or section must reflect the correct skill count:

| Namespace | Count |
|-----------|-------|
| scout | 8 |
| draft | 4 |
| review | 4 |
| flow | 7 |
| trace | 7 |
| prove | 9 |
| listen | 3 |
| program | 2 |
| topic | 6 |
| quest | 5 |
| mock | 3 |
| org | 4 |

FAIL if any count is missing or incorrect. PARTIAL if count is present but off by one.

---

### C-03 — Every sub-skill has a one-line description in non-bare mode (essential / coverage)

In full index and filtered modes, every listed sub-skill must be accompanied by a description on the same or immediately following line. One-word or fragment descriptions do not qualify.

FAIL if any sub-skill appears without a description. PARTIAL if ≥ 90% have descriptions.

---

### C-04 — Namespace filter behavior (essential / behavior)

`/signal <namespace>` must return only that namespace's skills — no other namespace headers or sub-skills appear in the output.

FAIL if any other namespace bleeds into filtered output.

---

### C-05 — Bare mode behavior (essential / behavior)

`/signal --bare` must produce only the command names, one per line, with no headers, descriptions, counts, routing hints, or decorative formatting.

FAIL if any non-command content appears in bare output.

---

### C-06 — Descriptions are specific and differentiating (recommended / depth)

Reading two descriptions from the same namespace, they must feel like different skills — not interchangeable. Descriptions must be specific enough to route a user to the right skill without trial and error.

FAIL: "Analyzes the codebase for issues."
PASS: "Audits API surface contracts between modules and flags breaking changes."

PARTIAL if descriptions are differentiated but lack actionable specificity.

---

### C-07 — Visual hierarchy (recommended / format)

Sub-skills must be visually subordinate to their namespace header. Acceptable mechanisms: indentation, smaller heading level, bullet list under header, table rows under header.

FAIL if sub-skills and namespace headers occupy the same visual level.

---

### C-08 — Routing hint per namespace (recommended / behavior)

Each namespace section includes a prompt inviting the user to describe their need or situation (e.g., "Describe your topic and we'll route you to the right skill."). The hint must be present and readable, not embedded in a sub-skill description.

PARTIAL if some but not all namespaces have routing hints.

---

### C-09 — Skill count in namespace header (aspirational / format)

The count of sub-skills appears directly in the namespace header line, not only in a subtitle or body text.

PASS: `### Scout — 8 skills`
FAIL: `### Scout` (count appears elsewhere)

---

### C-10 — T3 tier annotations on T3-only skills (aspirational / depth)

Skills that exist only in the T3 variant must carry an annotation indicating their tier restriction (e.g., `[T3]`, `(T3 only)`, or equivalent). Unannotated T3 skills are invisible to T1/T2 users reading the index.

PARTIAL if some but not all T3-only skills are annotated.

---

### C-11 — Namespace purpose tagline in header (aspirational / format)

Each namespace header includes a short purpose tagline following the count — a verb-led phrase answering "what is this namespace for?"

PASS: `### Scout — 8 skills — discover what's true before you design`
FAIL: `### Scout — 8 skills` (no tagline)
FAIL: `### Scout — 8 skills — scout namespace` (restates name, not purpose)

Tagline must start with a verb and answer the user's implicit question: "why would I come here?"

---

### C-12 — Routing hints as Markdown blockquote (aspirational / format)

Routing hints (C-08) must be formatted as a Markdown blockquote (`>`), not inline prose or a plain paragraph.

PASS:
```
> Describe your competitive landscape and we'll match you to the right scout skill.
```

FAIL:
```
Tip: Describe your competitive landscape and we'll match you to the right scout skill.
```

---

### C-13 — Descriptions reference quantified output artifacts (aspirational / depth)

Descriptions must name the concrete deliverable and, where meaningful, quantify it — specific counts, named artifact types, or rated outputs.

PASS: "Maps 5-8 named competitors with threat ratings per strategic dimension."
PASS: "Produces a per-persona scoring matrix across 12 adoption segments."
FAIL: "Analyzes competitors." (no artifact named, no quantity)
FAIL: "Generates a report." (artifact named but not quantified or typed)

---

### C-14 — Descriptions are bi-directional: mechanism AND deliverable (aspirational / depth)

Each description must carry two distinct pieces of information:
1. **Mechanism** — what the skill does (the action or analysis)
2. **Deliverable** — what you receive (the artifact or output)

Neither alone is sufficient for a PASS on this criterion.

FAIL: "Analyzes competitor positioning." (mechanism only — no deliverable)
FAIL: "Produces a threat matrix." (deliverable only — no mechanism)
PASS: "Analyzes competitor positioning across 4 strategic vectors to produce a ranked threat matrix." (mechanism + deliverable)

Note: C-13 (quantified artifacts) and C-14 (bi-directionality) are independent — a description can name a deliverable without specifying a mechanism, or specify counts without explaining the action.

---

### C-15 — Namespace taglines are mutually distinguishable (aspirational / format)

Each namespace's tagline (C-11) must be specific enough to its namespace that it could not plausibly describe any other namespace. Taglines must capture what is *unique* about that namespace's purpose, not generic phrases applicable to multiple namespaces.

FAIL: `— gather information` (applies equally to scout, prove, listen)
FAIL: `— analyze and produce outputs` (applies to every namespace)
PASS: `— discover what's true before you design` (specific to scout's pre-design validation role)
PASS: `— write the artifact when you know what you want` (specific to draft's production role)

Evaluation: attempt to swap two taglines. If the swap is plausible, both taglines FAIL this criterion.
```
