## mock-all Round 8 Scoring — Rubric v8

**Baseline:** V-05 R7 = 100% (12/12 aspirational). All R8 variations inherit that baseline; scoring notes only deviations.

---

### Scoring Structure

| Tier | Criteria | Weight | Per-criterion |
|------|----------|--------|---------------|
| Essential | C-01 – C-05 | 60% | 12% each |
| Recommended | C-06 – C-08 | 30% | 10% each |
| Aspirational | C-09 – C-20 | 10% | 0.833% each (denom = 12) |

All variations leave C-01–C-08 unchanged from R7 → 90% floor guaranteed before aspirational scoring.

---

### V-01 — Consolidated Role-Identity Preamble

**Axis:** C-18. Per-role "You ARE" blocks removed; single preamble + role-name headers retained.

**C-18 analysis:**
- Criterion: *"each phase must assign a named role identity... the model knows it IS the CLASSIFIER, not merely in step 1"*
- V-01 keeps role-name headers at each phase boundary (e.g., `## ROLE 1: CLASSIFIER`) — satisfies "each phase must assign"
- Preamble pre-loads the identity-violation mechanism ("crossing role boundaries is an identity violation") — satisfies "make wrong-phase behavior an identity violation"
- The two components together (preamble logic + per-phase name label) reconstitute what R7 achieved with per-role repetition
- Per-role repetition was redundant amplification, not the load-bearing element
- **Verdict: PASS**

| Criterion | V-01 | Note |
|-----------|------|------|
| C-09 | PASS | Unchanged |
| C-10 | PASS | Unchanged |
| C-11 | PASS | Unchanged |
| C-12 | PASS | Unchanged |
| C-13 | PASS | Unchanged |
| C-14 | PASS | Unchanged |
| C-15 | PASS | Unchanged |
| C-16 | PASS | Unchanged |
| C-17 | PASS | Unchanged |
| **C-18** | **PASS** | Preamble + role-name labels = minimum sufficient form |
| C-19 | PASS | Unchanged |
| C-20 | PASS | Unchanged |

**Aspirational:** 12/12 → 10%
**Total: 100%**

**Finding:** Per-role "You ARE" repetition is load-bearing only if the identity-violation mechanism is absent elsewhere. Preamble + label is a valid minimal form.

---

### V-02 — Inertia Gap Skeleton as 8th Classification Column

**Axis:** C-20 implementation depth. ROLE 1 table gains column "Inertia gap skeleton: Without this signal, {topic}'s story would be missing: ___"; ROLE 2 fills the blank before writing artifact body.

**C-20 analysis:**
- Criterion already passes in R7 (inertia question + ROLE 3 derivation bridge)
- V-02 doesn't change pass/fail; it changes *when* the inertia answer is constrained
- Pre-seeding in ROLE 1 forces the model to articulate the epistemic cost at classification time (namespace-level), before topic is applied in ROLE 2
- Result: ROLE 2 answers are namespace-pre-seeded, not free-form; topic specificity is additive rather than originating
- **Verdict: PASS (quality uplift, not criterion change)**

**C-11 check:** Classification table still appears before any artifact body ✓
**C-17 check:** Vocabulary columns unchanged; 8th column is additive ✓

| Criterion | V-02 | Note |
|-----------|------|------|
| C-09 – C-17 | PASS | Unchanged |
| C-18 | PASS | Unchanged |
| C-19 | PASS | Unchanged |
| **C-20** | **PASS+** | Same pass, measurably deeper inertia answers |

**Aspirational:** 12/12 → 10%
**Total: 100%**

**Finding:** Inertia skeleton in classification table is the strongest structural innovation in R8 — namespace epistemic cost is anchored before topic is applied. Candidate v9 criterion.

---

### V-03 — Prohibition-Forward Role Framing

**Axis:** C-18. "You ARE the CLASSIFIER" replaced with "CLASSIFIER: generate X only. Generating Y is prohibited."

**C-18 analysis:**
- Criterion: *"the model knows it IS the CLASSIFIER, not merely in step 1"*
- Prohibition-forward form names the role (CLASSIFIER) and identifies forbidden behaviors ✓
- But the rubric's test is specifically about *identity* violation, not *behavioral* prohibition
- "Generating Y is prohibited" = rule violation; "You ARE CLASSIFIER, so generating Y makes you NOT the CLASSIFIER" = identity violation
- The distinction is ontological: prohibition says the behavior is forbidden; identity says the behavior is self-contradictory
- The rubric explicitly separates these: "the model knows it *IS*... not merely *in step 1*" — prohibition-forward is closer to "here are step rules" than "here is who you are"
- **Verdict: PARTIAL** — role name present, wrong-phase behaviors named, but violation is behavioral not ontological

| Criterion | V-03 | Note |
|-----------|------|------|
| C-09 – C-17 | PASS | Unchanged |
| **C-18** | **PARTIAL** | Role name present; violation framing is behavioral, not identity |
| C-19 | PASS | Unchanged |
| C-20 | PASS | Unchanged |

**Aspirational:** 11.5/12 → 9.58%
**Total: 90% + 9.58% = 99.58% ≈ 99%**

**Finding:** C-18 requires ontological identity framing, not merely behavioral prohibition. "You ARE X" and "X: do only Y" are not equivalent for this criterion.

---

### V-04 — Checkbox Stop-Gate Lists

**Axis:** C-14, C-16. All prose stop-gate phrases converted to markdown checkbox lists (one checkbox per required field).

**C-14 analysis:**
- "explicit stop-gate phrase at each phase boundary" — checkboxes are explicit by construction ✓
- **Verdict: PASS**

**C-16 analysis:**
- "must name the specific fields or rows the model must have produced" — one checkbox per field is maximal enumeration clarity
- Checkbox format makes partial completion immediately visible (unchecked boxes remain)
- **Verdict: PASS (stronger implementation than prose)**

| Criterion | V-04 | Note |
|-----------|------|------|
| C-09 – C-13 | PASS | Unchanged |
| **C-14** | **PASS** | Checkboxes = explicit gate per field |
| C-15 | PASS | Unchanged |
| **C-16** | **PASS** | Checkbox-per-field exceeds prose enumeration in specificity |
| C-17 – C-20 | PASS | Unchanged |

**Aspirational:** 12/12 → 10%
**Total: 100%**

**Finding:** Checkbox format is an equally valid (and arguably superior) C-16 implementation — partial completion is structurally visible rather than semantically hidden in prose.

---

### V-05 — Combination (V-01 + V-02 + V-04)

**Axis:** Structural robustness. Preamble consolidation + inertia skeleton table + checkbox gates simultaneously.

- V-01 contribution: C-18 PASS with preamble + labels (confirmed above)
- V-02 contribution: C-20 quality uplift, no criterion risk
- V-04 contribution: C-14/C-16 PASS, checkbox clarity

No new C-18 risk introduced beyond V-01. No criterion interactions create failures.

| Criterion | V-05 | Note |
|-----------|------|------|
| C-09 – C-17 | PASS | Unchanged + V-04 checkbox strengthens C-16 |
| **C-18** | **PASS** | Inherits V-01 preamble + labels |
| C-19 | PASS | Unchanged |
| **C-20** | **PASS+** | Inherits V-02 inertia skeleton depth |

**Aspirational:** 12/12 → 10%
**Total: 100%**

---

### Rankings

| Rank | Variation | Score | Distinguisher |
|------|-----------|-------|---------------|
| 1 (tie) | V-02 | 100% | Strongest qualitative advance: inertia skeleton table column |
| 1 (tie) | V-04 | 100% | Checkbox gates — cleaner C-16 implementation |
| 1 (tie) | V-05 | 100% | Best overall structure: combines all valid advances |
| 1 (tie) | V-01 | 100% | Confirms preamble minimality for C-18 |
| 5 | V-03 | 99% | C-18 PARTIAL — prohibition-forward is not ontological identity |

---

### Excellence Signals

**Signal 1 — Inertia skeleton pre-seeded in classification table (V-02)**
The inertia gap column in ROLE 1 forces namespace-level epistemic cost articulation before topic is applied. When ROLE 2 fills in the skeleton, the answer is constrained to the namespace's function — the topic adds specificity to a pre-formed structure rather than generating from scratch. This produces artifact bodies traceable to the inertia answer at a structural level, not just a semantic one. **v9 candidate criterion:** "Inertia gap column in ROLE 1 classification table pre-seeds namespace-level epistemic cost; ROLE 2 answer must extend the skeleton, not originate it."

**Signal 2 — Confirmed minimality of C-18 (V-01)**
Preamble + role-name labels is the minimum sufficient form for C-18. Per-role "You ARE" repetition (R7) was redundant amplification. This matters for skill compression: identity enforcement can be centralized without criterion loss, freeing per-role blocks for content-specific vocabulary and stop-gate instructions.

**Non-signal — V-03 prohibition-forward framing**
This is not an alternative valid C-18 implementation. The criterion's ontological test ("knows it IS") is not satisfied by behavioral prohibition alone. The distinction is load-bearing: identity violation is self-contradictory; behavioral prohibition is merely forbidden. Skills that adopt prohibition-forward framing for conciseness accept a C-18 PARTIAL.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia gap skeleton pre-seeded as ROLE 1 classification table column anchors ROLE 2 answer specificity to namespace epistemic function before topic is applied", "consolidated role-identity preamble with per-phase role-name labels is minimum sufficient form for C-18 — per-role You-ARE repetition is redundant amplification not load-bearing mechanism"]}
```
