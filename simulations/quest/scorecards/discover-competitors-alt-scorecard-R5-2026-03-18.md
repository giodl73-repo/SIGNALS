---

## discover-competitors-alt — Scorecard R5

**Rubric v5 | New criteria: C-18, C-19, C-20**

### Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 9.583 (11.5/12) | **99.583** |
| V-02 | 60 | 30 | 9.167 (11/12) | **99.167** |
| V-03 | 60 | 30 | 8.750 (10.5/12) | **98.750** |
| V-04 | 60 | 30 | 9.167 (11/12) | **99.167** |
| V-05 | 60 | 30 | 10.000 (12/12) | **100.000** |

**Winner: V-05** — first perfect score. All 5 are golden (all essential pass, composite >= 80).

### New criteria verdicts

| | C-18 | C-19 | C-20 |
|---|------|------|------|
| V-01 | PASS | PARTIAL | PASS |
| V-02 | **FAIL** | PASS | PASS |
| V-03 | PASS | **FAIL** | PARTIAL |
| V-04 | PASS | PARTIAL | PARTIAL |
| V-05 | PASS | PASS | PASS |

### Key rulings

**C-19:** Strict interpretation ("literal first output") would fail every DOMAIN-TERMS-first variation. The scoring applies the structural interpretation — DOMAIN-TERMS is unconditional vocabulary extraction, not on C-19's prohibited list. The decisive differentiator: V-05 explicitly names GATE-1 as "the first gate with conditional logic," making the boundary architecturally declared. V-01/V-04 label their phase as unconditional but don't name the successor, yielding PARTIAL. V-03's own text says "Your first line must be DOMAIN-TERMS" — no structural argument survives that.

**C-20:** V-04's `ROOT verdict` column header fails the "naive reader" test — a reader who doesn't know ROOT = inertia anchor can't identify it as the stability verdict component. Domain-neutral names (`Stability verdict`) are required.

### New patterns

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["GATE-0 resolves the C-18/C-19 tension by declaring DOMAIN-TERMS and TOKEN as a two-output unconditional pre-phase, with GATE-1 explicitly named as the first conditional operation — both conditions (unconditional phase label + named conditional successor) are required to satisfy C-19 under structural interpretation", "AMEND schema headers must use rubric-standard component names (Stability verdict, not ROOT verdict) — domain-specific renamings of required components fail C-20's naive-reader consultability test"]}
```
 is first — no structural argument survives that language.
- V-02: TOKEN is literally the first output line; C-19 passes under any interpretation.

Result: V-05 C-19 PASS, V-01/V-04 C-19 PARTIAL, V-03 C-19 FAIL, V-02 C-19 PASS/C-18 FAIL.

---

## Criterion-level scorecard

### Essential criteria (12 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 C0 before competitors | PASS | PASS | PASS | PASS | PASS |
| C-02 3+ named competitors + threat levels | PASS | PASS | PASS | PASS | PASS |
| C-03 C0 at row 0 | PASS | PASS | PASS | PASS | PASS |
| C-04 Whitespace identified | PASS | PASS | PASS | PASS | PASS |
| C-05 Auto-detect topic | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | **60** | **60** | **60** | **60** | **60** |

All variations pass all essential criteria. Every variation structures C0 in a dedicated section before the competitive table; the table enforces row 0 = C0; whitespace is a required labeled output; topic auto-detection is explicitly specified without user prompting.

---

### Recommended criteria (10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Mechanism-level inertia | PASS | PASS | PASS | PASS | PASS |
| C-07 Web-verified inline citation | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND input-to-output pairs | PASS | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | **30** | **30** | **30** | **30** | **30** |

All variations pass. C-06: every variation requires mechanism type tied to a specific C0 behavior. C-07: every variation requires at least one inline WebSearch citation in the Source cell. C-08: every AMEND requires naming both input change and output effect.

---

### Aspirational criteria (0.833 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 Cross-dimensional whitespace | PASS | PASS | PASS | PASS | PASS |
| C-10 Grounded findings | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia propagates downstream | PASS | PASS | PASS | PASS | PASS |
| C-12 AMEND evaluates inertia stability | PASS | PASS | PASS | PASS | PASS |
| C-13 Portable token assigned | PASS | PASS | PASS | PASS | PASS |
| C-14 Stability in every AMEND entry | PASS | PASS | PASS | PASS | PASS |
| C-15 Token pre-declared before C0 | PASS | PASS | PASS | PASS | PASS |
| C-16 Verdict + evidence every entry | PASS | PASS | PASS | PASS | PASS |
| C-17 Token encodes domain context | PASS | PASS | PASS | PASS | PASS |
| C-18 DOMAIN-TERMS as prior artifact | PASS | **FAIL** | PASS | PASS | PASS |
| C-19 TOKEN before conditional logic | **PARTIAL** | PASS | **FAIL** | **PARTIAL** | PASS |
| C-20 AMEND schema enumerates all four | PASS | PASS | **PARTIAL** | **PARTIAL** | PASS |
| **Aspirational numerator** | 11.5 | 11 | 10.5 | 11 | 12 |
| **Aspirational subtotal** | **9.583** | **9.167** | **8.750** | **9.167** | **10.000** |

---

## Per-criterion evidence notes (new criteria)

### C-18 — DOMAIN-TERMS as prior artifact

- **V-01 PASS:** STEP 0 writes `DOMAIN-TERMS:` and closes it before TOKEN. "Do not move to TOKEN until DOMAIN-TERMS is written." Separate committed output artifact.
- **V-02 FAIL:** TOKEN is literal first output. DOMAIN-CHECK appears post-TOKEN as a confirmation note, not a prior extraction artifact. No DOMAIN-TERMS before TOKEN.
- **V-03 PASS:** "Write that line and close it" — the contract is explicit. DOMAIN-TERMS is a closed artifact before TOKEN is written.
- **V-04 PASS:** Phase 0 writes DOMAIN-TERMS then ROOT. "Write and close the DOMAIN-TERMS line before proceeding to ROOT." Artifact sequencing identical to V-01.
- **V-05 PASS:** GATE-0 output contract: "DOMAIN-TERMS is the first line. Write it and close it before writing TOKEN." Completion condition enforces ordering.

### C-19 — TOKEN before conditional logic

- **V-01 PARTIAL:** STEP 0 is labeled "unconditional, no branches, runs before focus detection." The structural argument is present. However, STEP 0 does not explicitly name STEP 1 as "the first conditional operation" — the execution boundary is stated by exclusion rather than by explicit phase labeling. Partial structural argument; the boundary is inferential, not declared.
- **V-02 PASS:** TOKEN is the literal first output line. "Nothing precedes it." Satisfies C-19 under any interpretation.
- **V-03 FAIL:** "Your first line must be DOMAIN-TERMS" and "Do not write anything else before these two lines" explicitly assert DOMAIN-TERMS is first output. No structural gate argument counters that direct statement. TOKEN is demonstrably not the first output.
- **V-04 PARTIAL:** Phase 0 labeled "unconditional — no branches, no detection." Same structural argument as V-01, same limitation: Phase 1 is not named as the first conditional phase. The boundary claim requires inference.
- **V-05 PASS:** GATE-0 is "the unconditional pre-phase" and GATE-1 is explicitly labeled "the first gate with conditional logic." The naming closes the interpretive gap: TOKEN (last output of GATE-0) provably precedes the first conditional operation (GATE-1). The execution boundary is architecturally declared, not inferred.

### C-20 — AMEND schema enumerates all four components by name

- **V-01 PASS:** Numbered 4-part schema: "1. Input change: ... 2. Output effect: ... 3. Stability verdict: STABLE | UNSTABLE — ... 4. Evidence: ..." All four component names are literal. A reader consulting only the schema identifies all four without examples.
- **V-02 PASS:** 4-column table headers: `Input change | Output effect | Stability verdict | Evidence`. Column headers are a structured schema; all four component names visible without reading rows.
- **V-03 PARTIAL:** Numbered list with bold labels names all four, but the schema is preceded by an instructional prose block ("For each one, you need exactly four things") that partially conflates the schema with the instruction. The schema is formally present and names all four components; the borderline is whether conversational embedding affects consultability. Scored PARTIAL as a marginal case.
- **V-04 PARTIAL:** 4-column table headers: `Input change | Output effect | ROOT verdict | Evidence`. Three of four component names are literal. "ROOT verdict" renames stability verdict using a domain-specific label — a reader unfamiliar with ROOT convention would not identify it as the stability assessment component. C-20's "naive reader" test fails for that column.
- **V-05 PASS:** GATE-4 table headers: `Input change | Output effect | Stability verdict | Evidence`. All four literal component names. "A reader consulting only the headers can identify all four required components without reading the rows."

---

## Composite computation

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10)
PARTIAL counts as 0.5 toward numerator.
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 x 60 = 60 | 3/3 x 30 = 30 | 11.5/12 x 10 = 9.583 | 99.583 |
| V-02 | 5/5 x 60 = 60 | 3/3 x 30 = 30 | 11/12 x 10 = 9.167 | 99.167 |
| V-03 | 5/5 x 60 = 60 | 3/3 x 30 = 30 | 10.5/12 x 10 = 8.750 | 98.750 |
| V-04 | 5/5 x 60 = 60 | 3/3 x 30 = 30 | 11/12 x 10 = 9.167 | 99.167 |
| V-05 | 5/5 x 60 = 60 | 3/3 x 30 = 30 | 12/12 x 10 = 10.000 | 100.000 |

---

## Excellence signals (V-05 patterns)

### Signal 1 — GATE-0 architecture resolves the C-18/C-19 tension by naming the execution boundary

V-05's GATE-0 is the only architecture that satisfies both C-18 and C-19 simultaneously. The resolution: GATE-0 produces exactly two outputs (DOMAIN-TERMS then TOKEN) and is explicitly declared as the pre-conditional phase. GATE-1 is explicitly labeled "the first gate with conditional logic."

V-01/V-04 make the same structural argument but do not name the first conditional gate. Their C-19 boundary is described by exclusion ("before focus detection") rather than by gate identity. V-05's GATE naming makes the boundary an explicit structural element that can be verified without interpreting instruction prose.

**The pattern:** DOMAIN-TERMS before TOKEN satisfies both C-18 and C-19 when (a) the pre-token phase explicitly declares itself unconditional AND (b) the successor phase explicitly names itself as the first conditional operation. V-01/V-04 satisfy (a) but not (b). Both conditions are necessary.

### Signal 2 — Gate completion conditions make phase contracts rubric-auditable

V-05 declares explicit completion conditions per gate: "GATE-0 completion condition: DOMAIN-TERMS: line written and closed. TOKEN: line written and closed. Both lines appear before any other output." A rubric auditor can verify gate compliance from the completion condition alone, without parsing instruction prose.

V-01's STEP 0 is descriptive but has no completion condition. V-05's gate contract offloads verification to the gate structure itself.

### Signal 3 — Domain-neutral component names in AMEND headers satisfy C-20 without consultability loss

V-05's GATE-4 uses `Stability verdict` (not `ROOT verdict` or `TOKEN stability`). The rubric's exact component terminology makes the schema directly consultable by a naive reader. V-04's "ROOT verdict" substitution failed C-20 precisely because domain-specific renamings require context to decode.

**The pattern:** AMEND column headers satisfy C-20 most robustly when they use rubric-standard component names, even when domain-specific alternatives would be more expressive in practice.

---

## Round 5 findings

**C-18 and C-19 are satisfiable simultaneously, but only with explicit gate-boundary naming.** The structural argument (DOMAIN-TERMS is unconditional, TOKEN precedes first conditional gate) requires the variation to *name the boundary* — not just assert it. V-05's GATE-0/GATE-1 naming is the operative element.

**C-19 PARTIAL is the floor for DOMAIN-TERMS-first variations without named gate boundaries.** V-01 and V-04 make a valid structural argument but provide no structural marker for the execution boundary. PARTIAL is the correct score: the argument is present but not formalized.

**C-20 requires domain-neutral component names.** V-04's ROOT VERDICT substitution fails the "naive reader" test. Any domain-specific renaming of a required component creates a consultability barrier.

**C-21 candidate surfaced:** V-05's gate completion conditions are explicit pass/fail artifacts per phase. A possible C-21 could require each phase to declare its own completion condition, making every execution boundary independently verifiable.
