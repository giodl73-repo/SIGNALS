---

# Quest Score — trace-permissions — Round 18

**Rubric:** v18 (42 criteria — C-01 through C-50 effective; C-48/C-49/C-50 new this round)
**Denominator:** 42
**State entering R18:** All five variations start from R17-V-05's architecture. C-01 through C-47 are confirmed PASS for all variations — each inherits the four-statement NON-OVERLAP DECLARATION (C-43/C-46/C-47), Phase 0 bilateral mandate (C-44), Phase 3 bilateral echo (C-45), closed authorship loop (C-21), Registry-preamble double-anchor (C-23), and full phase execution attestation (C-22). Differential scoring below covers only the three new criteria.

---

## Inherited Criteria — C-01 through C-47 (all variations)

All five variations carry R17-V-05's architecture unchanged. Evidence for key inherited criteria:

| Criterion Group | Evidence | Status (all V) |
|----------------|----------|----------------|
| C-01 to C-05 (Essential) | TABLE_1–TABLE_5 fully present; SE-0 ordering; FLS null-case stated; escalation vectors all checked | PASS |
| C-06 to C-08 (Recommended) | Dataverse-native terms; sharing rule conflict analysis; remediation specificity | PASS |
| C-09 to C-23 (Aspirational tier 1) | Schema Registry (C-20), CA-first authorship (C-19/C-21), double-anchor rows (C-23), phase labels in output body (C-22), quad-lock CEM (C-18) | PASS |
| C-24 to C-36 (Aspirational tier 2) | Preamble axis declaration A-1/A-2/A-3 (C-34); SE-4 STRUCTURED CLOSE TABLE_4 cross-reference CA-1.9 (C-35); TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION in Verdict (C-36) | PASS |
| C-37 to C-47 (Aspirational tier 3) | Attestation cross-link mandate (C-37); bilateral CEM sub-clause structure (C-38/C-40/C-44/C-45); four-statement NON-OVERLAP with CA-1.6 CS-side complement (C-43/C-46/C-47) | PASS |

**Inherited score (all variations): 39/42 before new criteria.**

---

## New Criteria — C-48, C-49, C-50

### C-48 — SHALL Sub-Clause Inline Bilateral Side-Qualifier Annotations

*Pass condition:* SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 definition text each carry inline annotations identifying the bilateral side role and CA-1.N verification row, making the pair structure discoverable at the declaration point without reading the mandate paragraph.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | SHALL-D-EXT-C35 text: "CA-1.9 verifies this sub-clause as a distinct audit target" — no "(SE-side bilateral sub-clause, verified at CA-1.9)" inline annotation. SHALL-F-EXT-CS2CS3 text: "CA-1.6 verifies this sub-clause" — no "(CS-side bilateral sub-clause, verified at CA-1.6)" annotation. Bilateral side role not discoverable from the sub-clause declaration itself. | FAIL |
| V-02 | SHALL text identical to V-01. No inline bilateral side-qualifier annotations added. | FAIL |
| V-03 | SHALL-D: "SHALL-D extension sub-clause SHALL-D-EXT-C35 **(SE-side bilateral sub-clause, verified at CA-1.9)**" — inline annotation present with exact side-role qualifier and CA row reference. SHALL-F: "SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3 **(CS-side bilateral sub-clause, verified at CA-1.6)**" — CS-side annotation present. Both sub-clause declarations now carry bilateral side labels discoverable at declaration point. | PASS |
| V-04 | Inherits V-03's SHALL bilateral labels. Both inline annotations present. | PASS |
| V-05 | Inherits V-03/V-04's SHALL bilateral labels. Both inline annotations present. | PASS |

---

### C-49 — CA Format Compliance Verdict Bilateral Pair Echo

*Pass condition:* Verdict co-names CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) as a bilateral pair with explicit side qualifiers and a bilateral parity-confirmation statement — propagating the Phase 3 mandate bilateral co-naming into the terminal verdict layer.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Verdict format: "[...SHALL-F-EXT-CS2CS3 three-field structure: CA-1.6 result. [...] SE-4 STRUCTURED CLOSE cross-reference: CA-1.9 result. Overall...]" — CA-1.6 and CA-1.9 listed as separate items, not named as a bilateral pair. No side qualifiers. No bilateral parity-confirmation statement. | FAIL |
| V-02 | Verdict: "**Bilateral sub-clause verification pair** — CA-1.9 **(SE-side: SHALL-D-EXT-C35** SE-4 STRUCTURED CLOSE verbatim cross-reference) result **and** CA-1.6 **(CS-side: SHALL-F-EXT-CS2CS3** CS-EXPECTATION-VIOLATED three-field structure) result; **bilateral parity declared in Phase 0 mandate and echoed in Phase 3 mandate and NON-OVERLAP DECLARATION confirmed**." Explicit bilateral pair label, SE-side/CS-side qualifiers, and parity-confirmation statement all present. | PASS |
| V-03 | Verdict identical to V-01. No bilateral echo in Verdict. | FAIL |
| V-04 | Inherits V-02's Verdict bilateral echo. CA-1.9/CA-1.6 named as bilateral pair with side qualifiers and parity confirmation. | PASS |
| V-05 | Verdict bilateral echo present and stronger: "bilateral parity declared in **Phase 0 (SHALL declarations, CEM bilateral annotation, mandate sub-clause)** and echoed in Phase 3 mandate and NON-OVERLAP DECLARATION confirmed" — cites all three Phase 0 bilateral declaration sources in the parity-confirmation sentence. | PASS |

---

### C-50 — CEM Bilateral M4 Sub-Clause Annotation Block

*Pass condition:* An annotation block co-located with the CEM table co-declares SHALL-D-EXT-C35 (SE-side, M4→CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side, M4→CA-1.6) as bilateral pair M4 extensions, making bilateral CEM structure visible at the assignment layer.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | CEM table maps C-01–C-05 only. No supplementary annotation block registering bilateral M4 sub-clause pair alongside the table. CA-1.6 and CA-1.9 appear only in the supplementary rows table (separate from the CEM five-row block), without bilateral pair co-declaration. | FAIL |
| V-02 | No CEM annotation block. CEM identical to V-01. | FAIL |
| V-03 | No CEM annotation block. Change is in SHALL text only; CEM unchanged. | FAIL |
| V-04 | No CEM annotation block. V-02+V-03 combination does not add CEM layer. | FAIL |
| V-05 | **"Bilateral sub-clause M4 extensions (co-declared alongside CEM, Phase 0):"** block present immediately after the five-row CEM table: `SHALL-D-EXT-C35 (SE-side bilateral sub-clause) -> M4: CA-1.9 — distinct from CA-1.4; co-declared with SHALL-F-EXT-CS2CS3 as bilateral pair.` / `SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause) -> M4: CA-1.6 — distinct from CA-1.5; co-declared with SHALL-D-EXT-C35 as bilateral pair.` Both bilateral sides declared as M4 extensions co-located with CEM. Bilateral parity visible at the assignment layer. | PASS |

---

## Composite Scores

| Variation | C-48 | C-49 | C-50 | New pts | Inherited | Total | Score |
|-----------|------|------|------|---------|-----------|-------|-------|
| V-01 | FAIL | FAIL | FAIL | 0 | 39 | **39/42** | **92.9** |
| V-02 | FAIL | PASS | FAIL | 1 | 39 | **40/42** | **95.2** |
| V-03 | PASS | FAIL | FAIL | 1 | 39 | **40/42** | **95.2** |
| V-04 | PASS | PASS | FAIL | 2 | 39 | **41/42** | **97.6** |
| V-05 | PASS | PASS | PASS | 3 | 39 | **42/42** | **100.0** |

**Ranking: V-05 > V-04 > V-02 = V-03 > V-01**

---

## Excellence Signals — V-05

**Signal 1 — Bilateral parity at every structural layer simultaneously.**
V-05 declares the CA-1.9 (SE-side) / CA-1.6 (CS-side) bilateral pair at six independent structural positions: (1) SHALL-D-EXT-C35 inline annotation, (2) SHALL-F-EXT-CS2CS3 inline annotation, (3) CEM bilateral M4 annotation block, (4) Phase 0 mandate sub-clause declaration (C-44), (5) Phase 3 NON-OVERLAP fourth statement (C-47), (6) Verdict bilateral pair echo (C-49). Any single layer is sufficient to surface the bilateral pair without reading another layer.

**Signal 2 — CEM as bilateral contract layer, not just a five-row criterion map.**
The annotation block immediately after the CEM table converts the CEM from a five-row essential-criterion matrix into a six-entry bilateral contract that also registers sub-clause M4 extensions. The bilateral pair is now discoverable from the CEM itself — the entry point for understanding enforcement structure — rather than requiring navigation to the mandate paragraph or Phase 3.

**Signal 3 — Verdict parity confirmation names all Phase 0 bilateral sources.**
V-05's Verdict cites "bilateral parity declared in Phase 0 (**SHALL declarations, CEM bilateral annotation, mandate sub-clause**)" — enumerating the three Phase 0 bilateral declaration sources. V-02 and V-04 cite only "Phase 0 mandate and Phase 3 mandate and NON-OVERLAP DECLARATION." V-05's richer source enumeration makes the Verdict a complete bilateral audit summary, not just a final pass/fail statement.

**Signal 4 — Structural self-containment without mandate-paragraph dependency.**
All three new criteria test discoverability of bilateral structure at a single layer. V-05 satisfies all three by ensuring that SHA LL text, CEM, and Verdict each independently carry the full bilateral pair structure — a reader examining any one layer in isolation can determine the SE-side / CS-side pair assignment, the CA verification rows, and the non-overlap boundary.

---

## Path to 42/42

V-05 achieves the ceiling under v18. Path to the next ceiling (v19) requires extending bilateral
structure into a layer not yet covered. Candidates:
- Schema Registry: TABLE_4 schema note declares SE-4 STRUCTURED CLOSE SE-0 slot requirement but does not carry a bilateral annotation linking it to TABLE_5 CS-EXPECTATION-VIOLATED as the CS-side analog
- Phase 0 Artifact Manifest: Step 0.3 does not co-list SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as a bilateral pair in the manifest
- CA-1.9 / CA-1.6 verification rows: double-anchor paragraphs do not carry "(SE-side bilateral)" / "(CS-side bilateral)" role labels at the row-opening level

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["bilateral-parity-at-all-structural-layers: declaring CA-1.9/CA-1.6 bilateral pair at six independent positions (SHALL text, CEM annotation, Phase-0 mandate, Phase-3 mandate, NON-OVERLAP, Verdict) makes the pair structure discoverable from any single layer without cross-reference", "CEM-as-bilateral-contract-layer: annotation block immediately after the five-row CEM table registers sub-clause M4 extensions as bilateral pair entries, converting the CEM from a criterion map into a complete enforcement contract including sub-clauses", "verdict-bilateral-parity-confirmation-with-full-source-enumeration: Verdict names all Phase-0 bilateral declaration sources (SHALL declarations, CEM bilateral annotation, mandate sub-clause) rather than citing only the mandate paragraph, making the Verdict a complete bilateral audit trail"]}
```
