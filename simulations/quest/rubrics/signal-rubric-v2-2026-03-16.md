Looking at the scorecard, I'll extract the excellence patterns that distinguish the highest-scoring variations and aren't already captured.

**Excellence signals identified:**

- **V-03 C-09 variant**: Headers carry not just count but a purpose tagline — `### Scout -- 8 skills -- discover what's true before you design`. Goes beyond count (C-09 already requires count; this is richer).
- **V-02, V-03**: Routing hints formatted as Markdown blockquote (`> Tip:` / `> Describe your...`), not inline prose.
- **V-03 C-06 evidence**: Descriptions reference quantified output artifacts — "5-8 named competitors with threat ratings", "per-persona scoring" — concrete deliverable language, not just specificity.

These become C-11, C-12, C-13. Scoring formula denominator updates from `/2` to `/5` for aspirational tier.

---

```markdown
# Signal Rubric — v2
**Updated**: 2026-03-16
**Scope**: `/signal` skill — full index, filtered, and bare modes
**Previous**: v1 (2026-03-16)
**Changes**: Added C-11, C-12, C-13 from R1 excellence signals; updated aspirational scoring denominator.

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

---

## Scoring Formula

```
score = (essential_pass / 5 × 60)
      + (recommended_pass / 3 × 30)
      + (aspirational_pass / 5 × 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (2 pts each)
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
| quest | 4 |
| mock | 3 |
| org | 4 |
| **Total** | **61** |

FAIL if any count is wrong or omitted when counts are present. If counts appear nowhere, score C-09 FAIL as well.

---

### C-03 — Every sub-skill has a one-line description in non-bare mode (essential / coverage)

In full-index and filtered modes, every listed sub-skill must have an accompanying description on the same or immediately following line. A bare name with no description is a FAIL.

Does not apply to `--bare` mode output.

---

### C-04 — `/signal <namespace>` filters to that namespace only (essential / behavior)

When the skill receives a namespace argument, it must output only that namespace's section. No other namespace blocks, no preamble unrelated to the requested namespace.

Evidence: explicit behavioral rule in the skill body covering "filtered mode."

---

### C-05 — `/signal --bare` produces only command names (essential / behavior)

`--bare` mode must output a flat list of slash-command names. One per line. No descriptions, no headers, no routing text, no blank-line groups.

Evidence: explicit behavioral rule in the skill body covering "bare mode."

---

### C-06 — Descriptions are specific and differentiating (recommended / depth)

No two descriptions should feel interchangeable. Each must identify what makes that skill distinct from its neighbors in the same namespace. Generic phrases ("performs analysis", "generates output") with no differentiating detail are a FAIL for that skill.

PARTIAL: fewer than 3 generic descriptions per namespace, but some entries are below full specificity.

---

### C-07 — Visual hierarchy — sub-skills subordinate to namespace headers (recommended / format)

There must be a clear, consistent two-level visual structure: namespace level (header, bold label, or equivalent) and sub-skill level (indented, prefixed, or otherwise visually nested). A flat list with no structural differentiation between namespaces and skills is a FAIL.

---

### C-08 — Routing hint present per namespace (recommended / behavior)

Each namespace section must include a prompt to the user describing how to engage ("describe your discovery need and the relevant scout skill will run", or equivalent). The hint must be specific to the namespace's domain noun, not a generic catch-all.

---

### C-09 — Skill count in namespace header (aspirational / format)

Each namespace header line includes the numeric count of skills in that namespace (e.g., `scout -- 8 skills`, `## Scout namespace -- 8 skills`). The count must be present on the header line itself, not in body text.

---

### C-10 — T3 tier annotations on T3-only skills (aspirational / depth)

Skills that are available only in the T3 tier are explicitly annotated as such (e.g., `[T3]`, `(T3 only)`, or equivalent inline marker). Absence of any T3 annotations when T3-restricted skills exist in the registry is a FAIL.

---

### C-11 — Namespace purpose tagline in count header (aspirational / format)

The namespace header carries not just the count but a short purpose tagline that orients the user to the namespace's role in the feature workflow. Example forms:

- `### Scout -- 8 skills -- discover what's true before you design`
- `## /flow -- 7 skills for signal behavior and event modeling`

The tagline must be specific to the namespace, not generic ("for your use", "available here"). Count-only headers (C-09) without a tagline do not satisfy this criterion.

---

### C-12 — Routing hints formatted as Markdown blockquote (aspirational / format)

Routing hints (C-08) are rendered as Markdown blockquotes using the `>` prefix:

```
> Tip: describe your discovery need and the most relevant scout skill will run.
```

or

```
> Describe your flow concern and the relevant skill will run.
```

Plain inline prose routing hints satisfy C-08 but not C-12. The `>` prefix must be present.

---

### C-13 — Descriptions reference quantified output artifacts (aspirational / depth)

At least half of the descriptions in each namespace name a concrete, quantified deliverable rather than a process label. Examples that pass:

- ✅ "competitive landscape map with 5-8 named competitors and threat ratings"
- ✅ "name shortlist with trademark clearance, domain availability, and per-persona scoring"
- ✅ "traffic-light feasibility ratings with team and timeline assessment"

Examples that fail this criterion (may still pass C-06):

- ❌ "competitive landscape analysis"
- ❌ "feasibility assessment"
- ❌ "stakeholder interview simulation"

FAIL if more than half the skills in any namespace use process-label descriptions without artifact quantification.

---

## Golden Threshold

**Golden**: all 5 essential criteria PASS **and** composite score ≥ 80.

A response with 5/5 essential + 3/3 recommended + 0/5 aspirational scores 90 — golden.
A response with 5/5 essential + 2/3 recommended + 0/5 aspirational scores 80 — golden at threshold.
A response with 4/5 essential (any) is not golden regardless of composite score.

---

## Scoring Worksheet

| Tier | Criteria | Points Each | Max |
|------|----------|-------------|-----|
| Essential | C-01 through C-05 | 12 | 60 |
| Recommended | C-06 through C-08 | 10 | 30 |
| Aspirational | C-09 through C-13 | 2 | 10 |
| **Total** | | | **100** |

PARTIAL on a recommended criterion = 5 points (0.5 credit).
```
