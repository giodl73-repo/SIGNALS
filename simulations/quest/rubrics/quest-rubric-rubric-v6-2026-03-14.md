`simulations/quest/rubrics/quest-rubric-rubric-v6-2026-03-14.md` written.

**Three patterns extracted, three criteria added. Two self-application edits made:**

**C-23** (c15-calibration-must-be-in-dr-block) — No edit to existing criteria needed. Self-applies as PASS: v6's Notes section already contains both the C-04 self-application slot (criterion ID + poor-output description) and the rejection log G-01/G-02/G-03 in the same section.

**C-24** (output-contract-completeness-gate-confirmed) — Self-application required adding the **Required Sections block** before the Essential Criteria table. A retroactive checklist achieves only what it names; the front-loaded section manifest achieves completeness at declaration time. v6 now has this block; C-24 self-applies as PASS.

**C-25** (role-identity-explicit-equivalence-language) — Self-application required adding a **C-25 N/A scope** note. This rubric has no role definition — the equivalence phrases are already embedded directly in C-11 and C-14 pass conditions. C-25 is excluded from the denominator for rubric documents that use this approach.

**v7 candidates** replaces v6 candidates: the promoted pattern (output-contract-completeness-gate → C-24) is removed; three surviving v6 candidates carry forward; two new patterns join from R5 (output-ordering-determines-c11-c14, v04-token-budget-reliability-gap).
S because it is the only one to use the phrase in its role definition |

Also updated:
- **Required Sections block** added before Essential Criteria table — C-24 self-application
- **C-25 N/A scope** added to Notes — C-25 self-application
- **Self-scoring projection** updated for C-23, C-24, C-25
- **v7 candidates** section updated

**Self-scoring projection (v6 against itself):**
- C-17: N/A (this rubric has no amend or revision phase; excluded from denominator)
- C-18: PASS (Notes section contains explicit enumerated banned-qualifier list of 8 terms)
- C-19: PASS (C-15 pass condition states output-state gate only; names no required construction mechanism)
- C-20: PASS (Required Sections block names Scoring section; Scoring section present in document)
- C-21: PASS (C-11 pass condition includes "or equivalent block (failure inventory, notes section)" language)
- C-22: PASS (C-13 pass condition explicitly states "construction-time filter activity alone does not satisfy this criterion")
- C-23: PASS (Notes section contains both: (1) C-15 self-application slot — "A poor output of this rubric would fail C-04" — criterion ID C-04 plus poor-output description; AND (2) rejection log G-01/G-02/G-03 — named rejected generic criteria; both items present in the same Notes section)
- C-24: PASS (Required Sections block now appears before Essential Criteria table; all required sections named before the first criteria table)
- C-25: N/A (this rubric has no role definition; equivalence phrases are embedded directly in C-11 and C-14 pass conditions; excluded from denominator per N/A scope note)

---

## Required Sections

All sections must appear in this order. Omitting any named section makes the rubric structurally incomplete.

| # | Section | Required Content |
|---|---------|-----------------|
| 1 | What Changed | version delta, new criterion IDs and signals, self-application edits made, self-scoring projection |
| 2 | Required Sections | ordered list of all sections with required content per section |
| 3 | Essential Criteria | 3-5 essential criteria; all five fields (ID, Text, Weight, Category, Pass Condition) populated |
| 4 | Recommended Criteria | 2-3 recommended criteria; all five fields populated |
| 5 | Aspirational Criteria | aspirational criteria; all five fields populated |
| 6 | Scoring | composite formula with band weights, golden threshold with all-essential-pass precondition, PARTIAL handling, N/A handling |
| 7 | Notes | C-15 self-application slot (criterion ID + poor output), C-18 banned-qualifier list, C-16/C-17/C-25 N/A scope, rejection log (named rejected generic criteria) |
| 8 | vN Candidates | patterns approaching but not yet promoted; each candidate names the pattern and the evidence needed to cross threshold |

---

## Essential Criteria

These must all pass. A rubric that fails any essential criterion is not usable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **All five required fields are present** — Each criterion row contains: ID, Text, Weight, Category, and Pass Condition. No field is left blank or missing. | essential | format | Every row in every criteria table contains all five fields with no field left blank or missing. |
| C-02 | **Weight distribution is within spec** — The rubric contains 3-5 essential criteria, 2-3 recommended criteria, and 1-2 aspirational criteria. | essential | correctness | Count of essential in [3,5]; count of recommended in [2,3]; count of aspirational in [1,2]. |
| C-03 | **Composite score formula and golden threshold are stated correctly** — The rubric declares the composite formula (60/30/10 split) and the golden threshold (all essential pass + composite >= 80). | essential | correctness | Formula present with weights 60, 30, 10 for essential/recommended/aspirational bands; threshold stated as >= 80 with the all-essential-pass precondition. |
| C-04 | **Criteria are skill-specific** — Essential criteria test the actual non-negotiable behaviors of the target skill, not generic document quality (no criteria like "is well-written" or "is complete"). | essential | correctness | At least 3 of the essential criteria name specific behaviors, outputs, or structural properties unique to the target skill; none are purely generic quality signals. |
| C-05 | **Pass conditions are binary and testable** — Every pass condition can be evaluated as pass/fail without subjective judgment; each uses observable signals (counts, presence/absence, specific patterns, measurable thresholds). | essential | behavior | All pass conditions use verifiable criteria; none require subjective assessment ("good", "sufficient", "appropriate" without a measurable anchor). |

---

## Recommended Criteria

These improve rubric usability. A rubric without them is acceptable but weaker.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Criteria ordered by weight tier** — Essential criteria appear before recommended, recommended before aspirational. Each tier is clearly separated and labeled. | recommended | format | Sections appear in order: essential -> recommended -> aspirational, with distinct headers or table sections per tier. |
| C-07 | **Categories drawn from the allowed set** — Every criterion category is one of the five canonical values: correctness, depth, format, coverage, behavior. No invented categories. | recommended | correctness | All category fields contain only: correctness, depth, format, coverage, or behavior; no other values. |
| C-08 | **Essential criteria cover distinct failure modes** — No two essential criteria test the same behavior; together they catch at least four distinct ways an output can fail to be useful. | recommended | coverage | No two essential criteria have overlapping pass conditions; reviewers can identify at least four distinct failure modes caught by the essential set. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Rubric is calibrated** — A reviewer using this rubric can correctly classify a mediocre output (scores < 80) and an excellent output (scores >= 80) without ambiguity. At least one essential criterion would catch a real failure in a poor output. | aspirational | depth | Reviewer can produce a concrete example of a poor output that fails >= 1 essential criterion, and a strong output that passes all essential and >= 2 recommended criteria. |
| C-10 | **Evolution hook present** — The rubric acknowledges it should grow as quest-golden discovers excellence patterns; frontmatter includes a version field and the document includes a note about how the rubric should be updated over time. | aspirational | behavior | Frontmatter has version field populated; OR document contains a section/note describing how the rubric should evolve as golden outputs are discovered. |
| C-11 | **Inertia framing in design rationale** — The rubric design rationale names the dominant failure mode for the target skill before listing any criteria. Naming the enemy first anchors every subsequent review decision as a persistent filter rather than a per-criterion afterthought. | aspirational | depth | Design rationale (or equivalent block: failure inventory, notes section, or named dominant-failure-mode statement) contains an explicit statement of the most common or most dangerous failure mode for the target skill; this block appears before the first criteria table; a prompt instruction that does not produce this block in the output does not satisfy this gate. |
| C-12 | **Pass conditions use closed-world gates** — Each pass condition is phrased as a binary gate with explicit unacceptable-signal anchors. Subjective terms ("good", "sufficient", "appropriate", "thorough", "complete") do not appear in pass conditions without a measurable anchor alongside them. | aspirational | behavior | No pass condition contains a bare subjective qualifier without a count, threshold, or presence/absence anchor; OR the rubric explicitly lists banned subjective terms and at least 3 pass conditions demonstrate the pattern ("X is present" / "count >= N" / "none of Y"). |
| C-13 | **Rejection log proves the specificity filter ran** — The design rationale or notes section names at least one generic criterion that was considered and rejected, with the rejection stated explicitly. Proving the filter ran is stronger than asserting the intent to run it. Construction-time filter activity alone does not satisfy this criterion; the deletion evidence must appear as a named section in the output document. | aspirational | depth | Design rationale or notes section in the output document contains at least one named example of a rejected generic criterion (e.g., "output is well-structured", "is clear and complete") stated as explicitly rejected, not merely implied; a prompt that ran a filter during construction but produced no named rejection log section in the output fails this criterion. |
| C-14 | **Design rationale precedes criteria tables** — The design rationale section (or equivalent intent block) appears in the output document before the first criteria table. Position is not cosmetic: when inertia framing and failure-mode enumeration are written before the criteria exist, they constrain construction rather than rationalizing it after the fact. V-04 and V-05 had identical content; only V-05 satisfied the positional gate. | aspirational | format | Design rationale section (or equivalent block describing dominant failure mode, rejected criteria, or construction intent) appears before the first Essential criteria table in the document; no criteria table appears above the design rationale text. |
| C-15 | **Self-application and rejection log co-present in design rationale** — The design rationale contains both (1) a self-application result naming at least one essential criterion ID that a concrete poor output would fail, and (2) at least one named rejected generic criterion. Both slots are populated in the same section with zero mutual interference. V-05 was the only R2 variation to achieve both simultaneously; R3 showed that auditor-calibration, interrogative-question, and self-application-gate routes all satisfy the pass condition — the gate is mechanism-agnostic. | aspirational | depth | Design rationale section contains: (1) at least one essential criterion ID cited as the failure point for a described poor output, AND (2) at least one explicitly rejected generic criterion named by its text; both items present in the same design rationale section, not distributed to separate appendices or notes. |
| C-16 | **Amend step covers all three primary criterion failure modes as distinct gates** — The rubric prompt's amend or revision step addresses all three primary ways a criterion can fail: (1) the criterion text is generic rather than skill-specific, (2) the pass condition is not binary and testable, (3) the criterion duplicates a failure mode already caught by another criterion. Each failure mode is a distinct explicit question, not bundled into freeform editorial guidance. | aspirational | behavior | Amend or revision checklist contains three distinct questions explicitly addressing: (1) generic-vs-specific content, (2) binary-pass-condition testability, (3) redundant-failure-mode overlap; all three present and distinct; none merged into a single open-ended revision prompt. N/A if the skill design includes no revision phase. |
| C-17 | **Amend-step gates use structural subheader labels, not inline prose numbering** — When an amend or revision step presents multiple named gates, each gate must appear as a distinct structural subheader label (e.g., "Gate 1:", "Gate 2:", "Gate 3:") rather than as inline numbered prose within a paragraph. The label format makes each gate independently addressable and scannable; prose numbering conflates the gate identity with the instruction text and prevents gate-level pass/fail assessment. R3 finding: variations that embedded gate numbers in prose paragraphs scored PARTIAL on C-16; variations with structural labels scored PASS. | aspirational | format | Amend or revision step contains >= 3 gate labels as structural subheaders or clearly delineated labeled blocks (e.g., bold header, colon-terminated label on its own line); inline numbered list items within a prose paragraph do not satisfy this criterion. N/A if the skill design includes no revision phase. |
| C-18 | **Banned-qualifier list is explicit and enumerated, not instructional** — The rubric prompt names the disallowed subjective terms explicitly by listing them as a closed vocabulary (e.g., "good / sufficient / appropriate / clear / complete / thorough") rather than only instructing reviewers to "avoid subjective language." An explicit enumerated list is a closed gate; a general instruction is an open filter that each reviewer re-interprets independently. R3 finding: V-04 (8 banned terms) and V-05 (6 banned terms) triggered the C-12 OR path and scored PASS; V-01, V-02, V-03 used the instruction-only approach and scored PARTIAL on C-12. | aspirational | behavior | Rubric prompt or construction section contains an explicit enumerated list of >= 4 banned subjective qualifier terms named individually; the list appears in the construction or design rationale section (not only embedded in a single pass condition); N/A if the skill produces no textual criteria with pass conditions. |
| C-19 | **Co-presence pass conditions are mechanism-agnostic output-state gates** — Pass conditions that require two items to co-exist in the same section specify only the output state — both items present in the named section — without naming a required construction mechanism or authoring route. Over-specifying the mechanism rejects valid outputs that achieve the same state through a different path. R3 finding: auditor-calibration route, interrogative-question route, and self-application-gate route all satisfied C-15's literal pass condition because C-15 tests output state only. | aspirational | behavior | Each co-presence requirement in the rubric (any pass condition requiring two distinct items in the same section) is stated as an output-state check (both X and Y appear in section Z) without naming a required construction route; OR the rubric contains a note confirming that multiple construction routes satisfy each co-presence gate. PASS if all co-presence pass conditions are mechanism-agnostic; PARTIAL if >= 1 co-presence condition names a required mechanism. |
| C-20 | **Output contract explicitly names Scoring section as required element** — The rubric prompt's output contract names a Scoring section containing formula, threshold, calibration examples, and evolution hook as a required output element. Omitting this from the output contract predicts joint failure on C-03, C-09, and C-10 simultaneously; no content-level refinement compensates for this structural omission. R4 finding: all three R4 variations omitted the Scoring section from their output contracts, producing a C-03/C-09/C-10 joint failure regardless of criteria quality. | aspirational | correctness | Rubric prompt output contract explicitly names a Scoring section (or equivalent notes/calibration block covering formula + threshold + calibration + evolution hook) as a required output element; absence of this element from the output contract is flagged as a structural gap that predicts joint C-03/C-09/C-10 failure. |
| C-21 | **C-11 and C-14 pass conditions name the failure-inventory route as an equivalent block** — C-11 and C-14 pass conditions include explicit "or equivalent block" language naming a failure inventory as an acceptable substitute for a formally-labeled Design Rationale section. Absent this language, rubrics built with a Failure Analyst skeleton receive PARTIAL on C-11 due to literal-label enforcement rather than output-state assessment. R4 finding: V-01's failure-analyst route correctly satisfied C-11 and C-14 via the "or equivalent block" language already present in C-14; C-11 lacked this language in v4 and required judgment rather than a clear gate. | aspirational | correctness | C-11 pass condition contains "or equivalent block," "or notes section," or "or failure-inventory" language explicitly naming a non-Design-Rationale route as satisfying; C-14 pass condition contains equivalent language; scoring a Failure Analyst phase output against these pass conditions produces PASS on both C-11 and C-14, not PARTIAL. |
| C-22 | **C-13 pass condition names construction-time filter activity as insufficient** — C-13 pass condition explicitly states that running a deletion filter during construction does not satisfy the criterion; the deletion evidence must appear as a named section in the final output document. Without this explicit disqualification, variations that run a thorough filter but omit an output slot receive PARTIAL rather than FAIL, understating the gap. R4 finding: V-03's Generic Rubric Filter deleted generic criteria with named reasons during Phase 1 but scored only PARTIAL on C-13 because the output slot was absent. | aspirational | correctness | C-13 pass condition contains an explicit statement that construction-time filter activity alone does not satisfy the criterion; the pass condition names a required output-document slot (named rejection log section or equivalent) as the gate; a rubric variation that runs a filter but produces no named rejection log section scores FAIL, not PARTIAL. |
| C-23 | **Self-application gate must be co-located with rejected criterion in DR section, not distributed to Scoring** — The design rationale or equivalent block must contain both C-15 slots in the same section: (1) criterion ID + description of a poor output that fails it, AND (2) at least one named rejected generic criterion. When the calibration example lands only in the Scoring section, it cannot constrain the criteria-building phase and C-15 fails regardless of content quality. R5 finding: all five R5 variations placed the calibration example only in Scoring; zero achieved C-15 PASS; the path is explicit co-location of both slots in the DR or Failure Inventory phase instruction. | aspirational | depth | Design rationale section (or equivalent block: failure inventory, notes section) contains both (1) at least one essential criterion ID cited as the failure point for a described poor output AND (2) at least one named rejected generic criterion; both items present in the same section; placing the criterion-ID + poor-output statement only in a Scoring or calibration section does not satisfy this gate. |
| C-24 | **Front-loaded output contract achieves section completeness; retroactive checklist achieves only what it names** — A rubric prompt that declares all required output sections as a named contract before the first phase instruction achieves section compliance across all sections simultaneously. A prompt that uses only a retroactive Phase 4 checklist achieves compliance only for sections it explicitly names; any omitted section produces a structural gap that no content-level refinement compensates for. R5 finding: V-01's three-item checklist (Failure Inventory, Rubric Table, Scoring) produced C-13 FAIL because Rejection Log was never added; V-02's five-section front-loaded contract achieved C-13/C-20/C-22 in a single structural decision. | aspirational | format | Rubric document contains a Required Sections block (or equivalent named preamble) enumerating all output sections before the first criteria table; OR the rubric prompt that generated this document declares all required sections in a front-loaded contract appearing before any phase instruction; a document with no section manifest and a retroactive checklist with fewer sections than the actual output does not satisfy this criterion. |
| C-25 | **Explicit equivalence phrase in role definition is the mechanism for non-canonical route PASS** — When a rubric prompt's pass condition permits a non-canonical route via "or equivalent block" language, the rubric prompt's role definition must contain that exact phrase. Structural equivalence — building the same output structure without using the exact phrase — registers PARTIAL rather than PASS, because the evaluator cannot confirm equivalence was intentional. R5 finding: V-05 is the only variation to achieve C-21 PASS; it is the only variation whose role definition contains "or equivalent block" and names the failure inventory explicitly; V-01 achieved structural equivalence without the phrase and scored PARTIAL. | aspirational | correctness | For each pass condition in this rubric that permits a non-canonical route via "or equivalent block" language, the rubric prompt or role definition that produced this rubric contains that exact phrase; a rubric produced by a prompt that achieves structural equivalence without the phrase scores PARTIAL on criteria gated by that language, not PASS; N/A if the rubric has no role definition (phrase equivalence is already embedded in the pass conditions directly). |

---

## Scoring

**Composite formula**:
(essential_pass_count / essential_total) x 60
+ (recommended_pass_count / recommended_total) x 30
+ (aspirational_pass_count / aspirational_total) x 10

**Golden threshold**: all essential criteria pass AND composite score >= 80.

PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not
satisfy the all-essential-pass precondition.

**N/A handling**: Structurally inapplicable criteria (e.g., C-16, C-17 for skills with no
revision phase; C-25 for rubric documents with no role definition) are excluded from both
numerator and denominator of their band.

---

## Notes

**C-15 self-application slot**: A poor output of this rubric would fail C-04 — its criteria
would be generic quality signals ("is clear", "is complete") rather than skill-specific
behavior gates. A strong output passes all five essential criteria and at least C-06 and C-08
from the recommended set.

**C-18 banned-qualifier list**: good / sufficient / appropriate / clear / complete / thorough /
comprehensive / adequate. These terms are banned from pass conditions without a measurable
anchor (count, threshold, presence/absence signal) alongside them.

**C-16/C-17 N/A scope**: Both criteria apply only to rubric prompts that include an amend or
revision phase. A rubric that omits a revision phase is not penalized; both criteria are
excluded from the denominator for that rubric.

**C-25 N/A scope**: Applies to rubric prompts with a role definition component. Rubric
documents that embed equivalence language directly in pass conditions rather than in a
separate role definition are excluded from the C-25 denominator.

**Rejection log** (complete, versioned):
- G-01: "Criteria are clearly written" — circular
- G-02: "Rubric is comprehensive" — no observable signal
- G-03: "Criteria are high quality" — tautological

**Version**: 6. Grows as /quest:golden discovers excellence patterns.

---

## v7 Candidates

Patterns approaching threshold but not yet promoted:

- **joint-failure-chain-annotation**: when C-03, C-09, and C-10 fail simultaneously, the
  scorecard commentary should annotate this as a single joint-failure chain with one root cause
  (missing Scoring section in output contract); per-criterion FAIL notes that do not cross-
  reference the chain leave the structural root cause invisible to the rubric author.
- **failure-analyst-skeleton-as-canonical-path**: V-01's failure-analyst route (Phase 1 failure
  inventory + Phase 2 derivation notes + Phase 3 rubric table + Scoring section) is the
  structural winner across R3-R5; a criterion naming this skeleton as the canonical path to
  Golden would give rubric authors a concrete target structure.
- **output-ordering-determines-c11-c14**: V-03 demonstrates that the output-ordering instruction
  alone — independent of phase framing quality — determines C-11/C-14 compliance; strong phase
  framing cannot compensate for an ordering that places the Rubric Table before any pre-criteria
  section; currently captured by C-14's pass condition but not surfaced as a root-cause
  diagnostic in the scorecard.
- **rejection-log-minimum-count-scales-with-aspirational-depth**: rubrics with >= 8 aspirational
  criteria may need >= 5 rejection log entries to demonstrate the specificity filter ran at
  sufficient depth; observed in v6 (3 entries, 15 aspirational criteria) but no variation test yet.
- **co-presence-section-scope-precision**: C-19 mechanism-agnostic finding may generalize to a
  requirement that co-presence gates name the exact section (not "anywhere in the document") to
  prevent diffuse co-presence that satisfies the letter but not the spirit of the gate.
- **v04-token-budget-reliability-gap**: V-04 achieves structural inclusion of Scoring but scores
  C-03 PARTIAL because the falsifiability check predicts Scoring presence varies across runs
  due to token budget consumption by dense Generic Rubric test applications; a criterion testing
  output reliability (not just output presence) would surface this class of structural fragility.
