# Quest Score — campaign-brief / Round 13 / Rubric v12

## Scoring Summary

**Rubric:** v12 — 32 criteria, 320 pts max
**Axis:** C-32 only — preamble forward-reference precision (designation + location)
**Baseline:** V-01 = R12 V-05 exact, which scored 310/310 under v11

---

## Shared Criteria — C-01 through C-31

All five variations are structurally identical except for C-32. V-01 is the R12 V-05 ceiling variation, which established PASS on all criteria through C-31. No variation regresses any prior criterion.

| Range | Score | Basis |
|---|---|---|
| C-01 – C-30 | 300/300 | Carried from R12 V-05 (31 PASS, 310/310 under v11) |
| C-31 | 10/10 | Bidirectional circuit present in all R13 variations: execution notes invoke preamble by structural designation name (`=== COMPRESSION-IMMUNE PREAMBLE ===`); preamble self-declares as structural contract |

**Subtotal before C-32:** 310/320 for all variations

---

## C-32 Scoring per Variation

**C-32 criterion:** When C-31 PASS, the COMPRESSION-IMMUNE PREAMBLE section contains forward-references naming each companion execution-note mechanism by **full clause designation AND block location** — creating a reference architecture navigable from the preamble alone when execution notes are elided.

**Scoring convention:** PASS = 10 pts, PARTIAL = 0 pts (diagnostic only), FAIL = 0 pts.

---

### V-01 — Control (R12 V-05 exact)

**TOKEN-PRESSURE GUARD references C-29 companion as:** `"The STORY execution note"`
**COMPRESSED-COLLAPSE GUARD references C-30 companion as:** `"The STATUS execution note"`

**C-32: PARTIAL**
Evidence: References use generic block names only. No clause designation. No explicit location within block. A model surviving preamble-preserved / execution-notes-elided compression cannot identify *which* execution note within STORY, nor its structural name. Navigation requires execution notes to be present — defeating the purpose of preamble immunity.

**C-32 score: 0/10**
**V-01 total: 310/320**

---

### V-02 — Location-only

**TOKEN-PRESSURE GUARD references C-29 companion as:** `"the declarative execution note in the STORY block"`
**COMPRESSED-COLLAPSE GUARD references C-30 companion as:** `"the declarative execution note in the STATUS block"`

**C-32: PARTIAL**
Evidence: Block location is present ("in the STORY block," "in the STATUS block"). However, "declarative execution note" is a role-type descriptor, not a clause designation. Under compression, if STORY contains multiple execution notes, the reference is ambiguous — "declarative" describes a class, not a specific clause. Clause designation absent means the loop is location-grounded but not designation-navigable.

**C-32 score: 0/10**
**V-02 total: 310/320**

---

### V-03 — Designation-only

**TOKEN-PRESSURE GUARD references C-29 companion as:** `"The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) clause"`
**COMPRESSED-COLLAPSE GUARD references C-30 companion as:** `"The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) clause"`

**C-32: PARTIAL**
Evidence: Full clause designations present — `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)` and `TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)` are unambiguous clause names. However, no block location is provided. A model with the preamble and the clause name can search for the clause — but if content is elided and the block structure is not recoverable, positional orientation is lost. The designation is the entry key; the location is the directory. Designation without location is navigable only when block structure survives compression.

**C-32 score: 0/10**
**V-03 total: 310/320**

---

### V-04 — Asymmetric (C-29 full, C-30 partial)

**TOKEN-PRESSURE GUARD references C-29 companion as:** `"The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"` (designation + location — full)
**COMPRESSED-COLLAPSE GUARD references C-30 companion as:** `"The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) clause"` (designation only — partial)

**C-32: PARTIAL**
Evidence: C-29 forward-reference achieves C-32 PASS individually — clause designation + block location, fully navigable from preamble alone. C-30 forward-reference achieves only designation without location (same as V-03). C-32 requires the closed reference loop to be complete for **all** companion mechanism references in the preamble. Asymmetric completion does not satisfy the criterion — a model surviving compression can navigate to C-29's companion but not C-30's. The preamble is only as navigable as its weakest forward-reference.

**C-32 score: 0/10**
**V-04 total: 310/320**

---

### V-05 — Full C-32 PASS

**TOKEN-PRESSURE GUARD references C-29 companion as:** `"The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"`
**COMPRESSED-COLLAPSE GUARD references C-30 companion as:** `"The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block"`

**C-32: PASS**
Evidence: Both preamble guards contain full clause designation + block location. Forward-references are:
- Unambiguous by designation (full clause name with `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical confirms structural role)
- Spatially grounded by block (STORY block / STATUS block — two distinct blocks, no ambiguity even if block structure is partially elided)

With C-31 PASS (execution notes invoke preamble by designation) and C-32 PASS (preamble guards invoke companion mechanisms by designation + location), the closed reference loop is complete:
- Entry from preamble → navigate to companion mechanisms by designation and block
- Entry from execution note → navigate to preamble by structural designation
- Either entry point survives single-location elision and recovers the full two-mechanism architecture

**C-32 score: 10/10**
**V-05 total: 320/320**

---

## Composite Scores

| Variation | C-01–C-30 | C-31 | C-32 | Total | Rank |
|---|---|---|---|---|---|
| V-05 | 300 | 10 | 10 | **320/320** | 1 |
| V-01 | 300 | 10 | 0 | **310/320** | 2 (tied) |
| V-02 | 300 | 10 | 0 | **310/320** | 2 (tied) |
| V-03 | 300 | 10 | 0 | **310/320** | 2 (tied) |
| V-04 | 300 | 10 | 0 | **310/320** | 2 (tied) |

V-01 through V-04 are diagnostically distinct (three failure modes on C-32) but score identically.

---

## Excellence Signals from V-05

**Signal A — Designation + location as an atomic unit for preamble forward-references:**
The clause name alone (V-03) tells the model *what* to find. The block location alone (V-02) tells the model *where* to look. Neither is sufficient independently under compression elision. V-05's forward-references treat `[clause designation] + [block location]` as an inseparable unit: the designation anchors the identity, the block location anchors the position. Together they form a self-contained pointer — navigable even when the referenced content is elided, because the pointer contains both the key and the directory.

**Signal B — Symmetry requirement for closed loop:**
V-04 demonstrates that partial completion of the loop (one guard fully specified, one guard designation-only) does not satisfy C-32. The preamble's navigability is bounded by its least-specified forward-reference. V-05 enforces symmetry: both guards — TOKEN-PRESSURE and COMPRESSED-COLLAPSE — carry the same reference precision. The loop is only closed when every path through it is navigable.

**Signal C — `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical as role confirmation:**
In both clause designations (`ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)` and `TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)`), the parenthetical confirms the structural relationship between the companion execution note and the preamble. A model reading the preamble forward-reference can confirm: this execution note was authored as a COMPRESSION-IMMUNE PREAMBLE invocation mechanism — it is structurally coupled to this preamble, not a coincidental clause. The parenthetical disambiguates in the case where a skill might have multiple clauses named similarly.

---

## Structural Chain Update

**Compression-immune consolidation chain (v12 complete):**

```
C-29 → C-30 → C-31 → C-32
```

- **C-29:** Zero-signal synthesis protection — dual-mechanism (structural mandate + execution-note clause)
- **C-30:** Timestamp isolation — dual-mechanism (structural isolation rule + execution-note clause)
- **C-31:** Multi-rule COMPRESSION-IMMUNE PREAMBLE — bidirectional circuit (preamble designated immune; execution notes invoke preamble by structural designation name)
- **C-32:** Closed reference loop — preamble forward-references name companion mechanisms by clause designation + block location; navigable from either entry point under single-location elision

**V-05 achieves all four. The chain is complete.**

---

## R14 Investigation Candidate

From V-05's excellence signals: the preamble's TOKEN-PRESSURE GUARD and COMPRESSED-COLLAPSE GUARD now contain full designation+location forward-references. R14 should test whether adding a **meta-declaration sentence** in the preamble intro — e.g., *"When this section references companion execution-note mechanisms, those references name the mechanism's clause designation and block location — they are navigable from this section alone without requiring the execution notes to be present"* — adds independently measurable protection, or whether the designation+location forward-references in the guards are already sufficient.

Specifically: does the meta-declaration add value when the guards themselves already encode navigation? Or does it create redundancy that serves as a secondary signal for compression-survival (the preamble now declares its own reference architecture, so a model reading only the preamble intro knows to trust and use the guard forward-references)?

If the meta-declaration produces measurably different recovery in the elision case — e.g., the model treats the guard forward-references as trusted navigable pointers rather than informational notes — it belongs in C-33. If it produces no measurable difference from V-05 alone, it is decorative.

---

```json
{"top_score": 320, "all_essential_pass": true, "new_patterns": ["Designation+location as atomic forward-reference unit in preamble guards: clause designation names the mechanism, block location grounds its position — neither alone is sufficient for navigability under single-location elision; both together form a self-contained pointer that survives compression", "Symmetric loop completion required: C-32 PASS requires all preamble guards to carry full designation+location forward-references — asymmetric completion (one guard full, one designation-only) leaves the loop open and does not satisfy the criterion"]}
```
