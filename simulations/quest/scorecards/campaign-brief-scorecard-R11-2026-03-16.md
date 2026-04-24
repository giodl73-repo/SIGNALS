Now I have everything needed to score all five R11 variations. Let me produce the full evaluation.

---

# Quest Score — campaign-brief / Round 11 / Rubric v10

**Skill target:** campaign-brief
**Round:** 11
**Rubric:** v10 (30 criteria, 300 pts max)
**R11 axis:** C-30 necessity and dual-mechanism structure for timestamp isolation rule

---

## Evaluation Framework

**Scoring:** PASS = 10 pts, PARTIAL = 0 pts, FAIL = 0 pts per criterion.
**R11 differentiating criterion:** C-30 only. All five variations preserve R10 best form on C-01–C-29.

---

## Per-Criterion Evaluation

### C-01 through C-20 — Structural scaffold (all variations)

All five R11 variations preserve the identical scaffold inherited from R10 best form:
- [TOPIC] with all required fields
- [DELTA] comparing to prior brief, first-run handling
- [STRATEGY] table (≥3 rows, all columns)
- [STATUS] with FULL/COMPRESSED density contract, inertia risk on all blocking gaps, BLOCKING-DETAIL when triggered, coverage calculation
- [CONFIDENCE] three dimensions, arithmetic average, binding dimension
- [STORY] 2–4 paragraphs prose, no lists/tables, no artifact filenames
- [VERDICT] status/rationale/inertia_cost (bounded/unbounded + action sub-label) / blocking / optional

Block order, field presence, and execution instructions are structurally identical across all variations. R10 validated all C-01–C-20 at PASS for the base form.

**C-01 through C-20: PASS (all five variations)**

---

### C-21 — Sparse-coverage synthesis protection

All five variations include the STORY rule: *"Sparse coverage: if found contains signals from only 1–2 namespaces, synthesize on available signals — do not default to a coverage disclaimer."* Identical text across V-01 through V-04. V-05 contains the same rule text, referenced via "COMPRESSION-IMMUNE PREAMBLE Rule 1."

**All variations: PASS**

---

### C-22 — Zero-signal synthesis mandate

All five variations contain an explicit zero-signal clause. V-01 through V-04 carry it in the preamble ZERO-SIGNAL SYNTHESIS RULE: *"Empty `found` is not grounds for omitting, hollowing, or shortening the STORY block... A STORY block that reports absence without characterizing what absence implies is a non-finding."* V-05 is identical, framed as RULE 1 within the COMPRESSION-IMMUNE PREAMBLE. The STORY execution note in each variation references the preamble clause for zero-coverage handling.

**All variations: PASS**

---

### C-23 — Bounded/unbounded inertia classification at verdict level

All five VERDICT execution notes contain the full bounded/unbounded structure with `action:` sub-label at both branches. Text is identical across all variations. Verdict-level recoverability classification is present regardless of COMPRESSED state.

**All variations: PASS**

---

### C-24 — Timestamp isolation dual-location mandate

Two structural locations required: entry format definition (Location 1: inline annotation on `found` date field) AND STATUS/STORY execution note (Location 2).

- **V-01:** Location 1 = inline arrow annotation on `<date>` field (*"timestamp is structurally separate from blocking entries; this field is NOT subject to COMPRESSED abbreviation"*). Location 2 = STATUS execution note (*"This is the second structural location for the timestamp isolation rule; the first is the inline annotation on the date field above"*). → **PASS**
- **V-02:** Same dual-location from V-01, execution note updated to name preamble as "the third location." Both required locations preserved. → **PASS**
- **V-03:** Same dual-location from V-01, execution note extended with COMPRESSED-COLLAPSE GUARD text. Both required locations preserved. → **PASS**
- **V-04:** Location 1 = inline annotation (unchanged). Location 2 = execution note (*"This is the second structural location for the timestamp isolation rule; the first is the inline annotation on the date field above. The preamble TIMESTAMP ISOLATION RULE is the third location."*) → **PASS**
- **V-05:** Location 1 = inline annotation, now pointing to COMPRESSION-IMMUNE PREAMBLE Rule 2 as primary. Location 2 = execution note (*"This is the second structural location for the timestamp isolation rule; the primary location is in the COMPRESSION-IMMUNE PREAMBLE above"*). Both required locations present. → **PASS**

**All variations: PASS**

---

### C-25 — TOKEN-PRESSURE GUARD on zero-signal synthesis rule

All variations: *"TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires unconditionally at any token budget."* Named-rule promotion present with unconditional-firing declaration.

**All variations: PASS**

---

### C-26 — VERDICT COMPRESSION GUARD on mandatory last-block sub-labels

All variations: VERDICT execution note contains *"VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is required regardless of COMPRESSED format state and regardless of token pressure."* Guard is a named instruction, not implied by format examples.

**All variations: PASS**

---

### C-27 — TOKEN-PRESSURE GUARD names conditional-dormancy failure mode

All variations: TOKEN-PRESSURE GUARD names *"conditional-context suppression — a failure mode in which the model treats the rule as dormant because `found` is large."* Failure mode is explicit: the model processing the condition as inactive (found is non-empty) and suppressing the clause. Terminology *conditional-context suppression* is equivalent to *conditional dormancy* — validated as C-27 PASS in R9/R10.

**All variations: PASS**

---

### C-28 — VERDICT COMPRESSION GUARD declares `action:` as mandatory invariant

All variations: *"The action sub-label is not optional format — it is the field that makes VERDICT self-contained and enables the team to derive their commit posture from this block alone without re-reading STORY or item-level gap entries."* Mandatory invariant status declared; omission framed as structural violation. Text identical across all five variations.

**All variations: PASS**

---

### C-29 — Dual-mechanism independence for zero-signal synthesis rule

Both mechanisms required: (1) preamble placement (positional), (2) TOKEN-PRESSURE GUARD naming conditional-dormancy failure mode (declarative).

All five R11 variations preserve R10 best form on this criterion:
- **Positional mechanism:** ZERO-SIGNAL SYNTHESIS RULE appears in preamble before phase execution.
- **Declarative mechanism:** TOKEN-PRESSURE GUARD names conditional-context suppression as the failure mode.

Both mechanisms present, orthogonal failure modes covered (elision vs. dormancy). Validated in R10.

**All variations: PASS**

---

### C-30 — Dual-mechanism independence for timestamp isolation rule *(differentiating criterion)*

Two independent mechanisms required — each guarding against a **different** failure mode:
- **Positional:** timestamp isolation rule in preamble (before token pressure builds, before COMPRESSED branch)
- **Declarative:** guard clause naming **COMPRESSED-collapse** as the failure mode (collaping found timestamps into the blocking summary)

| Variation | Positional mechanism | Declarative mechanism | Verdict |
|-----------|---------------------|----------------------|---------|
| V-01 | Absent — no preamble placement of timestamp rule | Absent — C-24 dual-location only (mid-doc, same failure-mode class) | **PARTIAL** |
| V-02 | Present — TIMESTAMP ISOLATION RULE in preamble | Absent — no COMPRESSED-COLLAPSE GUARD naming failure mode | **PARTIAL** |
| V-03 | Absent — no preamble placement | Present — COMPRESSED-COLLAPSE GUARD in STATUS execution note, naming COMPRESSED-collapse explicitly | **PARTIAL** |
| V-04 | Present — TIMESTAMP ISOLATION RULE in preamble, separate block | Present — COMPRESSED-COLLAPSE GUARD embedded within the preamble TIMESTAMP ISOLATION RULE block | **PASS** |
| V-05 | Present — RULE 2 in COMPRESSION-IMMUNE PREAMBLE | Present — COMPRESSED-COLLAPSE GUARD within RULE 2, naming COMPRESSED-collapse failure mode | **PASS** |

**Notes:**
- V-01: C-24's two locations (inline annotation + STATUS execution note) are both mid-document and subject to the same token-pressure suppression event. Neither guards against a *different* failure mode — both guard against location elision within the same class. C-30 PARTIAL.
- V-02: Preamble position added, but without a declarative guard, the rule is vulnerable to processing-without-absorption (model reads the preamble section but does not retain the constraint when the STATUS block is produced). C-30 PARTIAL.
- V-03: Declarative guard present mid-document (STATUS execution note), but without preamble placement, the guard itself is vulnerable to elision under token pressure before the STATUS block is reached. C-30 PARTIAL.
- V-04: Both mechanisms present. Preamble placement ensures rule encountered before token pressure builds. COMPRESSED-COLLAPSE GUARD (within the preamble block) names the specific failure mode. Failure modes are orthogonal: location-elision (countered by preamble) vs. processing-without-absorption (countered by declarative guard). C-30 **PASS**.
- V-05: Both mechanisms present within the COMPRESSION-IMMUNE PREAMBLE block. Guard clause explicitly states the orthogonality: *"preamble position guards against location elision; this guard clause guards against processing-without-absorption — orthogonal failure modes, each compensating when the other's protection is unavailable."* C-30 **PASS**.

---

## Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | P | P | P | P | P |
| C-02 | P | P | P | P | P |
| C-03 | P | P | P | P | P |
| C-04 | P | P | P | P | P |
| C-05 | P | P | P | P | P |
| C-06 | P | P | P | P | P |
| C-07 | P | P | P | P | P |
| C-08 | P | P | P | P | P |
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | P | P |
| C-18 | P | P | P | P | P |
| C-19 | P | P | P | P | P |
| C-20 | P | P | P | P | P |
| C-21 Sparse-coverage synthesis | P | P | P | P | P |
| C-22 Zero-signal synthesis mandate | P | P | P | P | P |
| C-23 Bounded/unbounded at verdict | P | P | P | P | P |
| C-24 Timestamp dual-location | P | P | P | P | P |
| C-25 TOKEN-PRESSURE GUARD exists | P | P | P | P | P |
| C-26 VERDICT COMPRESSION GUARD exists | P | P | P | P | P |
| C-27 Guard names failure mode | P | P | P | P | P |
| C-28 `action:` as mandatory invariant | P | P | P | P | P |
| C-29 Dual-mech: zero-signal synthesis | P | P | P | P | P |
| C-30 Dual-mech: timestamp isolation | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** | **PASS** |
| **Score** | **290/300** | **290/300** | **290/300** | **300/300** | **300/300** |

*(P = PASS = 10 pts; PARTIAL = 0 pts)*

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 (tie) | V-04 | 300/300 | C-30 PASS: two separate preamble blocks, COMPRESSED-COLLAPSE GUARD embedded in TIMESTAMP ISOLATION RULE block |
| 1 (tie) | V-05 | 300/300 | C-30 PASS: unified COMPRESSION-IMMUNE PREAMBLE, atomic contract, orthogonality explicitly named |
| 3 (tie) | V-01 | 290/300 | C-30 PARTIAL: R10 best form — C-24 dual-location only, no C-30 mechanisms |
| 3 (tie) | V-02 | 290/300 | C-30 PARTIAL: preamble position present, declarative guard absent |
| 3 (tie) | V-03 | 290/300 | C-30 PARTIAL: declarative guard present (mid-doc), preamble position absent |

---

## R11 Investigation Outcomes

**C-30 necessity (V-01 as control):** CONFIRMED. V-01 scores 290/300, not 300/300. C-24's dual-location (inline annotation + STATUS execution note) does not satisfy C-30 because both C-24 locations are mid-document and subject to the same token-pressure suppression event — they guard against the same failure-mode class (which location is reached first), not orthogonal failure modes. C-30 is independently necessary.

**C-30 preamble-only (V-02):** C-30 PARTIAL confirmed. Positional mechanism alone insufficient: a model that processes the preamble but does not absorb the timestamp isolation constraint will not be guarded at STATUS production time. Mirrors R10's V-01 result for C-29.

**C-30 declarative-only (V-03):** C-30 PARTIAL confirmed. Declarative mechanism alone insufficient: the COMPRESSED-COLLAPSE GUARD in the STATUS execution note is itself vulnerable to elision under token pressure before the STATUS block is reached. No positional fallback. Mirrors R10's V-02 result for C-29.

**C-30 full dual-mechanism (V-04):** 300/300 confirmed. Both mechanisms together achieve C-30 PASS. The COMPRESSED-COLLAPSE GUARD embedded within the preamble TIMESTAMP ISOLATION RULE block is the key structural element — guard and rule are co-located in the same semantic unit at document-head position, making processing-without-absorption more costly than compliance.

**V-05 COMPRESSION-IMMUNE PREAMBLE:** 300/300 confirmed. Unified block architecture achieves C-30 PASS with the additional property that both compression-critical rules form an atomic contract — suppressing either rule requires suppressing the entire named preamble block. V-05's explicit orthogonality statement (*"preamble position guards against location elision; this guard clause guards against processing-without-absorption — orthogonal failure modes"*) is the clearest articulation of the dual-mechanism principle in the variation series.

---

## Excellence Signals (from V-04 and V-05)

**V-04 pattern — Guard-clause co-location at preamble position:**
The COMPRESSED-COLLAPSE GUARD is embedded within the preamble TIMESTAMP ISOLATION RULE block itself, not in a separate STATUS execution note. Rule and guard are semantically co-located at document-head position. Any model path that reads the rule also reads the guard; no document-distance gap between rule and its protection mechanism. This contrasts with V-03's mid-document guard (rule in preamble absent, guard in STATUS) and eliminates the independent failure mode where the rule is present at one location and the guard present at a different, potentially unreachable location.

**V-05 pattern — COMPRESSION-IMMUNE PREAMBLE as atomic compression contract:**
Grouping both compression-critical rules under a single named block with an atomicity declaration (*"suppressing any rule in this block requires suppressing the entire preamble"*) creates a qualitatively stronger structural guarantee than two separate preamble blocks. The named container turns the preamble from a collection of individual rules into a compression contract: the model either processes all guarded rules or processes none. This makes selective suppression of one rule structurally indistinguishable from suppressing the entire preamble — raising the cost of non-compliance beyond what two independent blocks achieve.

**V-05 pattern — Orthogonality explicitly stated within guard clause:**
V-05's RULE 2 COMPRESSED-COLLAPSE GUARD explicitly names why the two mechanisms are orthogonal: *"preamble position guards against location elision; this guard clause guards against processing-without-absorption — orthogonal failure modes, each compensating when the other's protection is unavailable."* This self-documenting independence declaration is stronger than V-04's equivalent, where the orthogonality is structural but less explicitly articulated. Future rules can adopt this explicit orthogonality framing as a standard pattern for dual-mechanism independence.

---

## C-30 Independence Validation Summary

The R11 series confirms C-30's orthogonal-failure-mode requirement through three falsifiable tests:

| Test | Result | Conclusion |
|------|--------|-----------|
| V-01 (control): C-24 alone | 290 — PARTIAL | C-24 dual-location insufficient for C-30; both locations share failure-mode class |
| V-02: preamble-only | 290 — PARTIAL | Positional alone insufficient; no guard against processing-without-absorption |
| V-03: declarative-only | 290 — PARTIAL | Declarative alone insufficient; no positional fallback against elision |
| V-04 + V-05: dual-mech | 300 — PASS | Both mechanisms together necessary and sufficient |

---

```json
{"top_score": 300, "all_essential_pass": true, "new_patterns": ["Guard-clause co-location at preamble position: embedding the declarative COMPRESSED-COLLAPSE GUARD within the preamble rule block (not in a separate mid-document execution note) ensures rule and guard are semantically co-located, eliminating the document-distance gap that makes V-03 declarative-only vulnerable", "COMPRESSION-IMMUNE PREAMBLE as atomic compression contract: a named block grouping all compression-critical rules with an atomicity declaration transforms the preamble from a collection of individual rules into a single compression contract where selective suppression of any one rule requires suppressing the entire block", "Explicit orthogonality declaration within guard clause: naming which failure mode each mechanism guards against (location elision vs. processing-without-absorption) makes the independence contract self-documenting and strengthens absorption when the guard clause is encountered"]}
```
