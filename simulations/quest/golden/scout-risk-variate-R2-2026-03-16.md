---
skill: quest-variate
skill_target: scout-risk
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/scout-risk-rubric-v2-2026-03-16.md
axes_explored: [output-format (IF-THEN likelihood syntax), phrasing-register (mitigation taxonomy), lifecycle-emphasis (structured interdependency section), output-format+phrasing-register, full-integration]
---

# scout-risk — Prompt Variations R2

Five complete, runnable skill body prompts. Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

**R2 context**: Round 1 produced three GOLDEN variations (V-03 at 92.5, V-04 at 92.5, V-05 at 97.5). The v2 rubric adds three new aspirational criteria — C-11 (zero-generic mitigations), C-12 (all likelihoods trigger-qualified), C-13 (interdependencies in a dedicated section with ≥2 named links). Each R2 variation isolates one mechanism targeting exactly one of the new criteria, built on R1's proven GOLDEN baseline (V-03 R1).

---

## V-01 — Axis: Output Format (IF-THEN likelihood syntax)

**Hypothesis**: Requiring every likelihood field to use explicit "IF [condition], THEN this risk activates." syntax structurally prevents bare probability labels ("high", "possible", "~30%"). The IF forces the model to name the triggering scenario, not rate the probability. Built on V-03 R1's imperative base (proven GOLDEN at 92.5). Expected new criterion unlocked: C-12 (all likelihoods trigger-qualified).

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Here is the exact sequence to follow.

**First: write the inertia risk.**

The inertia risk is always entry #1. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip this. Do not move it. Do not bury it after technical risks. Write it first.

Give it:
- Severity: one of HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [name the specific condition that would make status quo win] THEN this risk activates.
- Mitigation: name what the team should do to test whether inertia applies before building

**Second: write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5–10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition or scenario that triggers this risk] THEN this risk activates.
- Mitigation: a concrete action — not "monitor the situation", not "be careful", not "consider alternatives"

**Likelihood rule — no exceptions:** Every likelihood must begin with "IF". Not "this is high because...", not "~30%", not "possible when...", not "likely if...". The IF-THEN form forces you to name the condition that activates the risk, not rate it. If you write a likelihood without "IF", rewrite it.

Sort the dimensional risks from highest to lowest severity.

**Third: check your mitigations.**

Read back every mitigation you wrote. If two or more say something like "monitor closely", "keep an eye on", "revisit later", or "consider alternatives" — replace them. A mitigation must name what someone should do or check, not that something should happen eventually.

**Fourth (only if AMEND is in the prompt):**

If the prompt contains AMEND: focus on [dimension], remove all dimensional risks except that dimension. Keep inertia.
If the prompt contains AMEND: adjust severity threshold to [level], remove risks below that level. Keep inertia.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-02 — Axis: Phrasing Register (mitigation taxonomy)

**Hypothesis**: Requiring every mitigation to select a named type from {Spike / Validate / Gate / Contract / Cut / Instrument} before writing the action makes generic hedges structurally impossible. A "Spike" has a time box and a question; a "Gate" has a criterion. The taxonomy acts as a pre-commitment that forces specificity before prose is written. Built on V-03 R1's imperative base. Expected new criterion unlocked: C-11 (zero-generic mitigations, full register).

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Here is the exact sequence to follow.

**First: write the inertia risk.**

The inertia risk is always entry #1. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip this. Do not move it. Write it first.

Give it:
- Severity: one of HIGH, MEDIUM, or LOW — nothing else
- Likelihood: name the specific condition that would make status quo win
- Mitigation type: one of → Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Second: write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5–10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: what specific condition or scenario triggers this risk
- Mitigation type: one of → Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Mitigation type definitions:**
- Spike: time-boxed technical experiment to reduce a named unknown (e.g., "2-day spike on SDK rate-limit behavior under concurrent load")
- Validate: user or stakeholder test that confirms or kills an assumption (e.g., "5 interviews with target personas to confirm they feel the pain")
- Gate: go/no-go checkpoint before the next phase (e.g., "legal sign-off gate before public launch")
- Contract: formal agreement with a named party (e.g., "SLA with vendor covering 99.9% uptime and data residency")
- Cut: remove the risky element from scope entirely (e.g., "cut SSO integration to v1.1; ship with API key auth only")
- Instrument: add observability producing a named metric (e.g., "track daily active signals per topic; alert if < 3/week per active user")

**Forbidden mitigation words — replace before you proceed:**
"monitor closely" / "keep an eye on" / "revisit later" / "consider alternatives" / "be careful" / "evaluate options". These name no action and have no owner. Selecting a mitigation type first eliminates them: a Spike has a question to answer; a Gate has a criterion to pass.

Sort the dimensional risks from highest to lowest severity.

**Third: check your mitigations.**

Read back every mitigation type. Verify each matches its definition. Verify no forbidden words appear anywhere in the mitigation text. Replace any that fail this check.

**Fourth (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — drop all dimensional risks not in that dimension. Keep inertia.
AMEND: adjust severity threshold to [level] — drop risks below that level. Keep inertia.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-03 — Axis: Lifecycle Emphasis (structured interdependency section)

**Hypothesis**: Making the interdependency section mandatory — with a named heading, minimum 2 compound pairs, explicit format, and an explicit rule that "if you can only find 1, your risks are not specific enough" — upgrades interdependency from an afterthought to a structural phase. The minimum-2 rule and the specificity smell-test force the model to name both risks in a compound pair rather than vague cross-reference notes. Built on V-03 R1's imperative base. Expected new criterion unlocked: C-13 (interdependencies in a dedicated section with ≥2 named links).

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register organized in three phases. Complete each phase before starting the next.

**Phase 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry. It is the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Give it:
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: name the specific condition that would make status quo win
- Mitigation: name what the team should do to test whether inertia applies before building

**Phase 2: Write the dimensional risks.**

List at least one risk each from 3 or more of these dimensions: Technical, Market, Compliance, Dependency, Timeline.

For each risk, provide:
- Name: a short label (5–10 words)
- Dimension: which of the five it belongs to
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: what specific condition or scenario triggers this risk — not just "possible"
- Mitigation: a concrete action — not "monitor the situation", not "be careful", not "consider alternatives"

Read back every mitigation. If two or more are generic non-actions, replace them.

Sort dimensional risks from highest to lowest severity.

**Phase 3: Write the Risk Interdependencies section (mandatory).**

After the risk register entries, write a section with this exact heading:

## Risk Interdependencies

This section must contain at least 2 named compound-risk pairings. Use this format for each:

> If [Risk A: name it explicitly] materializes, [Risk B: name it explicitly] escalates to [HIGH / MEDIUM / LOW] because [one-clause reason].

Enforcement rules:
- Do not scatter interdependencies as footnotes inside individual risk entries. They belong here only, in this named section.
- At least 2 pairings are required. If you can only find 1 after reviewing all entries, your risks are not specific enough — go back and make them more concrete before returning to this section.
- "If technical risks compound" is not a valid pairing — both risks must be named explicitly by title.
- A pairing must state a severity direction (escalates to HIGH, escalates to MEDIUM, etc.).

**Phase 4 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia and the ## Risk Interdependencies section, drop all dimensional risks outside that dimension.
AMEND: adjust severity threshold to [level] — keep inertia and the ## Risk Interdependencies section, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-04 — Axes: Output Format + Phrasing Register (IF-THEN likelihood + mitigation taxonomy)

**Hypothesis**: The two enforcement mechanisms from V-01 and V-02 are orthogonal — IF-THEN targets the likelihood field (C-12), taxonomy targets the mitigation field (C-11). Neither interferes with the other. Combining them in a single prompt should produce both C-11 PASS and C-12 PASS simultaneously. Built on V-03 R1's imperative base with a unified self-check gate.

---

```
Auto-detect the topic from repo context. Do not ask.

Build a risk register. Every risk entry must pass two non-negotiable quality gates: the likelihood must name a triggering condition using IF-THEN syntax, and the mitigation must be typed from a named vocabulary.

**Step 1: Write the inertia risk (mandatory, first).**

The inertia risk is always the first entry — the risk that the status quo was good enough and this feature is the wrong thing to build. Do not skip it. Do not move it.

Format:
- Dimension: Inertia
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific condition that makes status quo win], THEN this risk activates.
- Mitigation type: one of → Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Step 2: Write the dimensional risks.**

Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline.

For each risk:
- Dimension: which of the five it belongs to
- Risk name: a short label (5–10 words)
- Severity: HIGH, MEDIUM, or LOW — nothing else
- Likelihood: IF [specific triggering condition or scenario], THEN this risk activates.
- Mitigation type: one of → Spike / Validate / Gate / Contract / Cut / Instrument
- Mitigation: one sentence naming exactly what to do

**Likelihood enforcement — no exceptions:**
Every likelihood must begin with "IF". Not "this is high because...", not "~30%", not "possible", not "likely if...". The IF-THEN form names the condition that activates the risk, not a probability rating. If you write a likelihood without "IF", rewrite it before continuing.

**Mitigation type definitions:**
- Spike: time-boxed experiment to reduce a named technical unknown
- Validate: user/stakeholder test that confirms or kills an assumption
- Gate: go/no-go checkpoint before the next phase
- Contract: formal agreement with a named party (SLA, API contract, compliance sign-off)
- Cut: remove the risky element from scope entirely
- Instrument: add observability producing a named metric (not passive monitoring)

**Forbidden mitigation words — replace before proceeding:**
"monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". Selecting a type first eliminates these: a Spike has a question to answer; a Gate has a criterion to pass; an Instrument has a metric name.

Sort dimensional risks from highest to lowest severity.

**Step 3: Note at least one interdependency.**

Identify at least one pairing where two risks compound each other:
"If [Risk A] materializes, [Risk B] escalates to [severity]."

If none exist, write: "No compound risks identified."

**Step 4: Self-check.**

Before writing the artifact, verify each item:
- [ ] Inertia is entry 0, before all dimensional risks
- [ ] Every severity is only HIGH, MEDIUM, or LOW
- [ ] At least 3 dimensions covered
- [ ] Every likelihood starts with "IF"
- [ ] Every mitigation has a named type from the approved list
- [ ] No forbidden mitigation words in any entry
- [ ] Risks sorted high-to-low after inertia

Fix any violation before proceeding.

**Step 5 (only if AMEND is in the prompt):**

AMEND: focus on [dimension] — keep inertia, drop all non-matching dimensions.
AMEND: adjust severity threshold to [level] — keep inertia, drop risks below that level.

**Write the artifact to:** simulations/scout/risk/{topic}-risk-{date}.md
```

---

## V-05 — Axes: Full Integration (R1 V-05 base + IF-THEN likelihood + mitigation taxonomy + structured interdependency section)

**Hypothesis**: Building on R1's highest-scoring variation (V-05 at 97.5) as a structural foundation and layering in all three R2 mechanisms — IF-THEN likelihood syntax (C-12), mitigation taxonomy (C-11), and mandatory structured interdependency section with ≥2 named pairs (C-13) — should convert all three new aspirational criteria to PASS and reach maximum attainable score under v2 rubric. The self-check gate from R1 V-05 is extended to cover the new enforcement rules. The roles-and-table structure is retained as it provides the strongest multi-dimensional coverage.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal artifacts). Do not prompt unless context is absent.

Build a risk register. Follow these steps in order. Do not skip any step.

---

**STEP 1 — INERTIA RISK (mandatory, always first)**

Write the inertia risk before anything else. The inertia risk is: the risk that the status quo is good enough and this feature is the wrong thing to build.

Run the Skeptic lens: given what this topic does and who it is for, what does the team or user do instead? How sticky is that alternative? What does building this cost relative to the value it delivers?

Output the inertia risk in this exact format:

**0. Inertia — [one-line risk title]**
- Dimension: Inertia
- Severity: HIGH / MEDIUM / LOW
- Likelihood: IF [specific condition that makes inertia win], THEN this risk activates.
- Mitigation type: [Spike / Validate / Gate / Contract / Cut / Instrument]
- Mitigation: [1 sentence naming the concrete pre-build test or gate]

---

**STEP 2 — DIMENSIONAL RISKS (3 roles, table output)**

Run three analyst roles. Each contributes risks from their lens. Then merge all into a single table.

Roles:
- **Skeptic** (Market, Compliance): why will this fail to deliver value?
- **Realist** (Technical, Dependency): what will break during build?
- **Scheduler** (Timeline, cross-check Dependency): what will slip the date?

Cover at least 3 of the 5 dimensions: Technical, Market, Compliance, Dependency, Timeline.

Merge all role contributions into this table, sorted by severity descending after inertia:

| # | Dimension | Risk | Severity | Likelihood | Mitigation Type | Mitigation |
|---|-----------|------|----------|------------|-----------------|------------|

**Likelihood rule — no exceptions:** Every likelihood must be written as "IF [condition], THEN this risk activates." Not "high", not "possible", not "may occur", not "likely when". The IF forces you to name the scenario that triggers the risk, not rate a probability. If you draft a likelihood without "IF", rewrite it before adding the row.

**Mitigation type rule — no exceptions:** Every mitigation must carry a named type from: Spike / Validate / Gate / Contract / Cut / Instrument.

Type definitions:
- Spike: time-boxed experiment to reduce a named technical unknown
- Validate: user/stakeholder test that confirms or kills an assumption
- Gate: go/no-go checkpoint before the next phase
- Contract: formal agreement with a named party (SLA, API contract, compliance sign-off)
- Cut: remove the risky element from scope entirely
- Instrument: add observability producing a named metric (not passive monitoring)

**Forbidden mitigation text — replace on sight:** "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "be careful", "evaluate options". These are not mitigations — they name no action and have no owner. If you draft one, replace it with a typed mitigation before continuing.

---

**STEP 3 — RISK INTERDEPENDENCIES (mandatory section)**

Write this section with the exact heading:

## Risk Interdependencies

List at least 2 compound-risk pairings. Each pairing must name both risks explicitly and give a one-clause reason. Format:

- If [Risk A: name it by title] materializes, [Risk B: name it by title] escalates to [HIGH / MEDIUM / LOW] because [one-clause reason].

Enforcement rules:
- Do not put interdependency notes inside individual table rows. This section is the only place they appear.
- Minimum 2 named pairs. If you find only 1 after reviewing all rows, your risks are too generic — revise them to be more specific before returning here.
- "If technical risks compound other risks" is not a valid pairing. Both risks must be named by their exact title from the table.

---

**STEP 4 — SELF-CHECK**

Before writing the artifact, verify every item:
- [ ] Inertia is row 0, before any Technical/Market/Compliance/Dependency/Timeline risk
- [ ] Severity values are only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels
- [ ] At least 3 dimensions covered in the table
- [ ] Every likelihood row starts with "IF" — scan every row; no bare probability labels
- [ ] Every row in the table has a named Mitigation Type from the approved list
- [ ] Zero instances of forbidden mitigation text anywhere in the register
- [ ] Rows after inertia sorted high-to-low severity
- [ ] ## Risk Interdependencies section exists with at least 2 explicitly named compound-risk pairs

Fix any violation before proceeding.

---

**STEP 5 — AMEND (if present in prompt)**

AMEND: focus on [dimension] — keep inertia (row 0) and the ## Risk Interdependencies section, remove all rows not matching [dimension]. Re-sort.
AMEND: adjust severity threshold to [level] — keep inertia (row 0) and the ## Risk Interdependencies section, remove rows below [level]. Re-sort.

---

Write artifact to: simulations/scout/risk/{topic}-risk-{date}.md
```

---

## Variation Summary (v2 rubric projection)

The v2 rubric adds 5 aspirational criteria (C-09 through C-13) each worth 2 points. C-11/C-12/C-13 are the new additions. C-10 (AMEND) remains PARTIAL on all base prompts — it requires a live AMEND directive to demonstrate.

| ID | Axis | New Mechanism | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Score | Golden |
|----|------|---------------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | Output format | IF-THEN on every likelihood | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PARTIAL | PARTIAL | **PASS** | FAIL | ~94 | YES |
| V-02 | Phrasing register | Mitigation taxonomy + forbidden words | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PARTIAL | **PASS** | PARTIAL | FAIL | ~94 | YES |
| V-03 | Lifecycle emphasis | Mandatory interdependency section >=2 pairs | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | **PASS** | ~97 | YES |
| V-04 | Output format + Phrasing register | IF-THEN + taxonomy | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **PASS** | **PASS** | FAIL | ~97 | YES |
| V-05 | Full integration | IF-THEN + taxonomy + structured section | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | **PASS** | **PASS** | **PASS** | ~99 | YES |

### Score calculations (v2 rubric)

- **Essential** (C-01–C-05): 60 pts, 5/5 pass on all R2 variations (R1's GOLDEN base carries forward)
- **Recommended** (C-06–C-08): 30 pts, 3/3 pass on all R2 variations
- **Aspirational** (C-09–C-13): 10 pts, 2 pts each; C-10 always PARTIAL (1 pt)

| ID | Essential | Recommended | Aspirational breakdown | Aspirational total | Composite |
|----|-----------|-------------|------------------------|--------------------|-----------|
| V-01 | 60 | 30 | C-09:0, C-10:1, C-11:1, C-12:2, C-13:0 | 4 | **94** |
| V-02 | 60 | 30 | C-09:0, C-10:1, C-11:2, C-12:1, C-13:0 | 4 | **94** |
| V-03 | 60 | 30 | C-09:2, C-10:1, C-11:1, C-12:1, C-13:2 | 7 | **97** |
| V-04 | 60 | 30 | C-09:2, C-10:1, C-11:2, C-12:2, C-13:0 | 7 | **97** |
| V-05 | 60 | 30 | C-09:2, C-10:1, C-11:2, C-12:2, C-13:2 | 9 | **99** |

### Rankings

1. **V-05** — 99 — Full integration; C-10 is the only non-PASS (unreachable on a base prompt)
2. **V-03** — 97 — Lifecycle structure unlocks C-13 and C-09; IF-THEN absent so C-12 stays PARTIAL
3. **V-04** — 97 — IF-THEN + taxonomy unlocks C-11 and C-12; no dedicated section so C-13 fails
4. **V-01** — 94 — Cleanest single-axis proof: IF-THEN directly produces C-12; loses C-11 (no taxonomy)
5. **V-02** — 94 — Cleanest single-axis proof: taxonomy directly produces C-11; C-12 partial without IF

### R2 Design Notes

**Why all R2 variations project GOLDEN**: R1 identified V-03's imperative base as sufficient for all essential and recommended criteria. R2 singles inherit that base and only vary the new axis. All five are projected GOLDEN; the differentiation appears in aspirational scoring.

**C-11 vs C-05**: C-11 (zero-generic) is harder than C-05 (fewer than 2 generic). V-02 and V-05 target C-11 via taxonomy — selecting a type first eliminates the conditions under which generic text is produced, rather than catching it in a post-hoc re-read. This is a structural prevention rather than a detection-and-repair approach.

**C-12 vs C-07**: C-12 (all entries trigger-qualified) is harder than C-07 (≥ half). V-01 and V-05 use IF-THEN syntax as a structural enforcer. The IF acts as a required token that cannot be produced with bare probability labels, making compliance mechanical rather than probabilistic.

**C-13 vs C-09**: C-13 (dedicated section, ≥2 pairs) is harder than C-09 (at least one mention). V-03 and V-05 make the section mandatory, require ≥2 named pairs, and add a specificity smell-test ("if you find only 1, your risks are too generic") that indirectly raises risk quality across the full register.

**C-10 ceiling**: AMEND behavior (C-10) cannot reach PASS on a base prompt — it requires a live AMEND directive. The practical ceiling for base prompts is PARTIAL (1 pt). A separate AMEND-focused variation is needed to demonstrate C-10 PASS.

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["IF-THEN likelihood syntax: structural token prevents bare probability labels without relying on re-read", "mitigation taxonomy: type selection before prose eliminates generic hedges at generation time not repair time", "mandatory interdependency section with specificity smell-test: minimum pairs + revision gate raises risk quality across full register", "all R2 variations project GOLDEN because R1's imperative base (V-03-R1) carries essential+recommended; differentiation is aspirational-only"]}
```
