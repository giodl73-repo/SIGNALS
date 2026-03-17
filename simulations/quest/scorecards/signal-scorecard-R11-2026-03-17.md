## Round 11 Scorecard -- /signal

### Leaderboard

| Rank | Variation | Asp (27) | Score | Golden? |
|------|-----------|----------|-------|---------|
| 1 | **V-04** P+Q (both gates full) | 27/27 | **100.00** | YES |
| 1 | **V-05** Full golden baseline | 27/27 | **100.00** | YES |
| 3 | V-01 P only (FULL format check) | 26/27 | **99.63** | no |
| 3 | V-02 Q only (BARE order check) | 26/27 | **99.63** | no |
| 5 | V-03 Neither (control) | 25/27 | **99.26** | no |

---

### Per-criterion evaluation

**C-01 through C-33**: PASS across all five variations. All share the identical R10 V-05 baseline -- catalog, headers, footers, PARSE MODE, SECTION FORMAT, ALIGNMENT WIDTH TABLE, DOMAIN NOUN TABLE, per-section self-check, transcription gate, slash-strip examples, and all existing compliance gate checks are unchanged.

**C-34 (FULL gate format check)**:
- V-01, V-04, V-05: **PASS** -- "run all **four** checks" + Check 4 specifies header, "-> " lines, dispatch footer
- V-02, V-03: **FAIL** -- "run all **three** checks" -- Check 4 absent

**C-35 (BARE gate order check)**:
- V-02, V-04, V-05: **PASS** -- "run all **three** checks" + Check 3 specifies positional group boundaries (first 8 = scout-*, next 4 = draft-*, ... last 4 = org-*)
- V-01, V-03: **FAIL** -- "run **both** checks" -- order check absent

---

### Independence verification

| Test | Result | Meaning |
|------|--------|---------|
| V-01 - V-03 | +0.37 | C-34 independent |
| V-02 - V-03 | +0.37 | C-35 independent |
| V-04 - V-01 | +0.37 | no P x Q interaction |
| V-04 - V-02 | +0.37 | no P x Q interaction |
| V-04 = V-05 | 100.00 | ceiling confirmed |

---

### Excellence signals

1. **Gate-check type symmetry**: V-04/V-05 are the only variations where every check type (completeness, format, order, scope) that applies to a mode is present in that mode's gate. V-03 has two asymmetries; V-01/V-02 have one each.

2. **Format check mirrors the spec**: FULL gate Check 4 restates SECTION FORMAT sub-elements verbatim at the enforcement point -- creating a runtime verification rather than a distant reference.

3. **Positional group boundaries for headerless output**: BARE gate Check 3 uses line-range groupings ("first 8 lines are scout-* names...") rather than namespace name lists, which is the only valid order check for BARE mode where there are no headers to anchor identity.

**Rubric status**: v11 saturated. All 27 aspirational criteria pass at 100.00. No remaining gate-check asymmetries. R12 would need a new axis entirely.

Scorecard written to `simulations/quest/scorecards/signal-scorecard-R11-2026-03-17.md`.

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Gate-check type symmetry across modes: every check type (completeness, format, order, scope) applicable to a mode must be present in that mode's gate -- closing asymmetries is the path from 99.26 to 100.00", "Format check embeds the spec at the gate: FULL Check 4 restates SECTION FORMAT sub-elements verbatim, creating a runtime enforcement point rather than a distant reference", "Positional group boundaries for headerless output: BARE gate order check uses line-range groupings rather than namespace name lists -- the only valid order invariant when headers are absent"]}
```
derived pad computation per row |
| C-17 | aspirational | PASS | "NAMESPACE CATALOG -- TRANSCRIPTION GATE" appears before all behavioral rule sections |
| C-18 | aspirational | PASS | BARE Check 2: "exactly 61 lines (8 scout + 4 draft + ... = 61)" -- labeled breakdown present |
| C-19 | aspirational | PASS | PARSE MODE: "Canonical namespaces (exactly these 12): scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org" |
| C-20 | aspirational | PASS | FILTER Check 2 states canonical counts for all 12 namespaces |
| C-21 | aspirational | PASS | "Begin with scout-competitors. End with org-committee." explicit anchors in BARE MODE |
| C-22 | aspirational | PASS | "NAMESPACE CATALOG -- TRANSCRIPTION GATE" with "confirm you have read all 61 entries" pre-transcription gate |
| C-23 | aspirational | PASS | "The catalog below IS the output for FULL and FILTER modes." labeled as literal output |
| C-24 | aspirational | PASS | All three modes (FULL, BARE, FILTER) have explicit pre-emission compliance gates |
| C-25 | aspirational | PASS | FULL MODE compliance restart gate covers namespace-presence (Check 1) + count (Check 2) |
| C-26 | aspirational | PASS | Transcription gate: "confirm you have read all 61 entries" requires counted acknowledgment |
| C-27 | aspirational | PASS | "Per-section count self-check: before emitting the dispatch footer...verify the number of sub-skill lines equals the canonical count...AND equals the N stated in the header. If either count differs, restart." |
| C-28 | aspirational | PASS | FULL gate Check 3 (order): "Canonical order: scout, draft, review, flow, trace, prove, listen, program, topic, quest, mock, org. (First: scout. Last: org.)" -- present in all variations |
| C-29 | aspirational | PASS | FILTER gate Check 3 (format): requires header, "-> " lines, and dispatch footer -- present in all variations |
| C-30 | aspirational | PASS | Slash-strip worked examples present: "/scout-competitors becomes scout-competitors" (first) + "/org-committee becomes org-committee" (last) |
| C-31 | aspirational | PASS | Labeled breakdown appears in transcription gate ("8 scout + 4 draft + ... = 61") and BARE Check 2 (same breakdown) |
| C-32 | aspirational | PASS | "DOMAIN NOUN TABLE" heading present; named formal table with 12 rows |
| C-33 | aspirational | PASS | FULL gate Check 3 enumerates all 12 namespace names in canonical sequence with "First section: scout. Last section: org." |

---

### C-34 -- FULL MODE compliance gate includes section-format verification (Check 4)

| Variation | C-34 | Evidence |
|-----------|------|----------|
| V-01 | **PASS** | "Before emitting FULL output, run all **four** checks" + Check 4 (format): "(1) a header line in the form '- /\<namespace\> -- \<purpose\> -- \<N\> skills', (2) sub-skill lines each using the '-> ' separator, (3) a dispatch footer in the form 'Run any sub-skill directly...'" |
| V-02 | **FAIL** | "Before emitting FULL output, run all **three** checks" -- Check 4 absent; FULL gate stops after Check 3 (order) |
| V-03 | **FAIL** | "Before emitting FULL output, run all **three** checks" -- same as V-02; control baseline |
| V-04 | **PASS** | "Before emitting FULL output, run all **four** checks" + Check 4 identical to V-01 |
| V-05 | **PASS** | "Before emitting FULL output, run all **four** checks" + Check 4 identical to V-01; canonical golden text |

---

### C-35 -- BARE MODE compliance gate includes canonical namespace emit-order check (Check 3)

| Variation | C-35 | Evidence |
|-----------|------|----------|
| V-01 | **FAIL** | "Before emitting bare output, run **both** checks" -- only Check 1 (format) and Check 2 (completeness); order check absent |
| V-02 | **PASS** | "Before emitting bare output, run all **three** checks" + Check 3 (order): "first 8 lines are scout-* names, next 4 are draft-* names..." through "last 4 are org-* names" |
| V-03 | **FAIL** | "Before emitting bare output, run **both** checks" -- same as V-01; control baseline |
| V-04 | **PASS** | "Before emitting bare output, run all **three** checks" + Check 3 identical to V-02 |
| V-05 | **PASS** | "Before emitting bare output, run all **three** checks" + Check 3 identical to V-02; canonical golden text |

---

## Composite Score Computation

Formula: `composite = 100.00 - (27 - asp_pass) x 0.37`

| Variation | C-34 | C-35 | Asp (27) | Score |
|-----------|------|------|----------|-------|
| V-01 | PASS | FAIL | 26/27 | **99.63** |
| V-02 | FAIL | PASS | 26/27 | **99.63** |
| V-03 | FAIL | FAIL | 25/27 | **99.26** |
| V-04 | PASS | PASS | 27/27 | **100.00** |
| V-05 | PASS | PASS | 27/27 | **100.00** |

### Independence verification

| Test | Computation | Result | Interpretation |
|------|-------------|--------|----------------|
| V-01 - V-03 | 99.63 - 99.26 | **+0.37** | C-34 (P) is independent: FULL gate format check contributes exactly one criterion |
| V-02 - V-03 | 99.63 - 99.26 | **+0.37** | C-35 (Q) is independent: BARE gate order check contributes exactly one criterion |
| V-04 - V-01 | 100.00 - 99.63 | **+0.37** | Adding Q to P gives same increment (no interaction) |
| V-04 - V-02 | 100.00 - 99.63 | **+0.37** | Adding P to Q gives same increment (no interaction) |
| V-04 vs V-05 | 100.00 = 100.00 | **equal** | Ceiling confirmed; V-04 and V-05 are structurally equivalent under v11 |

**Conclusion**: P and Q are fully independent. Each adds exactly +0.37. Mode symmetry closure
is confirmed complete.

---

## Excellence Signals (from V-04 and V-05)

The top variations (V-04, V-05 at 100.00) succeed where V-01/V-02/V-03 do not because of
**complete gate-check type coverage across all output modes**. Three patterns define the ceiling:

### Pattern 1: Gate-check type symmetry across modes

Every check type that is meaningful for a given output mode is present in that mode's gate:

| Check type | FULL gate | BARE gate | FILTER gate |
|------------|-----------|-----------|-------------|
| Completeness | Check 2 (count) | Check 2 (61 lines) | Check 2 (namespace count) |
| Format | Check 4 | Check 1 (bare format) | Check 3 (section format) |
| Order | Check 3 | Check 3 | N/A (single ns) |
| Scope | Check 1 (all 12) | (implicit in order) | Check 1 (ns scope) |

V-03 is missing both Check 4 from FULL and Check 3 from BARE -- two asymmetries
simultaneously. V-01 closes the FULL gap but not BARE. V-02 closes the BARE gap but not FULL.
Only V-04/V-05 close both.

### Pattern 2: Format check phrasing mirrors the specification

FULL gate Check 4 specifies three required sub-elements directly from SECTION FORMAT:
(1) header in the form "- /\<namespace\> -- \<purpose\> -- \<N\> skills"
(2) sub-skill lines each using the "-> " separator
(3) dispatch footer in the form "Run any sub-skill directly, or describe your \<domain-noun\>..."

This is not a new rule -- it is a runtime verification of SECTION FORMAT at the gate. The
repetition creates a second enforcement point for the same contract, in the location where
failure triggers a restart. Embedding the spec in the gate is more robust than a distant
reference.

### Pattern 3: BARE gate order check uses positional group boundaries

FULL gate Check 3 names all 12 namespaces in sequence (appropriate when headers are present
to anchor namespace identity). BARE gate Check 3 uses a complementary formulation: numbered
group boundaries by line range ("first 8 lines are scout-* names, next 4 are draft-* names,
...last 4 are org-* names"). In headerless output, positional group offsets are the only
structural invariant available. The positional formulation is the uniquely correct order check
for BARE mode.

---

## R11 Summary

| Goal | Result |
|------|--------|
| Confirm C-34 (P) independent | YES -- V-01 - V-03 = +0.37 |
| Confirm C-35 (Q) independent | YES -- V-02 - V-03 = +0.37 |
| Confirm no P x Q interaction | YES -- V-04 - V-01 = V-04 - V-02 = +0.37 |
| Ceiling confirmed at 100.00 | YES -- V-04 = V-05 = 100.00 |
| Mode symmetry closure complete | YES -- all three gates now have format + order checks where applicable |

**Golden prompt for v11**: V-05 (canonical R10 V-05 text, confirmed at 100.00 under v11
rubric). V-04 is structurally equivalent and also qualifies as golden.

**Rubric status**: v11 saturated. All 27 aspirational criteria achieved. No open asymmetries
remain in the gate-check coverage matrix. The rubric may be complete for the `signal` skill
at this level of specification depth, or R12 would need to identify a new axis entirely.
