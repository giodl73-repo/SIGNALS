## Signal Quest Scorecard -- signal-check R10

**Rubric**: v10 (C-01 -- C-34; 26 aspirational) | **Formula**: `90 + (asp_pass / 26) * 10`

**Single variable**: Rule 3 non-substitutability declaration framing (C-33) and ENFORCEMENT STACK NOTE label structure (C-34), with C-28 as orthogonality anchor.

---

### Criterion evaluation

All variations pass C-01 -- C-05 (essential) and C-06 -- C-08 (recommended). All pass C-09 -- C-27. Differences are confined to three criteria:

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | What's tested |
|----|------|------|------|------|------|---------------|
| C-28 | PASS | PASS | **FAIL** | PASS | PASS | Heading encodes existence assertion vs. generic label |
| C-33 | **FAIL** | PASS | PASS | **FAIL** | PASS | Reader-function framing vs. activation/standing framing |
| C-34 | PASS | **FAIL** | PASS | **FAIL** | PASS | Inline failure-class labels vs. prose-sentence in ENFORCEMENT STACK NOTE |

Key floor-criterion behavior:
- **C-29 passes in V-01/V-04**: labeled sections + non-substitutability assertion are intact; C-33 fails because activation/standing framing doesn't map to reader consulting logic
- **C-21 passes in V-02/V-04**: failure classes are named in body prose; C-34 fails because the class requires body parsing rather than label scanning

---

### Score summary

| Rank | Variation | Asp pass | Composite | Fail criteria |
|------|-----------|----------|-----------|---------------|
| 1 | **V-05** | 26/26 | **100.00** | None |
| 2 | V-01 | 25/26 | **99.62** | C-33 |
| 2 | V-02 | 25/26 | **99.62** | C-34 |
| 2 | V-03 | 25/26 | **99.62** | C-28 |
| 5 | V-04 | 24/26 | **99.23** | C-33, C-34 |

---

### Isolation verification

- **C-33 independent of C-29**: V-01 has labeled sections and the non-substitutability assertion (C-29 PASS) but uses activation/standing framing -- explaining rule mechanics, not the reader's consulting act. C-33 fails alone.
- **C-34 independent of C-21**: V-02 names failure classes in ENFORCEMENT STACK NOTE prose (C-21 PASS) but the class is inside a sentence body, requiring parsing rather than label scanning. C-34 fails alone.
- **C-33 orthogonal to C-28**: V-01 passes C-28 (heading) but fails C-33 (body). V-03 fails C-28 but passes C-33. Each structural location is independently achievable.
- **V-04 additive**: two independent failures produce 24/26, not 25/26 -- no shared credit.

---

### Excellence signals from V-05

**Captured (C-33 + C-34)**: R9 V-05 already encodes both. No new language needed.

**Candidate R11 signals**:
1. **Failure class in top-level rule heading** -- e.g., `Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:`. Currently C-34 requires entering the ENFORCEMENT STACK NOTE; this would make the taxonomy recoverable from a top-level heading scan.
2. **Reader-position named in function framing** -- e.g., "a committing engineer reading for what to fix" vs. "a reviewer reading for what is already lost". Removes the ambiguity of generic "you" for multi-role teams.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Failure class encoded directly in top-level rule heading (e.g., Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:), making diagnostic taxonomy recoverable from a top-level heading scan without entering the ENFORCEMENT STACK NOTE block", "Reader-position named explicitly in reader-function framing (a committing engineer reading for what to fix vs a reviewer reading for what is already lost), making the consulting act concrete for multi-role teams"]}
```
beling | PASS | PASS | PASS | PASS | PASS | |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type | PASS | PASS | PASS | PASS | PASS | |
| C-14 | STANDING RULES block precedes all inventory and analysis | PASS | PASS | PASS | PASS | PASS | |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS | PASS | PASS | PASS | PASS | All four items carry verbatim absence phrases |
| C-16 | Every constraint explicitly enumerates all output locations | PASS | PASS | PASS | PASS | PASS | Rules 1, 2, 3 all carry Applies-to |
| C-17 | Verbatim absence phrases embedded at point of use | PASS | PASS | PASS | PASS | PASS | Phrases appear inline within each dimension block |
| C-18 | Advisory register carried structurally through framing vocabulary | PASS | PASS | PASS | PASS | PASS | "preflight" / "pilot" structural framing throughout |
| C-19 | Triple enforcement stack declared as unit with interdependency named | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT STACK NOTE: "No rule substitutes for another" |
| C-20 | Location-enumeration requirement expressed as named meta-rule | PASS | PASS | PASS | PASS | PASS | Rule 3 governs all Rule declarations |
| C-21 | Each rule in enforcement stack assigned a named failure class | PASS | PASS | PASS | PASS | PASS | V-02/V-04: failure classes in prose sentence; C-21 passes, C-34 fails |
| C-22 | Location-enumeration meta-rule includes temporal activation gate | PASS | PASS | PASS | PASS | PASS | "at rule-creation time" present in all |
| C-23 | Meta-rule self-application declared in rule body | PASS | PASS | PASS | PASS | PASS | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Activation gate framed as rule-validity condition | PASS | PASS | PASS | PASS | PASS | "does not exist as an active rule" present in all |
| C-25 | Body self-application includes proximate scope pointer | PASS | PASS | PASS | PASS | PASS | "declares its scope below" present |
| C-26 | Activation gate carries both obligation framing and validity framing | PASS | PASS | PASS | PASS | PASS | Obligation + existence registers both present in all |
| C-27 | Validity condition uses rule-existence framing | PASS | PASS | PASS | PASS | PASS | "does not exist as an active rule" in all |
| C-28 | Rule name encodes existence assertion (heading-level) | PASS | PASS | **FAIL** | PASS | PASS | V-03: "CONSTRAINTS ARE LOCATION-COMPLETE" lacks ontological claim |
| C-29 | Dual register expressed as labeled sections with non-substitutability declaration | PASS | PASS | PASS | PASS | PASS | All: "Obligation:" / "Existence condition:" labeled; non-subst. assertion present |
| C-30 | Step-up disclaimer naming inadequacy of status framing | PASS | PASS | PASS | PASS | PASS | "'Not operative' understates the condition" in all |
| C-31 | Temporal gate expressed as "at rule-creation time" | PASS | PASS | PASS | PASS | PASS | All: "scope must be discharged at rule-creation time, not retroactively" |
| C-32 | Location annotation explicitly covers rules not yet written | PASS | PASS | PASS | PASS | PASS | All: "any rule added in the future" in Applies-to |
| C-33 | Non-substitutability declaration assigns distinct function description to each register (action-spec / loss-model) | **FAIL** | PASS | PASS | **FAIL** | PASS | V-01/V-04: activation/standing framing explains rule mechanics, not reader consulting behavior; C-29 still passes |
| C-34 | Each rule's heading or inline label encodes its failure class | PASS | **FAIL** | PASS | **FAIL** | PASS | V-02/V-04: prose-sentence format requires body parsing; C-21 still passes because failure classes are named |

---

## Score summary

| Variation | C-28 | C-33 | C-34 | Asp fail | Asp pass | Composite | Rank |
|-----------|------|------|------|----------|----------|-----------|------|
| V-05 | PASS | PASS | PASS | 0 | 26/26 | **100.00** | 1 |
| V-01 | PASS | FAIL | PASS | 1 (C-33) | 25/26 | **99.62** | 2 |
| V-02 | PASS | PASS | FAIL | 1 (C-34) | 25/26 | **99.62** | 2 |
| V-03 | FAIL | PASS | PASS | 1 (C-28) | 25/26 | **99.62** | 2 |
| V-04 | PASS | FAIL | FAIL | 2 (C-33, C-34) | 24/26 | **99.23** | 5 |

---

## Criterion isolation verification

**C-33 vs C-29**: V-01 fails C-33 but passes C-29. The non-substitutability assertion ("These two registers are not substitutes") and labeled sections ("Obligation:" / "Existence condition:") satisfy C-29. C-33 requires the additional step of mapping each register to the reader's decision logic ("tells you what to do" / "tells you what you lose"). Activation/standing framing explains rule mechanics but not reader consulting behavior. Isolation confirmed: C-33 is a strict tightening of C-29.

**C-34 vs C-21**: V-02 fails C-34 but passes C-21. The prose-sentence format ("Rule 1 addresses the absence-drift failure: outputs that appear complete...") names the failure class, satisfying C-21. But the class appears inside a sentence body, requiring the reviewer to parse the sentence rather than read a label. C-34 requires the class in the label itself. Isolation confirmed: C-34 is a strict tightening of C-21.

**C-33 vs C-28**: V-03 fails C-28 (generic heading) but passes C-33 (reader-function framing in body). V-01 passes C-28 (ontological heading) but fails C-33 (body framing). C-28 tests the heading structural location; C-33 tests body-level non-substitutability text. Each is achievable without the other in either direction. Orthogonality confirmed.

**C-33 + C-34 combined (V-04)**: Both fail independently. Combined score is 24/26, not 25/26 -- confirms no shared credit or overlap between the two criteria. C-29 and C-21 still pass (floor criteria unaffected by failing their strict tightenings).

---

## Excellence signals from V-05

V-05 is R9 V-05 verbatim. The two new criteria (C-33, C-34) were already encoded in R9's ceiling output. No new language was required.

**EX-01 (captured as C-33)**: "the obligation tells you what to do; the existence condition tells you what you lose if you do not" -- reader-decision function framing that maps each register to a concrete consulting act. This is the property V-01 isolates by removing.

**EX-02 (captured as C-34)**: ENFORCEMENT STACK NOTE uses inline label format: "Rule 1 (absence declaration) -- prevents silent omissions:" with the failure class co-located in the label, not embedded in sentence prose. A reviewer scanning labels recovers the diagnostic taxonomy without entering body text. This is the property V-02 isolates by replacing with prose-sentence format.

**Candidate R11 signals** (not yet captured as criteria):

**R11-EX-01 (failure class in top-level rule heading)**: The ENFORCEMENT STACK NOTE inline labels place failure-class names one structural level below the top-level rule headings. Currently the STANDING RULES block carries: "Rule 1 -- ABSENCE MUST BE DECLARED:" / "Rule 2 -- SKILL REFERENCE FORMAT:" / "Rule 3 -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:". None encodes the failure class (absence drift / reference ambiguity / constraint scope gaps) in the top-level heading. A future output could encode both: "Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:". This would make the diagnostic taxonomy recoverable from a top-level heading scan without entering the ENFORCEMENT STACK NOTE block at all. Currently satisfying C-34 requires entering the ENFORCEMENT STACK NOTE; this candidate criterion would make C-34 satisfaction visible one structural level higher. C-34 and this candidate criterion are independently testable: C-34 tests ENFORCEMENT STACK NOTE labels; this tests top-level rule headings.

**R11-EX-02 (reader-position named in function framing)**: The C-33 framing ("tells you what to do" / "tells you what you lose") addresses a generic reader. A tighter version would name the reader's role explicitly: "a committing engineer reading for what to fix" (action-spec register) vs. "a reviewer reading for what is already lost" (loss-model register). Naming the reader's position makes the consulting act concrete and removes the ambiguity of who "you" is -- relevant for multi-role teams where the obligation is resolved by a different person than the one who bears the consequence.

---

## Rank and recommendation

| Rank | Variation | Score | Fail criteria |
|------|-----------|-------|---------------|
| 1 | V-05 | 100.00 | None |
| 2 | V-01 | 99.62 | C-33 |
| 2 | V-02 | 99.62 | C-34 |
| 2 | V-03 | 99.62 | C-28 |
| 5 | V-04 | 99.23 | C-33, C-34 |

**Top variation**: V-05 (100.00). Passes all 26 aspirational criteria. R9 ceiling carried forward intact under the v10 rubric.

**V-01, V-02, V-03 tied at 99.62**: Each isolates a single independent criterion failure. No cascading failures -- the floor criteria (C-29, C-21) all pass because the failing criteria (C-33, C-34, C-28) test strictly tighter properties at different structural locations.

**V-04 at 99.23**: Only variation scoring below 99.62. Failing two independent criteria produces additive score impact (24/26 vs 25/26 for single failures). Confirms C-33 and C-34 have no shared credit.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Failure class encoded directly in top-level rule heading (e.g., Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:), making diagnostic taxonomy recoverable from a top-level heading scan without entering the ENFORCEMENT STACK NOTE block", "Reader-position named explicitly in reader-function framing (a committing engineer reading for what to fix vs a reviewer reading for what is already lost), making the consulting act concrete for multi-role teams"]}
```
