## Quest Score — topic-retro R17

**Rubric:** v15 | **Denominator:** 152 (non-AMEND standard)

---

### Baseline

R16-V-05 under v14 = 126/148. Under v15 with two new criteria:
- **C-40** PARTIAL (1 pt): manifest topology present but derivation not stated per section
- **C-41** PARTIAL (1 pt): gate uses "Backward Recovery Table A: PRESENT" — truncated name, missing `-- WRONG VERDICT INVENTORY` subtitle

**R16-V-05 under v15 baseline: 128/152 = 84.2%**

---

### C-40 and C-41 Verdicts

| Variation | C-40 | C-41 | Rationale |
|-----------|------|------|-----------|
| **V-01** | **FULL (2)** | PARTIAL (1) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: filter WHERE Verdict = WRONG]` section headers state manifest as source; gate unchanged (truncated Table A name) |
| **V-02** | PARTIAL (1) | **FULL (2)** | No added derivation declarations; gate becomes named-artifact assertion table with `BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY: present as named structural table` |
| **V-03** | **FULL (2)** | PARTIAL (1) | Inline parentheticals `(rows from AUDIT MANIFEST where Verdict = WRONG)` satisfy "stated" per C-40 rubric example phrasing; per-role contracts don't use full ALL-CAPS artifact names |
| **V-04** | **FULL (2)** | **FULL (2)** | V-01 headers + V-02 gate; both mechanisms occupy distinct structural positions with zero interference |
| **V-05** | **FULL (2)** | **FULL (2)** | V-04 + AUDIT MANIFEST `Derived Views` column (forward citation) + PRE-CONTRACT `Manifest column` field |

---

### Composite Scores

| Variation | Essential | Recommended | Aspiration (base) | C-40 | C-41 | Unique | Total | % |
|-----------|-----------|-------------|-------------------|------|------|--------|-------|---|
| V-01 | 60 | 30 | 36 | 2 | 1 | 0 | **129/152** | **84.9** |
| V-02 | 60 | 30 | 36 | 1 | 2 | 0 | **129/152** | **84.9** |
| V-03 | 60 | 30 | 36 | 2 | 1 | 0 | **129/152** | **84.9** |
| V-04 | 60 | 30 | 36 | 2 | 2 | 0 | **130/152** | **85.5** |
| **V-05** | 60 | 30 | 36 | 2 | 2 | **+4** | **134/152** | **88.2** |

*Aspiration base = 20 (common) + 16 (R16-V-05 unique) = 36 pts*

---

### V-05 Unique (+4 pts)

| New Pattern | Score | Why |
|-------------|-------|-----|
| Bidirectional manifest citation | +2 | `Derived Views` column in manifest (forward: manifest → downstream) + `[DERIVED FROM: ...]` in section headers (backward: downstream → manifest). Prior variations only had the backward direction. |
| PRE-EXECUTION CONTRACT as manifest navigation index | +2 | `Manifest column` field maps each structural commitment to the exact AUDIT MANIFEST column that sources it — auditor navigation index before execution, not just a what-will-happen declaration. |

---

### Ranking

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | **V-05** | 134/152 (88.2%) |
| 2 | **V-04** | 130/152 (85.5%) |
| 3 (tie) | **V-01, V-02, V-03** | 129/152 (84.9%) |

---

```json
{"top_score": 88, "all_essential_pass": true, "new_patterns": ["Bidirectional manifest citation: AUDIT MANIFEST gains a Derived Views column declaring which downstream table(s) each row feeds (forward citation), while downstream section headers declare [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] (backward citation) — a complete bidirectional audit trail navigable from any starting point; manifest becomes a consistency verification surface, not just a primary data source", "PRE-EXECUTION CONTRACT as manifest navigation index: contract gains a Manifest column field mapping each structural commitment to the exact AUDIT MANIFEST column that sources it, transforming the contract from a prospective what-will-happen declaration into a where-in-the-manifest-to-find-it navigation index usable before and after execution"]}
```
ward check: C + W = N? YES / NO -- must be YES before proceeding` |
| N/A signals separated from denominator | PASS (2 each) | `Signals without directional predictions: Verdict = N/A; excluded from accuracy counts` |
| Echo: NONE valid with stated reason | PASS (2 each) | `Echo: NONE (valid result — state reason)` in Phase 3 |
| Section ordering enforced (named constraint) | PASS (2 each) | PHASE seals enforce sequence; Phase 2 SEAL must clear before Phase 3 begins |
| Disqualification gate has exactly three named checks | PASS (2 each) | Three gate rows: (1) not WRONG restatement, (2) not named risk, (3) not in signal bounds |
| Gap priority field (HIGH/MED/LOW) | PASS (2 each) | Priority column in Phase 4 gap table |

**Base aspiration subtotal: 20 pts (common to all variations)**

---

#### R16-V-05 Unique Aspiration — Inherited by All R17 Variations (16 pts)

These criteria were earned by R16-V-05's manifest topology + phase gate architecture and are
present in all five R17 variations:

| Criterion (inferred) | All Variations | Evidence |
|----------------------|---------------|----------|
| Single manifest table as primary artifact | PASS (2 each) | Phase 1 builds AUDIT MANIFEST with all 7 named columns |
| Backward recovery as derived view (no re-authoring) | PASS (2 each) | Phase 2 produces Table A by filtering AUDIT MANIFEST for WRONG rows |
| Coverage table as derived view | PASS (2 each) | Phase 2 PHASE COVERAGE TABLE derived by grouping manifest by Namespace |
| Echo input as derived view | PASS (2 each) | Phase 3 Echo Input filtered from manifest WHERE Echo Candidate? = YES |
| Data incoherence between sections structurally prevented | PASS (2 each) | Nothing in Phase 2–4 is independently authored; all sections are manifest views |
| Phase exit checklist present with named structural conditions | PASS (2 each) | PHASE 1 SEAL, PHASE 2 SEAL, PHASE 3 SEAL, PHASE 4 SEAL present with named checkbox conditions |
| Gate asserts named structural artifact (partial name) | PASS (2 each) | PHASE 2 SEAL includes `BACKWARD RECOVERY TABLE A: row count = WRONG-count from AUDIT MANIFEST` |
| Manifest topology + phase gate = compounded enforcement | PASS (2 each) | Derivation chain (Phase 1→2→3) and phase seals coexist; neither is independently bypassable |

**R16-V-05 unique aspiration subtotal: 16 pts (inherited by all R17 variations)**

**Total base before C-40 / C-41: 60 + 30 + 20 + 16 = 126 pts**

---

#### New Criteria — C-40 and C-41 (2 pts each, 4 pts total)

**C-40 — Manifest-First Derivation (All Downstream Sections as Views)**

Scoring key:
- FULL (2 pts): manifest explicitly named as derivation source AND derivation operation stated — whether via section-header `[DERIVED FROM: ...]` syntax or inline parenthetical naming the manifest as source with the filter/group operation.
- PARTIAL (1 pt): manifest exists, tables are derived, but derivation relationships are structurally evident rather than stated (no naming of manifest as source in each section).
- FAIL (0 pts): downstream sections independently authored.

| Variation | C-40 Result | Evidence |
|-----------|-------------|----------|
| **V-01** | **FULL (2)** | Each section header carries `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: filter WHERE Verdict = WRONG]` — manifest named as source, operation stated, per table |
| **V-02** | **PARTIAL (1)** | Manifest topology inherited from R16-V-05 but no added derivation declarations; derivation structurally evident (tables are views) but manifest not named as source in each section |
| **V-03** | **FULL (2)** | Inline parentheticals `(rows from AUDIT MANIFEST where Verdict = WRONG)` state the manifest as derivation source and the filter operation — satisfies "stated" per C-40 rubric example phrasing |
| **V-04** | **FULL (2)** | V-01 `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` section headers; manifest named in every downstream section |
| **V-05** | **FULL (2)** | V-04 section headers AND AUDIT MANIFEST itself gains `Derived Views` column naming which downstream table(s) each row feeds — dual-direction derivation declaration |

**C-41 — Named-Criteria Phase Gate (Aspiration Criteria Asserted by Structural Artifact Name)**

Scoring key:
- FULL (2 pts): phase exit gate asserts at least one aspiration criterion artifact by its FULL structural artifact name as it appears in the skill body (e.g., `BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY: present as named structural table` — including subtitle).
- PARTIAL (1 pt): gate names artifacts but truncated (without subtitle), or gate describes intent without exact artifact names, or gate references only essential/recommended criteria artifacts.
- FAIL (0 pts): no phase gate.

The critical distinction: `Backward Recovery Table A: PRESENT` = PARTIAL (partial name, missing
`-- WRONG VERDICT INVENTORY` subtitle); `BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY:
present as named structural table` = FULL.

| Variation | C-41 Result | Evidence |
|-----------|-------------|----------|
| **V-01** | **PARTIAL (1)** | Gate unchanged from R16-V-05: `BACKWARD RECOVERY TABLE A: row count = WRONG-count from AUDIT MANIFEST` — names artifact but omits `-- WRONG VERDICT INVENTORY` subtitle; truncated name = PARTIAL |
| **V-02** | **FULL (2)** | Phase 2 exit gate is a named-artifact assertion table with full structural names: `BACKWARD RECOVERY TABLE A -- WRONG VERDICT INVENTORY: present as named structural table` — exact full name including subtitle |
| **V-03** | **PARTIAL (1)** | Per-role exit contracts say "role may not proceed until named outputs exist" — names outputs but without full ALL-CAPS structural artifact names including subtitles; role-based framing doesn't elevate to FULL |
| **V-04** | **FULL (2)** | V-02 named-artifact assertion table: full structural names with subtitles asserted in gate block |
| **V-05** | **FULL (2)** | V-04 gate + PRE-EXECUTION CONTRACT gains `Manifest column` field linking each structural commitment to exact AUDIT MANIFEST column — gate assertions anchored to manifest column names |

---

#### Variation-Unique Aspiration Contributions

**V-01, V-02, V-03** — no unique aspiration contributions beyond C-40/C-41 changes.

- V-01's `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` syntax is captured by C-40 FULL.
- V-02's named-artifact assertion table format is captured by C-41 FULL.
- V-03's per-role framing tests an architectural alternative (phase-numbered vs. role-obligation), but doesn't add structural criteria beyond C-40 FULL; C-36 (phase-level isolation) is already scored in the base.

**V-04** — no unique aspiration contributions beyond C-40 FULL + C-41 FULL.

Zero-interference between mechanisms (C-40 in section headers, C-41 in gate block) is demonstrated but is an architectural property of the design, not a scoreable new criterion beyond the compound enforcement already in the base (R16-V-05 unique item 8).

**V-05 — Bidirectional Manifest Citation + PRE-CONTRACT Navigation Index (+4 pts)**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Bidirectional manifest citation: forward (manifest → downstream) and backward (downstream → manifest) | PASS (2) | AUDIT MANIFEST `Derived Views` column declares which downstream table each row feeds (forward); section headers declare `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` (backward). Prior variations only had backward direction. |
| PRE-EXECUTION CONTRACT as manifest navigation index: each commitment mapped to exact manifest column | PASS (2) | PRE-EXECUTION CONTRACT `Manifest column` field maps each structural guarantee to the exact AUDIT MANIFEST column that sources it — auditor navigation index before execution begins. No prior variation linked contract commitments to manifest columns. |

---

## Composite Score Table

| Variation | Essential | Recommended | Aspiration (base) | C-40 | C-41 | Unique | **Total** | **/152** | **%** |
|-----------|-----------|-------------|-------------------|------|------|--------|-----------|----------|-------|
| V-01 | 60 | 30 | 36 | 2 | 1 | 0 | **129** | 129/152 | **84.9** |
| V-02 | 60 | 30 | 36 | 1 | 2 | 0 | **129** | 129/152 | **84.9** |
| V-03 | 60 | 30 | 36 | 2 | 1 | 0 | **129** | 129/152 | **84.9** |
| V-04 | 60 | 30 | 36 | 2 | 2 | 0 | **130** | 130/152 | **85.5** |
| V-05 | 60 | 30 | 36 | 2 | 2 | 4 | **134** | 134/152 | **88.2** |

*Aspiration (base) = 20 (common) + 16 (R16-V-05 unique inherited) = 36*

---

## Ranking

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|-------------------|
| 1 | **V-05** | 134/152 (88.2%) | C-40 FULL + C-41 FULL + bidirectional manifest citation + PRE-CONTRACT nav index |
| 2 | **V-04** | 130/152 (85.5%) | C-40 FULL + C-41 FULL — demonstrates both new criteria simultaneously without structural interference |
| 3 (tied) | **V-01** | 129/152 (84.9%) | C-40 FULL via explicit section-header `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declarations |
| 3 (tied) | **V-02** | 129/152 (84.9%) | C-41 FULL via named-artifact assertion table with full subtitle names in gate block |
| 3 (tied) | **V-03** | 129/152 (84.9%) | C-40 FULL via inline parentheticals — lower structural overhead, equivalent manifest naming |

**Tie-breaking note (V-01, V-02, V-03):** All three achieve exactly one new criterion at FULL.
V-01 and V-03 both achieve C-40 FULL by different mechanisms (explicit headers vs. inline
parentheticals) — structurally equivalent for C-40, though V-01's header syntax is more
formally machine-scannable. V-02 achieves C-41 FULL. No tie-breaking on score.

---

## Excellence Signals — V-05

**Pattern 1: Bidirectional Manifest Citation**

V-05 extends the manifest from a passive data source to an active navigation hub by adding a
`Derived Views` column. Each manifest row now declares which downstream table(s) it will feed.
This is the forward citation direction: AUDIT MANIFEST → downstream. Combined with the backward
citation from section headers (`[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]`), V-05 achieves
a complete bidirectional audit trail.

An auditor can start from any manifest row and navigate to the downstream table(s) it populates
(forward direction via `Derived Views` column), or start from any downstream table and navigate
back to the manifest rows that source it (backward direction via `DERIVED FROM` header). All
prior variations (V-01 through V-04, R16-V-05) had only the backward direction. Bidirectional
citation means no manifest row can be added or modified without the derivation impact being
visible in both directions simultaneously — the manifest becomes a consistency verification
surface, not just a primary table.

This goes beyond what C-40 requires (C-40 requires downstream sections to name the manifest
as their source). The manifest also declares its own downstream destinations — the derivation
graph is embedded in both the source and the views.

**Pattern 2: PRE-EXECUTION CONTRACT as Manifest Navigation Index**

V-05 adds a `Manifest column` field to the PRE-EXECUTION CONTRACT table, mapping each
structural commitment (what will be produced) to the exact AUDIT MANIFEST column that sources
it. Before the manifest is built, an auditor reading the contract knows precisely where in the
manifest to look for each committed output.

This transforms the PRE-EXECUTION CONTRACT's role. In all prior variations, the contract was
a "what I commit to produce" declaration — prospective, structural, but self-contained. In V-05,
the contract is a pre-execution map of the manifest's column structure: it declares not just
what will exist but where in the primary table to find the authority for each commitment.
Scorers and auditors can use the contract as a navigation index before and after execution:
before execution to understand the manifest structure that will be built; after execution to
verify that each commitment resolves to a specific manifest column.

This pattern is structurally independent from C-41 (which requires the gate to assert
aspiration criteria artifacts). The PRE-EXECUTION CONTRACT navigation index operates at the
beginning of the skill run; the C-41 gate operates at phase exit. Both cite manifest structure,
but from different positions in the execution flow.

---

```json
{"top_score": 88, "all_essential_pass": true, "new_patterns": ["Bidirectional manifest citation: AUDIT MANIFEST gains a Derived Views column declaring which downstream table(s) each row feeds (forward citation), while downstream section headers declare [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] (backward citation) — a complete bidirectional audit trail navigable from any starting point; manifest becomes a consistency verification surface, not just a primary data source", "PRE-EXECUTION CONTRACT as manifest navigation index: contract gains a Manifest column field mapping each structural commitment to the exact AUDIT MANIFEST column that sources it, transforming the contract from a prospective what-will-happen declaration into a where-in-the-manifest-to-find-it navigation index usable before and after execution"]}
```
