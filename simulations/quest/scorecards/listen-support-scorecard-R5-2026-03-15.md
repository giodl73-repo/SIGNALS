## listen-support Round 5 — Scorecard (Rubric v5)

### Baseline Reminder

R4 V-05-class outputs score **98.18** under v5 (C-01–C-17 all PASS, C-18/C-19 both FAIL). R5 objective: close C-18 (3-node ID chain: matrix → commitment row → body headline) and C-19 (standalone vocabulary pre-flight gate before body generation, >= 3 of 5 items, naming artifacts by section name).

---

### Per-Variation Analysis

#### V-01 — Output Format: Compact Cell ID 3-Node Chain

**C-18 (Vocabulary Planning Artifact Linkage):**
- Vocabulary Matrix uses Cell IDs (`SRE-P1`, `Sup-P2`, etc.) as row header identifiers
- STEP 3B commitment table has "Cell ID" column — node 1→2 link present
- Body header template: `## T-NN — {Title} *(Cell: XX-P#)*` — **ID is in the `##` headline**, not a metadata subline — node 3 present
- CONSTRAINT MANIFEST row: "Tickets with Cell ID in commitment table AND body header (C-18) = total ticket count"
- VERIFICATION MANIFEST has three rows labeling nodes 1, 2, 3 explicitly
- 3-node chain complete; scorer reads headline → looks up STEP 3B by Cell ID → looks up matrix by Cell ID — two lookups, zero body text
- **C-18: PASS**

**C-19 (Multi-Criteria Vocabulary Pre-Flight Gate):**
- Standalone `### VOCABULARY PRE-FLIGHT CHECK` section between STEP 3B and STEP 4
- Checks 4 items: (a) matrix completeness, (b) commitment table completeness, (c) phrase-to-cell traceability, (d) phase-register alignment
- Names artifacts: "Vocabulary Matrix", "STEP 3B", "Constraint Manifest"
- Has `PRE-FLIGHT RESULT: [ ALL PASS — proceed to PERFORMANCE MODE ] / [ BLOCKED ]`
- 4 of 5 items >= 3 required; body generation (STEP 4) follows in output order; artifacts named by section name
- Inter-role differentiation (item e) not checked — not required since >= 3 is met
- **C-19: PASS**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Ticket inventory present | PASS | STEP 5 table with all 6 required fields |
| C-02 Persona attribution | PASS | 5 named roles; constraint ≥3 distinct |
| C-03 Persona voice | PASS | PERFORMANCE MODE first-person mandate; no third-person |
| C-04 Gap analysis | PASS | STEP 8 with doc/design/operational, T-NN refs, ≥2 entries each |
| C-05 Volume/severity distribution | PASS | Constraint Manifest: P0 ≤25%, high-vol ≤50% |
| C-06 Ticket count 6–12 | PASS | Constraint Manifest declares 6–12 |
| C-07 Cross-persona coverage | PASS | ≥3 distinct personas; no single >50% |
| C-08 Gap actionability | PASS | Named artifacts per gap entry; ≥2 entries per category |
| C-09 Ticket clustering | PASS | STEP 3 Theme Declaration with underlying failures |
| C-10 Lifecycle/resolution | PASS | STEP 7B Resolution Paths table for high-vol/P0/P1 |
| C-11 Multi-stage structural integrity | PASS | TABLE CHECK + VERIFICATION MANIFEST; cross-referenced T-IDs |
| C-12 Role-phase compound coverage | PASS | STEP 3A cross-matrix; any role ≥3 tickets → ≥2 phases |
| C-13 Phase-calibrated severity | PASS | STEP 2 Phase Map norms; P2/P3 in P1, P0/P1 in P3 |
| C-14 Phase-anchored body voice | PASS | VOCABULARY MATRIX phase-specific register templates |
| C-15 Pre-generation constraint declaration | PASS | CONSTRAINT MANIFEST (pre) + VERIFICATION MANIFEST (post) |
| C-16 Per-ticket vocabulary pre-commitment | PASS | STEP 3B commitment table; body opens with committed phrase |
| C-17 Role-phase vocabulary matrix | PASS | 5 roles × 3 phases = 15 cells; distinct register descriptions |
| **C-18 Vocabulary artifact linkage** | **PASS** | Cell ID at all 3 nodes: matrix header → STEP 3B column → `*(Cell: XX-P#)*` headline |
| **C-19 Pre-flight gate** | **PASS** | 4-item standalone block; names artifacts; blocking declaration; before STEP 4 |

**Score:**
```
Essential:     5/5   → 60.0
Recommended:   3/3   → 30.0
Aspirational:  11/11 → 10.0
Composite:     100.0
```

---

#### V-02 — Lifecycle Emphasis: Standalone 5-Item Blocking Gate

**C-18:**
- VOCABULARY MANIFEST uses VM Row IDs; STEP 3B has VM Row ID column — 2 nodes present
- Body header format: `## T-NN — {Title}` with `- VM Row: {VM Row ID}` in a **metadata subline** below the headline — the `##` headline line itself does NOT contain the VM Row ID
- R5 document gap analysis confirms: "VM Row ID appears in body metadata line but the rubric requires >= 75% of headers to cite the ID as a headline annotation; scorers must still read the metadata line"
- Variation hypothesis explicitly predicts: "C-18 PARTIAL (VM Row ID in metadata line satisfies two of three chain nodes — commitment table cites VM Row ID, body metadata cites VM Row ID, but body headline does not)"
- **C-18: PARTIAL** (2 of 3 chain nodes; body headline does not cite the ID)

**C-19:**
- Standalone `### VOCABULARY PRE-FLIGHT GATE` section between STEP 3B and STEP 4
- 5 items: (a) VOCABULARY MANIFEST completeness, (b) commitment table completeness, (c) phrase-to-manifest traceability, (d) phase-register alignment, (e) inter-role register differentiation
- All 5 items name artifacts by section name ("VOCABULARY MANIFEST", "STEP 3B", "CONSTRAINT MANIFEST")
- Declares `GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 ]` / `GATE: [ CLOSED — ... ]`
- Strongest blocking declaration language of all 5 variations
- **C-19: PASS**

| Criterion | Result |
|-----------|--------|
| C-01–C-17 (inherited from R4 V-05) | All PASS |
| **C-18 Vocabulary artifact linkage** | **PARTIAL** — VM Row ID in metadata subline, not headline |
| **C-19 Pre-flight gate** | **PASS** — 5-item standalone blocking gate; strongest declaration |

**Score:**
```
Essential:     5/5        → 60.0
Recommended:   3/3        → 30.0
Aspirational:  (10 + 0.5) / 11 × 10 = 10.5/11 × 10 → 9.55
Composite:     99.55
```

---

#### V-03 — Phrasing Register: Semantic REG-ID Scheme

**C-18:**
- REGISTER VOCABULARY MATRIX uses REG-IDs (`REG-SRE-SETUP`, `REG-CUST-CONFUSE`, etc.) as row identifiers
- STEP 3B commitment table has "REG-ID" column — node 1→2 link present
- Body header template: `## T-NN — {Title} *(Reg: REG-xxx-TYPE)*` — **REG-ID is in the `##` headline** — node 3 present
- VERIFICATION MANIFEST row: "Bodies with `*(Reg: REG-xxx-TYPE)*` headline annotation (C-18) = total"
- 3-node chain complete: matrix row → STEP 3B REG-ID column → body headline annotation
- Novel property: TYPE label in the ID itself encodes register semantics without lookup
- **C-18: PASS**

**C-19:**
- Standalone `### VOCABULARY PRE-FLIGHT CHECK` section between STEP 3B and STEP 4
- Checks 3 items: (a) Register Vocabulary Matrix completeness, (b) Commitment table completeness, (e) Inter-role register differentiation
- Names artifacts: "Register Vocabulary Matrix", "Constraint Manifest", "STEP 3B"
- Has `PRE-FLIGHT RESULT: [ ALL PASS — proceed ] / [ BLOCKED — revise before continuing ]`
- 3 of 5 items — exactly at minimum threshold
- Items (c) phrase-to-cell traceability and (d) phase-register alignment are NOT checked
- Still satisfies rubric: >= 3 items, artifacts named by section name, before body generation, blocking declaration
- **C-19: PASS** (minimum threshold)

| Criterion | Result |
|-----------|--------|
| C-01–C-17 (inherited from R4 V-05) | All PASS |
| **C-18 Vocabulary artifact linkage** | **PASS** — REG-ID 3-node chain; semantic encoding in ID string |
| **C-19 Pre-flight gate** | **PASS** — 3-item gate; minimum compliance |

**Score:**
```
Essential:     5/5   → 60.0
Recommended:   3/3   → 30.0
Aspirational:  11/11 → 10.0
Composite:     100.0
```

---

#### V-04 — Combined: V-01 Cell IDs + V-02 5-Item Gate

**C-18:**
- VOCABULARY MATRIX with compact Cell IDs (`SRE-P1` format) — same scheme as V-01
- STEP 3B: "Cell ID" column
- Body header template: `## T-NN — {Title} *(Cell: XX-P#)*` — Cell ID in headline
- CONSTRAINT MANIFEST row: "Tickets with Cell ID in commitment table AND body header (C-18) = total ticket count"
- VERIFICATION MANIFEST has 3 rows labeled "C-18 node 1/2/3"
- **C-18: PASS**

**C-19:**
- Standalone `### VOCABULARY PRE-FLIGHT GATE` section between STEP 3B and STEP 4
- 5 items (same as V-02): (a) matrix completeness, (b) commitment table completeness, (c) phrase-to-cell traceability, (d) phase-register alignment, (e) inter-role register differentiation
- Names artifacts: "VOCABULARY MATRIX", "STEP 3B", "CONSTRAINT MANIFEST"
- Declares `GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 ]` / `GATE: [ CLOSED — ]`
- **C-19: PASS**

| Criterion | Result |
|-----------|--------|
| C-01–C-17 | All PASS |
| **C-18 Vocabulary artifact linkage** | **PASS** — Cell ID 3-node chain (V-01 mechanism) |
| **C-19 Pre-flight gate** | **PASS** — 5-item standalone blocking gate (V-02 mechanism) |

**Score:**
```
Essential:     5/5   → 60.0
Recommended:   3/3   → 30.0
Aspirational:  11/11 → 10.0
Composite:     100.0
```

---

#### V-05 — Full Combination (All R4 V-05 + VM Body Headline + 5-Item Gate)

**C-18:**
- VOCABULARY MANIFEST with VM Row IDs (VM-SRE-P1 format) — R4 V-05 mechanism retained
- STEP 3B: "VM Row ID" column — node 1→2 link present (same as R4 V-05)
- **NEW R5**: Body header template: `## T-NN — {Title} *(VM: VM-xxx-P#)*` — **VM Row ID now in the `##` headline**, not the metadata subline
- STEP 3B instruction explicitly describes: "VOCABULARY MANIFEST row (VM Row ID) → STEP 3B commitment row (VM Row ID) → body headline (VM Row ID)"
- CONSTRAINT MANIFEST has dedicated row: "Tickets with VM Row ID in body headline annotation (C-18 node 3) = total ticket count"
- STEP 5 TABLE CHECK includes: "Every ticket body will have `*(VM: VM-xxx-P#)*` headline annotation: Y / N"
- STEP 4 instruction calls out: "Body header MUST include `*(VM: VM-xxx-P#)*` as a headline annotation, completing the C-18 3-node chain: VOCABULARY MANIFEST → STEP 3B → body headline"
- Body generation template (STEP 6) includes explicit TRACEABILITY comment explaining the 2-lookup chain
- STEP 4 also retains: metadata line `- VM Row: {row ID}` as a second reference point
- **C-18: PASS** — strongest implementation: headline annotation + redundant metadata line + constraint manifest pre-commitment + TABLE CHECK + STEP 4 explicit instruction + STEP 6 traceability commentary

**C-19:**
- Standalone `### VOCABULARY PRE-FLIGHT GATE` section between STEP 3B and STEP 4
- 5 items: (1) VOCABULARY MANIFEST completeness, (2) commitment table completeness, (3) phrase-to-manifest traceability, (4) phase-register alignment, (5) inter-role register differentiation with explicit example citation
- All items name artifacts by section name: "VOCABULARY MANIFEST", "STEP 3B", "CONSTRAINT MANIFEST"
- Declares `GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 PERFORMANCE MODE ]`
- Declares `GATE: [ CLOSED — ___ items failed — revise VOCABULARY MANIFEST and/or STEP 3B, then re-run this gate ]`
- STEP 4 instruction explicitly back-references: "Registers MUST differ between roles in the same phase — confirmed by Item 5 of the VOCABULARY PRE-FLIGHT GATE above" — forward-coupling gate output to body generation rule
- **C-19: PASS** — strongest implementation: 5 items + artifact-named + explicit gate OPEN/CLOSED + blocking declaration + forward cross-reference from gate to STEP 4

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-17 (inherited from R4 V-05) | All PASS | |
| **C-18 Vocabulary artifact linkage** | **PASS** | VM Row ID at all 3 nodes including `##` headline `*(VM: VM-xxx-P#)*`; Constraint Manifest pre-commits node 3 count; TABLE CHECK verifies; STEP 6 embeds audit commentary |
| **C-19 Pre-flight gate** | **PASS** | 5-item standalone blocking gate; artifacts named by section; gate output cross-referenced by STEP 4 instruction |

**Score:**
```
Essential:     5/5   → 60.0
Recommended:   3/3   → 30.0
Aspirational:  11/11 → 10.0
Composite:     100.0
```

---

### Scorecard Summary

| Variation | C-18 | C-19 | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|------|------|-----------|-------------|--------------|-----------|------|
| **V-05** | PASS | PASS | 5/5 | 3/3 | 11/11 | **100.0** | **1** |
| **V-04** | PASS | PASS | 5/5 | 3/3 | 11/11 | **100.0** | **2** |
| **V-01** | PASS | PASS | 5/5 | 3/3 | 11/11 | **100.0** | **3** |
| **V-03** | PASS | PASS | 5/5 | 3/3 | 11/11 | **100.0** | **4** |
| V-02 | PARTIAL | PASS | 5/5 | 3/3 | 10+0.5/11 | **99.55** | 5 |

**Ranking by structural guarantee strength (composite-tie-breaker):**

1. **V-05** — VM Row ID in headline (`*(VM: ...)*`) + Constraint Manifest pre-commits node 3 count + TABLE CHECK verifies annotation + STEP 4 instruction cross-references gate Item 5 + STEP 6 template embeds TRACEABILITY commentary explaining the 2-lookup chain. Most layers of enforcement for both C-18 and C-19 simultaneously.
2. **V-04** — Clean Cell ID 3-node chain (compact format) + full 5-item gate. Compositionally independent mechanisms from V-01 and V-02; lower structural overhead than V-05.
3. **V-01** — Cell ID 3-node chain complete; 4-item gate (missing item e: inter-role differentiation). Gate is named and standalone; slightly lighter than V-04/V-05.
4. **V-03** — Semantic REG-ID scheme (novel: TYPE encoded in ID string, register drift visible without matrix lookup); 3-item gate at minimum threshold; missing items c/d (traceability, phase-register alignment) from the gate.
5. **V-02** — Strongest C-19 gate (5-item, GATE: OPEN/CLOSED) but C-18 PARTIAL: VM Row ID stays in metadata subline, not headline; only 2 of 3 chain nodes visible without body text.

---

### Excellence Signals (from V-05 and R5 patterns)

**Signal 1 — Headline-level ID annotation as C-18 node 3:**
Placing the vocabulary ID directly in the `## T-NN — {Title} *(ID)*` headline line — not in a metadata subline — enables the 2-lookup chain without any body text access. The key distinction from R4: R4 V-02/V-05 put the VM Row ID in the metadata line; R5 V-01/V-03/V-04/V-05 promote it to the headline. This single structural move closes C-18.

**Signal 2 — Constraint Manifest pre-commits C-18 node 3 as a structural target:**
V-05 adds "Tickets with VM Row ID in body headline annotation (C-18 node 3) = total ticket count" to the Constraint Manifest. This means C-18 compliance is declared before any content is generated — it becomes a structural pre-commitment, not just a post-hoc audit item. This extends the C-15 two-pass mechanism to cover vocabulary traceability as well.

**Signal 3 — Semantic register encoding in ID string (V-03 novel pattern):**
REG-IDs (`REG-SRE-SETUP`, `REG-CUST-CONFUSE`) encode register type in the identifier itself. A scorer scanning headlines can detect register drift without opening the matrix — if a Phase-1 C-xx ticket shows `*(Reg: REG-CUST-ADVANCED)*`, the TYPE mismatch is visible at the headline. No prior round used self-describing IDs.

**Signal 4 — Gate cross-reference in body generation instruction (V-05):**
STEP 4 instruction includes "Registers MUST differ between roles in the same phase — confirmed by Item 5 of the VOCABULARY PRE-FLIGHT GATE above." This forward-couples the gate output to the body generation rule: Item 5 is not just a check, it becomes a named precondition for generation. If the gate is CLOSED, STEP 4 cannot proceed with this instruction satisfied.

**Signal 5 — Body generation template embeds traceability audit protocol (V-05):**
The STEP 6 template block includes a TRACEABILITY comment explaining the exact 2-lookup chain: "scorer reads the headline, looks up STEP 3B by VM Row ID (node 2), then looks up the VOCABULARY MANIFEST by VM Row ID (node 1) — two lookups, no body text required." This embeds the C-18 audit protocol at the point of use, making the guarantee self-documenting.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Headline-level vocabulary ID annotation in `## T-NN` line (not metadata subline) completes C-18 3-node chain with O(1) body-text-free traceability", "Constraint Manifest pre-commits C-18 node 3 count as a structural target before content generation, extending the C-15 two-pass mechanism to vocabulary traceability", "Semantic register encoding in ID string (REG-SRE-SETUP, REG-CUST-CONFUSE): TYPE label visible at headline scan without matrix lookup — register drift detectable without opening vocabulary artifacts", "Gate output cross-referenced by body generation instruction ('confirmed by Item 5 of the VOCABULARY PRE-FLIGHT GATE above') — forward-coupling gate result to generation rule", "Body generation template embeds C-18 audit protocol as inline TRACEABILITY comment, making the 2-lookup chain self-documenting at point of use"]}
```
