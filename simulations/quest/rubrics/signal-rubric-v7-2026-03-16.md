**v7 written** to `simulations/quest/rubrics/signal-rubric-v7-2026-03-16.md`.

---

**One new criterion extracted from R7:**

**C-23 — Meta-rule inline evidence** (aspirational / depth)

Each RULE that enforces a meta-criterion (C-20, C-21, or C-22) must carry inline evidence: either a quoted string from the artifact it verifies, or an explicit RULE number reference. Without it, compliance verification requires a search; with it, verification is O(1) at the point of enforcement.

- **V-05 PASS** — all three meta-rules carry inline evidence (RULE 12 quotes RULE 9's count assertion; RULE 13 quotes the "14/14" gate string; RULE 14 names RULE 11 by number)
- **V-03 PARTIAL** — RULE 14 (C-22) names RULE 11, but RULE 12 (C-20) and RULE 13 (C-21) carry no forward references
- **V-04 FAIL** — meta-rules state requirements but carry no inline evidence
- **V-01/V-02 FAIL** — missing RULE entries for C-21/C-22, so C-23 is moot

**Formula**: aspirational_pass / 15 x 10 (~0.67 pts each, was ~0.71)
ential | coverage | Every sub-skill has a one-line description in non-bare mode |
| C-04 | essential | behavior | `/signal <namespace>` filters to that namespace only |
| C-05 | essential | behavior | `/signal --bare` produces only command names |
| C-06 | recommended | depth | Descriptions are specific and differentiating -- no two are interchangeable across namespaces |
| C-07 | recommended | format | Visual hierarchy -- sub-skills subordinate to namespace headers |
| C-08 | recommended | behavior | Routing hint per namespace ("describe your need") |
| C-09 | aspirational | format | Skill count embedded in namespace header line |
| C-10 | aspirational | depth | T3 tier annotations on T3-only skills |
| C-11 | aspirational | format | Namespace purpose tagline appended to the count header (e.g., `-- discover what's true before you design`) |
| C-12 | aspirational | format | Routing hints formatted as Markdown blockquote (`>`) rather than inline prose |
| C-13 | aspirational | depth | Descriptions reference quantified output artifacts -- specific counts, named deliverables, or rated outputs |
| C-14 | aspirational | depth | Descriptions are bi-directional -- each specifies both the mechanism (what the skill does) AND the deliverable (what you receive) |
| C-15 | aspirational | format | Namespace taglines are mutually distinguishable -- no two taglines are interchangeable across namespaces |
| C-16 | aspirational | format | The bidir split is enforced by a visual separator (`->`) in every description |
| C-17 | aspirational | depth | All description quality rules consolidated into an explicit numbered list (RULE 1 through RULE N) in the skill output |
| C-18 | aspirational | depth | Each RULE labeled with its rubric criterion ID (C-NN), making criterion-to-rule mapping invertible by inspection |
| C-19 | aspirational | behavior | Quality contract includes a named compliance checkpoint that explicitly gates output generation with "invalid output / do not proceed" language |
| C-20 | aspirational | depth | The RULE enforcing C-17 contains a self-verifying count assertion stating the exact rule count and criterion range covered |
| C-21 | aspirational | behavior | The compliance gate states the explicit quantified PASS threshold ("N/N checked = valid output") in addition to the FAIL gate |
| C-22 | aspirational | depth | The gate criterion (C-19) is itself represented as a numbered RULE entry in the quality contract, completing the bijection |
| C-23 | aspirational | depth | Each RULE that enforces a meta-criterion (C-20, C-21, C-22) carries inline evidence -- a quoted string or explicit RULE number -- pointing to the artifact it verifies |

---

## Scoring Formula

```
score = (essential_pass / 5 x 60)
      + (recommended_pass / 3 x 30)
      + (aspirational_pass / 15 x 10)
```

- Essential tier: 60 points max (12 pts each)
- Recommended tier: 30 points max (10 pts each)
- Aspirational tier: 10 points max (~0.67 pts each)
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

Rationale: Two variations with identical scores should not be structurally equivalent when one is auditable in O(1) and the other requires O(N) inference. C-18 discriminates this structural advantage.

FAIL if RULE labels are present but criterion IDs are absent. PARTIAL if criterion IDs are present on some but not all rules.

---

### C-19 -- Compliance checkpoint gates output generation (aspirational / behavior)

The skill must include a named compliance checkpoint -- a checklist or equivalent verification block -- that explicitly gates output generation. The gate must state, in the skill itself, that all items must be resolved before the model proceeds (e.g., "All 15 boxes checked = valid output. Any unchecked box = invalid output; do not proceed."). A numbered rule list without a gate does not satisfy this criterion even if it satisfies C-17 and C-18.

Rationale: A model reading rules may proceed despite non-compliance; a model encountering an explicit "do not proceed" gate must resolve each item. This is a qualitatively different failure-prevention mechanism not captured by rule-list compliance alone.

FAIL if compliance is enforced only via rule-following instructions with no named gate. PARTIAL if a gate is present but does not include explicit "invalid output / do not proceed" language.

---

### C-20 -- Self-verifying count assertion in the C-17 rule (aspirational / depth)

The RULE that enforces C-17 (the explicit-rule-set rule) must contain a count assertion stating the exact total number of rules and the range of criterion IDs covered -- e.g., "This list contains exactly 15 rules, one per aspirational criterion C-09 through C-23. Count = 15. None outside." The assertion must be embedded in the RULE itself, not only in a preamble or header.

Rationale: C-17 requires rules to be enumerated. C-20 requires the enumeration to be self-validating -- the count is machine-checkable by comparing the stated total against the actual count of RULE entries. A rule set that asserts "N rules covering C-09 through C-NN" can be verified in O(1): count the rules, compare to the stated total, verify the range endpoints. A rule set without this assertion requires O(N) inspection to confirm completeness. The structural difference is real even when both satisfy C-17. Source: V-03 R6 -- RULE 9 (C-17) states "Exactly 11 rules, one per aspirational criterion C-09 through C-19. Count = 11."

FAIL if the count and criterion range are not asserted explicitly within the RULE enforcing C-17.

---

### C-21 -- Quantified pass threshold in compliance gate (aspirational / behavior)

The compliance gate (C-19) must include an explicit quantified PASS condition -- a fraction of the form "N/N boxes checked = valid output" -- in addition to the required FAIL gate. C-19 requires "any unchecked box = invalid output; do not proceed." C-21 requires the complementary PASS threshold to be stated explicitly in the same gate block, making both halves of the gate binary explicit.

Rationale: A gate that states only the failure condition leaves the pass condition implicit ("if no failures, proceed"). Making the pass condition explicit -- "15/15 checked = valid output" -- converts the gate from a failure-only block into a complete binary decision contract: one branch for pass, one for fail, both stated. Source: V-04 R6 -- COMPLIANCE AUDIT includes "11/11 checked = valid output" threshold line paired with failure gate.

FAIL if the compliance gate states only the failure condition without an explicit "N/N = valid output" pass threshold.

---

### C-22 -- Gate criterion self-represented as a RULE entry (aspirational / depth)

The criterion that mandates the compliance gate (C-19) must itself appear as a numbered RULE entry in the quality contract (e.g., `RULE 11 (C-19): Output must be preceded by a COMPLIANCE AUDIT checkpoint...`). A quality contract that contains C-19's gate block but does not include a corresponding RULE (C-19) entry does not satisfy this criterion.

Rationale: C-18 requires every criterion to have a labeled RULE. C-19 is a criterion. A quality contract that enforces C-19 via a gate block but does not include RULE N (C-19) violates C-18's bijection requirement through the gate criterion specifically. Without C-22, the gate criterion is represented in the contract as a gate block but absent from the rule list, breaking the bijection: the gate checks N boxes, but the rule list covers only C-09 through C-18. Source: V-02 R6 -- adds RULE 11 (C-19) to restore the one-to-one bijection that V-01's 10-rule set (covering only C-09 through C-18) had broken.

FAIL if C-19 is enforced only via a gate block with no corresponding numbered RULE entry. PARTIAL if RULE N (C-19) is present but the gate block does not meet the "invalid output / do not proceed" standard required by C-19.

---

### C-23 -- Meta-rule inline evidence (aspirational / depth)

Each RULE entry that enforces a meta-criterion (C-20, C-21, or C-22) must carry inline evidence: either a quoted string from the artifact it verifies, or an explicit named reference (RULE number) to the artifact's location. A meta-rule that states a requirement without pointing to its evidence artifact does not satisfy this criterion.

Rationale: C-20, C-21, and C-22 each verify a specific artifact embedded in the quality contract (the count assertion in RULE (C-17), the pass-threshold string in the gate block, the RULE entry for C-19 respectively). Without inline evidence, a compliance checker verifying any of these meta-criteria must search the entire contract to locate the artifact and confirm the requirement. With inline evidence, the artifact is quoted or named at the point of enforcement, making each meta-verification O(1) without search. V-05 R7 demonstrates the pattern: RULE 12 (C-20) quotes RULE 9's exact count assertion verbatim; RULE 13 (C-21) quotes the "14/14 checked = valid output" string from the gate block; RULE 14 (C-22) names RULE 11 by number ("find RULE 11 (C-19) above and confirm it exists"). The structural advantage over V-04 (no forward references) and V-03 (only C-22's RULE carries a reference) is real even when all three pass C-20, C-21, and C-22.

PASS if all three meta-rules (RULE for C-20, RULE for C-21, RULE for C-22) carry inline evidence.
PARTIAL if some but not all meta-rules carry inline evidence (as in V-03 R7: RULE (C-22) names RULE 11, but RULE (C-20) and RULE (C-21) do not quote or reference their artifacts).
FAIL if no meta-rule carries inline evidence.

---

## Summary of Changes v6 -> v7

| | v6 | v7 |
|--|--|--|
| Aspirational count | 14 | 15 |
| Aspirational denominator | /14 | /15 |
| Aspirational pts each | ~0.71 | ~0.67 |
| New criteria | -- | C-23 |
| Source signals | R6 V-03 (C-20), V-04 (C-21), V-02 (C-22) | R7 V-05 (C-23) |
| Discrimination target | v5 could not separate V-02/V-04/V-05 on meta-structure | v7 separates V-05 (PASS) from V-03 (PARTIAL) and V-04 (FAIL) on meta-rule evidence |

### New criterion rationale

**C-23** (V-05 R7 pattern): C-20, C-21, and C-22 each require a meta-rule to enforce a structural property of a specific named artifact. A meta-rule can satisfy C-20 by asserting "RULE (C-17) must contain a count" -- this states the requirement. C-23 requires more: the meta-rule must also carry the evidence, by quoting the artifact's exact string or naming its RULE number. The distinction is between *stating a requirement* and *anchoring the requirement to its evidence*. V-05's three meta-rules all anchor; V-03's RULE (C-22) anchors but RULE (C-20) and RULE (C-21) do not; V-04's meta-rules none anchor. This three-way discrimination was invisible to v6.
