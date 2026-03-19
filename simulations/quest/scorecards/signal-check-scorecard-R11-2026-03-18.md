---

## Signal Quest Scorecard -- signal-check R11

**Rubric**: v11 (C-01 -- C-36; 28 aspirational) | **Formula**: `90 + (asp_pass / 28) * 10`

---

### Criterion evaluation

All variations pass C-01--C-05 (essential), C-06--C-08 (recommended), and C-09--C-27. Differences confined to three criteria:

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | What's tested |
|----|------|------|------|------|------|---------------|
| C-28 | PASS | PASS | **FAIL** | PASS | PASS | Heading encodes existence assertion vs. obligation claim |
| C-35 | **FAIL** | PASS | PASS | **FAIL** | PASS | Failure class in top-level heading vs. ENFORCEMENT STACK NOTE only |
| C-36 | PASS | **FAIL** | PASS | **FAIL** | PASS | Named reader-position vs. generic "you" in function framing |

**Key floor behavior:**
- **C-34 passes in V-01/V-04**: ENFORCEMENT STACK NOTE inline labels "(absence declaration)" etc. satisfy the looser "heading or inline label" gate; top-level headings carry no failure class so C-35 fails
- **C-33 passes in V-02/V-04**: "tells you what to do / what you lose if you do not" satisfies action-spec/loss-model; C-36 fails because "you" is unresolved
- **C-27/C-30 pass in V-03**: body text "does not exist as an active rule" and step-up disclaimer survive unchanged; C-28 fails because "SCOPE MUST BE EXPLICITLY DECLARED" is obligation, not existence assertion

---

### Score summary

| Rank | Variation | Asp pass | Composite | Fail criteria |
|------|-----------|----------|-----------|---------------|
| 1 | **V-05** | 28/28 | **100.00** | None |
| 2 | V-01 | 27/28 | **99.64** | C-35 |
| 2 | V-02 | 27/28 | **99.64** | C-36 |
| 2 | V-03 | 27/28 | **99.64** | C-28 |
| 5 | V-04 | 26/28 | **99.29** | C-35, C-36 |

---

### Isolation verification

- **C-35 independent of C-36**: V-01 passes C-36 (named roles) but fails C-35 (no failure class in heading). V-02 passes C-35 (failure class in heading) but fails C-36 (generic "you"). Each structural location independently achievable.
- **C-35 independent of C-28**: V-03 heading carries "Constraint Scope Gaps" (C-35 PASS) but "SCOPE MUST BE EXPLICITLY DECLARED" is obligation not ontological (C-28 FAIL). Same heading, two independently testable properties.
- **C-34 floor under C-35 regression**: V-01/V-04 both fail C-35 yet C-34 passes via ENFORCEMENT STACK NOTE inline labels -- the looser gate holds.
- **V-04 additive**: 26/28, not 27/28 -- no shared credit between C-35 and C-36 failures.

---

### Excellence signals from V-05

**C-35 -- heading carries three layers at once**: `Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:` embeds rule number (navigation) + failure class (diagnostic taxonomy) + enforcement assertion (obligation/existence) in a single heading. Diagnostic taxonomy recoverable without entering any nested block.

**C-36 -- role-specific consulting acts**: "the obligation tells **a committing engineer reading for what to fix**; the existence condition tells **a reviewer reading for what is already lost**" eliminates the undifferentiated "you" shared by two distinct consulting roles.

**Candidate R12 signals**: (1) ENFORCEMENT STACK NOTE inline labels partially redundant once failure classes live in top-level headings -- candidate: forward-reference pattern; (2) reader-position naming currently scoped only to Rule 3's non-substitutability block -- candidate: per-rule reader-position naming keyed to each rule's failure mode.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Failure class encoded directly in top-level rule heading (e.g., Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:) collapses two-step heading-then-ENFORCEMENT-NOTE lookup into single heading scan, making diagnostic taxonomy recoverable without entering any nested block", "Named reader-position in function framing (a committing engineer reading for what to fix / a reviewer reading for what is already lost) resolves generic you to role-specific consulting acts, making each register's entry point concrete for multi-role teams"]}
```
replaces generic "you" with two named role-decision pairs. Each register is now keyed to a specific consulting act: the obligation register is for engineers who need to take action; the existence register is for reviewers who need to assess what is already lost. Multi-role teams no longer share an undifferentiated "you" -- each role reads the rule from its own entry point.

**Candidate R12 signals flagged in V-05:**
1. **ENFORCEMENT STACK NOTE partial redundancy**: once failure classes live in top-level headings, the parenthetical labels in the ENFORCEMENT STACK NOTE ("Rule 1 (absence declaration)") partially duplicate information already visible in the heading. Candidate: forward-reference from ENFORCEMENT STACK NOTE to heading, eliminating duplication.
2. **Per-rule reader-position naming**: reader-position framing currently applies only to Rule 3's non-substitutability declaration. Candidate: each rule names its own reader position keyed to its failure mode -- e.g., "a committing engineer" for Rule 1's absence-drift failure, "a skill-reference consumer" for Rule 2's reference-ambiguity failure.

---

### Full Criterion Table

#### Essential (C-01--C-05) -- all variations: 5/5 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Four-item preflight check structure (CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE) | PASS | PASS | PASS | PASS | PASS |
| C-02 | STATUS field with three canonical states (OK / FLAG / OPEN) | PASS | PASS | PASS | PASS | PASS |
| C-03 | Advisory framing declared at output header | PASS | PASS | PASS | PASS | PASS |
| C-04 | Not-a-verdict framing in readiness summary | PASS | PASS | PASS | PASS | PASS |
| C-05 | Advisory register maintained throughout output | PASS | PASS | PASS | PASS | PASS |

#### Recommended (C-06--C-08) -- all variations: 3/3 PASS

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Readiness summary section present | PASS | PASS | PASS | PASS | PASS |
| C-07 | CROSS-ITEM PATTERNS section present | PASS | PASS | PASS | PASS | PASS |
| C-08 | MISSING SIGNAL GUIDE section present | PASS | PASS | PASS | PASS | PASS |

#### Aspirational (C-09--C-36) -- R11 axis highlighted

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|-----------|------|------|------|------|------|---------------|
| C-09 | Named STANDING RULES block present | PASS | PASS | PASS | PASS | PASS | All: "STANDING RULES" header present |
| C-10 | STANDING RULES contains Rule 1 and Rule 2 | PASS | PASS | PASS | PASS | PASS | All: Rule 1 (absence) + Rule 2 (skill format) present |
| C-11 | Readiness summary uses pilot-briefing language | PASS | PASS | PASS | PASS | PASS | "preflight check / pilot sees everything" in all |
| C-12 | Four dimensions structured with consistent labeling | PASS | PASS | PASS | PASS | PASS | CAUSAL GAP / SEQUENCE / STALENESS / COHERENCE in all |
| C-13 | MISSING SIGNAL GUIDE names each missing signal type | PASS | PASS | PASS | PASS | PASS | Named examples per gap type in all |
| C-14 | STANDING RULES block precedes all inventory and analysis | PASS | PASS | PASS | PASS | PASS | STANDING RULES before GATHER YOUR SIGNALS in all |
| C-15 | Each dimension specifies required verbatim absence phrases | PASS | PASS | PASS | PASS | PASS | "Required verbatim absence phrase" block in all four items |
| C-16 | Every constraint explicitly enumerates all output locations it governs | PASS | PASS | PASS | PASS | PASS | Rules 1, 2, 3 carry Applies-to in all |
| C-17 | Verbatim absence phrases embedded at point of use within each dimension | PASS | PASS | PASS | PASS | PASS | Phrases inline within each dimension block |
| C-18 | Advisory register carried structurally through framing vocabulary | PASS | PASS | PASS | PASS | PASS | "preflight / pilot" structural framing throughout |
| C-19 | Triple enforcement stack declared as unit with interdependency named | PASS | PASS | PASS | PASS | PASS | ENFORCEMENT STACK NOTE: "No rule substitutes for another" |
| C-20 | Location-enumeration requirement expressed as named meta-rule | PASS | PASS | PASS | PASS | PASS | Rule 3 governs all Rule declarations |
| C-21 | Each rule in enforcement stack assigned a named failure class | PASS | PASS | PASS | PASS | PASS | All: failure classes named in ENFORCEMENT STACK NOTE prose |
| C-22 | Location-enumeration meta-rule includes temporal activation gate | PASS | PASS | PASS | PASS | PASS | "at rule-creation time" present in all |
| C-23 | Meta-rule self-application declared in rule body | PASS | PASS | PASS | PASS | PASS | "This requirement self-applies: Rule 3 itself declares its scope below" |
| C-24 | Activation gate framed as rule-validity condition | PASS | PASS | PASS | PASS | PASS | "does not exist as an active rule" present in all |
| C-25 | Body self-application includes proximate scope pointer | PASS | PASS | PASS | PASS | PASS | "declares its scope below" in all |
| C-26 | Activation gate carries both obligation and validity framing | PASS | PASS | PASS | PASS | PASS | "Obligation:" and "Existence condition:" labeled sections in all |
| C-27 | Validity condition uses rule-existence framing | PASS | PASS | PASS | PASS | PASS | "does not exist as an active rule" in all |
| C-28 | Rule name encodes existence assertion (heading-level) | PASS | PASS | **FAIL** | PASS | PASS | V-03: "SCOPE MUST BE EXPLICITLY DECLARED" is obligation claim, not ontological |
| C-29 | Dual register as labeled sections with non-substitutability declaration | PASS | PASS | PASS | PASS | PASS | "Obligation:" / "Existence condition:" with non-subst. assertion in all |
| C-30 | Step-up disclaimer naming inadequacy of status framing | PASS | PASS | PASS | PASS | PASS | "'Not operative' understates the condition" in all |
| C-31 | Temporal gate expressed as "at rule-creation time" | PASS | PASS | PASS | PASS | PASS | "scope must be discharged at rule-creation time, not retroactively" in all |
| C-32 | Location annotation explicitly covers rules not yet written | PASS | PASS | PASS | PASS | PASS | "any rule added in the future" in Applies-to in all |
| C-33 | Non-substitutability assigns distinct function description (action-spec / loss-model) | PASS | PASS | PASS | PASS | PASS | V-01/V-03/V-05: auto-pass via C-36; V-02/V-04: "tells you what to do / what you lose" |
| C-34 | Each rule's heading or inline label encodes failure class | PASS | PASS | PASS | PASS | PASS | V-01/V-04: inline labels in ENFORCEMENT STACK NOTE; V-02/V-03/V-05: auto-pass via C-35 |
| **C-35** | Failure class in top-level rule heading (diagnostic-heading) | **FAIL** | PASS | PASS | **FAIL** | PASS | V-01/V-04: no failure class prefix in headings; V-02/V-03/V-05: "Rule N -- [Class] --" |
| **C-36** | Reader-position named explicitly in function framing (reader-position-framing) | PASS | **FAIL** | PASS | **FAIL** | PASS | V-02/V-04: generic "you"; V-01/V-03/V-05: "a committing engineer... / a reviewer..." |

---

### Composite scores

| Variation | Asp pass / 28 | Composite | All essential |
|-----------|---------------|-----------|---------------|
| V-01 | 27/28 | 99.64 | YES |
| V-02 | 27/28 | 99.64 | YES |
| V-03 | 27/28 | 99.64 | YES |
| V-04 | 26/28 | 99.29 | YES |
| **V-05** | **28/28** | **100.00** | YES |

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["Failure class encoded directly in top-level rule heading (e.g., Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:) collapses two-step heading-then-ENFORCEMENT-NOTE lookup into single heading scan, making diagnostic taxonomy recoverable without entering any nested block", "Named reader-position in function framing (a committing engineer reading for what to fix / a reviewer reading for what is already lost) resolves generic you to role-specific consulting acts, making each register's entry point concrete for multi-role teams"]}
```
