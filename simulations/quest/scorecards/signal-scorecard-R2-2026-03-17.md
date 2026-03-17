Now I have all the material needed. Let me score all five variations.

---

## Quest Score — `/signal` Round 2

**Rubric**: `signal-rubric-v2-2026-03-17.md`
**Variations**: V-01 through V-05 from `signal-variate-R2-2026-03-17.md`
**Scoring context**: Prompt-design evaluation (no trace artifact). C-04/C-05 scored from prompt instruction quality. C-13 scored from reference-vs-output format comparison.

---

## Per-Variation Scoring

### V-01 — Domain Noun Lookup Table + Alignment Character-Count Example

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | NAMESPACE CATALOG contains all 12 namespaces in declared order |
| C-02 | essential | PASS | Each namespace lists individually named commands |
| C-03 | essential | PASS | Every command has a one-line description in the catalog |
| C-04 | essential | PASS | BARE MODE section: "No `/` prefix. No descriptions. No headers. No blank lines. One name per line." Clear. |
| C-05 | essential | PASS | PARSE MODE declares `FILTER (one namespace only; <namespace> = the word after /signal)` |
| C-06 | recommended | PASS | All 12 namespace headers state exact counts; counts match authoritative list |
| C-07 | recommended | PASS | Every namespace in catalog ends with a footer |
| C-08 | recommended | PASS | Every header carries a purpose phrase (e.g. "8 skills for discovery and research") |
| C-09 | aspirational | PASS | "emit sub-skill descriptions verbatim; do not paraphrase" + pre-populated catalog |
| C-10 | aspirational | PASS | ALIGNMENT RULE + character-count example with 19-char padding guide; output should be scannable |
| C-11 | aspirational | PASS | Standalone DOMAIN NOUN TABLE maps all 12 namespaces to specific nouns; no generic placeholder survives |
| C-12 | aspirational | PASS | Explicit char-count rule: "Count characters in the longest command name in that section, then pad shorter names to match." Example provided. |
| C-13 | aspirational | PASS | Inline reference uses `->` format; SECTION FORMAT specifies `->` format; no mismatch |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 5/5 → 10  
**Composite: 100** | Band: **Gold**

---

### V-02 — Pre-Emit Compliance Gate + Bare Mode Output Fence

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | NAMESPACE REFERENCE includes all 12 namespaces |
| C-02 | essential | PASS | Sub-skills listed per namespace |
| C-03 | essential | PASS | Descriptions on every command line |
| C-04 | essential | PASS | PRE-EMIT CHECK: "If your output contains any word that is not a command name, MODE: BARE is violated. Restart." + first-6-lines fenced example. Strong behavioral guard. |
| C-05 | essential | PASS | Filter gate: "emit exactly one namespace section. Do not emit any section for any other namespace." + compliance check |
| C-06 | recommended | PASS | Counts in namespace headers match authoritative list |
| C-07 | recommended | PASS | Footers present in all 12 namespaces in NAMESPACE REFERENCE with specific domain nouns |
| C-08 | recommended | PASS | Purpose phrases in all namespace headers |
| C-09 | aspirational | PASS | Reference section pre-populated; "emit verbatim" implied by template |
| C-10 | aspirational | PASS | "Pad command names within each section so all `->` separators align vertically." — instruction present; output should be scannable even without char-count rule |
| C-11 | aspirational | PASS | Inline reference footers are pre-resolved with specific domain nouns; SECTION FORMAT `<domain-noun>` placeholder is overridden by concrete reference examples |
| C-12 | aspirational | **PARTIAL** | Alignment instruction present ("Pad command names… align vertically") but no character-count example or concrete numeric rule. Instruction alone is weaker — model may pad inconsistently across sections. |
| C-13 | aspirational | PASS | Both reference and SECTION FORMAT use `->` list format; no mismatch |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: PARTIAL on C-12 → 4 full passes / 5 → 8  
**Composite: 98** | Band: **Gold**

---

### V-03 — C-13 Table Path (Table Format in Reference + Output Spec)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | 12 namespace tables in NAMESPACE CATALOG |
| C-02 | essential | PASS | Sub-skills listed in table rows |
| C-03 | essential | PASS | Description column present on every row |
| C-04 | essential | PASS | BARE FORMAT + COMPLIANCE CHECK: "zero tables, zero descriptions, zero headers? If no, restart." |
| C-05 | essential | PASS | FILTER mode + compliance check for exactly 1 table |
| C-06 | recommended | PASS | Counts in `## /namespace` headers |
| C-07 | recommended | PASS | Italicized footer line in every namespace section |
| C-08 | recommended | PASS | Purpose phrases in all headers |
| C-09 | aspirational | PASS | "emit tables verbatim in this order" |
| C-10 | aspirational | PASS | Markdown table format enforces column discipline automatically; `| Command | Description |` header creates natural visual alignment |
| C-11 | aspirational | PASS | NAMESPACE DOMAIN NOUNS table provides all 12 specific nouns; footers in catalog are pre-resolved |
| C-12 | aspirational | **N/A** | Variation uses Markdown table format; C-12 applies to `->` list only. Adjust denominator to 4. |
| C-13 | aspirational | PASS | Reference uses `| Command | Description |` tables; output spec specifies `| Command | Description |` tables; formats match |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 4/4 (denominator adjusted) → 10  
**Composite: 100** | Band: **Gold**

---

### V-04 — Phrasing Economy (No Gate, No Alignment Rule)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | NAMESPACE REFERENCE contains all 12 namespaces |
| C-02 | essential | PASS | Sub-skills listed per namespace |
| C-03 | essential | PASS | Descriptions on every command |
| C-04 | essential | PASS | "BARE MODE: emit command names without `/` prefix, no descriptions, no headers, no blank lines, one per line." Sufficient. |
| C-05 | essential | PASS | PARSE MODE declares `FILTER (one namespace only)` |
| C-06 | recommended | PASS | Counts in namespace headers |
| C-07 | recommended | PASS | Footers in NAMESPACE REFERENCE are pre-resolved ("research goal", "draft artifact", etc.) |
| C-08 | recommended | PASS | Purpose phrases in headers |
| C-09 | aspirational | PASS | "NAMESPACE REFERENCE (emit verbatim):" guards description fidelity |
| C-10 | aspirational | **PARTIAL** | No alignment instruction. Model may copy the pre-aligned reference (PASS) or follow the unpadded SECTION FORMAT template (ragged). Behavior is non-deterministic across runs. |
| C-11 | aspirational | PASS | SECTION FORMAT has generic `<domain>` but NAMESPACE REFERENCE (verbatim) overrides with specific nouns. Model copies from reference. |
| C-12 | aspirational | **FAIL** | No alignment instruction anywhere in the prompt. C-12 requires explicit padding instruction; verbatim copy alone is insufficient to guarantee column-aligned output reliably. |
| C-13 | aspirational | PASS | Both reference and SECTION FORMAT use `->` list format; no mismatch |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09=P, C-10=PARTIAL(0), C-11=P, C-12=F, C-13=P → 3/5 → 6  
**Composite: 96** | Band: **Gold**

*Note: Variate predicted 92. My analysis gives 96 because the SECTION FORMAT template uses `->` throughout (C-13 intact) and the inline reference footers reliably satisfy C-11. The 4-point gap likely reflects the variate's harsher treatment of C-10 (FAIL rather than PARTIAL) and possibly a more conservative view on the `<domain>` generic placeholder in the SECTION FORMAT conflicting with C-11 on some runs.*

---

### V-05 — Full Integration (All R1/R2 Learnings)

| Criterion | Category | Verdict | Evidence |
|-----------|----------|---------|----------|
| C-01 | essential | PASS | STEP 4 NAMESPACE REFERENCE contains all 12 namespaces |
| C-02 | essential | PASS | Sub-skills listed per namespace |
| C-03 | essential | PASS | Descriptions on every command |
| C-04 | essential | PASS | BARE mode: "Expected first 6 lines:" fenced example + "Total output: 57 lines. Nothing else." + COMPLIANCE GATE check |
| C-05 | essential | PASS | FILTER mode instruction + COMPLIANCE GATE: "FILTER mode: exactly 1 namespace section, no others" |
| C-06 | recommended | PASS | Counts in headers, matched against "The count (<N>) must equal the number of sub-skills listed." |
| C-07 | recommended | PASS | Footers in STEP 4 reference; pre-resolved domain nouns |
| C-08 | recommended | PASS | Purpose phrases in all 12 namespace headers |
| C-09 | aspirational | PASS | "emit verbatim; do not invent or paraphrase descriptions" |
| C-10 | aspirational | PASS | STEP 3 alignment rule + 3-line concrete example showing padded names; all output will be scannable |
| C-11 | aspirational | PASS | STEP 3 domain noun two-column table + STEP 4 pre-resolved footers; doubly reinforced |
| C-12 | aspirational | PASS | "Count characters in the longest name in the section; pad shorter names to that length." + concrete example with `/scout-competitors`, `/scout-stakeholders`, `/scout-market` showing padding |
| C-13 | aspirational | PASS | STEP 4 reference uses `->` lists; STEP 3 section template uses `->` lists; no mismatch |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 5/5 → 10  
**Composite: 100** | Band: **Gold**

---

## Leaderboard

| Rank | V | Composite | Band | Essential | Recommended | Aspirational | Key Differentiator |
|------|---|-----------|------|-----------|-------------|--------------|-------------------|
| 1 (tie) | **V-01** | **100** | Gold | 5/5 | 3/3 | 5/5 | Standalone domain noun table + char-count example; compact, clean |
| 1 (tie) | **V-03** | **100** | Gold | 5/5 | 3/3 | 4/4 | Table format eliminates alignment concern entirely; C-12 N/A |
| 1 (tie) | **V-05** | **100** | Gold | 5/5 | 3/3 | 5/5 | All learnings integrated; most robust behavioral guardrails |
| 4 | V-02 | 98 | Gold | 5/5 | 3/3 | 4/5 | C-12 PARTIAL — alignment instruction without char-count rule |
| 5 | V-04 | 96 | Gold | 5/5 | 3/3 | 3/5 | C-12 FAIL (no alignment instruction), C-10 PARTIAL |

**All 5 essential criteria pass across all 5 variations.** The entire spread is in the aspirational tier, which is the intended design for Round 2.

---

## Excellence Signals

Patterns from the top-scoring variations (V-01, V-03, V-05) that distinguish them from V-02/V-04:

### 1. Domain noun lookup table as a separate authoritative section
V-01 and V-05 place the domain noun table outside the SECTION FORMAT template and outside the inline reference — it stands alone as an authoritative lookup. This gives the model two independent confirmation sources (the table AND the pre-resolved footer in the reference) rather than one. V-03 achieves the same via a NAMESPACE DOMAIN NOUNS Markdown table. Result: C-11 PASS across all three, no `<domain>` literal leakage.

### 2. Character-count alignment rule paired with a concrete padded example
V-01 and V-05 prove that alignment instruction alone (V-02) is weaker than instruction + example. The three-line example showing `/scout-competitors`, `/scout-stakeholders`, `/scout-market` with explicit padding makes the rule unambiguous. V-02's "pad command names… align vertically" is sufficient for C-10 but insufficient for C-12 (which requires reliable, instruction-backed alignment, not just occasional alignment from verbatim copying).

### 3. Table format as an alternative C-13 compliance path
V-03 demonstrates that C-13 can be satisfied through table consistency rather than `->` consistency. The Markdown table's `| Command | Description |` header enforces column discipline automatically, making the explicit alignment instruction (C-12) unnecessary. This is a structurally different path to 100: instead of adding rules for `->` alignment, switch the format to one that is self-aligning.

---

## C-12 Is the Discriminator

The entire score spread between 96–100 lives on C-12 and C-10. The test question was: *does an explicit alignment instruction matter, and does adding a character-count example to that instruction matter?*

| Variation | Alignment instruction | Char-count example | C-12 result |
|-----------|----------------------|-------------------|-------------|
| V-04 | None | None | FAIL |
| V-02 | Yes | No | PARTIAL |
| V-01/V-05 | Yes | Yes | PASS |
| V-03 | N/A (table format) | N/A | N/A |

The answer is: **instruction matters (V-02 vs V-04), and example matters (V-01/V-05 vs V-02).** Both components are load-bearing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Standalone domain noun lookup table as a separate authoritative section gives the model two independent confirmation sources and eliminates generic placeholder leakage into footers", "Alignment instruction paired with a concrete character-count example is the reliable path to C-12 PASS; instruction alone (without example) produces only C-12 PARTIAL", "Markdown table format satisfies C-13 via table consistency rather than arrow-list consistency, making C-12 N/A and achieving 100 through format self-discipline rather than explicit padding rules"]}
```
