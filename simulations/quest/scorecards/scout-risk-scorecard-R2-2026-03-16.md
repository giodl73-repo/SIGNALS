## scout-risk — Quest Score R2

**Rubric**: v2 (13 criteria: 5 essential / 3 recommended / 5 aspirational)
**Scoring**: Essential = 12 pts each (60 total), Recommended = 10 pts each (30 total), Aspirational = 2 pts each PASS / 1 pt PARTIAL (10 total)

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (60 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Inertia risk first | PASS | PASS | PASS | PASS | PASS |
| C-02 | Multi-dimensional coverage ≥3 | PASS | PASS | PASS | PASS | PASS |
| C-03 | Risk anatomy complete | PASS | PASS | PASS | PASS | PASS |
| C-04 | Severity scale correct | PASS | PASS | PASS | PASS | PASS |
| C-05 | Mitigations specific/actionable | PASS | PASS | PASS | PASS | PASS |

**Evidence summary:**

- **C-01**: All five explicitly place inertia as entry #1 / Step 1 / Phase 1 with hard enforcement ("Do not skip. Do not move it. Write it first."). PASS across the board.
- **C-02**: All five require coverage of ≥3 of 5 dimensions with explicit list. PASS across the board.
- **C-03**: All five require severity + likelihood + mitigation for every entry. PASS across the board.
- **C-04**: All five prohibit anything outside HIGH/MEDIUM/LOW. V-05 additionally enforces this in the self-check gate. PASS across the board.
- **C-05**: V-01 has the re-read gate ("if two or more say 'monitor closely'... replace them"). V-02/V-04/V-05 add taxonomy + forbidden words list preventing generic text at generation time. V-03 has re-read gate. All reach the ≥ C-05 bar (fail condition is ≥2 generic). PASS across the board.

---

### Recommended Criteria (30 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Risks dimension-labeled | PASS | PASS | PASS | PASS | PASS |
| C-07 | Likelihood qualified beyond binary | PASS | PASS | PASS | PASS | PASS |
| C-08 | Risks ordered by priority | PASS | PASS | PASS | PASS | PASS |

**Evidence summary:**

- **C-06**: All five include explicit `Dimension:` field in the required format. V-05 uses a table column. PASS across the board.
- **C-07**: V-01/V-04/V-05 enforce IF-THEN syntax structurally — every likelihood must begin with "IF", which forces condition naming by construction. V-02 asks "what specific condition or scenario triggers this risk" — quality instruction gets ≥ half. V-03 uses "what specific condition or scenario triggers this risk — not just 'possible'" — same bar. C-07 passes at ≥ half, and all five clear that threshold. PASS across the board.
- **C-08**: All five include explicit sort instruction ("Sort dimensional risks from highest to lowest severity"). V-04/V-05 additionally enforce this in the self-check gate. PASS across the board.

---

### Aspirational Criteria (10 pts — 2 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Risk interdependencies noted | FAIL | FAIL | PASS | PASS | PASS |
| C-10 | AMEND behavior demonstrated | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-11 | Full mitigation specificity (zero-generic) | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-12 | All likelihoods trigger-qualified | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-13 | Interdependencies in dedicated section ≥2 pairs | FAIL | FAIL | PASS | FAIL | PASS |

**Evidence by criterion:**

**C-09** — V-01/V-02: No interdependency requirement anywhere in the prompt. FAIL. V-03: Mandatory "## Risk Interdependencies" section with ≥2 named pairs enforced. PASS. V-04: Step 3 requires "at least one interdependency" — single mention in the prompt flow, not a dedicated section. Meets C-09 (≥1 mention). PASS. V-05: Mandatory section with ≥2 pairs. PASS.

**C-10** — All five include the AMEND handling step with correct behavior (keep inertia, narrow scope or recalibrate, retain anatomy). However, C-10 is only demonstrable with a live AMEND directive — these are base prompts. The mechanism is present but untriggered. PARTIAL across the board (1 pt each). This is the irreducible ceiling for base-prompt variations.

**C-11** — V-01: The re-read gate ("if two or more are generic... replace them") catches ≥2 but does not enforce zero-generic. A single instance of generic mitigation survives. PARTIAL (mechanism is detection, not prevention). V-02: Taxonomy pre-commitment + full forbidden words list + verification step. Selecting "Spike/Validate/Gate/Contract/Cut/Instrument" before writing prose structurally excludes generic hedges — a Spike requires a named unknown and time-box, a Gate requires a criterion. PASS. V-03: Re-read gate only (same as V-01). PARTIAL. V-04: Taxonomy + forbidden words + self-check checkbox "Zero instances of forbidden mitigation text" — structural prevention + verification. PASS. V-05: Taxonomy + forbidden words + self-check "Zero instances of forbidden mitigation text anywhere in the register". PASS.

**C-12** — V-01: "Every likelihood must begin with 'IF'" is a required syntactic token. Cannot produce a bare probability label alongside IF-THEN structure. Mechanical enforcement. PASS. V-02: Asks "what specific condition or scenario triggers this risk" — semantic instruction rather than syntactic enforcer. Gets most but without the IF token, bare labels can slip through on some entries. PARTIAL (exceeds ≥half C-07 bar, short of C-12 all-entries bar). V-03: Same quality instruction as V-02. PARTIAL. V-04: IF-THEN enforced via "Every likelihood must begin with 'IF'" + self-check "Every likelihood row starts with 'IF' — scan every row". PASS. V-05: "Every likelihood must be written as 'IF [condition], THEN this risk activates.'" + self-check scan. PASS.

**C-13** — V-01: No interdependency section at all. FAIL. V-02: No interdependency section at all. FAIL. V-03: Mandatory "## Risk Interdependencies" section with exact heading, ≥2 named pairs required, enforcement rules (no scatter, no vague pairs, both risks named explicitly), specificity smell-test ("if you find only 1, your risks are not specific enough — go back and revise"). PASS. V-04: Step 3 asks for "at least one interdependency" in a simple note format — no dedicated section heading, no ≥2 pairs requirement, no named-pair enforcement. Falls short of C-13's structural bar. FAIL. V-05: Mandatory section with exact heading "## Risk Interdependencies", ≥2 named pairs, enforcement rules, specificity smell-test, self-check "## Risk Interdependencies section exists with at least 2 explicitly named compound-risk pairs". PASS.

---

## Score Computation

| ID | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Golden? |
|----|---------------|-----------------|-------------------|-----------|---------|
| V-01 | 60 | 30 | C-09:0, C-10:1, C-11:1, C-12:2, C-13:0 = **4** | **94** | YES |
| V-02 | 60 | 30 | C-09:0, C-10:1, C-11:2, C-12:1, C-13:0 = **4** | **94** | YES |
| V-03 | 60 | 30 | C-09:2, C-10:1, C-11:1, C-12:1, C-13:2 = **7** | **97** | YES |
| V-04 | 60 | 30 | C-09:2, C-10:1, C-11:2, C-12:2, C-13:0 = **7** | **97** | YES |
| V-05 | 60 | 30 | C-09:2, C-10:1, C-11:2, C-12:2, C-13:2 = **9** | **99** | YES |

---

## Rankings

1. **V-05 — 99** — Full integration. All three new criteria pass. C-10 PARTIAL is the only gap — unreachable on a base prompt without a live AMEND directive. The self-check gate in STEP 4 with 8 checkboxes covering all enforcement dimensions is the structural anchor.
2. **V-03 — 97** — Lifecycle structure. Mandatory interdependency section with specificity smell-test unlocks C-09 + C-13. IF-THEN absent, so C-12 is PARTIAL; taxonomy absent, so C-11 is PARTIAL.
3. **V-04 — 97** — Output format + phrasing register. IF-THEN + taxonomy unlocks C-11 + C-12. No dedicated interdependency section, so C-13 fails. Tie with V-03 at 97 but different gap profile.
4. **V-01 — 94** — Cleanest C-12 proof. IF-THEN as syntactic token reliably enforces all likelihoods. No taxonomy, no section — C-11 PARTIAL, C-13 FAIL.
5. **V-02 — 94** — Cleanest C-11 proof. Taxonomy pre-commitment structurally prevents generic mitigations. No IF-THEN token, no section — C-12 PARTIAL, C-13 FAIL.

---

## Excellence Signals from V-05

**Signal 1 — Syntactic token > semantic instruction for C-12**: Requiring the literal string "IF" at the start of every likelihood field is a structural enforcer. The model cannot produce "high" or "~30%" if the field must begin with "IF [condition], THEN this risk activates." — the syntax excludes the violation by construction. Contrast V-02's "what specific condition or scenario triggers this risk" (semantic instruction, not a form constraint), which cannot guarantee all entries reach the C-12 bar.

**Signal 2 — Type selection before prose for C-11**: Requiring selection of a named type (Spike/Validate/Gate/Contract/Cut/Instrument) before writing the mitigation sentence eliminates generic text at generation time. Each type has a structural obligation — a Spike has a named unknown and time-box, a Gate has a criterion. "Monitor closely" is incompatible with any of the six types. This is prevention at source, not detection-and-repair.

**Signal 3 — Specificity smell-test as an indirect register quality lever**: V-03/V-05's rule "if you find only 1 pairing after reviewing all rows, your risks are too generic — revise them" ties the interdependency count to the underlying risk specificity. The smell-test propagates quality pressure backwards through the full register: specific risks produce specific pairings; generic risks cannot. The interdependency section becomes a quality signal for the entire output, not just itself.

**Signal 4 — Extended self-check consolidates all R2 enforcement into a single verification pass**: V-05's STEP 4 checklist covers all eight dimensions (inertia position, severity vocab, dimension count, IF-THEN scan, type presence, forbidden text, sort order, interdependency section). A unified gate after all content is written provides a catch-all safety net that doesn't require the model to remember each rule while writing individual entries.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["syntactic token enforcement (IF) structurally excludes bare probability labels without relying on re-read or semantic instruction", "mitigation type selection before prose generation eliminates generic hedges at source rather than catching them in post-hoc repair", "interdependency specificity smell-test ('if only 1 pairing exists, risks are too generic') propagates quality pressure backward through the full register", "unified self-check checklist as final gate covers all R2 enforcement dimensions in a single verification pass"]}
```
