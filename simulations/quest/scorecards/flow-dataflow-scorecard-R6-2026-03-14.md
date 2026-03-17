## flow-dataflow — Round 6 Scoring

> Only V-01 is provided with a full prompt. V-02–V-05 are described by axis only (no prompt text). Scoring below covers V-01 in full; V-02–V-05 are noted as **not provided**.

---

## V-01 — Role Sequence (Commerce → Finance → Operations)

### Essential (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | STAGE TRACE defines POS Terminal → IMS → ERP Finance Ledger with schema in/out per stage. Every item has an unbroken origin chain. |
| C-02 | Boundary error handling | **PASS** | BOUNDARY CHECK format mandates `Error handling: [mechanism — or "no handling — see [A-06]"]`. Silence structurally impossible. |
| C-03 | Data loss point identification | **PASS** | Each STAGE block requires `Loss point: [one concrete failure scenario — not "errors may occur"]`. Generic phrasing explicitly prohibited. |
| C-04 | Schema state at each stage | **PASS** | Each STAGE block requires `Schema in:` and `Schema out:` with explicit instruction to note name or type changes. |

**Essential score: 4 / 4 → 60 pts**

---

### Recommended (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-05 | Latency characterization | **PASS** | STAGE block requires `Latency: [value, range, or characterization: real-time / near-real / batch / daily]` for every stage. |
| C-06 | Stale data windows | **PASS** | [A-05] STALE ANALYSIS requires normal-operation AND failure-mode staleness windows separately, with [A-04] elapsed totals cited. |
| C-07 | Domain framing | **PASS** | [A-01] locks entity names (SKU, POS transaction record, stock-on-hand quantity, store cache entry). STAGE and BOUNDARY blocks require named entity per block. |

**Recommended score: 3 / 3 → 30 pts**

---

### Aspirational (10 pts) — 17 criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-08 | Recovery prescriptions | **PASS** | [A-06] requires named recovery per loss point and per "no handling" annotation. Explicit formula: "Fall back to [A-02] if [condition]" closes the loop with C-15. |
| C-09 | Pattern trade-off analysis | **PASS** | [A-08] requires naming one alternative pattern with ≥2 dimensions, with [A-02] as comparison anchor. |
| C-10 | Pre-trace domain context gate | **PASS** | [A-01] DOMAIN CONTEXT written first, locking entity names, downstream consumer (Finance), and cadence (18:00 close). Stage and stale content required to reuse these terms verbatim. |
| C-11 | Interleaved boundary gates | **PASS** | SC-2: "Write BC-1 before Stage 2. Write BC-2 before Stage 3." Applied inline via "Apply SC-2 strictly" inside Role 1 instructions. |
| C-12 | Domain entity exposure per boundary | **PASS** | BOUNDARY CHECK block has required field `Domain entity at boundary: [named entity from [A-01] — not "data" or "records"]`. |
| C-13 | Pre-declared staleness contract | **PASS** | [A-01] declares the staleness SLA before Stage 1. [A-05] derives stale rows by evaluating elapsed totals against this threshold — not post-hoc assertion. |
| C-14 | Additive elapsed time calculation | **PASS** | SC-3 mandates `Elapsed total (cumulative):` inside each BOUNDARY CHECK block, computed as sum of all prior latencies + boundary overhead. [A-05] cites [A-04] for this total. |
| C-15 | Incumbent baseline | **PASS** | [A-02] INCUMBENT BASELINE uses ≥1 entity from [A-01]. [A-06] mandates "Cite [A-02] at least once" in recovery prescriptions, closing the comparison loop per C-15 definition. |
| C-16 | Cross-role reference chain | **PASS** | SC-1 requires every role to open with `Citing:` line listing [A-xx] tokens built on. Role 2 cites [A-01], [A-04], [A-05]; Role 3 cites [A-01], [A-02], [A-06], [A-07]. Prose back-references explicitly prohibited. |
| C-17 | Immutability declaration | **PASS** | SC-5: "No role may revise it after that point." [A-01] must contain verbatim: "This threshold is fixed. No role may revise it after Stage 1 is written." Prohibition is explicit, not just early-declaration. |
| C-18 | Incremental boundary elapsed computation | **PASS** | SC-3: "Compute this field inside the BOUNDARY CHECK block — it may not be deferred to STALE ANALYSIS." Cumulative total is a structural side effect of writing each boundary block. |
| C-19 | Machine-verifiable citation convention | **PASS** | [A-xx] token form declared in ARTIFACT REGISTRY. SC-1 enforces uniform application. Every citation target reachable by token match. |
| C-20 | Stage-write progression gate | **PASS** | SC-2: "Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and Stage N+1 is fully complete with all four required fields present." Named gate condition explicitly stated. |
| C-21 | Binary freshness verdict per boundary | **PASS** | SC-4: "Each BOUNDARY CHECK must include 'Freshness verdict: FRESH \| STALE' derived by comparing the cumulative elapsed total against the threshold declared in [A-01]." Boundary without verdict explicitly fails. |
| C-22 | Formal pre-declared registry table | **PASS** | ARTIFACT REGISTRY is a 4-column table (Token, Artifact, Owner, Description) enumerating [A-01]–[A-10] before any role output. Includes phase gate artifacts as first-class rows. Every citation target must appear as a row. |
| C-23 | Phase gate self-verification checklists | **PASS** | [A-09] (post Role 1) and [A-10] (post Role 2) are model-produced checklists with named criterion identifiers (C-01, C-02, SC-2, SC-3, SC-4, SC-5, SC-1) and tick-or-fail format. Role N+1 may not begin until all items are ✓. |
| C-24 | Upfront constraint section with inline callback syntax | **PASS** | STRUCTURAL CONSTRAINTS section (SC-1–SC-5) declared before any role. Role instructions callback by ID: "Per SC-5, append:", "Apply SC-2:", "Per SC-2:", "Per SC-3:", "Per SC-4:". Phase gate checklists reference SC-x identifiers. Two-level enforcement is complete. |

**Aspirational score: 17 / 17 → 10 pts**

---

### V-01 Composite

```
Essential passed:     4 / 4   =>  (4 / 4)  * 60 = 60
Recommended passed:   3 / 3   =>  (3 / 3)  * 30 = 30
Aspirational passed:  17 / 17 =>  (17 / 17) * 10 = 10
                                   Composite      = 100

Golden: ✓ (all 4 essential pass AND composite >= 80)
```

---

## V-02–V-05: Not Provided

These variations are described by axis (Output Format, Phrasing Register, Role Sequence + Inertia Framing, Output Format + Lifecycle Emphasis) but no prompt text was included in this scoring run. They cannot be scored.

---

## Excellence Signals from V-01

**1. Phase gate artifacts registered as first-class rows in the ARTIFACT REGISTRY**
[A-09] and [A-10] (the checklists themselves) appear as rows in the pre-role registry table. This makes the verification structure enumerable alongside data artifacts — any evaluator can confirm all checklist outputs are pre-declared and account for them.

**2. Non-natural role ordering as a structural stress test for C-16**
Commerce-first forces Finance (Role 2) and Operations (Role 3) to cite Commerce's stale SLA and incumbent baseline via [A-xx] tokens rather than re-declare or infer. The unnatural ordering surfaces citation laziness if it exists.

**3. "Fall back to [A-02] if [condition]" recovery formula closes the C-15 loop explicitly**
Instead of loosely requiring [A-02] to be referenced somewhere, [A-06] mandates the exact formula, ensuring the incumbent baseline appears in a named recovery action — not merely in a trade-off narrative.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase gate artifacts registered as first-class rows in the pre-role registry table — verification structure becomes enumerable alongside data artifacts", "non-natural domain role ordering as structural stress test for cross-role citation — forces downstream roles to cite upstream tokens rather than infer shared context", "explicit recovery formula anchoring incumbent baseline — named formula in recovery prescriptions closes the C-15 comparison loop without relying on prose proximity"]}
```
