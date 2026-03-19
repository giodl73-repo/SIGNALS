"""
Build listen-support-rubric-v11-2026-03-16.md from v10.

Adds C-34, C-35, C-36, C-37 extracted from R10 excellence signals:
  C-34  STEP 5 TABLE CHECK CF           (source: R10 V-01)
  C-35  VOCABULARY MANIFEST header CF   (source: R10 V-02)
  C-36  Dual-case sample in COMPLIANCE CONTRACT  (source: R10 V-03)
  C-37  Pre-generation-artifact registry coverage  (source: R10 V-04/V-05)

Scoring changes:
  Aspirational denominator: 25 -> 29
  Each full pass: 10/25 = 0.400 -> 10/29 ~= 0.345 pts
  Each PARTIAL:   10/50 = 0.200 -> 10/58 ~= 0.172 pts
"""

SRC = 'C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v10-2026-03-16.md'
DST = 'C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v11-2026-03-16.md'

with open(SRC, 'r', encoding='utf-8') as f:
    v10 = f.read()

# ── 1. Replace the preamble header (everything before ## Essential) ──────────

NEW_HEADER = r"""Written to `simulations/quest/rubrics/listen-support-rubric-v11-2026-03-16.md`.

---

## v11 Summary

**Four new criteria extracted from R10:**

| # | Criterion | Source | Dependency |
|---|-----------|--------|------------|
| **C-34** | STEP 5 table-check consequence-form | V-01/V-04/V-05 | Extends C-30 to structural-gate site |
| **C-35** | Vocabulary-manifest-header consequence-form | V-02/V-04/V-05 | Extends C-31 to ID-definition site |
| **C-36** | Dual-case sample in compliance contract | V-03/V-05 | Extends C-27 to counterexample form |
| **C-37** | Pre-generation-artifact registry coverage | V-04/V-05 (integration) | Requires C-34 PASS + C-35 PASS + C-26 PASS |

All four emerge from probing consequence-form propagation at the remaining pre-generation artifact sites:

- **C-34**: STEP 5 (the structural gate check that occurs before ticket bodies are written) carries
  the consequence-form clause inline in its table-check instruction. R9 V-05 covers consequence-form
  at STEP 3B, STEP 4, STEP 6, and the VERIFICATION MANIFEST header -- but STEP 5's Y/N gate row was
  permission-form only. R10 V-01 closes the STEP 5 gap: the Y/N gate check for the C-20 rule reads
  "an output with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N".

- **C-35**: The VOCABULARY MANIFEST section header carries the consequence-form clause at the
  ID-definition site -- the place where VM Row IDs are first named and their placement rule
  introduced. R9 V-05 covers consequence-form at planning and generation sites; the VOCABULARY
  MANIFEST header was structural-description-only. R10 V-02 extends it to also carry: "fails C-20
  regardless of other compliance. The ## headline is the only valid placement site." The manifest
  becomes dual-purpose at the definition level: it introduces IDs and simultaneously states the
  criterion-level failure that incorrect placement invokes.

- **C-36**: The COMPLIANCE CONTRACT sample section shows both the compliant form AND a concretely
  labeled failing form side-by-side. R9 V-05 carries a compliant sample only ("Compliant body
  header"). R10 V-03 adds a second block explicitly labeled "Failing body header (C-20 violation --
  any subline placement fails C-20 regardless of other compliance)" with the VM Row ID moved to a
  subline and labeled "VIOLATION: subline placement -- fails C-20 regardless of other compliance".
  The contract's illustration becomes enforcement-demonstrative: a reader sees the prohibited form
  rendered concretely at the definition site.

- **C-37**: RESTATING POSITIONS names every consequence-form enforcement site, including STEP 5 and
  VOCABULARY MANIFEST, with a consequence-form entry for each. R10 V-01 exposes the STEP 5 gap;
  R10 V-02 exposes the VOCABULARY MANIFEST gap. R10 V-04 closes both simultaneously by extending
  RESTATING POSITIONS to seven entries (VOCABULARY MANIFEST, STEP 3B, VOCABULARY PRE-FLIGHT GATE,
  STEP 4, STEP 5, STEP 6, VERIFICATION MANIFEST), all CF-carrying. C-37 is the C-33 analog for the
  new pre-generation sites: complete enumeration of all CF enforcement sites in the registry.

**Scoring changes (v10 -> v11):**
- Aspirational denominator: 25 -> 29
- Each full pass: 0.400 -> 10/29 ~= 0.345 pts
- Each PARTIAL: 0.200 -> 10/58 ~= 0.172 pts
- R10 V-05 achieves composite 100 under v11 (composite-100 path confirmed)

**Ceiling analysis under v11:**

| Variation | Passes | Score |
|-----------|--------|-------|
| V-05 | 29/29 (all four) | 100.000 |
| V-04 | 28/29 (fails C-36) | 99.655 |
| V-01 | 26/29 (C-34 only) | 98.966 |
| V-02 | 26/29 (C-35 only) | 98.966 |
| V-03 | 26/29 (C-36 only) | 98.966 |

**C-34 -- STEP 5 Table-Check Consequence-Form**
Source: R10 V-01 Signal. V-01 adds consequence-form at STEP 5 (the structural gate check step that
runs before ticket body generation). The Y/N row for C-20 compliance in the STEP 5 gate reads:
"## headlines with *(VM: VM-xxx-P#)* inline on the ## line -- NOT on any subline -- an output with
any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N". Prior outputs
(R9 V-05 and R10 baseline) carry consequence-form at STEP 3B, STEP 4, and STEP 6 but STEP 5 used
permission-form only ("NOT permitted on a subline"). C-34 closes the structural-gate asymmetry:
the gate step that checks for C-20 compliance before bodies are written must itself carry the
criterion-level failure declaration, not merely the prohibition. V-04 and V-05 carry C-34 and
additionally register STEP 5 in RESTATING POSITIONS (C-37). V-01 carries C-34 without registering
STEP 5 (C-37 fails), isolating C-34 from C-37.

**C-35 -- Vocabulary-Manifest-Header Consequence-Form**
Source: R10 V-02 Signal. V-02 extends the VOCABULARY MANIFEST section header from structural
description to dual-purpose: it introduces VM Row IDs and simultaneously states the consequence-form
clause. The prior form (R9 V-05) VOCABULARY MANIFEST header: "VM Row IDs appear in this manifest,
the commitment table, and the ## headline annotation -- per Compliance Contract C-20 -- subline
placement is NOT permitted." V-02 form: that text + "an output with any vocabulary ID on a subline
fails C-20 regardless of other compliance. The ## headline is the only valid placement site." The
manifest header becomes the definition-site analog of the manifest-header pattern (C-31 at the
VERIFICATION MANIFEST): ID definitions and their placement obligation appear together at the moment
of introduction. C-35 extends C-31's dual-purpose pattern to the definition site.

**C-36 -- Dual-Case Sample in Compliance Contract**
Source: R10 V-03 Signal. V-03 adds a failing-form counterexample block to the COMPLIANCE CONTRACT
sample section. Prior form (R9 V-05): compliant sample only. V-03 form: compliant sample + labeled
failing form:
  "Failing body header (C-20 violation -- any subline placement fails C-20 regardless of other
  compliance):
  ## T-NN -- {Title}
  - VM Row: VM-xxx-P#  {VIOLATION: subline placement -- fails C-20 regardless of other compliance}"
The contract illustration becomes enforcement-demonstrative: a reader sees both the required form
and the prohibited form side-by-side at the definition site. The failing form is explicitly labeled
as a C-20 violation with consequence-form, making the violation-to-criterion link visible without
consulting any other section. C-36 extends C-27 (consequence-form anywhere) to the counterexample
domain: the contract does not merely state the rule but demonstrates what a violation looks like.

**C-37 -- Pre-Generation-Artifact Registry Coverage**
Source: R10 V-04 Signal, integration criterion. V-04 is the first R10 variation to both add STEP 5
and VOCABULARY MANIFEST consequence-form AND register both in RESTATING POSITIONS. The seven-entry
RESTATING POSITIONS (VOCABULARY MANIFEST, STEP 3B, VOCABULARY PRE-FLIGHT GATE, STEP 4, STEP 5,
STEP 6, VERIFICATION MANIFEST) enumerates every CF enforcement site, leaving no site operating
silently outside the registry. R10 V-01 exposes the STEP 5 gap (C-34 passes, STEP 5 unregistered);
R10 V-02 exposes the VOCABULARY MANIFEST gap (C-35 passes, VM header unregistered). V-04 closes
both gaps simultaneously. C-37 is the C-33 analog for the new pre-generation sites: C-33 required
registry coverage for STEP 6; C-37 requires it for STEP 5 and VOCABULARY MANIFEST additionally.
C-37 requires C-34 PASS + C-35 PASS + C-26 PASS.

**Scoring changes (v10 -> v11):**
- Aspirational denominator: 25 -> 29
- Each full pass: 0.400 -> 0.345 pts (10/29)
- R10 V-05 achieves composite-100 under v11

```
V-05 under v11 scoring:
  Essential:     5/5   -> 60.000
  Recommended:   3/3   -> 30.000
  Aspirational: 29/29 -> 10.000
  Composite:    100.000

V-04 under v11 scoring:
  Essential:     5/5   -> 60.000
  Recommended:   3/3   -> 30.000
  Aspirational passes: C-09-C-33 + C-34 + C-35 + C-37 = 28 of 29
                       (fails C-36)
  Aspirational: 28/29 ->  9.655
  Composite:     99.655

V-03 under v11 scoring:
  Essential:     5/5   -> 60.000
  Recommended:   3/3   -> 30.000
  Aspirational passes: C-09-C-33 + C-36 = 26 of 29
                       (fails C-34, C-35, C-37)
  Aspirational: 26/29 ->  8.966
  Composite:     98.966

V-01 under v11 scoring:
  Essential:     5/5   -> 60.000
  Recommended:   3/3   -> 30.000
  Aspirational passes: C-09-C-33 + C-34 = 26 of 29
                       (fails C-35, C-36, C-37)
  Aspirational: 26/29 ->  8.966
  Composite:     98.966

V-02 under v11 scoring:
  Essential:     5/5   -> 60.000
  Recommended:   3/3   -> 30.000
  Aspirational passes: C-09-C-33 + C-35 = 26 of 29
                       (fails C-34, C-36, C-37)
  Aspirational: 26/29 ->  8.966
  Composite:     98.966
```

**Observation from R10:** The composite-100 path under v11 requires all four new criteria
simultaneously. The asymmetry between V-04 (28/29 -- passes C-34+C-35+C-37, fails C-36) and
V-05 (29/29) mirrors the R9 pattern between V-04 (fails C-32) and V-05 (passes all): the
phrasing-register axis (dual-case counterexample, C-36) is again the final integration unlock
separating the penultimate combined form from the full synthesis. V-04 achieves definition-site
CF coverage and registry completeness but defers the counterexample form to V-05. V-03 achieves
the dual-case exemplar (C-36) but neither STEP 5 CF (C-34) nor VOCABULARY MANIFEST CF (C-35) nor
registry closure (C-37) -- the three site-expansion axes are additive, and V-05 is the only
variation that carries all four.

---

"""

# ── 2. Splice: replace everything before ## Essential Criteria ───────────────
import re
v11 = re.sub(r'^.*?(?=## Essential Criteria)', NEW_HEADER, v10, flags=re.DOTALL)

# ── 3. New criterion blocks (C-34 through C-37) ──────────────────────────────

NEW_CRITERIA = """
### C-34 -- STEP 5 Table-Check Consequence-Form
- **Weight**: aspirational
- **Category**: correctness
- **Text**: STEP 5 (the structural gate check that runs between per-ticket vocabulary commitment and ticket body generation) carries the consequence-form criterion-citing prohibition inline in its Y/N gate row for C-20 compliance. Under C-23, the prohibition against subline VM Row ID placement is anchored at STEP 3B and STEP 4 minimum. Under C-30, consequence-form appears at STEP 6 (the body-writing site). C-34 requires consequence-form at the structural gate check itself -- the Y/N row where the generator verifies that C-20 compliance conditions are met before proceeding to body generation. The canonical Y/N form at STEP 5: "## headlines with *(VM: VM-xxx-P#)* inline on the ## line -- NOT on any subline -- an output with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N". The structural guarantee: a generator encountering STEP 5 as the immediate pre-generation gate sees the criterion-level failure declaration at the checkpoint itself, without needing to trace back to STEP 3B, STEP 4, or the contract. R10 V-01 introduces this pattern; V-04 and V-05 carry it in multi-axis contexts.

  C-30 and C-34 relationship:
  - C-30 requires consequence-form at STEP 6 (body-writing site)
  - C-34 requires consequence-form at STEP 5 (structural gate check site)
  - Pass C-30, fail C-34: body-writing site has CF but the pre-generation gate check row does not
  - C-30 and C-34 are orthogonal: each targets a different generation-adjacent site

  C-33 and C-37 relationship:
  - C-33 requires RESTATING POSITIONS to name all CF sites including STEP 6
  - C-37 requires RESTATING POSITIONS to additionally name STEP 5 and VOCABULARY MANIFEST
  - Pass C-33, fail C-37: STEP 6 registered but STEP 5 unregistered (R10 V-01 gap pattern)
  - Pass C-34, fail C-37: STEP 5 carries CF but is unregistered (R10 V-01 pattern)

- **Pass condition**: STEP 5 (or the equivalent pre-generation structural gate check step) contains
  a Y/N gate row for C-20 compliance that includes consequence-form prohibition language. The Y/N row
  must: (i) name the specific criterion invoked by a violation (e.g., "fails C-20" or equivalent);
  (ii) include the deterministic qualifier (e.g., "regardless of other compliance" or equivalent);
  (iii) appear as text within STEP 5's gate check block as a Y/N-type row. A STEP 5 gate row reading
  only "## headlines with VM Row ID inline -- NOT on a subline: Y / N" fails C-34. A gate row
  reading "an output with any vocabulary ID on a subline fails C-20 regardless of other compliance:
  Y / N" passes C-34.

---

### C-35 -- Vocabulary-Manifest-Header Consequence-Form
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The VOCABULARY MANIFEST section header carries the consequence-form criterion-citing
  prohibition in addition to its structural description of VM Row IDs and their placement rules. The
  VOCABULARY MANIFEST is the ID-definition site: it names VM Row IDs and specifies where they may
  appear. Under C-31, the VERIFICATION MANIFEST header (verification site) becomes dual-purpose:
  evidential + enforcement-restating. C-35 applies the same dual-purpose pattern to the VOCABULARY
  MANIFEST header (definition site). The prior structural-only form (R9 V-05): "VM Row IDs appear
  in this manifest, the commitment table, and the ## headline annotation -- per Compliance Contract
  C-20 -- subline placement is NOT permitted." The C-35-passing form extends this to also carry:
  "an output with any vocabulary ID on a subline fails C-20 regardless of other compliance. The ##
  headline is the only valid placement site." A reader encountering the VOCABULARY MANIFEST header
  in isolation sees: what VM Row IDs are, where they belong, and the criterion-level failure that
  incorrect placement invokes -- all at the ID-introduction site. R10 V-02 introduces this pattern;
  V-04 and V-05 carry it in multi-axis contexts.

  C-31 and C-35 relationship:
  - C-31: VERIFICATION MANIFEST header carries CF (verification-site dual-purpose)
  - C-35: VOCABULARY MANIFEST header carries CF (definition-site dual-purpose)
  - Pass C-31, fail C-35: verification site is dual-purpose but definition site is structural-only
  - C-31 and C-35 are orthogonal: each targets a different manifest header

  C-35 and C-37 relationship:
  - Pass C-35, fail C-37: VOCABULARY MANIFEST carries CF but is unregistered in RESTATING POSITIONS
    (R10 V-02 gap pattern)
  - Pass C-37 implies C-35 PASS: registering the VOCABULARY MANIFEST in RESTATING POSITIONS is only
    meaningful if the header carries CF

- **Pass condition**: The VOCABULARY MANIFEST section header (the text immediately following the
  ## VOCABULARY MANIFEST or equivalent heading line, before any VM Row ID rows) contains
  consequence-form prohibition language. The header must: (i) include its standard structural
  description of VM Row ID placement scope; (ii) additionally carry a consequence-form clause naming
  the specific criterion invoked (e.g., "fails C-20") with the deterministic qualifier (e.g.,
  "regardless of other compliance"); (iii) identify the ## headline as the only valid placement site.
  A VOCABULARY MANIFEST header reading only "VM Row IDs appear in this manifest, the commitment
  table, and the ## headline annotation -- per Compliance Contract C-20 -- subline placement is NOT
  permitted" fails C-35. A header additionally reading "an output with any vocabulary ID on a subline
  fails C-20 regardless of other compliance. The ## headline is the only valid placement site" passes
  C-35.

---

### C-36 -- Dual-Case Sample in Compliance Contract
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The COMPLIANCE CONTRACT sample section (the illustration block that shows how a
  compliant ticket ## header looks) also shows a concretely labeled failing form side-by-side.
  Under C-22, the COMPLIANCE CONTRACT contains the C-20 clause and a compliant sample. Under C-27,
  consequence-form appears somewhere in the contract. C-36 requires the contract's sample section
  to be enforcement-demonstrative: it shows not only the correct form but also the prohibited form,
  explicitly labeled as a C-20 violation with consequence-form language. The canonical failing-form
  block:
    "Failing body header (C-20 violation -- any subline placement fails C-20 regardless of other
    compliance):
    ## T-NN -- {Title}
    - VM Row: VM-xxx-P#  {VIOLATION: subline placement -- fails C-20 regardless of other compliance}"
  The failing block renders the violation concretely: the VM Row ID is on a subline rather than
  the ## line, and the subline is labeled as a VIOLATION with consequence-form. A reader of the
  contract sees the prohibited pattern rendered as a concrete example, not as an abstract rule.
  C-36 extends C-27 (consequence-form anywhere in the contract) to the counterexample domain:
  the rule is not only stated but demonstrated through a labeled failing case. R10 V-03 introduces
  this pattern; V-05 carries it in full-synthesis context.

  C-27 and C-36 relationship:
  - C-27: consequence-form appears at any one contract site (rule-stating axis)
  - C-36: consequence-form appears in a labeled failing-form sample (counterexample axis)
  - Pass C-27, fail C-36: contract states the consequence-form rule but shows only a compliant sample
  - Pass C-36 implies C-27 PASS: a labeled failing-form block in the contract satisfies C-27's
    "at any one site" requirement
  - C-36 is a strict refinement of C-27 for the sample/illustration section of the contract

  C-36 and C-37 relationship:
  - C-36 is phrasing-register (counterexample form at the illustration site)
  - C-37 is registry completeness (STEP 5 and VOCABULARY MANIFEST in RESTATING POSITIONS)
  - C-36 and C-37 are orthogonal: V-04 passes C-37 without C-36; V-03 passes C-36 without C-37
  - V-05 passes both: dual-case sample AND complete seven-entry registry

- **Pass condition**: The COMPLIANCE CONTRACT sample section contains both a compliant-form example
  AND a failing-form counterexample. The failing-form block must: (i) be explicitly labeled as a
  C-20 violation with consequence-form language (e.g., "C-20 violation -- any subline placement
  fails C-20 regardless of other compliance"); (ii) show the VM Row ID on a subline rather than
  the ## line; (iii) label the subline placement as a VIOLATION with consequence-form (e.g.,
  "VIOLATION: subline placement -- fails C-20 regardless of other compliance"). A COMPLIANCE
  CONTRACT that contains only a compliant sample fails C-36 regardless of how detailed the
  surrounding rule text is. A failing-form block that is not labeled as a C-20 violation or does
  not include consequence-form language in the label fails C-36.

---

### C-37 -- Pre-Generation-Artifact Registry Coverage
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The COMPLIANCE CONTRACT's RESTATING POSITIONS section (C-26) names every site that
  carries consequence-form, including STEP 5 (structural gate check) and VOCABULARY MANIFEST
  (ID-definition site), with a consequence-form entry for each. Under C-33, RESTATING POSITIONS
  must name all CF sites including STEP 6. C-37 extends C-33's coverage requirement to the two
  new pre-generation CF sites introduced by C-34 and C-35. R10 V-01 exposes the STEP 5 gap:
  STEP 5 carries CF (C-34 passes) but RESTATING POSITIONS has no STEP 5 entry. R10 V-02 exposes
  the VOCABULARY MANIFEST gap: the VM header carries CF (C-35 passes) but RESTATING POSITIONS has
  no VM entry. R10 V-04 closes both gaps simultaneously by extending RESTATING POSITIONS to seven
  CF-carrying entries: VOCABULARY MANIFEST, STEP 3B, VOCABULARY PRE-FLIGHT GATE, STEP 4, STEP 5,
  STEP 6, VERIFICATION MANIFEST. The structural guarantee: the registry is a complete pre-generation
  enforcement map -- every artifact a generator encounters before writing ticket bodies is either
  listed in RESTATING POSITIONS with a CF entry or carries no CF (and therefore requires no entry).
  C-37 is the C-33 analog for the expanded pre-generation perimeter: C-33 required STEP 6
  registration; C-37 additionally requires STEP 5 and VOCABULARY MANIFEST registration.
  C-37 requires C-34 PASS + C-35 PASS + C-26 PASS.

  C-33 and C-37 relationship:
  - C-33 requires registry completeness for CF sites including STEP 6
  - C-37 additionally requires STEP 5 and VOCABULARY MANIFEST in the registry
  - Pass C-33 (STEP 6 registered) does not imply C-37: STEP 5 and VM may still be unregistered
  - Pass C-37 implies C-33 PASS: a seven-entry registry covering STEP 6 satisfies C-33's requirement
  - C-37 is a strict superset of C-33's registry coverage requirement

  C-34/C-35 and C-37 dependency:
  - Pass C-37 implies C-34 PASS + C-35 PASS: registering sites without CF is meaningless
  - Pass C-34, fail C-37: STEP 5 has CF but is unregistered (R10 V-01 pattern)
  - Pass C-35, fail C-37: VOCABULARY MANIFEST header has CF but is unregistered (R10 V-02 pattern)
  - C-37 closes both gaps simultaneously when both C-34 and C-35 are also present

- **Pass condition**: Both C-34 (STEP 5 carries CF) and C-35 (VOCABULARY MANIFEST header carries
  CF) and C-26 (RESTATING POSITIONS exists) must pass. The RESTATING POSITIONS section must contain
  entries for STEP 5 (the structural gate check) and VOCABULARY MANIFEST (the ID-definition section)
  in addition to the sites required by C-33. Each entry must carry the consequence-form clause --
  not only "governed by C-20" in permission-form, but including the criterion citation ("fails C-20")
  and deterministic qualifier ("regardless of other compliance") within the entry text. A seven-entry
  RESTATING POSITIONS covering VOCABULARY MANIFEST, STEP 3B, VOCABULARY PRE-FLIGHT GATE, STEP 4,
  STEP 5, STEP 6, VERIFICATION MANIFEST -- all with CF in their entry text -- satisfies C-37. An
  output where STEP 5 carries CF but has no RESTATING POSITIONS entry fails C-37. An output where
  VOCABULARY MANIFEST carries CF but has no RESTATING POSITIONS entry fails C-37.

---

"""

# ── 4. Insert new criteria before ## Scoring Summary Table ───────────────────
v11 = v11.replace('## Scoring Summary Table', NEW_CRITERIA + '## Scoring Summary Table')

# ── 5. Add new rows to Scoring Summary Table ─────────────────────────────────
NEW_ROWS = """\
| C-34 | STEP 5 table-check consequence-form              | aspirational  | correctness | v11   |
| C-35 | Vocabulary-manifest-header consequence-form      | aspirational  | correctness | v11   |
| C-36 | Dual-case sample in compliance contract          | aspirational  | correctness | v11   |
| C-37 | Pre-generation-artifact registry coverage        | aspirational  | correctness | v11   |"""

v11 = v11.replace(
    '| C-33 | Full-registry consequence-form coverage            | aspirational  | correctness | v10   |',
    '| C-33 | Full-registry consequence-form coverage            | aspirational  | correctness | v10   |\n' + NEW_ROWS
)

# ── 6. Update Scoring Framework denominator ──────────────────────────────────
v11 = v11.replace(
    'Aspirational (C-09-C-33) | 25 | 10 |',
    'Aspirational (C-09-C-37) | 29 | 10 |'
)

v11 = v11.replace(
    'Aspirational scoring: `(pass_count + 0.5 * partial_count) / 25 * 10` (denominator increased from 21 in v9 to 25 in v10).',
    'Aspirational scoring: `(pass_count + 0.5 * partial_count) / 29 * 10` (denominator increased from 25 in v10 to 29 in v11).'
)

# ── 7. Update Scoring Worked Example denominator reference ───────────────────
v11 = v11.replace(
    'aspirational_pass = 1/25 = 0.04 ->  0.04 * 10 =  0.40',
    'aspirational_pass = 1/29 = 0.034 ->  0.034 * 10 =  0.34'
)

# ── 8. Add v11 Change Log entry ───────────────────────────────────────────────
V11_CHANGELOG = """
---

## v11 Change Log

**New aspirational criteria (from R10 excellence signals):**

- **C-34** -- STEP 5 table-check consequence-form. Source: R10 V-01 (STEP 5 Y/N gate row), V-04
  (V-01 axis + registry closure), V-05 (full synthesis). R9 V-05 carries consequence-form at
  STEP 3B, STEP 4, STEP 6, and the VERIFICATION MANIFEST header. STEP 5 -- the structural gate
  check immediately preceding body generation -- carried a permission-form gate row only. R10 V-01
  closes this gap by adding the CF clause to the Y/N row: "an output with any vocabulary ID on a
  subline fails C-20 regardless of other compliance: Y / N". The structural guarantee: the
  pre-generation gate check itself carries the criterion-level failure declaration, not only the
  downstream generation and verification sites. V-01 passes C-34 but fails C-37 (STEP 5
  unregistered), isolating C-34 from C-37. V-04 passes both C-34 and C-37.

- **C-35** -- Vocabulary-manifest-header consequence-form. Source: R10 V-02 (VOCABULARY MANIFEST
  header extended), V-04 (V-02 axis + registry closure), V-05 (full synthesis). R9 V-05 VOCABULARY
  MANIFEST header: structural description only ("VM Row IDs appear in this manifest, the commitment
  table, and the ## headline annotation -- per Compliance Contract C-20 -- subline placement is NOT
  permitted"). R10 V-02 extends the header to carry the CF clause and explicitly names the ##
  headline as the only valid placement site. The manifest becomes dual-purpose at the
  ID-definition level: definitions and their placement obligation appear together at the moment of
  introduction. C-35 extends C-31's dual-purpose pattern (at the VERIFICATION MANIFEST) to the
  VOCABULARY MANIFEST. V-02 passes C-35 but fails C-37 (VOCABULARY MANIFEST unregistered).

- **C-36** -- Dual-case sample in compliance contract. Source: R10 V-03 (failing-form block added
  to COMPLIANCE CONTRACT sample), V-05 (full synthesis). R9 V-05 COMPLIANCE CONTRACT sample
  section: compliant form only. R10 V-03 adds a labeled failing-form counterexample explicitly
  marked as a C-20 violation with consequence-form, showing the VM Row ID on a subline and labeling
  it "VIOLATION: subline placement -- fails C-20 regardless of other compliance". The contract
  illustration becomes enforcement-demonstrative: a reader sees both the required form and the
  prohibited form at the definition site. C-36 extends C-27 (consequence-form stated in the
  contract) to the counterexample domain. V-03 passes C-36 but fails C-34, C-35, and C-37. V-05
  passes C-36 as part of full synthesis. C-36 is orthogonal to C-37: dual-case sample (phrasing
  form) and registry completeness (site enumeration) are independent axes. V-04 passes C-37 without
  C-36; V-03 passes C-36 without C-37.

- **C-37** -- Pre-generation-artifact registry coverage. Source: R10 V-04 (first STEP 5 + VOCABULARY
  MANIFEST registration in RESTATING POSITIONS), V-05 (full synthesis). Integration criterion
  requiring C-34 PASS + C-35 PASS + C-26 PASS. R10 V-01 exposes the STEP 5 gap; R10 V-02 exposes
  the VOCABULARY MANIFEST gap. R10 V-04 closes both simultaneously with a seven-entry RESTATING
  POSITIONS (VOCABULARY MANIFEST, STEP 3B, VOCABULARY PRE-FLIGHT GATE, STEP 4, STEP 5, STEP 6,
  VERIFICATION MANIFEST), all CF-carrying. The registry becomes a complete pre-generation
  enforcement map: every artifact a generator encounters before writing ticket bodies is either
  enumerated with a CF entry or carries no CF. C-37 is the C-33 analog for the expanded perimeter:
  C-33 required STEP 6 registration; C-37 additionally requires STEP 5 and VOCABULARY MANIFEST
  registration. V-04 achieves C-37 without C-36 (no dual-case sample); V-05 achieves C-36 and
  C-37 simultaneously, continuing the pattern where the phrasing-register axis is the final
  integration unlock for composite-100.

**Aspirational tier re-weighting note:** Tier expands from 25 criteria (v10) to 29 criteria (v11).
Tier still totals 10 points. Denominator 25 -> 29. Each full pass = 10/29 ~= 0.345 pts; each
PARTIAL = 10/58 ~= 0.172 pts. No formula change needed beyond denominator.

**Ceiling analysis:**
R10 V-05 achieves composite 100 under v11. V-04 (C-09-C-33 + C-34 + C-35 + C-37 PASS, fails C-36)
reaches 28/29 = composite 99.655. V-01 (C-09-C-33 + C-34 PASS, fails C-35 + C-36 + C-37) reaches
26/29 = composite 98.966. V-02 (C-09-C-33 + C-35 PASS, fails C-34 + C-36 + C-37) reaches 26/29 =
composite 98.966. V-03 (C-09-C-33 + C-36 PASS, fails C-34 + C-35 + C-37) reaches 26/29 = composite
98.966. Composite-100 under v11 requires all four new criteria simultaneously. The phrasing-register
axis (C-36, dual-case counterexample form) is again the differentiator between V-04 (99.655) and
V-05 (100.000), continuing the pattern where the phrasing-register axis is the final integration
unlock for composite-100.

---

**Summary of new criteria and their R10 sources:**

| New criterion | Signal | Source variation | Dependency | Differentiates |
|---------------|--------|-----------------|------------|----------------|
| C-34 STEP 5 table-check CF | Signal 1 | R10 V-01 (STEP 5 Y/N gate row) | Extends C-30 to structural-gate site | V-01/V-04/V-05 (pass C-34) vs V-02/V-03 (fail C-34) |
| C-35 VOCABULARY MANIFEST header CF | Signal 2 | R10 V-02 (VM header) | Extends C-31 to definition site | V-02/V-04/V-05 (pass C-35) vs V-01/V-03 (fail C-35) |
| C-36 Dual-case sample in contract | Signal 3 | R10 V-03 (failing-form block) | Extends C-27 to counterexample form | V-03/V-05 (pass C-36) vs V-01/V-02/V-04 (fail C-36) |
| C-37 Pre-generation-artifact registry coverage | Signal 4 | R10 V-04 (STEP 5 + VM registered) | Requires C-34 PASS + C-35 PASS + C-26 PASS | V-04/V-05 (pass C-37) vs V-01/V-02/V-03 (fail C-37) |
"""

v11 = v11 + V11_CHANGELOG

# ── 9. Write output ───────────────────────────────────────────────────────────
with open(DST, 'w', encoding='utf-8') as f:
    f.write(v11)

print('Done. Written', len(v11), 'chars to', DST)
checks = ['C-34', 'C-35', 'C-36', 'C-37',
          '29 | 10 |', 'denominator increased from 25 in v10 to 29 in v11',
          'v11 Change Log', '## C-34', '### C-34', '### C-37']
for c in checks:
    print(f'  {c!r:55s} -> {c in v11}')
