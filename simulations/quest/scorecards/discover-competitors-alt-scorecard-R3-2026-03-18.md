## discover-competitors-alt — R3 Scorecard

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 (tie) | **V-01** Token-first pre-declaration | **100** | YES |
| 1 (tie) | **V-02** Prose AMEND + STABILITY tag | **100** | YES |
| 1 (tie) | **V-04** Minimal combination | **100** | YES |
| 1 (tie) | **V-05** Full lifecycle + stability matrix | **100** | YES |
| 5 | **V-03** Conversational token contract | **98.33** | YES |

---

### C-13 / C-14 Breakdown

**V-03** is the only non-perfect scorer. Two PARTIAL verdicts:

- **C-13 PARTIAL** — Conversational `> **Token: [YOUR-TOKEN]**` format lacks code-block structural enforcement. Despite 4 explicit anti-examples and 5 positive examples, prose register introduces model variance; the model could produce a borderline phrase like `> **Token: the signal workflow lock**` that passes casual inspection.

- **C-14 PARTIAL** — "This check is required for every amendment -- not just one" is a prose imperative with no structural backstop. Unlike a table column (`[TOKEN] stable?`) or mandatory tag (`STABILITY:`), model can silently skip an entry.

All other variations have structural enforcement for both criteria.

---

### Excellence Signals (3 new patterns for R4)

1. **Pre-declaration makes token creation structurally prior** — Committing to `TOKEN: [identifier]` before writing C0 eliminates role-description drift because the identifier is committed before any mechanism description is written (V-01, V-04, V-05).

2. **Two-column stability matrix (verdict + evidence) prevents empty-form C-14 compliance** — V-05's separate evidence column closes the failure mode where a model writes "Stable" on every entry without reasoning. Both columns are required; a verdict without evidence fails the output contract.

3. **Domain-adaptive token naming encodes product context** — V-05 requiring `SIGNAL-LOCK` over `MECH` makes generic stability reasoning structurally wrong — the domain name in the token frames every downstream reference and prevents detachment from product context.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-declaration makes token creation structurally prior — committing to TOKEN identifier before C0 description begins eliminates role-description drift because the name exists before any description is written", "Two-column stability matrix (verdict + evidence) prevents empty-form C-14 compliance — requiring both verdict and supporting evidence closes the failure mode where model writes Stable without reasoning", "Domain-adaptive token naming encodes product context in the token identifier itself, making generic stability reasoning structurally wrong because the token name frames every downstream reference"]}
```
rcement via table column. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 6/6 → 10
**Composite: 100**
**Golden:** YES

---

### V-02 — Per-entry tagged stability field in prose AMEND

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | C0 section precedes Competitive Map section. |
| C-02 | 3+ named competitors with threat levels | PASS | "Rows 1-N are named external competitors -- minimum 3." Threat levels required on every row. |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | Whitespace Finding section present with specific dimension requirement. |
| C-05 | Auto-detect topic without prompting | PASS | "Read the repo context... Do not ask the user for the topic, competitors, or market category." |
| C-06 | Mechanism-level inertia reasoning | PASS | `INERTIA-REF: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description]`. Mechanism tied to C0 specifically. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | Prose AMEND with `Output effect:` line per entry. Three examples each name specific effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. |
| C-10 | Grounded findings | PASS | Third slot mandatory (`vs INERTIA-REF:`), requires competitive map to support. "Do not write general domain observations." |
| C-11 | Inertia reference propagates downstream | PASS | `vs INERTIA-REF` column in competitive map; `vs INERTIA-REF:` third slot in findings; `STABILITY:` line in AMEND references INERTIA-REF. |
| C-12 | AMEND evaluates inertia stability | PASS | Every AMEND entry has STABILITY line. C-12 at-least-one requirement exceeded. |
| C-13 | Inertia mechanism assigned portable token | PASS | INERTIA-REF is hardcoded as the fixed token in the template — eliminates model-choice variance entirely. "INERTIA-REF is the portable token for this analysis." It appears verbatim in column headers and finding slots. |
| C-14 | Inertia stability in every AMEND entry | PASS | Prose `STABILITY:` tag per entry with explicit instruction: "An amendment without it does not pass." Example format shows STABILITY line for all 3 entries. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 6/6 → 10
**Composite: 100**
**Golden:** YES

---

### V-03 — Portable token contract as opening obligation

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | "First: nail C0." / "Then: map at least 3 external competitors." Ordering explicit. |
| C-02 | 3+ named competitors with threat levels | PASS | "map at least 3 external competitors... Threat level: HIGH / MEDIUM / LOW -- be explicit." |
| C-03 | C0 at row 0 in competitive map | PASS | "Write C0 first. Always." Not a table-row specification, but structural ordering enforced by prose imperatives. |
| C-04 | Whitespace identified | PASS | "Name one specific gap... Don't say 'there's room to innovate' -- name the specific uncontested dimension." |
| C-05 | Auto-detect topic without prompting | PASS | "Start by reading the repo... Don't ask the user for the topic, competitors, or market category." |
| C-06 | Mechanism-level inertia reasoning | PASS | "explain the stickiness: what would users lose if they switched, what habit would break, or what workaround already covers most of the need." Mechanism tied to C0 behavior. |
| C-07 | Web-verified claim with inline citation | PASS | "Look up at least one competitor with WebSearch. Put the citation right next to that competitor -- not in a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | "Give at least 2 adjustments. For each: Say what the user changes as input. Say what changes in the output as a result -- be specific, not just 'you can adjust.'" |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. Focus-active handling present. |
| C-10 | Grounded findings | PASS | "Name a specific competitor from the map (or C0)... Don't write general domain observations that don't require the competitive analysis." |
| C-11 | Inertia reference propagates downstream | PASS | Obligation 2: "Use it verbatim in every finding -- in the third slot." Instructions require TOKEN in findings and AMEND. |
| C-12 | AMEND evaluates inertia stability | PASS | "Check your token: state whether the amendment would change what your token refers to, or leave it stable." Exceeds at-least-one requirement (applies to every entry). |
| C-13 | Inertia mechanism assigned portable token | PARTIAL | Opening contract gives 4 anti-examples and 5 valid examples. Format `> **Token: [YOUR-TOKEN]**` is conversational blockquote, not a code block. Risk: model could produce borderline phrasing (e.g., `> **Token: the signal workflow lock**`) despite examples. Conversational register lacks structural format enforcement — `TOKEN: [identifier]` code block would eliminate this risk. |
| C-14 | Inertia stability in every AMEND entry | PARTIAL | Obligation 3 says "For every amendment entry in AMEND: state whether your token's referent would change or stay stable... This check is required for every amendment -- not just one." Instruction is explicit, but no structural enforcement (no table column, no tagged line format). Prose-only imperative has higher model-variance than `STABILITY:` tag or table column — model may satisfy 2 of 3 entries and miss one. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** (4 PASS + 0.5 PARTIAL + 0.5 PARTIAL) / 6 × 10 = 5/6 × 10 = 8.33
**Composite: 98.33**
**Golden:** YES (all essential pass, composite ≥ 80)

---

### V-04 — Token-first anchor + per-entry STABILITY imperative (minimal combination)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Token Declaration → C0 Inertia Anchor → Competitive Map. Structural ordering. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | Whitespace Finding section with specific dimension requirement. |
| C-05 | Auto-detect topic without prompting | PASS | "Read the repo context... Do not prompt the user." |
| C-06 | Mechanism-level inertia reasoning | PASS | `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description]`. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | Prose AMEND with `Output effect:` line per entry. Three examples with specific effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. Focus-active cross-dimensional proof required when active. |
| C-10 | Grounded findings | PASS | "each finding must require the competitive map." Third slot mandatory. |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN in C0 field label, `vs [TOKEN]` column header, findings third slot label, AMEND STABILITY line. |
| C-12 | AMEND evaluates inertia stability | PASS | STABILITY line per entry — exceeds at-least-one requirement. |
| C-13 | Inertia mechanism assigned portable token | PASS | Token Declaration step with `TOKEN: [short identifier]` code block, valid examples listed, role-description anti-examples explicit. Token declared before C0 is written. |
| C-14 | Inertia stability in every AMEND entry | PASS | "STABILITY: line is required for every amendment entry. An entry without it does not pass." Explicit per-entry tag with format `STABILITY: [Stable \| Shifts -- reason]` shown in example for all 3 entries. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 6/6 → 10
**Composite: 100**
**Golden:** YES

---

### V-05 — Full lifecycle with domain-adaptive token and stability matrix

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | ROOT (Step A + Step B) executes before Phase 1. C0 is at ROOT level, competitors are in Phase 2. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." Phase 2 complete condition verifies this. |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0: C0 re-states ROOT mechanism. `vs [TOKEN]` = `[ROOT]`." |
| C-04 | Whitespace identified | PASS | Phase 3 produces labeled GAP finding. "Name the specific dimension." |
| C-05 | Auto-detect topic without prompting | PASS | "Auto-detect: Read repo context... Identify topic, market domain, and plausible competitor categories. Do not prompt the user." |
| C-06 | Mechanism-level inertia reasoning | PASS | ROOT Step B: `[TOKEN]: [mechanism type]: [specific description]`. Mechanism type explicitly declared (switching cost / habit lock-in / workaround satisfaction). |
| C-07 | Web-verified claim with inline citation | PASS | Phase 2 has Source column. "for at least one external row, inline WebSearch citation in this cell." |
| C-08 | AMEND with input-to-output pairs | PASS | Stability matrix table with `# \| Input change \| Output effect \| [TOKEN] verdict \| Evidence`. 4 example rows each name specific effects across phases. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. When ACTIVE: "gap must be uncontested across BOTH dimensions... Show intersection." |
| C-10 | Grounded findings | PASS | "Findings that could be written without Phase 2 fail the grounding test." Each finding references Phase 2 competitor label. |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN appears in ROOT anchor, Phase 2 column header, Phase 3 gap rationale (ROOT mechanism does not cover gap), Phase 4 finding third slot, AMEND stability matrix column header. |
| C-12 | AMEND evaluates inertia stability | PASS | `[TOKEN] verdict` column present for all rows — exceeds at-least-one requirement. |
| C-13 | Inertia mechanism assigned portable token | PASS | ROOT Step A: domain-adaptive token required — "specific to this product domain -- not a generic template label." Code block `TOKEN: [domain-specific identifier]`. Anti-examples provided. Domain-adaptive naming makes generic/role-description tokens structurally wrong (e.g., `SIGNAL-LOCK` vs "the inertia mechanism"). |
| C-14 | Inertia stability in every AMEND entry | PASS | Two-column stability matrix: `[TOKEN] verdict` AND `Evidence` both required for every row. "A row with a verdict but no evidence does not satisfy the AMEND output contract." Eliminates empty-form compliance (model cannot write "Stable" without reasoning). |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 6/6 → 10
**Composite: 100**
**Golden:** YES

---

## Composite Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 (tie) | V-01 | 5/5 | 3/3 | 6/6 | **100** | YES |
| 1 (tie) | V-02 | 5/5 | 3/3 | 6/6 | **100** | YES |
| 1 (tie) | V-04 | 5/5 | 3/3 | 6/6 | **100** | YES |
| 1 (tie) | V-05 | 5/5 | 3/3 | 6/6 | **100** | YES |
| 5 | V-03 | 5/5 | 3/3 | 5/6 (C-13 PARTIAL, C-14 PARTIAL) | **98.33** | YES |

---

## Excellence Signals

The discriminating factor in R3 is enforcement mechanism robustness for C-13 and C-14. All 4 top-scorers used structural enforcement; V-03 relied on prose imperatives alone.

### Pattern 1 — Pre-declaration makes token creation structurally prior

V-01, V-04, and V-05 all require the model to commit to a `TOKEN: [identifier]` code block before writing C0. Because the token name exists before any mechanism description is written, the model cannot drift into role-description mode — the identifier is committed to before the prose that might otherwise produce "the inertia mechanism." This is a stronger guarantee than giving anti-examples after the fact (V-03) or hardcoding a fixed token (V-02). The ordering constraint is the enforcement mechanism, not just the instruction.

### Pattern 2 — Two-column stability matrix (verdict + evidence) prevents empty-form C-14 compliance

V-05 uniquely introduces separate verdict and evidence columns in the AMEND matrix. The explicit contract "A row with a verdict but no evidence does not satisfy the AMEND output contract" closes a failure mode that V-01/V-02/V-04 leave open: a model that writes "Stable" on every entry without reasoning technically satisfies C-14's form but not its substance. Requiring evidence that supports the verdict makes each stability entry load-bearing, not mechanical.

### Pattern 3 — Domain-adaptive token naming encodes context that prevents generic labels

V-05 requires the token to be "specific to this product domain -- not a generic template label." Instructions like `SHEET-LOCK` for a spreadsheet-replacing tool, `CLI-HABIT` for a CLI-first tool, or `SIGNAL-LOCK` for Signal make it structurally difficult to produce a generic stability answer — the domain context embedded in the token name shapes every downstream reference. This is an architectural improvement over domain-neutral tokens (MECH, INERTIA-REF), which allow downstream reasoning to detach from the product context.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-declaration makes token creation structurally prior — committing to TOKEN identifier before C0 description begins eliminates role-description drift because the name exists before any description is written", "Two-column stability matrix (verdict + evidence) prevents empty-form C-14 compliance — requiring both verdict and supporting evidence closes the failure mode where model writes Stable without reasoning", "Domain-adaptive token naming encodes product context in the token identifier itself, making generic stability reasoning structurally wrong because the token name frames every downstream reference"]}
```
