## trace-contract R8 Scorecard

### Scoring Method

Trace artifact is placeholder → scoring is design-level: each variation is evaluated against what its axis description, structural innovations, and R7 carry-forward logically produce.

**Floor assumptions** (established through R1–R6, carried by all R8 variants):
- C-01–C-08: PASS (90 pts)
- C-09–C-12: PASS (pattern recognition, amendment suggestion, structural templates, phase-gate)
- C-15, C-17, C-18, C-19, C-20, C-21: PASS (R3–R6 established criteria)

**R7 platinum** (C-13, C-14, C-16, C-22) carried only by variations that explicitly require those mechanisms. V-05 is the only variation that declares full platinum carry-forward.

**Gate-token note:** R7 V-01 and V-02 both failed C-13 (tokens present but not cleanly positioned as stand-alone bracket tokens). R8 V-01, V-04, and V-05 explicitly rework the gate mechanism → C-13 PASS. V-02 and V-03 do not target the gate → C-13 FAIL.

---

### Per-Variation Evaluation

#### V-01 — C-23 isolation (gate structured-metadata manifest)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Role assignment and boundary statement present from prior rounds |
| C-02 | PASS | Coverage obligation explicit |
| C-03 | PASS | One-finding-per-deviation enforced |
| C-04 | PASS | Spec-anchored expected output |
| C-05 | PASS | Symptom-restatement disqualifier present |
| C-06 | PASS | Connectors lens applied |
| C-07 | PASS | Summary verdict with severity counts |
| C-08 | PASS | Zero-finding affirmation |
| C-09 | PASS | Amendment suggestions on breaking findings |
| C-10 | PASS | Pattern grouping present |
| C-11 | PASS | Tabular/block format with labeled fields |
| C-12 | PASS | Phase-gate prose confirmation |
| C-13 | PASS | Gate token upgraded → bracket token correctly positioned as stand-alone |
| C-14 | FAIL | Not targeted; per-finding connector-impact slot absent |
| C-15 | PASS | `recommended-action` slot in breaking template established R3+ |
| C-16 | FAIL | Severity-stratified templates not targeted |
| C-17 | PASS | Rationale line in resolution slot established R3+ |
| C-18 | PASS | Clause-precise spec refs established R4+ |
| C-19 | PASS | Behavioral protocol block before Phase 1 established R5+ |
| C-20 | PASS | Patterns embedded in Phase 5 summary established R5+ |
| C-21 | PASS | Named phase-role headings established R6+ |
| C-22 | FAIL | "Without structural overhead" framing suggests no full skeleton pre-declaration |
| C-23 | PASS | `[EXPECTED-SEALED \| clauses:N \| date:YYYY-MM-DD \| author:contract-expert \| phase:1-complete]` with echoed `gate-clauses` in closure token |
| C-24 | FAIL | Not targeted |
| C-25 | FAIL | Not targeted |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 12/17
**Total: 102/107**

---

#### V-02 — C-24 isolation (multi-branch Patterns handling)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Established floor |
| C-09 | PASS | Established |
| C-10 | PASS | Established (C-24 extends, not replaces) |
| C-11 | PASS | Established |
| C-12 | PASS | Established |
| C-13 | FAIL | Variation does not rework gate token; R7 positioning issue not resolved |
| C-14 | FAIL | Not targeted |
| C-15 | PASS | Established |
| C-16 | FAIL | Not targeted |
| C-17 | PASS | Established |
| C-18 | PASS | Established |
| C-19 | PASS | Established |
| C-20 | PASS | Established |
| C-21 | PASS | Established |
| C-22 | FAIL | Not targeted; no skeleton declaration |
| C-23 | FAIL | Gate token not upgraded |
| C-24 | PASS | Three named branches: zero (affirmative statement), singleton (per-finding attribution), multi (grouped-by-root-cause sections) |
| C-25 | FAIL | Not targeted |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 11/17
**Total: 101/107**

---

#### V-03 — C-25 isolation (hypothesis self-test rule)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Established floor |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established |
| C-13 | FAIL | Gate not reworked; R7 positioning issue persists |
| C-14 | FAIL | Not targeted |
| C-15 | PASS | Established |
| C-16 | FAIL | Not targeted |
| C-17 | PASS | Established |
| C-18 | PASS | Established |
| C-19 | PASS | Established |
| C-20 | PASS | Established |
| C-21 | PASS | Established |
| C-22 | FAIL | Not targeted |
| C-23 | FAIL | Not targeted |
| C-24 | FAIL | Not targeted |
| C-25 | PASS | `hypothesis-draft:` → `self-test: (can this be written without knowing the system?)` → `mechanism:` triple slot with binary YES/NO gate before mechanism field is accepted |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 11/17
**Total: 101/107**

---

#### V-04 — C-23 × C-24 (gate manifest + Patterns branches in artifact skeleton)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Established floor |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established |
| C-13 | PASS | Skeleton pre-declares gate token format with structured fields → correctly positioned bracket token |
| C-14 | FAIL | Per-finding connector-impact slot not declared in skeleton; not targeted |
| C-15 | PASS | Established |
| C-16 | FAIL | Severity-stratified templates not declared; not targeted |
| C-17 | PASS | Established |
| C-18 | PASS | Established |
| C-19 | PASS | Established |
| C-20 | PASS | Established |
| C-21 | PASS | Established |
| C-22 | PASS | Skeleton pre-declared before Phase 1 with all section headers and template slots in final position — the pre-declaration of gate token + Patterns template is done via a full skeleton |
| C-23 | PASS | Gate manifest with `clauses:N` and identity fields embedded in skeleton |
| C-24 | PASS | Three-branch Patterns block pre-declared in skeleton: `ZERO-PATTERNS:`, `SINGLETON:`, `MULTI-PATTERN:` with distinct pass conditions per branch |
| C-25 | FAIL | Not targeted |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 14/17
**Total: 104/107**

---

#### V-05 — Full R8 ceiling (C-23/24/25 + R7 platinum C-13/14/16/22)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 | PASS | Established floor |
| C-09 | PASS | Established |
| C-10 | PASS | Established |
| C-11 | PASS | Established |
| C-12 | PASS | Established |
| C-13 | PASS | R7 platinum; bracket token correctly positioned |
| C-14 | PASS | R7 platinum; `connector-impact:` slot on every finding tier in stratified templates |
| C-15 | PASS | Established; `recommended-action` slot present |
| C-16 | PASS | R7 platinum; three distinct template blocks (breaking / degraded / cosmetic), each unconditionally mandatory for its tier |
| C-17 | PASS | Established; rationale sentence in resolution slot |
| C-18 | PASS | Established; clause-precise `spec:` field |
| C-19 | PASS | Established; behavioral protocol block before Phase 1 |
| C-20 | PASS | Established; Patterns as named sub-block in Phase 5 |
| C-21 | PASS | Established; named phase-role headings |
| C-22 | PASS | R7 platinum; complete artifact skeleton pre-declared |
| C-23 | PASS | Full metadata manifest: `clauses:N \| date: \| author: \| phase:1-complete` + closure echo |
| C-24 | PASS | Three-branch with explicit per-branch instructions: ZERO requires affirmative label + confirmation; SINGLETON requires attribution per finding; MULTI requires root-cause grouped sections |
| C-25 | PASS | `hypothesis-draft:` → `self-test: [YES/NO — could this be written from the deviation line alone without knowing the system?]` → `mechanism:` — YES answer disqualifies the draft; model must rewrite before proceeding |

**Essential:** 60/60 | **Recommended:** 30/30 | **Aspirational:** 17/17
**Total: 107/107**

---

### Composite Summary

| Variation | Essential | Recommended | Aspirational | **Total** | Essential Pass |
|-----------|-----------|-------------|--------------|-----------|----------------|
| V-05 | 60 | 30 | 17 | **107** | YES |
| V-04 | 60 | 30 | 14 | **104** | YES |
| V-01 | 60 | 30 | 12 | **102** | YES |
| V-02 | 60 | 30 | 11 | **101** | YES |
| V-03 | 60 | 30 | 11 | **101** | YES |

**Ranking:** V-05 > V-04 > V-01 > V-02 = V-03

---

### Excellence Signals from V-05

**1. Metadata manifest converts gate from event to invariant.**
The C-23 clause count embedded in `[EXPECTED-SEALED | clauses:N | ...]` means the gate is no longer just a boundary marker — it is a checksum. The closure token echoes `gate-clauses:N`, making clause-count drift detectable without re-reading the expected section. The gate carries provenance, not just position.

**2. Branch exhaustion eliminates the silent-omission gap for cardinality-zero.**
Prior rounds required Patterns grouping only when N ≥ 2. Zero-finding and singleton cases were implicitly skippable. V-05's three named branches with distinct pass conditions (affirmative label for zero, per-finding attribution for singleton) make every cardinality case structurally mandatory. The Patterns section cannot be empty or absent regardless of finding count.

**3. Necessary-information self-test converts named disqualifier to mechanical procedure.**
C-05 named the disqualification rule; C-25 operationalizes it. The `draft → self-test: YES/NO → mechanism` triple slot embeds the decision at write time. A YES answer is a structural blocking condition — the hypothesis slot cannot be filled until the model produces a mechanism that could not have been written from the deviation line alone. Quality gates that live in instructions are advisory; quality gates embedded in template slots are enforcing.

**4. V-05 = V-04 + severity-stratified connector-impact + self-test.**
V-04 reaches 104 by combining the two structural layers (gate manifest, Patterns skeleton). V-05's three additional points come from C-14 (per-finding connector-impact, not just at-least-one), C-16 (stratified templates eliminating conditional-field language), and C-25 (self-test decision procedure). The gap between 104 and 107 is the difference between coverage and enforcement.

---

```json
{"top_score": 107, "all_essential_pass": true, "new_patterns": ["Metadata manifest at gate: encoding a verifiable clause-count invariant in the gate token converts the phase boundary from a positional marker into a count-checksum", "Branch exhaustion for cardinality-zero: naming the zero-findings case explicitly with an affirmative label requirement closes the silent-omission gap that N>=2 conditions leave open", "Self-test decision procedure embedded in template slot: the necessary-information question converts a named symptom-restatement disqualifier into a mechanical YES/NO blocking condition at hypothesis-write time"]}
```
