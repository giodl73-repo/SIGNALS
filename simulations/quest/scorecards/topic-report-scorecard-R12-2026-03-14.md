## Round 12 Scoring: `topic-report` (R12)

---

### Base Analysis

All five R12 variations inherit R11 V-04 (D+E+F) verbatim, which scores 37/37 aspirational under v12. Each variation adds content to the base without removing or modifying any existing criterion-satisfying element. No addition breaks a prior criterion. Under v12 all five score identically; the discrimination lives entirely in candidate criteria C-46, C-47, C-48.

---

### Essential Criteria -- C-01 to C-05 (all variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-01 | Artifact written and path echoed | PASS | PASS | PASS | PASS | PASS | PHASE 4 CONFIRM writes `simulations/{topic}/status-{date}.md` and echoes path; G-1 registers the obligation |
| C-02 | Progress table with accurate counts | PASS | PASS | PASS | PASS | PASS | SLOT 1 markdown table template; PHASE 1 DISCOVER builds coverage table; CHECKPOINT freezes values |
| C-03 | Open signals listed with owners | PASS | PASS | PASS | PASS | PASS | SLOT 2 lists `{namespace}/{skill-type} | owner:` for every open signal from CHECKPOINT |
| C-04 | Readiness statement calibrated | PASS | PASS | PASS | PASS | PASS | SLOT 3 writes single sentence from LOCKED BLOCKERS; G-4 registers the calibration obligation |
| C-05 | Recommended next step present | PASS | PASS | PASS | PASS | PASS | SLOT 4 derives skill from most critical BLOCKERS item; G-5 prohibits generic steps |

**Essential score: 5/5 (all)**

---

### Recommended Criteria -- C-06 to C-08 (all variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|---------|
| C-06 | `--format teams` ASCII card | PASS | PASS | PASS | PASS | PASS | Branch B template: four sections, 40-line / 80-char limits, G-6 registered |
| C-07 | Content matches topic-status | PASS | PASS | PASS | PASS | PASS | Single PHASE 1 DISCOVER source, single BLOCKERS block; no divergence path |
| C-08 | Open signals include type and namespace | PASS | PASS | PASS | PASS | PASS | SLOT 2 format: `{namespace}/{skill-type}` explicitly required |

**Recommended score: 3/3 (all)**

---

### Aspirational Criteria -- C-09 to C-45 (all variations)

All five inherit the 37/37 pass from R11 V-04. Criterion-by-criterion confirmation:

| ID | Criterion | All 5 | Key evidence |
|----|-----------|-------|-------------|
| C-09 | Readiness references blocking signals | PASS | BLOCKERS names cited in SLOT 3 sentence via G-7a/G-7b invariants |
| C-10 | Explicit prohibited character enumeration | PASS | G-8 VERIFICATION names backtick, less-than, greater-than by character |
| C-11 | BLOCKERS pre-computation block | PASS | Step 2b emits named BLOCKERS block before any write phase |
| C-12 | Teams card passes character-level scan | PASS | G-8 VERIFICATION instructs explicit scan; Branch B template uses `+ - |` only |
| C-13 | Bidirectionality as two named invariants | PASS | G-7a COMPLETENESS and G-7b EXCLUSIVITY are separately named and verifiable |
| C-14 | Branch sealing instruction | PASS | [RULE BRANCH-SEAL] at dispatch; [RULE BRANCH-SEAL-B] at Branch B entry |
| C-15 | BLOCKERS LOCK directive | PASS | Step 2d: "The BLOCKERS list is now frozen and final. No additions, removals, or revisions..." |
| C-16 | In-render verification scan | PASS | LAYER 3 VERIFY executes G-7a COMPLETENESS SCAN + G-7b EXCLUSIVITY SCAN before write |
| C-17 | Rules co-located at governed positions | PASS | [RULE G-7a/G-7b] at SLOT 3; [RULE G-9 INERTIA] at SLOT 4; [RULE SLOT1/2-SOURCE] at their slots |
| C-18 | Three-layer co-location at write point | PASS | === THREE-LAYER WRITE POINT (BRANCH A) ===: DECLARE + ANCHOR (LOCKED ref) + VERIFY all present |
| C-19 | Contract label chaining (register -> annotation -> scan header) | PASS | G-7a/G-7b assigned at register, propagated to [RULE G-7a/G-7b] annotations, G-7a/G-7b SCAN headers |
| C-20 | Worked examples in [RULE] annotations | PASS | correct/violation pairs inside [RULE G-7a COMPLETENESS], [RULE G-7b EXCLUSIVITY], [RULE G-9 INERTIA] |
| C-21 | Inertia framing at NEXT STEP | PASS | "Leaving this open holds the topic at Not Ready." stall cost in G-9 INERTIA rule and example |
| C-22 | Explicit THREE-LAYER WRITE POINT header | PASS | === THREE-LAYER WRITE POINT (BRANCH A) === enumerates LAYER 1/2/3 before model encounters any layer |
| C-23 | Criterion-tagged violation examples | PASS | "(omits review/design -- G-7a violation)" and "(no stall cost -- G-9 INERTIA / C-21 violation)" |
| C-24 | Contract label chaining for single-position invariants | PASS | G-9 INERTIA at register -> [RULE G-9 INERTIA] at SLOT 4 |
| C-25 | Branch B independent THREE-LAYER header | PASS | === THREE-LAYER WRITE POINT (BRANCH B) === with LAYER 1/2/3 inside Branch B only |
| C-26 | Dual-chain co-presence at annotation slot | PASS | [RULE G-9 INERTIA] (C-24) + "(G-9 INERTIA / C-21 violation)" (C-23) at same annotation |
| C-27 | Dual-branch three-layer closure | PASS | Both C-22 (main) and C-25 (Branch B) headers present |
| C-28 | Dual-identifier violation example | PASS | "(no stall cost -- G-9 INERTIA / C-21 violation)" -- register label + rubric ID in one fragment |
| C-29 | Explicit named recovery directive in Branch B header | PASS | "re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A" |
| C-30 | Slot-indexed contract register | PASS | G-1 [PHASE 4], G-2 [SLOT 1 / BRANCH A], G-7 [SLOT 3 / BRANCH A | BRANCH B], G-9 INERTIA [SLOT 4 / ...] |
| C-31 | Branch B SLOT 4 complete attention-recovery envelope | PASS | C-28 + C-29 both present |
| C-32 | Register-to-violation closed traceability loop | PASS | C-28 + C-30 both present |
| C-33 | Branch B forward-to-procedural navigation coordination | PASS | C-29 + C-30 both present |
| C-34 | Explicit named recovery directive in main-branch header | PASS | "re-read this BRANCH A header... Prohibited: cross-reference Branch B instructions from this path" |
| C-35 | Branch-qualified slot indexing | PASS | G-7 [SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]; G-9 INERTIA [SLOT 4 / BRANCH A | BRANCH B] |
| C-36 | Explicit temporal coordination statement | PASS | Coordination line: "branch-qualified slot annotations...are the reference for this recovery directive (recovery phase)" |
| C-37 | Main-branch SLOT 4 complete attention-recovery envelope | PASS | C-34 + C-35 both present |
| C-38 | Named recovery directive with declared temporal role | PASS | C-34 + C-36 both present |
| C-39 | Branch-qualified forward map with declared planning role | PASS | C-35 + C-36 both present |
| C-40 | Criterion-tagged contamination consequence | PASS | "SLOT 3 contamination consequence:" line in Branch A header; consequence text names G-4/C-13/C-16 violations |
| C-41 | Format-type-qualified Branch B register entries | PASS | G-7 [... BRANCH B (one card row, no markdown)]; G-9 INERTIA [... BRANCH B (two card rows, no markdown)] |
| C-42 | Temporal-role annotation in register header | PASS | === CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] === |
| C-43 | Consequence-grounded contamination guard with format-navigable Branch B entries | PASS | C-40 + C-41 both present |
| C-44 | Contamination consequence with declared temporal context | PASS | C-40 + C-42 both present |
| C-45 | Format-type-qualified forward map with declared planning role | PASS | C-41 + C-42 both present |

**Aspirational score: 37/37 (all)**

---

### Candidate Criteria (C-46, C-47, C-48) -- Not yet in v12 denominator

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-46: Criterion tag `[C-40]` on contamination consequence label | PASS | FAIL | PASS | PASS | FAIL | V-01/V-03/V-04: label reads `SLOT 3 contamination consequence [C-40]:`; V-02/V-05: label reads `SLOT 3 contamination consequence:` -- ID appears only inside consequence prose, not on label |
| C-47: Format-type qualifiers on Branch A register entries | FAIL | PASS | PASS | PASS | FAIL | V-02/V-03/V-04: G-2 `(markdown table, four columns:...)`, G-3 `(markdown list, one item per signal)`, G-4/G-5 `(markdown sentence, prose)`; V-01/V-05: G-2/G-3 carry branch-qualified slot annotations only, no format-type qualifier |
| C-48: Named contamination format-vector declaration | FAIL | FAIL | FAIL | PASS | FAIL | V-04 only: `Contamination format-vector [C-48]:` line explicitly names Branch B format-type constraints as structural contamination mechanism; all other variations have C-34+C-41 co-present but not declared as a joint property |

**V-01=V-02 tie confirmed**: both gain exactly one candidate criterion above neutral. C-46 and C-47 are structurally independent (different phases, different positions) -- no composite C-49 can be confirmed from R12 alone; both approaches produce the same marginal gain.

---

### Composite Scores Under v12

```
Scoring formula:
  essential_pass    = 5/5 = 1.0
  recommended_pass  = 3/3 = 1.0
  aspirational_pass = 37/37 = 1.0

composite = (1.0 * 60) + (1.0 * 30) + (1.0 * 10) = 100.0
```

| Variation | Essential | Recommended | Aspirational | Composite v12 | Candidate count |
|-----------|-----------|-------------|--------------|---------------|-----------------|
| V-04 (G+H+I) | 5/5 | 3/3 | 37/37 | **100.0** | 3 (C-46, C-47, C-48) |
| V-03 (G+H) | 5/5 | 3/3 | 37/37 | **100.0** | 2 (C-46, C-47) |
| V-01 (G only) | 5/5 | 3/3 | 37/37 | **100.0** | 1 (C-46) |
| V-02 (H only) | 5/5 | 3/3 | 37/37 | **100.0** | 1 (C-47) |
| V-05 (neutral) | 5/5 | 3/3 | 37/37 | **100.0** | 0 |

**All five tie at 100.0 under v12.** Ranking is determined by candidate criteria count: V-04 > V-03 > V-01 = V-02 > V-05.

---

### Projected v13 Scores (if C-46, C-47, C-48 confirmed; denominator /40)

| Variation | v12 | C-46 | C-47 | C-48 | Projected v13 | Notes |
|-----------|-----|------|------|------|---------------|-------|
| V-04 (G+H+I) | 100.0 | + | + | + | 40/40 = 100.0 | All confirmed |
| V-03 (G+H) | 100.0 | + | + | -- | 39/40 = 99.7 | Fails C-48 |
| V-01 (G only) | 100.0 | + | -- | -- | 38/40 = 99.5 | Fails C-47, C-48 |
| V-02 (H only) | 100.0 | -- | + | -- | 38/40 = 99.5 | Fails C-46, C-48; tie with V-01 |
| V-05 (neutral) | 100.0 | -- | -- | -- | 37/40 = 99.2 | Baseline |

*Composite with /40 denominator: (5/5 * 60) + (3/3 * 30) + (N/40 * 10)*

---

### Excellence Signals from V-04

**Signal 1 -- Criterion-tagged consequence label extends traceability to the recovery-phase directive label itself.** `SLOT 3 contamination consequence [C-40]:` adds `[C-40]` at the label position, creating a three-level contamination-traceability chain: (1) register prohibition at planning phase (G-7/G-9 entries); (2) consequence prose text at recovery phase (names C-04/C-13/C-16 inline); (3) label tag `[C-40]` at the label position itself. A model encountering the consequence line reaches C-40's definition from the label without parsing the embedded prose IDs. This is the consequence-level analogue of C-23's criterion-tagged violation pattern, applied one structural level higher (label vs. violation text).

**Signal 2 -- Symmetric format pre-delivery closes the default-path planning-phase format-ambiguity gap.** C-41 gave the model format-type constraints for Branch B positions at register-read time; C-47 extends this symmetrically to Branch A. After V-04, a model reads the register and knows both the slot destination AND the structural format for every write position on both execution paths before encountering any branch-specific template content. The planning-phase register is now a complete format specification, not just a slot map.

**Signal 3 -- Named contamination format-vector converts C-34+C-41 co-presence into a declared joint property.** The `Contamination format-vector [C-48]:` line makes explicit what was previously only structural: the Branch B format-type constraints (from C-41, established at planning time) are the specific mechanism by which C-34's cross-branch prohibition fires. The three-point contamination arc -- (1) format-type declarations at planning phase, (2) named format-vector as contamination mechanism, (3) named consequence at recovery phase -- is now fully navigable from any entry point. Co-presence of C-34 and C-41 was previously deducible by reading both; V-04 makes it criterion-tagged and structurally declared.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["criterion-tagged consequence label creates recovery-phase criterion-traceability at the label position, extending C-23 tagging pattern from violation text to consequence label", "symmetric format pre-delivery extends planning-phase format-type annotation from Branch B (C-41) to Branch A, making the register a complete format specification for all execution paths at register-read time", "named contamination format-vector converts structural co-presence of prohibition (C-34) and format declarations (C-41) into a declared joint property with criterion tag, making the contamination mechanism navigable from planning-phase, mechanism, and consequence positions independently"]}
```
