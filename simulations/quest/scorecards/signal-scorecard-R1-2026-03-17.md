## Quest Score — `/signal` Round 1

**Rubric**: `simulations/quest/rubrics/signal-rubric-v1-2026-03-17.md`
**Variations**: 5 (V-01 through V-05)
**Scoring mode**: Prompt design assessment — each variation scored on likelihood of producing passing output per criterion.

---

## Per-Variation Criterion Scores

### V-01 — Table Layout

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | PASS | NAMESPACE CATALOG lists all 12 in fixed order |
| C-02 | essential | PASS | SUB-SKILL DESCRIPTIONS provides every sub-skill by name |
| C-03 | essential | PASS | Table format enforces `| Command | Description |` column discipline |
| C-04 | essential | PASS | BARE MODE section explicit with example lines; no compliance gate |
| C-05 | essential | PASS | `/signal <namespace>` mode declared; "emit one namespace table only" |
| C-06 | recommended | PASS | NAMESPACE CATALOG states authoritative counts; header template has `<N> skills` |
| C-07 | recommended | PASS | Template includes `> Run any sub-skill directly...` blockquote footer |
| C-08 | recommended | PASS | Header template `## /<namespace> -- <purpose phrase> -- <N> skills` present |
| C-09 | aspirational | PASS | Descriptions listed verbatim in SUB-SKILL DESCRIPTIONS; "use verbatim in table" |
| C-10 | aspirational | PARTIAL | Table format is consistent but descriptions reference (`->`) differs from output format (table); model may mix formats |

**Essentials**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1.5/2
**Score**: (5/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 60 + 30 + 7.5 = **97.5**
**All essential pass**: YES

---

### V-02 — Conversational Imperative

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | PASS | Numbered list 1–12 names all namespaces with counts |
| C-02 | essential | PARTIAL | Skills provided in paragraph inline form ("scout: competitors (...), feasibility (...)"); model must convert to per-line format — conversion friction present |
| C-03 | essential | PARTIAL | Descriptions are there but paragraph source format risks inline output rather than per-skill lines; FORMAT GUIDANCE is appended after the reference, not integrated |
| C-04 | essential | PASS | "Emit just the command names. No descriptions. No headers. No blank lines... Nothing else." Clear. |
| C-05 | essential | PASS | "Show only that namespace... Do not mention other namespaces." Explicit. |
| C-06 | recommended | PASS | Counts in numbered list: "1. scout (8 skills)" |
| C-07 | recommended | PASS | FORMAT GUIDANCE explicitly instructs: "End each section with: 'Run any sub-skill directly...'" |
| C-08 | recommended | PASS | Purpose phrases embedded in numbered list (e.g., "discovery and research before committing to a design") |
| C-09 | aspirational | PASS | Descriptions listed verbatim in THE SKILLS PER NAMESPACE section |
| C-10 | aspirational | PARTIAL | Paragraph-format skill reference creates scannability risk; `->` example is guidance not structure; layout decisions partly delegated to model |

**Essentials**: 4/5 (C-02 and C-03 each 0.5) | **Recommended**: 3/3 | **Aspirational**: 1.5/2
**Score**: (4/5 × 60) + (3/3 × 30) + (1.5/2 × 10) = 48 + 30 + 7.5 = **85.5**
**All essential pass**: NO (C-02, C-03 partial)

---

### V-03 — Lifecycle / Explicit Branching

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | PASS | PHASE 3 catalog lists all 12 with fixed-order table |
| C-02 | essential | PASS | PHASE 4 lists every sub-skill by full command name |
| C-03 | essential | PASS | PHASE 4 explicitly: "Use these descriptions verbatim. Do not paraphrase." |
| C-04 | essential | PASS | CONTRACT BARE: "No leading `/`. No descriptions. No headers. No blank lines." + COMPLIANCE CHECK restarts on failure |
| C-05 | essential | PASS | CONTRACT NAMESPACE: "Emit that namespace section only. Do not emit any other namespace sections." + COMPLIANCE CHECK |
| C-06 | recommended | PASS | PHASE 3 table has authoritative count per row (8, 4, 4, 7, 7, 9, 3, 2, 6, 4, 3, 4) |
| C-07 | recommended | PARTIAL | CONTRACT FULL specifies `FOOTER: "Run any sub-skill directly, or describe your <domain>..."` — `<domain>` is a generic placeholder; model must infer per-namespace domain word without embedded examples |
| C-08 | recommended | PASS | PHASE 3 table includes purpose phrase per namespace row |
| C-09 | aspirational | PASS | Verbatim instruction + full catalog in PHASE 4 |
| C-10 | aspirational | PASS | Output format specified: `/<namespace>-<skill>  -> <description>` with spacing; namespace sections separated by blank line |

**Essentials**: 5/5 | **Recommended**: 2.5/3 (C-07 partial) | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (2.5/3 × 30) + (2/2 × 10) = 60 + 25 + 10 = **95**
**All essential pass**: YES

---

### V-04 — Format + Phrasing (Combination)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | PASS | NAMESPACE REFERENCE embeds all 12 sections inline |
| C-02 | essential | PASS | All sub-skills listed in `->` format inside NAMESPACE REFERENCE |
| C-03 | essential | PASS | One-line descriptions on every `->` line; descriptions are the output, not instructions about the output |
| C-04 | essential | PASS | BARE MODE: "Emit skill names only. No leading `/`. No descriptions. No headers. No separators." Clear. |
| C-05 | essential | PASS | "FILTER: show only the named namespace" declared in PARSE MODE FIRST |
| C-06 | recommended | PASS | All 12 namespace headers include count: "- /scout -- 8 skills for discovery and research" |
| C-07 | recommended | PASS | All 12 footers embedded verbatim in NAMESPACE REFERENCE with per-namespace domain word (e.g., "research goal", "artifact", "scenario") |
| C-08 | recommended | PASS | Purpose phrase in every namespace header in NAMESPACE REFERENCE |
| C-09 | aspirational | PASS | Descriptions embedded verbatim; model copies reference, does not construct |
| C-10 | aspirational | PASS | `->` list with alignment instruction ("Align the `->` separator within each section (pad with spaces)"); footers separate each section naturally |

**Essentials**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = **100**
**All essential pass**: YES

---

### V-05 — Full Integration (Format + Phrasing + Lifecycle)

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | PASS | STEP 4 embeds all 12 namespace sections inline |
| C-02 | essential | PASS | All sub-skills in STEP 4 reference with `->` format |
| C-03 | essential | PASS | Descriptions on every `->` line + "do not invent new descriptions" constraint |
| C-04 | essential | PASS | STEP 2: "BARE -- emit bare command names... No `/` prefix. No descriptions. No headers. No blank lines." + COMPLIANCE GATE: "BARE mode: zero headers, zero descriptions, zero blank lines between namespaces. Fail any check -> restart from STEP 2." |
| C-05 | essential | PASS | STEP 2: "FILTER -- emit only the section for the named namespace." + COMPLIANCE GATE: "FILTER mode: exactly 1 namespace section, no others." |
| C-06 | recommended | PASS | All 12 namespace headers in STEP 4 include authoritative count |
| C-07 | recommended | PASS | All 12 footers embedded verbatim in STEP 4 with per-namespace domain word |
| C-08 | recommended | PASS | Purpose phrase in every namespace header in STEP 4 |
| C-09 | aspirational | PASS | "do not invent new descriptions" + full verbatim reference inline |
| C-10 | aspirational | PASS | `->` list with alignment instruction ("Align the `->` separator within each section (pad with spaces)"); consistent across all 12 sections |

**Essentials**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Score**: (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = **100**
**All essential pass**: YES

---

## Leaderboard

| Rank | Variation | Score | Essential | C-04/C-05 strength | Key gap |
|------|-----------|-------|-----------|---------------------|---------|
| 1 | V-05 Full Integration | 100 | 5/5 PASS | Highest — compliance gate enforces restart on failure | None |
| 2 | V-04 Format + Phrasing | 100 | 5/5 PASS | High — clear inline reference; no gate | No enforcement on BARE/FILTER |
| 3 | V-01 Table Layout | 97.5 | 5/5 PASS | High — explicit with example | C-10 PARTIAL: table vs `->` format inconsistency |
| 4 | V-03 Lifecycle | 95 | 5/5 PASS | Very high — contracts + compliance check | C-07 PARTIAL: generic `<domain>` placeholder in footer |
| 5 | V-02 Conversational | 85.5 | Partial fail | High — explicit bare/filter instructions | C-02/C-03 PARTIAL: paragraph-format skill reference creates conversion friction |

**Golden threshold check** (score >= 80, all essential pass):
- V-05: GOLD
- V-04: GOLD
- V-01: GOLD
- V-03: GOLD (95, all essential)
- V-02: SILVER (85.5, essential partials on C-02/C-03)

---

## Excellence Signals from V-05

**What made the top variation better:**

1. **Inline pre-formatted reference as the output** — STEP 4 embeds the full catalog already formatted as the expected output. The model copies, not constructs. This eliminates C-02, C-03, C-09 failure modes at the source.

2. **Per-namespace domain words in embedded footers** — Each footer in STEP 4 has a specific domain word ("your topic", "your artifact", "your scenario", "your hypothesis") rather than a generic `<domain>` placeholder. This removes C-07 ambiguity that V-03 carries.

3. **Mode-gated compliance check with restart** — The compliance gate at the end targets each invocation mode independently (`FULL`, `FILTER`, `BARE`) and instructs restart on failure. This is the strongest insurance for C-04 and C-05 — the two behavioral criteria most likely to fail in practice.

4. **"Do not invent new descriptions" explicit constraint** — This addresses the most common failure pattern in catalog-style skills: model paraphrase that drifts from canonical one-liners. Locks C-09 from the supply side.

5. **Step numbering frames output as sequential execution** — STEP 1 DETECT → STEP 2 EMIT → STEP 3 FORMAT → STEP 4 REFERENCE → COMPLIANCE GATE creates a mental model of ordered phases, reducing the chance the model skips a phase or conflates modes.

---

## Failure Patterns

| Pattern | Seen in | Effect |
|---------|---------|--------|
| Paragraph-format skill reference requires conversion | V-02 | C-02/C-03 partial; output may be inline prose not per-skill lines |
| Generic `<domain>` placeholder in footer template | V-03 | C-07 partial; footer text varies or is omitted for some namespaces |
| Format inconsistency between reference and output spec | V-01 | C-10 partial; model may output `->` in place of table or vice versa |
| No compliance gate on BARE/FILTER mode | V-01, V-02, V-04 | Elevated C-04/C-05 failure risk vs V-03/V-05 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["embed pre-formatted reference verbatim so model copies output not constructs it", "use per-namespace domain words in footers not generic placeholders", "mode-gated compliance gate with restart instruction targets behavioral criteria directly"]}
```
