**v19 rubric written** to `simulations/quest/rubrics/topic-new-rubric-v19-2026-03-15.md`.

---

## New criterion extracted from R20 excellence signals

| ID | Sharpens | Gap closed | Source |
|----|----------|-----------|--------|
| **C-60** | C-58 | Instrument-map form vs. instrument-map completeness — C-58 requires a mapping table with an instrument-class column (satisfied by a two-column replace form: `IR-NN \| Override Instrument Class`); C-60 requires the supplement form — three columns: `IR-NN \| What This Skill Overrides It With \| Override Instrument Class` — preserving the semantic description alongside the enforcement-class column, so each row is self-legible without consulting the INERTIA REGISTER | R20 V-03/V-05 (three-column supplement achieves 51/51; V-04 two-column replace also achieves 51/51 but lacks semantic-legibility property) |

**Denominator**: 51 → 52  
**Formula**: `aspirational_pass / 52 × 10`

---

**Extraction rationale:**

R20 produced three perfect-scoring variations (V-03, V-04, V-05). V-04 uses the replace form of C-58 and achieves 51/51 — confirming the replace form fully satisfies C-58. V-03 and V-05 use the supplement form and also achieve 51/51. The distinction between V-03/V-05 and V-04 is that the supplement form preserves a description column, making each override entry self-explanatory without a register lookup. This is a structural property above C-58's minimum — analogous to how C-58 sharpens C-56 (flat list vs. instrument map), C-60 sharpens C-58 (instrument class only vs. instrument class plus description). The replace form answers *how*; the supplement form answers *what* and *how* simultaneously.
