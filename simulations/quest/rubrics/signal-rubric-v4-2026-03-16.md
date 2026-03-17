Reading the R3 scorecard for new excellence signals before writing the rubric.

From the R3 evidence, two new patterns emerge:

**C-16** — From V-02 C-14 FAIL vs V-03 C-14 PASS: V-02 fails because descriptions are "deliverable-only" with "no mechanism verb." V-03 passes because the `->` separator *mechanically enforces* the split — structure isn't just present, it's syntactically required. This is distinct from C-14 (bi-directionality exists) — it's about the enforcement marker.

**C-17** — From V-04 C-06 evidence: "7 explicit rules produce maximally specific descriptions." V-03 achieves 100 through rules that are structurally present; V-04 goes further by making the rule set *numbered and enumerable* — every description rule is a named RULE N, making compliance auditable by inspection rather than inference. This is a meta-criterion about the quality contract being explicit.

Aspirational denominator: /7 → /9.

---

```markdown
# Signal Rubric — v4
**Updated**: 2026-03-16
**Scope**: `/signal` skill — full index, filtered, and bare modes
**Previous**: v3 (2026-03-16)
**Changes**: Added C-16, C-17 from R3 excellence signals (V-02/V-03 `->` enforcement
delta; V-04 7-rule explicit contract); updated aspirational scoring denominator from /7 to /9.

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
| C-16 | aspirational | format | The bidir split is enforced by a visual separator (`->`) in every description — mechanism and deliverable are syntactically separated, not just conceptually present; descriptions without `->` (or equivalent marker) fail regardless of content |
| C-17 | aspirational | depth | All description quality rules are consolidated into an explicit numbered list (RULE 1 through RULE N) in the skill output — the complete quality contract is auditable in a single pass, not inferred from examples |

---

## Scoring Formula

```
score = (essential_pass / 5 × 60)
      + (recommended_pass / 3 × 30)
      + (aspirational_pass / 9 × 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (~1.11 pts each)
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

FAIL if any count is missing or incorrect.

---

### C-03 — Every sub-skill has a one-line description (essential / coverage)

In full-index and filtered modes, every sub-skill entry must be followed by at least one line of description. Bare mode is exempt.

FAIL if any skill has no description in non-bare mode.

---

### C-04 — Filtered mode scopes correctly (essential / behavior)

`/signal <namespace>` must output only the skills belonging to that namespace. No other namespaces may appear in the output.

FAIL if output includes skills from other namespaces or omits the target namespace.

---

### C-05 — Bare mode is names-only (essential / behavior)

`/signal --bare` must output exactly the command names, one per line, with no headers, descriptions, annotations, or blank section separators.

FAIL if any non-name content appears (headers, routing hints, T3 labels, blank lines between sections).

---

### C-06 — Descriptions are specific and differentiating (recommended / depth)

No two descriptions may be interchangeable. Each description must be specific enough that a reader could distinguish the skill from all others in the same namespace without seeing the skill name.

PARTIAL if most descriptions are specific but a few feel generic or duplicative.

---

### C-07 — Visual hierarchy (recommended / format)

Namespace headers must be visually dominant over sub-skill lines. Acceptable patterns: `###` header with indented or plain `/skill-name` lines; bold header with subordinate list. Sub-skill names must not compete with namespace headers for visual weight.

PARTIAL if hierarchy is present but inconsistent across namespaces.

---

### C-08 — Routing hint per namespace (recommended / behavior)

Each namespace section must include a routing hint — a prompt-style phrase that helps the user decide whether this namespace fits their need (e.g., "Describe your need: I want to understand competitive risk before committing to a design").

Acceptable formats: inline prose or blockquote (see C-12 for aspirational format).

PARTIAL if routing hints are present for fewer than 10 of 12 namespaces.

---

### C-09 — Skill count in namespace header (aspirational / format)

The namespace header line must embed the skill count explicitly (e.g., `### scout -- 8 skills` or `### scout (8)`). Count must be accurate per C-02.

---

### C-10 — T3 tier annotations (aspirational / depth)

Skills available only in T3 tier must be annotated in the output (e.g., `*(T3)*` suffix). A T3 skill list or legend must be present. The set of annotated skills must be complete and accurate.

---

### C-11 — Namespace purpose tagline (aspirational / format)

Each namespace header must include a purpose tagline — a short phrase (beginning with a verb) that describes the namespace's intent (e.g., `-- discover what's true before you design`). Tagline must be appended to the count header line.

---

### C-12 — Routing hints as blockquotes (aspirational / format)

All routing hints (C-08) must be formatted using Markdown blockquote syntax (`>` at line start). Inline prose routing hints do not satisfy this criterion even if they satisfy C-08.

---

### C-13 — Quantified output artifacts in descriptions (aspirational / depth)

Descriptions must reference quantified deliverables: specific counts, named output formats, or rated outputs. Vague deliverables ("a report", "an analysis") do not satisfy this criterion.

Examples that pass: "5-8 rivals each rated HIGH/MEDIUM/LOW", "per-persona scoring across 12 dimensions", "MoSCoW-prioritized list with dependency graph".

---

### C-14 — Bi-directional descriptions (aspirational / depth)

Each description must specify both (a) the mechanism — what the skill *does*, expressed as an action verb phrase — and (b) the deliverable — what the user *receives*, expressed as a concrete noun phrase. Descriptions that specify only the deliverable (deliverable-only) or only the action (mechanism-only) do not satisfy this criterion.

FAIL if the majority of descriptions are deliverable-only or mechanism-only, with no structural bidir split.

---

### C-15 — Mutually distinguishable namespace taglines (aspirational / format)

Taglines (C-11) must pass the SWAP TEST: no tagline may be reassigned to a different namespace without becoming false or misleading. Implementations that assert distinctness without providing LOCKED/GENERIC example pairs, or without a stated swap-test rule, score PARTIAL at most.

Examples of LOCKED taglines: "map the competitive and regulatory landscape before design begins" (scout-locked), "predict what customers will say before they have the chance to say it" (listen-locked).

---

### C-16 — `->` separator as mechanical bidir enforcement (aspirational / format)

The bidir constraint (C-14) must be enforced syntactically, not just stylistically. Every description must use `->` (or a declared equivalent separator) to split the mechanism phrase from the deliverable phrase. Descriptions that are conceptually bidir but lack the separator do not satisfy this criterion.

Rationale: C-14 tests whether bidir content is present; C-16 tests whether the structure is mechanically enforced so that compliance is unambiguous. A description without `->` cannot be verified as bidir by inspection alone.

FAIL if `->` is absent from the majority of descriptions, even if the descriptions are substantively bidir.

---

### C-17 — Explicit numbered rule set (aspirational / depth)

The skill output must contain an explicit numbered list of the description quality rules it applies (RULE 1, RULE 2, ... RULE N). The rule set must be enumerated in the output itself — not implied by examples or inferred from the description pattern. Each rule must be independently checkable.

Rationale: V-04 R3 evidence shows that making rules explicit and numbered produces a self-auditing quality contract. A reviewer can check each rule independently rather than holistically judging description quality. This criterion is the meta-level enforcement of C-06, C-13, C-14, C-15, and C-16 together.

FAIL if rules are implicit, described only in prose, or present only as examples without enumeration.
```

---

**Summary of changes v3 → v4:**

| | v3 | v4 |
|--|--|--|
| Aspirational count | 7 | 9 |
| Aspirational denominator | /7 | /9 |
| New criteria | — | C-16 (`->` enforcement), C-17 (explicit rule set) |
| Source signals | R2 V-04 | R3 V-02/V-03 delta, V-04 C-06 |
