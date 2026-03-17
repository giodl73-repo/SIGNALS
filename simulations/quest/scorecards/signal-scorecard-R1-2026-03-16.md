## Scorecard: /signal (Round 1)

---

### Rubric Reference

| ID | Weight | Category | Criterion |
|----|--------|----------|-----------|
| C-01 | essential | correctness | All 12 namespaces present |
| C-02 | essential | correctness | Sub-skill counts match canonical |
| C-03 | essential | coverage | Every sub-skill has one-line description (non-bare) |
| C-04 | essential | behavior | `/signal <ns>` filters to that namespace only |
| C-05 | essential | behavior | `/signal --bare` produces command names only |
| C-06 | recommended | depth | Descriptions specific and differentiating |
| C-07 | recommended | format | Visual hierarchy — sub-skills subordinate to headers |
| C-08 | recommended | behavior | Routing hint per namespace |
| C-09 | aspirational | format | Skill count in namespace header |
| C-10 | aspirational | depth | T3 tier annotations on T3-only skills |

Scoring formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)`

---

### V-01 — Output Format: Indented List

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 12 namespaces listed in explicit data section (`scout -- 8 skills:` through `org -- 4 skills:`) |
| C-02 | PASS | Counts match canonical exactly: scout(8), draft(4), review(4), flow(7), trace(7), prove(9), listen(3), program(2), topic(6), quest(4), mock(3), org(4) |
| C-03 | PASS | Every sub-skill has `->` description; no bare names in the data section |
| C-04 | PASS | "FILTERED MODE: When a namespace argument is present, output only that namespace's section. One namespace block." |
| C-05 | PASS | "BARE MODE: output only slash-command names as a flat list. One command per line. No descriptions. No headers." |
| C-06 | PASS | Descriptions are specific: "competitive landscape analysis leading with inertia as primary competitor", "technical feasibility with traffic-light ratings and team/timeline assessment" — distinct across all namespaces |
| C-07 | PASS | Namespace header line (`scout -- 8 skills:`) at one level; sub-skills indented with `->` arrow — clear subordination |
| C-08 | PASS | Per-section: "Run any sub-skill directly, or describe your `<domain noun>` and the most relevant `<namespace>` skill will run." Present for all 12 sections |
| C-09 | PASS | Data section explicitly includes count in every namespace header (`scout -- 8 skills:`, `draft -- 4 skills:`, ...) |
| C-10 | FAIL | No T3 annotations anywhere in the skill body |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 1/2 × 10 = **5**
**Composite: 95** ✅ Golden

---

### V-02 — Phrasing Register: Declarative/Imperative

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 12 namespace sections in registry: Scout through Org, all present |
| C-02 | PASS | Header counts match: `## Scout namespace -- 8 skills` ... `## Org namespace -- 4 skills` — all match canonical |
| C-03 | PASS | Every skill has `--` description; format rule 5: "Do not omit skills" enforces completeness |
| C-04 | PASS | "4. Filtered mode: emit only the matching namespace section. Same structure as full." |
| C-05 | PASS | "3. Bare mode: one command name per line, no headers, no descriptions. Format: `/<command-name>`" |
| C-06 | PARTIAL | Descriptions are specific but slightly terser than other variations; some entries truncated: `/prove-interview -- persona-driven stakeholder interview simulation` (missing "grounded in documented roles"), `/scout-compliance -- regulatory and policy scan before design begins` (missing enforcement risk). No 3+ generic in one namespace, but lower resolution. |
| C-07 | PASS | `##` headers with backtick-formatted entries below — strong markdown visual hierarchy |
| C-08 | PASS | Footer per section: `> Describe your discovery need and the relevant scout skill will run.` — present across all 12 |
| C-09 | PASS | `## Scout namespace -- 8 skills` etc. — count inline in every header |
| C-10 | FAIL | No T3 annotations |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 2.5/3 × 30 = **25** (C-06 as PARTIAL = 0.5)
**Aspirational**: 1/2 × 10 = **5**
**Composite: 90** ✅ Golden

---

### V-03 — Visual Hierarchy: Section Headers with Counts

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 12 namespace sections present with `###` headers |
| C-02 | PASS | `### Scout -- 8 skills`, `### Draft -- 4 skills` etc. — all match canonical counts |
| C-03 | PASS | Every skill has a description; the format rule states "Descriptions must name the concrete output artifact or method" |
| C-04 | PASS | "FILTERED MODE (when /signal `<namespace>`): Print only the section for that namespace. Same structure as full index. One section only." |
| C-05 | PASS | "BARE MODE OUTPUT (when --bare): Print all 61 command names as a flat list. One per line. No descriptions. No headers. No tips." |
| C-06 | PASS | Descriptions are the most specific of all non-V-05 variations: "Competitive landscape map leading with inertia as primary competitor, then 5-8 named competitors with threat ratings", "Name shortlist with trademark clearance, domain availability, and per-persona scoring" — quantified artifacts throughout |
| C-07 | PASS | `###` headers (stronger than `##` of V-02/V-04) with flush-left skill entries below — clearest section delineation |
| C-08 | PASS | `> Tip: describe your discovery need and the most relevant scout skill will run.` — present in all 12 sections |
| C-09 | PASS | `### Scout -- 8 skills -- discover what's true before you design` — count + purpose phrase in every header |
| C-10 | FAIL | No T3 annotations |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 1/2 × 10 = **5**
**Composite: 95** ✅ Golden

---

### V-04 — Routing-First + Count Headers

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 12 namespaces in `NAMESPACE SECTIONS` block |
| C-02 | PASS | `## /scout -- 8 skills for discovery and research` etc. — all counts correct |
| C-03 | PASS | Every skill has `->` description in the skill registry |
| C-04 | PASS | "FILTERED MODE: When given a namespace name, output only that namespace's section (including routing tip). No routing guide, no other sections." |
| C-05 | PASS | "BARE MODE: When --bare, output only command names. One per line. No descriptions, headers, or routing text." |
| C-06 | PASS | Descriptions specific: "/quest-golden -> full optimization loop: variate -> score -> extract -> evolve rubric -> converge", "/trace-contract -> expected vs actual output comparison with mismatch severity per delta" — concrete artifacts, no duplicates |
| C-07 | PASS | `##` section headers with indented `->` entries — clear two-level hierarchy |
| C-08 | PASS | Best C-08 among V-01–V-04: global routing decision tree at top ("Research & Discovery -> /scout (8 skills)") PLUS per-section tips in every namespace block |
| C-09 | PASS | `## /scout -- 8 skills for discovery and research` — count in every header |
| C-10 | FAIL | No T3 annotations |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 1/2 × 10 = **5**
**Composite: 95** ✅ Golden

---

### V-05 — Full Integration

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 12 namespaces in output, Scout through Org |
| C-02 | PASS | All header counts match canonical: `## Scout namespace -- 8 skills` ... `## Org namespace -- 4 skills` |
| C-03 | PASS | Every skill has `->` description; some are the most detailed of all variations |
| C-04 | PASS | "FILTERED MODE: print only the matching namespace section (including its routing tip). Include the T3 annotations. Omit the routing guide and all other sections." |
| C-05 | PASS | "BARE MODE: print all 61 command names, one per line, no other text. Begin with /scout-competitors and end with /org-committee." — most precise bare-mode spec |
| C-06 | PASS | Highest specificity across all variations: `/scout-competitors -> ...5-8 rivals with threat ratings (HIGH/MEDIUM/LOW)`, `/trace-contract -> three-directory expected-vs-actual comparison with mismatch severity per delta`. Artifacts quantified and method-named throughout. |
| C-07 | PASS | `##` headers with purpose phrase + indented entries — strong hierarchy; purpose phrase adds orientation beyond just a count |
| C-08 | PASS | Global routing decision tree at top ("What are you trying to do? → Research before committing → /scout...") plus per-section routing tip in every namespace block — deepest C-08 implementation |
| C-09 | PASS | `## Scout namespace -- 8 skills -- discover what's true before you design` — count present in every header |
| C-10 | PASS | 24 skills carry `*(T3)*` annotation; T3 list explicitly defined in the prompt: `T3 ANNOTATION RULE: skills whose full runbook loads on demand carry *(T3)*` |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 2/2 × 10 = **10**
**Composite: 100** ✅ Golden

---

### Leaderboard

| Rank | ID | Composite | All Essential | Notes |
|------|----|-----------|---------------|-------|
| 1 | V-05 | **100** | ✅ | Only variation to pass C-10; strongest C-08 and C-06 |
| 2 | V-03 | **95** | ✅ | Most specific descriptions + `###` visual hierarchy; second-strongest C-06 |
| 3 | V-04 | **95** | ✅ | Best C-08 among non-V-05 (global routing guide + per-section tips) |
| 4 | V-01 | **95** | ✅ | Solid, familiar format; no clear differentiation from V-04 |
| 5 | V-02 | **90** | ✅ | Imperative precision is clean but descriptions slightly truncated; C-06 PARTIAL |

---

### Excellence Signals — V-05

**What made V-05 the best:**

1. **Global routing decision tree before namespace sections** — the "What are you trying to do?" guide with all 12 category-to-namespace mappings lets users orient at the macro level without reading individual namespace sections. Users who don't know the taxonomy get an immediate entry point. This is structurally different from per-section routing tips: it's a navigation layer above the index itself.

2. **T3 annotation as expectation management** — `*(T3)*` on 24 skills tells users before they run a skill that an extended runbook loads on demand. This prevents surprise on first invocation and helps users plan session depth. It answers a question users have ("which of these are the big ones?") that the index alone doesn't surface.

3. **Purpose phrase in namespace headers** — `-- gather evidence before claiming something is true` in the header adds orientation meaning that a bare count doesn't. It answers "why would I use this namespace?" at a glance. All other variations either omit the phrase or use briefer "for X" suffixes.

4. **Bare mode order contract** — "Begin with /scout-competitors and end with /org-committee" eliminates any ambiguity about ordering. Other variations say "one per line" but leave ordering implicit.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["global routing decision tree before namespace sections answers macro orientation before users read any namespace detail", "T3 tier annotation in the index itself manages runbook-load expectations before first invocation"]}
```
