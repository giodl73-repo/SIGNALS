Written to `simulations/quest/rubrics/signal-rubric-v5-2026-03-16.md`.

---

**Two new criteria, denominator /9 → /11:**

**C-18** (aspirational / depth) — Each RULE is labeled with its rubric criterion ID (e.g., `RULE 6 (C-14)`), making criterion-to-rule mapping invertible by inspection. Source: R4 E-2 — V-02 and V-04 scored identically at 100 despite V-04 being O(1) auditable and V-02 requiring O(N) inference. The rubric couldn't see the difference; C-18 fixes that.

**C-19** (aspirational / behavior) — The quality contract includes a named compliance checkpoint with explicit "invalid output / do not proceed" gate language. A rule list that satisfies C-17 and C-18 but has no gate does not satisfy C-19. Source: R4 E-3 — V-05's COMPLIANCE AUDIT block is structurally distinct from V-04's rule list: one instructs, the other gates.

**Updated scoring formula:**
```
aspirational_pass / 11 x 10   (~0.91 pts each, was ~1.11)
```

**C-17 definition also tightened**: Added an explicit FAIL condition for quality rules that escape into appendix/separate contract blocks — the R4 E-1 pattern (SEPARATOR CONTRACT fragmentation) is now part of the definition, not just implicit.
need") |
| C-09 | aspirational | format | Skill count embedded in namespace header line |
| C-10 | aspirational | depth | T3 tier annotations on T3-only skills |
| C-11 | aspirational | format | Namespace purpose tagline appended to the count header (e.g., `-- discover what's true before you design`) |
| C-12 | aspirational | format | Routing hints formatted as Markdown blockquote (`>`) rather than inline prose |
| C-13 | aspirational | depth | Descriptions reference quantified output artifacts — specific counts, named deliverables, or rated outputs (e.g., "5-8 named competitors with threat ratings", "per-persona scoring") |
| C-14 | aspirational | depth | Descriptions are bi-directional — each specifies both the mechanism (what the skill does) AND the deliverable (what you receive), not one or the other alone |
| C-15 | aspirational | format | Namespace taglines are mutually distinguishable — no two taglines are interchangeable across namespaces; each captures what is unique about that namespace's purpose |
| C-16 | aspirational | format | The bidir split is enforced by a visual separator (`->`) in every description — mechanism and deliverable are syntactically separated, not just conceptually present; descriptions without `->` (or equivalent marker) fail regardless of content |
| C-17 | aspirational | depth | All description quality rules are consolidated into an explicit numbered list (RULE 1 through RULE N) in the skill output — the complete quality contract is auditable in a single pass, not inferred from examples |
| C-18 | aspirational | depth | Each RULE in the quality contract is labeled with its rubric criterion ID (C-NN), making criterion-to-rule mapping invertible without inference — a scorer can map from any criterion to its enforcing rule and back by inspection alone |
| C-19 | aspirational | behavior | The quality contract includes a named compliance checkpoint (pre-flight checklist or equivalent) that explicitly gates output generation — "all items checked = proceed; any unchecked = invalid output, do not proceed"; a rule list without a gate does not satisfy this criterion |

---

## Scoring Formula

```
score = (essential_pass / 5 x 60)
      + (recommended_pass / 3 x 30)
      + (aspirational_pass / 11 x 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (~0.91 pts each)
- PARTIAL on a recommended criterion = 0.5 criterion credit

**Golden threshold**: all 5 essential PASS **and** composite >= 80

---

## Criterion Definitions

### C-01 -- All 12 namespaces present (essential / correctness)

The output must include sections for all 12 canonical namespaces:
`scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`, `quest`, `mock`, `org`.

FAIL if any namespace is absent or misspelled.

---

### C-02 -- Sub-skill counts match canonical registry (essential / correctness)

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

### C-03 -- Every sub-skill has a one-line description (essential / coverage)

In full-index and filtered modes, every sub-skill entry must be followed by at least one line of description. Bare mode is exempt.

FAIL if any skill has no description in non-bare mode.

---

### C-04 -- Filtered mode scopes correctly (essential / behavior)

`/signal <namespace>` must output only the skills belonging to that namespace. No other namespaces may appear in the output.

FAIL if output includes skills from other namespaces or omits the target namespace.

---

### C-05 -- Bare mode is names-only (essential / behavior)

`/signal --bare` must output exactly the command names, one per line, with no headers, descriptions, annotations, or blank section separators.

FAIL if any non-name content appears (headers, routing hints, T3 labels, blank lines between sections).

---

### C-06 -- Descriptions are specific and differentiating (recommended / depth)

No two descriptions may be interchangeable. Each description must be specific enough that a reader could distinguish the skill from all others in the same namespace without seeing the skill name.

PARTIAL if most descriptions are specific but a few feel generic or duplicative.

---

### C-07 -- Visual hierarchy (recommended / format)

Namespace headers must be visually dominant over sub-skill lines. Acceptable patterns: `###` header with indented or plain `/skill-name` lines; bold header with subordinate list. Sub-skill names must not compete with namespace headers for visual weight.

PARTIAL if hierarchy is present but inconsistent across namespaces.

---

### C-08 -- Routing hint per namespace (recommended / behavior)

Each namespace section must include a routing hint -- a prompt-style phrase that helps the user decide whether this namespace fits their need (e.g., "Describe your need: I want to understand competitive risk before committing to a design").

Acceptable formats: inline prose or blockquote (see C-12 for aspirational format).

PARTIAL if routing hints are present for fewer than 10 of 12 namespaces.

---

### C-09 -- Skill count in namespace header (aspirational / format)

The namespace header line must embed the skill count explicitly (e.g., `### scout -- 8 skills` or `### scout (8)`). Count must be accurate per C-02.

---

### C-10 -- T3 tier annotations (aspirational / depth)

Skills available only in T3 tier must be annotated in the output (e.g., `*(T3)*` suffix). A T3 skill list or legend must be present. The set of annotated skills must be complete and accurate.

---

### C-11 -- Namespace purpose tagline (aspirational / format)

Each namespace header must include a purpose tagline -- a short phrase (beginning with a verb) that describes the namespace's intent (e.g., `-- discover what's true before you design`). Tagline must be appended to the count header line.

---

### C-12 -- Routing hints as blockquotes (aspirational / format)

All routing hints (C-08) must be formatted using Markdown blockquote syntax (`>` at line start). Inline prose routing hints do not satisfy this criterion even if they satisfy C-08.

---

### C-13 -- Quantified output artifacts in descriptions (aspirational / depth)

Descriptions must reference quantified deliverables: specific counts, named output formats, or rated outputs. Vague deliverables ("a report", "an analysis") do not satisfy this criterion.

Examples that pass: "5-8 rivals each rated HIGH/MEDIUM/LOW", "per-persona scoring across 12 dimensions", "MoSCoW-prioritized list with dependency graph".

---

### C-14 -- Bi-directional descriptions (aspirational / depth)

Each description must specify both (a) the mechanism -- what the skill *does*, expressed as an action verb phrase -- and (b) the deliverable -- what the user *receives*, expressed as a concrete noun phrase. Descriptions that specify only the deliverable (deliverable-only) or only the action (mechanism-only) do not satisfy this criterion.

FAIL if the majority of descriptions are deliverable-only or mechanism-only, with no structural bidir split.

---

### C-15 -- Mutually distinguishable namespace taglines (aspirational / format)

Taglines (C-11) must pass the SWAP TEST: no tagline may be reassigned to a different namespace without becoming false or misleading. Implementations that assert distinctness without providing LOCKED/GENERIC example pairs, or without a stated swap-test rule, score PARTIAL at most.

Examples of LOCKED taglines: "map the competitive and regulatory landscape before design begins" (scout-locked), "predict what customers will say before they have the chance to say it" (listen-locked).

---

### C-16 -- `->` separator as mechanical bidir enforcement (aspirational / format)

The bidir constraint (C-14) must be enforced syntactically, not just stylistically. Every description must use `->` (or a declared equivalent separator) to split the mechanism phrase from the deliverable phrase. Descriptions that are conceptually bidir but lack the separator do not satisfy this criterion.

Rationale: C-14 tests whether bidir content is present; C-16 tests whether the structure is mechanically enforced so that compliance is unambiguous. A description without `->` cannot be verified as bidir by inspection alone.

FAIL if `->` is absent from the majority of descriptions, even if the descriptions are substantively bidir.

---

### C-17 -- Explicit numbered rule set (aspirational / depth)

The skill output must contain an explicit numbered list of the description quality rules it applies (RULE 1, RULE 2, ... RULE N). The rule set must be enumerated in the output itself -- not implied by examples or inferred from the description pattern. Each rule must be independently checkable.

Rationale: Making rules explicit and numbered produces a self-auditing quality contract. A reviewer can check each rule independently rather than holistically judging description quality. This criterion is the meta-level enforcement of C-06, C-13, C-14, C-15, and C-16 together.

FAIL if rules are implicit, described only in prose, or present only as examples without enumeration. FAIL if any quality rule (including structural validity conditions such as C-16 enforcement) lives outside the numbered RULE list in an appendix or separate contract block -- the numbered list must be the single authoritative location for all quality rules.

---

### C-18 -- Criterion-ID labels on each RULE (aspirational / depth)

Each numbered RULE in the quality contract must be labeled with the rubric criterion ID it enforces (e.g., `RULE 6 (C-14)`). Labels must be present in the RULE heading itself, not in a separate lookup table. A reviewer must be able to map from any criterion ID to its enforcing RULE -- and from any RULE to its criterion ID -- by inspection, without inference.

Rationale: V-02 (R4) and V-04 (R4) both achieve 100/100 on the v4 rubric, but V-04's criterion-ID labels make the rule list bidirectionally traceable while V-02's unlabeled rules require a scorer to infer the mapping. Two variations with identical scores should not be structurally equivalent when one is auditable in O(1) and the other requires O(N) inference. C-18 discriminates this structural advantage.

FAIL if RULE labels are present but criterion IDs are absent. PARTIAL if criterion IDs are present on some but not all rules.

---

### C-19 -- Compliance checkpoint gates output generation (aspirational / behavior)

The skill must include a named compliance checkpoint -- a checklist or equivalent verification block -- that explicitly gates output generation. The gate must state, in the skill itself, that all items must be resolved before the model proceeds (e.g., "All 7 boxes checked = valid output. Any unchecked box = invalid output; do not proceed."). A numbered rule list without a gate does not satisfy this criterion even if it satisfies C-17 and C-18.

Rationale: V-05 (R4) introduces a COMPLIANCE AUDIT block that converts the quality contract from passive instructions (rules to follow) into an active pre-flight gate (conditions that must be met before any output is generated). A model reading rules may proceed despite non-compliance; a model encountering an explicit "do not proceed" gate must resolve each item. This is a qualitatively different failure-prevention mechanism not captured by rule-list compliance alone.

FAIL if compliance is enforced only via rule-following instructions with no named gate. PARTIAL if a gate is present but does not include explicit "invalid output / do not proceed" language.

---

## Summary of Changes v4 -> v5

| | v4 | v5 |
|--|--|--|
| Aspirational count | 9 | 11 |
| Aspirational denominator | /9 | /11 |
| Aspirational pts each | ~1.11 | ~0.91 |
| New criteria | -- | C-18 (criterion-ID labels), C-19 (compliance gate) |
| Source signals | R3 V-02/V-03, V-04 | R4 E-2 (V-02 vs V-04 label delta), E-3 (V-05 audit gate) |
