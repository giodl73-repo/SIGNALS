## quest:score — topic-retro R20 — Rubric v18

---

### Scoring Setup

**Mode assumed:** FRESH (no `{{amend}}` specified in variations)
**Denominator:** 164 pts (168 total − 4 AMEND-exclusive pts; C-46 and C-47 are non-AMEND criteria and count)
**Base:** R19-V-05 — all C-01 through C-45 PASS; C-46 PARTIAL (1 pt), C-47 PARTIAL (1 pt) → **162/164**

Point structure reminder (aspirational):
- C-09–C-43: 35 criteria × 2 pts = 70 pts
- C-44–C-47: 4 criteria × 2 pts = 8 pts
- Essential (C-01–C-05): 60 pts | Recommended (C-06–C-08): 30 pts
- Total applicable (FRESH): 164 pts

---

### Per-Variation Scoring

#### V-01 — C-47 Single Axis: Standalone Authority Block, SEAL Unchanged

**C-47 — Preamble as Canonical Name Registry**
Standalone `**Canonical downstream table set**` block added below the three-entry-point table. Five-row registry enumerates exact canonical identifiers, phase, and source manifest rows. This is a standalone named declaration block, not entry-point prose. C-45 was already PASS (three-row navigation table). C-47 requires a *separate* named declaration block — V-01 provides it.
**C-47: PASS (2 pts)** ↑ from PARTIAL

**C-46 — SEAL-Preamble Cross-Reference Integrity Check**
Phase 0 SEAL cross-check inherits R19-V-05 form: requires Derived Views entries to use exact canonical names from the canonical set, but the reference in the SEAL item is to "preamble's canonical names" generically — it does not name the `**Canonical downstream table set**` authority block explicitly. C-46 pass condition: "cross-check must reference the preamble declaration by name — not an implicit inline list." Generic preamble reference fails this.
**C-46: PARTIAL (1 pt)** — unchanged

All other criteria: unchanged from R19-V-05 base (all PASS).

**V-01 Score: 163/164 (99.4%)**

---

#### V-02 — C-46 Single (N/A Control): Named SEAL Item, Block Absent

**C-47 — Preamble as Canonical Name Registry**
Preamble retains R19-V-05 three-row navigation table only. Canonical table names exist distributed across FORWARD VERIFIED inline enumeration and assignment rules prose — not as a standalone named declaration block. C-45 PASS with canonical names in entry-point row content satisfies C-45 but not C-47's standalone-block requirement.
**C-47: PARTIAL (1 pt)** — unchanged from R19-V-05

**C-46 — SEAL-Preamble Cross-Reference Integrity Check**
Phase 0 SEAL gains an explicit item: "Derived Views entries cross-checked against `**Canonical downstream table set**` authority block in ASSESSOR NAVIGATION PREAMBLE (named explicitly)." The SEAL item is structurally well-formed — it names the authority block correctly. But the authority block it references does not exist as a standalone structural artifact; the canonical names are only in inline/prose form. The rubric's N/A trigger ("Preamble absent (C-47 N/A) makes C-46 non-applicable") applies in spirit: the C-47 block is absent as a standalone entity, making the SEAL cross-check unexecutable. The named SEAL item references a non-existent structural element — a SEAL item that cannot be satisfied by anything in the document is N/A, not PARTIAL.
**C-46: N/A (0 pts)** ↓ from PARTIAL — SEAL item present but its prerequisite absent; correctly confirms the N/A condition

All other criteria: unchanged from R19-V-05 base.

**V-02 Score: 161/164 (98.2%)**

---

#### V-03 — Phrasing Register Negative Control: Prose Names, Inline Reference

**C-47 — Preamble as Canonical Name Registry**
Canonical names listed as a prose sentence embedded in the entry point 2 cell of the navigation table: "e.g., Phase 2 coverage table, Phase 3 accuracy table…" with an informal label. This is entry-point prose content, not a standalone named declaration block. No new structural element added — same configuration as R19-V-05.
**C-47: PARTIAL (1 pt)** — unchanged

**C-46 — SEAL-Preamble Cross-Reference Integrity Check**
SEAL cross-check references "downstream table names listed in entry point 2 above" — an informal inline reference targeting entry-point row content, not a named authority block. Rubric: "Cross-check present but referencing an implicit or inline canonical set rather than the named preamble authority block = PARTIAL." This is exactly the inline-reference failure mode.
**C-46: PARTIAL (1 pt)** — unchanged

V-03 is a structural clone of R19-V-05 under different surface phrasing. Confirms the rubric's distinction between information-present and structure-enforced is correctly operationalized: naming and intent do not substitute for structural form.

**V-03 Score: 162/164 (98.8%)**

---

#### V-04 — C-47 + C-46 Combined: Both Criteria Satisfied Independently

**C-47 — Preamble as Canonical Name Registry**
V-01 standalone `**Canonical downstream table set**` authority block present below the three-entry-point table. Same block as V-01 — standalone named declaration, exact identifiers, phase and source. C-47 pass condition fully satisfied.
**C-47: PASS (2 pts)** ↑ from PARTIAL

**C-46 — SEAL-Preamble Cross-Reference Integrity Check**
Phase 0 SEAL gains explicit item: "Derived Views entries cross-checked against `**Canonical downstream table set**` authority block in ASSESSOR NAVIGATION PREAMBLE by name — generic preamble reference or inline enumeration = FAIL this item." This item names the authority block explicitly and specifies the failure conditions precisely. The C-47 block exists (standalone) so the cross-check is executable. The SEAL item names the authority block by its exact label, not generically. C-46 pass condition fully satisfied.
**C-46: PASS (2 pts)** ↑ from PARTIAL

No modification surface interference: C-47 lives in the preamble structure; C-46 lives in Phase 0 SEAL. The two changes do not touch each other's structural context.

All other criteria: unchanged from R19-V-05 base (all PASS).

**V-04 Score: 164/164 (100.0%)**

---

#### V-05 — Full Integration: Cross-Binding Between Registry, SEAL, and Navigation Declarations

**C-47 — Preamble as Canonical Name Registry**
V-04 standalone `**Canonical downstream table set**` authority block present. Identical structural guarantee as V-04. The block also serves as the citation target named by FORWARD VERIFIED and the assignment rules — but those citations are in other structural elements, not in the C-47 block itself. C-47 evaluates the preamble block structure alone.
**C-47: PASS (2 pts)**

**C-46 — SEAL-Preamble Cross-Reference Integrity Check**
V-04 SEAL cross-check item present, naming the authority block explicitly. V-05 additionally strengthens the SEAL wording: "Cross-check must name the `**Canonical downstream table set**` block explicitly — 'preamble generally' or inline enumeration = FAIL." The authority block exists (C-47 PASS). The cross-check names it by label. The embedded failure-condition statement in the SEAL item is not required by C-46's pass condition but does not harm it. C-46 fully satisfied — same as V-04.
**C-46: PASS (2 pts)**

**C-44 — SEAL-Enforced Bidirectional Navigation Completeness**
Already PASS from R19-V-05. V-05's FORWARD VERIFIED declaration cites "**Canonical downstream table set** declared in ASSESSOR NAVIGATION PREAMBLE" as the source of canonical identifiers, and the Derived Views assignment rules instruct use of "exact identifiers from the `**Canonical downstream table set**` authority block." These additions reinforce C-44's exact-naming requirement and bidirectional check statements, but C-44 was already at full credit. No uplift beyond PASS.
**C-44: PASS (2 pts)** — unchanged, reinforced

All other criteria: unchanged from R19-V-05 base (all PASS).

**V-05 Score: 164/164 (100.0%)**

The structural difference between V-04 and V-05 is architectural, not scorable within v18: V-05 creates mutual enforcement — FORWARD VERIFIED, assignment rules, and SEAL all reference the canonical registry by the same explicit label. Any future drift (renamed downstream table, new phase added) is caught at SEAL time by three independent validators referencing a single named source. V-04 satisfies the rubric criteria; V-05 makes them drift-proof.

---

### Summary Table

| Variation | C-46 | C-47 | Score | % | vs R19-V-05 |
|-----------|------|------|-------|---|-------------|
| **V-04** | PASS (2) | PASS (2) | **164/164** | **100.0%** | +2 |
| **V-05** | PASS (2) | PASS (2) | **164/164** | **100.0%** | +2 |
| V-01 | PARTIAL (1) | PASS (2) | 163/164 | 99.4% | +1 |
| V-03 | PARTIAL (1) | PARTIAL (1) | 162/164 | 98.8% | 0 |
| V-02 | N/A (0) | PARTIAL (1) | 161/164 | 98.2% | −1 |

---

### Excellence Signals from V-05

V-05 is the preferred top scorer because V-04 achieves the rubric ceiling but V-05 achieves the architectural property that makes the ceiling self-enforcing across future rounds.

**Pattern 1 — Registry-anchor cross-binding:** When a canonical registry block exists (C-47), all structural elements that depend on its contents — FORWARD VERIFIED declarations, Derived Views assignment rules, SEAL cross-check items — should reference it by its exact label rather than by location or implication. A registry that is named in only one place (the SEAL) can drift silently; a registry named consistently by all dependents is locatable from any audit entry point.

**Pattern 2 — Embedded failure conditions in SEAL items:** V-05's SEAL item includes explicit disqualifying forms ("'preamble generally' or inline enumeration = FAIL this item"). This transfers rubric enforcement logic into the skill output itself: a future assessor reading the SEAL does not need to consult the rubric to determine what constitutes failure — the SEAL item carries its own failure contract. This is distinct from format-contract string checking (C-23) — it applies to structural reference targets, not field value forms.

These are the candidates for C-48 and C-49 in v19.

---

### Control Validation

- **V-02 confirms N/A propagation:** A SEAL item that names a non-existent authority block scores lower than a generic SEAL cross-check that at least references existing (if implicit) canonical content. Prerequisites must exist before the criteria that depend on them can be satisfied.
- **V-03 confirms structure vs. content distinction:** Prose embedded in entry-point cells and informal inline SEAL references reproduce R19-V-05 exactly regardless of phrasing register. The criteria are structural, not lexical.

---

```json
{"top_score": 164, "all_essential_pass": true, "new_patterns": ["Registry-anchor cross-binding: all structural elements depending on the canonical registry (FORWARD VERIFIED, Derived Views assignment rules, SEAL cross-check items) must reference it by its exact label — consistent naming from all dependents makes the registry locatable from any audit entry point and catches drift at SEAL time", "Embedded failure conditions in SEAL items: SEAL items for structural reference targets should name their own disqualifying forms inline (e.g., 'generic reference = FAIL this item'), transferring rubric enforcement logic into the skill output so assessors do not need to consult the rubric to determine failure"]}
```
