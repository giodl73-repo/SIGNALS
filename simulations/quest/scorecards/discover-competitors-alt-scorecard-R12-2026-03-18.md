## R12 Scoring — `discover-competitors-alt` (Rubric v12)

> No trace artifact. Scoring against prompt specification: does each variation's design reliably produce rubric-compliant output?

---

### Criterion Evaluation — V-01 (Baseline, full text available)

| ID | Criterion | V-01 | Evidence |
|----|-----------|------|----------|
| C-01 | Competitive map with C0 row 0, threat levels, whitespace | **PASS** | GATE-2 template has C0 at row 0 with `—` threat, H/M/L for competitors; GATE-3 has WHITESPACE block |
| C-02 | C0 labeled as C0, not competitor | **PASS** | Template shows `C0 — [name]` at row 0 with `—` in threat column |
| C-03 | Distinct whitespace finding | **PASS** | GATE-3 REQUIRED OUTPUTS separates WHITESPACE block from findings |
| C-04 | Whitespace names specific uncontested dimension | **PASS** | Prose says "'room to innovate' alone fails" |
| C-05 | Auto-detect without prompting | **PASS** | "Infer domain, competitors, and market from repo context — do not ask the user" |
| C-06 | Mechanism-level inertia reasoning | **PASS** | GATE-2 requires `[TOKEN]: [mechanism type: switching cost \| habit lock-in \| workaround satisfaction] → [specific C0 behavior]` |
| C-07 | Web-verified claim with inline citation | **PASS** | GATE-2 requires "≥1 inline WebSearch citation within a competitor entry" + "Run a WebSearch" |
| C-08 | AMEND section with input-to-output pairs | **PASS** | GATE-4 schema names Input change + Output effect per row |
| C-09 | Cross-dimensional whitespace | **PASS** | GATE-3 includes cross-dimensional whitespace "only if FOCUS ACTIVE" with intersection requirement |
| C-10 | Grounded findings | **PASS** | "Findings must reference named competitor rows — findings readable without the competitive map fail" |
| C-11 | Inertia reference propagates downstream | **PASS** | TOKEN appears in `vs [TOKEN]:` and `[TOKEN] exposure:` — downstream propagation structurally required |
| C-12 | AMEND evaluates inertia stability | **PASS** | Stability verdict column requires "does TOKEN shift?" |
| C-13 | Token assigned portable token | **PASS** | GATE-0 declares `TOKEN: [domain-adaptive identifier]` as copyable token |
| C-14 | Stability in every AMEND entry | **PASS** | Schema requires "all four cells filled per row" including Stability verdict |
| C-15 | Token pre-declared before C0 description | **PASS** | GATE-0 (unconditional) runs before GATE-2 (C0 description) by execution ordering |
| C-16 | Stability verdict with evidence every entry | **PASS** | Evidence cells required "distinct from verdict text; 'Stable.' alone fails" |
| C-17 | Token encodes domain context | **PASS** | GATE-0 requires "at least one DOMAIN-TERMS term embedded" in TOKEN |
| C-18 | DOMAIN-TERMS committed before token construction | **PASS** | Separate `DOMAIN-TERMS:` line committed and closed before `TOKEN:` line; two discrete output artifacts |
| C-19 | TOKEN before any conditional logic | **PASS** | GATE-0 is unconditional and first; "nothing before them, nothing between them" |
| C-20 | AMEND schema enumerates all four components | **PASS** | GATE-4 schema table names all four: Input change, Output effect, Stability verdict, Evidence |
| C-21 | Pre-phase declares unconditional nature AND conditional successor | **PASS** | GATE-0 header: "UNCONDITIONAL — GATE-1 is the first conditional operation" |
| C-22 | AMEND schema names naive-reader consultable | **PASS** | "Input change," "Output effect," "Stability verdict," "Evidence" — all domain-neutral standard terms |
| C-23 | Pre-execution manifest enumerates all gates before first gate runs | **PASS** | EXECUTION PLAN table before GATE-0 lists all 5 gates with explicit execution-mode labels |
| C-24 | Manifest as native markdown table | **PASS** | EXECUTION PLAN uses pipe-and-hyphen table syntax outside code fence |
| C-25 | TOKEN required in every gate's output specification | **PASS** | `[TOKEN] required?` column with Yes/No cells in every gate's REQUIRED OUTPUTS table |
| C-26 | Per-gate REQUIRED OUTPUTS as structurally named blocks | **PASS** | Every gate has `**REQUIRED OUTPUTS:**` heading with dedicated table |
| C-27 | REQUIRED OUTPUTS sole spec — completion conditions replaced | **PASS** | Gates have instructional prose only, no parallel completion condition sections |
| C-28 | REQUIRED OUTPUTS as native markdown table per gate | **PASS** | All gate REQUIRED OUTPUTS use pipe-and-hyphen markdown |
| C-29 | TOKEN-required column per gate REQUIRED OUTPUTS table | **PASS** | `[TOKEN] required?` column with explicit Yes cells naming TOKEN by committed value after substitution |
| C-30 | Bracket-notation substitution rule declared | **PASS** | "substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4" |
| C-31 | GATE-0 REQUIRED OUTPUTS retains template form with propagation declaration | **PASS** | GATE-0 uses `[TOKEN] required?` column header; TOKEN Yes-cell states "GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers" |
| C-32 | Gate manifest includes TOKEN-propagation column | **PASS** | 4th column "TOKEN propagation" present in EXECUTION PLAN. GATE-0: "DECLARE — TOKEN committed here; committed value propagates to GATE-1+ REQUIRED OUTPUTS column headers by substitution." GATE-1+: "INHERIT — committed TOKEN substituted into REQUIRED OUTPUTS column header." Decisive test: GATE-0 = declaration site, GATE-1+ = substitution sites — readable from manifest alone without per-gate prose |

**V-01: 5/5 essential · 3/3 recommended · 24/24 aspirational → 60 + 30 + 10 = 100**

---

### Cross-Variation Diff Table

All variations share the same gate structure (C-01–C-31 identical). Differences are confined to the manifest TOKEN-propagation column content (C-32) and any structural additions in V-03/V-05.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 to C-31 | PASS | PASS | PASS | PASS | PASS |
| **C-32** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

**C-32 reasoning per variation:**

- **V-01** — `DECLARE` / `INHERIT` labels with "committed TOKEN substituted" in INHERIT cells. "INHERIT" covers "inheritance site"; "substituted" appears inline, satisfying "substitution/inheritance site." Readable from manifest alone. **PASS**
- **V-02** — Uses exact rubric vocabulary: "Declaration site" / "Substitution/inheritance site" verbatim. Most literal alignment with C-32 operative test. **PASS**
- **V-03** — Pre-manifest TOKEN-PROPAGATION ARCHITECTURE block provides the contract, then compact `DECLARE` / `SUBSTITUTE` labels in manifest column identify GATE-0 and GATE-1+ roles. Dual-layer architecture amplifies C-32 signal. **PASS**
- **V-04** — Bracket-notation `[TOKEN] propagation` column header participates in substitution lifecycle; extended substitution rule in cells identifies GATE-0 as declaration site and GATE-1+ as substitution sites. Decisive test (does bracket notation in manifest header cause committed-value substitution there?) does not affect C-32 pass — column cell content still identifies the roles. **PASS**
- **V-05** — Full prose manifest column (V-02 style) + dedicated propagation row in GATE-0 REQUIRED OUTPUTS table (R11 V-02 form). Maximum dual-layer coverage. Manifest column alone satisfies C-32; propagation row in GATE-0 table satisfies C-31 with maximum explicitness. **PASS**

---

### Composite Scores

| Rank | Variation | Essential | Recommended | Aspirational | Composite |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 (tie) | V-01 | 60 | 30 | 10 | **100** |
| 1 (tie) | V-02 | 60 | 30 | 10 | **100** |
| 1 (tie) | V-03 | 60 | 30 | 10 | **100** |
| 1 (tie) | V-04 | 60 | 30 | 10 | **100** |
| 1 (tie) | V-05 | 60 | 30 | 10 | **100** |

All 5 pass the golden threshold (all essential pass, composite ≥ 90).

---

### Excellence Signals

**From V-01 (compact binary labels):**
- `DECLARE` / `INHERIT` with one-clause rationale is the minimum viable C-32 form. The inclusion of "substituted" in the INHERIT cell body prevents the ambiguity the variation file flagged — no inference required.

**From V-02 (rubric-vocabulary prose):**
- Echoing "Declaration site" / "Substitution/inheritance site" verbatim is the highest-reliability C-32 signal. Model compliance probability is maximized because the column cell pre-answers the operative test without any interpretation step.

**From V-03 (pre-manifest architecture block):**
- A TOKEN-PROPAGATION ARCHITECTURE block before the manifest primes the column content rather than being redundant — it provides a plain-prose contract that the compact table labels abbreviate. Useful if compact labels alone prove fragile under model drift.

**From V-04 (bracket notation in manifest column header):**
- Making the column header itself participate in the substitution lifecycle creates a consistency signal: if the model substitutes the committed value into the header, it confirms substitution is understood at manifest level; if it outputs `[TOKEN] propagation` literally, it reveals substitution is scoped to REQUIRED OUTPUTS tables only. V-04 is the best diagnostic variation for detecting substitution-scope confusion.

**From V-05 (maximum dual-layer):**
- Verbose manifest column (C-32) + dedicated GATE-0 propagation row (C-31) is belt-and-suspenders. Neither layer depends on the other for compliance — each independently satisfies its criterion.

---

### R13 Implications

C-32 is **non-separating at current fidelity** — all 5 variations satisfy it without difficulty. The manifest TOKEN-propagation column is now well-understood by the rubric chain. To produce separation in R13, a new criterion would need to require one of:

1. **Manifest column carries BOTH a STATUS label (DECLARE/SUBSTITUTE) AND a SCOPE field** naming which output artifacts TOKEN appears in per gate (not just "committed TOKEN in column header" but "column header + C0 field label + map column" for GATE-2, etc.)
2. **Bracket-substitution active in manifest column header** — require that after GATE-0 commits `SIGNAL-LOCK`, the manifest column header reads `SIGNAL-LOCK propagation` in GATE-1+ rows, not `[TOKEN] propagation` — testing whether substitution scope extends to the manifest itself

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["DECLARE/INHERIT binary labels with inline 'substituted' evidence satisfy C-32 without prose overhead — minimum viable form confirmed", "C-32 is non-separating at current fidelity — any reasonable manifest TOKEN-propagation column implementation passes; R13 must require manifest-column SCOPE fields or bracket-substitution active in manifest column header to produce separation"]}
```
