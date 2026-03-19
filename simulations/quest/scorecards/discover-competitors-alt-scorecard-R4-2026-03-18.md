Now I have everything needed. Writing the scorecard.

---

## discover-competitors-alt — R4 Scorecard

### Rubric: v4 (17 criteria — C-01 through C-17)

Aspirational tier expanded: 6 → 9 criteria (adds C-15, C-16, C-17), 1.11 pts each.

---

### Carry-forward baseline

R3 verdicts for C-01 through C-14 carry into R4 except where a variation was redesigned. R4 V-03 is a full redesign (R3 V-03 scored 98.33 due to C-13 PARTIAL + C-14 PARTIAL). All other R3 C-14 winners scored 100 on those criteria. The three new criteria (C-15, C-16, C-17) require fresh evaluation.

---

### V-01 — Domain extraction before token declaration

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Token Declaration → C0 section → Competitive Map. Structural ordering preserved from R3. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | Whitespace Finding section with specific dimension requirement and "generic statement does not pass." |
| C-05 | Auto-detect topic without prompting | PASS | "Read the repo context... Do not ask the user for the topic, competitors, or market category. Proceed immediately." |
| C-06 | Mechanism-level inertia reasoning | PASS | `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description tied to what C0 does or provides]`. Tied to C0 behavior. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, include an inline citation (URL or publication name) from a WebSearch result in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | Numbered list with bold heading + "Output effect:" line per entry. Three examples with specific section-level effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. When ACTIVE: "gap must be uncontested across BOTH dimensions... Show the intersection." Mechanism present. |
| C-10 | Grounded findings | PASS | Third slot mandatory. "Do not write general domain observations — each finding must require the competitive map to support it." |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN used in: C0 field label, `vs [TOKEN]` column header, findings third slot label, STABILITY: and EVIDENCE: lines in every AMEND entry. |
| C-12 | AMEND evaluates inertia stability | PASS | STABILITY: line required per entry — exceeds at-least-one requirement. |
| C-13 | Inertia mechanism assigned portable token | PASS | Step 2 uses `TOKEN: [domain-adaptive identifier]` code block. Role descriptions explicitly excluded: "The inertia mechanism," "the stickiness factor," and "the C0 lock-in" do not qualify. |
| C-14 | Inertia stability in every AMEND entry | PASS | "Both STABILITY: and EVIDENCE: lines are required for every amendment entry. An entry that omits either line does not pass." Structural per-entry enforcement. |
| C-15 | Token pre-declared before C0 description begins | PASS | "Execute this step before writing anything else." Step 1 extracts DOMAIN-TERMS; Step 2 commits `TOKEN: [...]`. C0 section is a separate subsequent block. Token exists as an output artifact before any C0 mechanism prose is written. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | PASS | Separate STABILITY: and EVIDENCE: tags required per entry. "A STABILITY: verdict without EVIDENCE: is not sufficient — the reasoning must be present." Three examples each carry both tags. |
| C-17 | Token identifier encodes domain context | PASS | Step 1 commits `DOMAIN-TERMS: [term-1], [term-2]` before token naming. Step 2 requires token to include at least one DOMAIN-TERMS term. "A generic placeholder alone (MECH, LOCK, INERTIA-REF) does not pass." Structural extraction eliminates drift — model cannot produce MECH after having written SIGNAL, PLUGIN, TOPIC in the prior step. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 9/9 → 10
**Composite: 100**
**Golden:** YES

---

### V-02 — Single-line verdict+evidence AMEND format

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Token Declaration → C0 Inertia Anchor → Competitive Map. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | GAP section with specific dimension requirement. "A generic statement does not pass." |
| C-05 | Auto-detect topic without prompting | PASS | "Read the repo context... Do not ask the user for the topic, competitors, or market category. Proceed immediately." |
| C-06 | Mechanism-level inertia reasoning | PASS | `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description]`. Mechanism typed and tied to C0. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, inline WebSearch citation (URL or publication name) in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | "Output effect:" per entry. Three examples with specific section-level effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. Focus ACTIVE path present. |
| C-10 | Grounded findings | PASS | Third slot mandatory. "Do not write general domain observations." |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN in C0 field label, `vs [TOKEN]` column, findings third slot, STABILITY: line in AMEND. |
| C-12 | AMEND evaluates inertia stability | PASS | STABILITY line per entry — exceeds at-least-one. |
| C-13 | Inertia mechanism assigned portable token | PASS | Token Declaration uses code block `TOKEN: [domain-specific identifier]`. Negative examples explicit: MECH, INERTIA-REF, LOCK, HABIT alone all fail. Positive examples: SIGNAL-LOCK, WORKFLOW-GRIP, SHEET-HABIT, CLI-INERTIA. Role descriptions excluded. |
| C-14 | Inertia stability in every AMEND entry | PASS | `STABILITY: [verdict] — [evidence]` required per entry. "A verdict without a reason does not pass" — explicit per-entry contract with all 3 examples showing the combined form. |
| C-15 | Token pre-declared before C0 description begins | PASS | "Execute before writing anything else." Token Declaration section with code block precedes C0 section. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | PASS | Single-line `STABILITY: [verdict] — [evidence]` format with dash-separated evidence clause. "STABILITY: Stable alone is not sufficient; STABILITY: Stable — [reason] is the minimum." Evidence is structurally required — omitting the dash clause produces a visibly incomplete form. |
| C-17 | Token identifier encodes domain context | PARTIAL | Instruction-only — strong naming guidance with four explicit negative examples and four positive examples (e.g., `SIGNAL-LOCK` for a signal-gathering tool). However, no DOMAIN-TERMS extraction step forces the model to commit product vocabulary before naming the token. The model must infer domain terms from repo context without an intermediate output commitment. A model under token pressure could still produce `CLI-HABIT` from the examples list rather than deriving a fresh domain-specific identifier from this repo. Weaker than structural extraction. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** (8 PASS + 0.5 PARTIAL) / 9 × 10 = 9.44
**Composite: 99.44**
**Golden:** YES

---

### V-03 — Token as absolute first output

*Note: R4 V-03 is a full redesign. R3 V-03 scored 98.33 (C-13 PARTIAL + C-14 PARTIAL). R4 redesign replaces conversational blockquote token with code block and adds structural STABILITY:/EVIDENCE: tags.*

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | TOKEN → Focus Detection → C0 → Competitive Map. C0 section precedes competitor rows. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | GAP section present. "A generic statement does not pass." |
| C-05 | Auto-detect topic without prompting | PASS | "Auto-detect (after focus resolved): Read repo context... Do not prompt the user." |
| C-06 | Mechanism-level inertia reasoning | PASS | `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description]`. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, inline WebSearch citation... in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | "Each amendment requires three parts: 1. Input change. 2. Output effect. 3. STABILITY. 4. EVIDENCE." |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. Focus ACTIVE path present. |
| C-10 | Grounded findings | PASS | Third slot mandatory. "No general domain observations — each finding must require the competitive map." |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN in C0 field label, `vs [TOKEN]` column, findings third slot. AMEND references TOKEN in STABILITY/EVIDENCE lines. |
| C-12 | AMEND evaluates inertia stability | PASS | STABILITY: per entry — exceeds at-least-one. |
| C-13 | Inertia mechanism assigned portable token | PASS | TOKEN declared as the literal first output in code block `TOKEN: [domain-specific identifier — must include at least one product-domain term from repo context]`. Negative examples (MECH, INERTIA-REF) excluded. Positive examples (SIGNAL-LOCK, WORKFLOW-ANCHOR, SHEET-GRIP, CLI-HABIT). Code block format eliminates the conversational register risk from R3 V-03. |
| C-14 | Inertia stability in every AMEND entry | PASS | "Both STABILITY: and EVIDENCE: lines are required for every entry. A verdict without supporting evidence does not pass." Structural two-tag enforcement replaces R3's prose-only imperative. |
| C-15 | Token pre-declared before C0 description begins | PASS | "Your first output line must be the token declaration." TOKEN appears before focus detection, auto-detect, and all sections. Maximum structural precedence — no execution path places C0 before TOKEN. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | PASS | Separate STABILITY: and EVIDENCE: tags required per entry. "Both STABILITY: and EVIDENCE: lines are required for every entry." Examples carry both tags for all 3 entries. |
| C-17 | Token identifier encodes domain context | PARTIAL | Instruction-only with examples, but TOKEN is the absolute first output — before auto-detect, before focus resolution, before any section. The model must choose a domain-specific token immediately from repo context without an intermediate output step that commits vocabulary. No DOMAIN-TERMS extraction line is produced before the token declaration. This is the sharpest C-17 risk in the set: the strictest C-15 enforcement (first output line) is structurally in tension with C-17 structural enforcement (extraction requires an intermediate output). The model has read repo context, but producing a domain-adaptive token as the very first output without a vocabulary-commitment artifact is instruction-dependent. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** (8 PASS + 0.5 PARTIAL) / 9 × 10 = 9.44
**Composite: 99.44**
**Golden:** YES

---

### V-04 — Minimal combination of all three

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | Token Declaration → C0 Inertia Anchor → Competitive Map. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0 is C0." |
| C-04 | Whitespace identified | PASS | Whitespace Finding section. Specific dimension requirement. |
| C-05 | Auto-detect topic without prompting | PASS | "Read the repo context... Do not prompt the user. Resolve focus: state before producing any output." |
| C-06 | Mechanism-level inertia reasoning | PASS | `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] -> [Specific description tied to what C0 does or provides]`. |
| C-07 | Web-verified claim with inline citation | PASS | "For at least one external row, inline WebSearch citation... in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | Four-part structure per entry: input change + output effect + STABILITY + EVIDENCE. Three examples with specific section-level effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction. Focus ACTIVE: "Show the intersection — state what the focus lens adds that the competitive map alone would not surface." |
| C-10 | Grounded findings | PASS | Third slot mandatory. "Each finding must require the competitive map — no general domain observations." |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN in C0 field label, `vs [TOKEN]` column header, findings third slot, STABILITY:/EVIDENCE: lines in AMEND. |
| C-12 | AMEND evaluates inertia stability | PASS | STABILITY: per entry — exceeds at-least-one. |
| C-13 | Inertia mechanism assigned portable token | PASS | Step 2: `TOKEN: [domain-adaptive identifier]` code block. "role descriptions are not tokens." Anti-examples and valid examples explicit. |
| C-14 | Inertia stability in every AMEND entry | PASS | "STABILITY: and EVIDENCE: ... A STABILITY verdict without EVIDENCE does not pass." Per-entry structural tags. |
| C-15 | Token pre-declared before C0 description begins | PASS | "Execute before anything else." Step 1 extracts DOMAIN-TERMS; Step 2 commits `TOKEN: [...]` in code block. C0 section is subsequent. Explicit ordering constraint. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | PASS | Four-part AMEND structure: part 3 is STABILITY:, part 4 is EVIDENCE:, each required. "A STABILITY verdict without EVIDENCE does not pass." Three examples carry both. |
| C-17 | Token identifier encodes domain context | PASS | Step 1: `DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]` committed as output artifact before token naming. Step 2: "The token must include at least one term from DOMAIN-TERMS." Examples: SIGNAL-LOCK, WORKFLOW-HABIT, TOPIC-GRIP. Extraction step makes DOMAIN-TERMS visible — model cannot ignore a prior output commitment when choosing the token. Structural enforcement equivalent to V-01. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 9/9 → 10
**Composite: 100**
**Golden:** YES

---

### V-05 — Full lifecycle with deep structural enforcement

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | C0 named before competitors | PASS | ROOT phase (Steps A+B+C) executes before Phase 1 and Phase 2. C0 named in ROOT Step C; competitors in Phase 2. |
| C-02 | 3+ named competitors with threat levels | PASS | "minimum 3 named external competitors. No generic labels. Every row: explicit HIGH / MEDIUM / LOW threat." Phase 2 completion condition verifies. |
| C-03 | C0 at row 0 in competitive map | PASS | "Row 0: C0 re-states ROOT mechanism. `vs [TOKEN]` = `[ROOT]`." |
| C-04 | Whitespace identified | PASS | Phase 3 produces labeled GAP finding. "Name the specific dimension." |
| C-05 | Auto-detect topic without prompting | PASS | "Read repo context... Identify topic, market domain, and plausible competitor categories. Do not prompt the user. Proceed immediately." |
| C-06 | Mechanism-level inertia reasoning | PASS | ROOT Step C: `[TOKEN]: [mechanism type]: [specific description tied to C0's behavior]`. Mechanism type declared; description tied to specific C0 behavior. |
| C-07 | Web-verified claim with inline citation | PASS | Phase 2 Source column: "for at least one external row, inline WebSearch citation in this cell. Not a footnote." |
| C-08 | AMEND with input-to-output pairs | PASS | Stability matrix table: `# \| Input change \| Output effect \| [TOKEN] verdict \| Evidence`. Four example rows with specific phase-level output effects. |
| C-09 | Cross-dimensional whitespace finding | PASS | Focus INACTIVE → vacuous satisfaction (and explicit instruction: "state why ROOT mechanism does not cover this gap"). Focus ACTIVE: "gap must be uncontested across BOTH... Show intersection." |
| C-10 | Grounded findings | PASS | "Findings that could be written without Phase 2 fail the grounding test." Phase 2 competitor label required in each finding. |
| C-11 | Inertia reference propagates downstream | PASS | TOKEN used in: ROOT Step C field label, Phase 2 `vs [TOKEN]` column header, Phase 3 gap rationale, Phase 4 finding third slot, AMEND `[TOKEN] verdict` column header. Full propagation chain named. |
| C-12 | AMEND evaluates inertia stability | PASS | `[TOKEN] verdict` column present for every row — exceeds at-least-one. |
| C-13 | Inertia mechanism assigned portable token | PASS | ROOT Step B: `TOKEN: [domain-adaptive identifier]` code block. "A generic placeholder alone (MECH, LOCK, INERTIA-REF) fails C-17." Domain-specific examples given. Anti-examples explicit. |
| C-14 | Inertia stability in every AMEND entry | PASS | Two-column matrix: `[TOKEN] verdict` AND `Evidence` both required per row. "A row with a verdict but no evidence does not satisfy the output contract." |
| C-15 | Token pre-declared before C0 description begins | PASS | ROOT Step B: "TOKEN is committed. C0 description begins in Step C — not before." ROOT complete condition explicitly lists: "TOKEN declared before Step C begins." Phased ordering makes the constraint structurally enforceable — Step C cannot begin until Step B produces TOKEN. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | PASS | Two-column table contract: `[TOKEN] verdict \| Evidence` both required per row. "A row with a verdict but no evidence does not satisfy the output contract. A row with evidence but no verdict does not satisfy the output contract. 'Stable' without reasoning does not satisfy the Evidence column." Strongest C-16 enforcement in this set. |
| C-17 | Token identifier encodes domain context | PASS | ROOT Step A extracts `DOMAIN-TERMS: [term-1], [term-2], [term-3 if available]`. ROOT Step B requires token to include at least one DOMAIN-TERMS term. "A generic placeholder alone (MECH, LOCK, INERTIA-REF) fails C-17." DOMAIN-TERMS artifact is written before TOKEN — structural extraction prevents domain-neutral drift. |

**Essential:** 5/5 → 60
**Recommended:** 3/3 → 30
**Aspirational:** 9/9 → 10
**Composite: 100**
**Golden:** YES

---

## Composite Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden |
|------|-----------|-----------|-------------|--------------|-----------|--------|
| 1 (tie) | **V-01** Domain extraction + pre-declaration + two-tag evidence | 5/5 | 3/3 | 9/9 | **100** | YES |
| 1 (tie) | **V-04** Minimal combination | 5/5 | 3/3 | 9/9 | **100** | YES |
| 1 (tie) | **V-05** Full lifecycle deep enforcement | 5/5 | 3/3 | 9/9 | **100** | YES |
| 4 (tie) | **V-02** Single-line verdict+evidence | 5/5 | 3/3 | 8.5/9 | **99.44** | YES |
| 4 (tie) | **V-03** Token as absolute first output | 5/5 | 3/3 | 8.5/9 | **99.44** | YES |

---

## C-17 Breakdown — The Single Discriminating Criterion

All variations pass C-15 and C-16. The only split is C-17.

**PASS (V-01, V-04, V-05):** Domain term extraction as a prior output artifact. The model commits `DOMAIN-TERMS: SIGNAL, PLUGIN, TOPIC` in the output before choosing the token. It cannot then produce `MECH` without visibly violating an artifact it already wrote. The extraction step is the enforcement — not instruction, not examples.

**PARTIAL (V-02, V-03):** Instruction-only with negative/positive examples. V-02 has no extraction step; V-03 adds a structural tension: TOKEN is the absolute first output (strictest C-15), but this timing precludes an intermediate vocabulary-commitment step. The ultra-strict C-15 enforcement of V-03 *actively works against* C-17 structural enforcement — the faster the token must appear, the less output is available to lock in domain vocabulary first.

---

## Excellence Signals

### Pattern 1 — Extraction step creates an un-overwritable vocabulary commitment

V-01, V-04, and V-05 all produce `DOMAIN-TERMS: [...]` as a visible output artifact before the TOKEN line. This is architecturally stronger than instruction-only for C-17: the model cannot choose a token that ignores SIGNAL, PLUGIN, and TOPIC without producing an output that contradicts its own prior declaration. The extraction artifact is the enforcement — domain specificity becomes a consistency constraint, not a naming suggestion.

### Pattern 2 — Maximum C-15 strictness (first-line TOKEN) creates structural tension with C-17

V-03's hypothesis — that placing TOKEN as the absolute first output eliminates all C-15 ordering ambiguity — is confirmed. But the consequence is that no intermediate output can lock in domain vocabulary before the token choice. V-03 is the strictest possible C-15 design and simultaneously the weakest C-17 design in this set. The two criteria pull in opposite directions when no extraction step mediates them. V-01/V-04/V-05 resolve this tension by completing extraction before declaration — preserving C-15 (token before C0) while satisfying C-17 (extraction before token).

### Pattern 3 — Per-evidence-tag coverage (C-16) is format-independent across all three passing formats

C-16 passes in three structurally different formats: two separate STABILITY:/EVIDENCE: lines (V-01, V-03, V-04), single dash-separated line `STABILITY: verdict — reason` (V-02), and two-column table (V-05). All three enforce the verdict+evidence pairing. The operative criterion is evidence *presence*, not container format. No format advantage at the PASS threshold; V-05's table is marginally stronger at preventing silent omission (a missing cell is visually obvious) but all five variations satisfy C-16 at or above threshold.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Extraction step creates an un-overwritable vocabulary commitment — producing DOMAIN-TERMS as a prior output artifact makes domain specificity a consistency constraint rather than a naming suggestion; the model cannot choose a generic token without contradicting its own prior output", "Maximum C-15 strictness (first-line TOKEN) creates structural tension with C-17 — placing TOKEN as the absolute first output precludes any intermediate vocabulary-commitment step, making the strictest C-15 design simultaneously the weakest C-17 design; variations resolve this tension by sequencing extraction before declaration"]}
```
