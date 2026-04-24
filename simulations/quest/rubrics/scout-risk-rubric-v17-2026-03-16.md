`scout-risk-rubric-v17-2026-03-17.md` written. Here's the summary of what changed:

---

## v16 -> v17: Three new criteria from R17

### C-51 — Closure declaration consists of two syntactically independent sentences (escalates C-50)
**Source**: V-01 (sentence 1 alone: PARTIAL) and V-02 (sentence 2 alone: PARTIAL). The isolation test proves the compound AND is enforced — both halves are individually necessary. The structural implication: the two halves must be syntactically independent sentences, not merged into a single compound sentence. When independent, each is auditable by local inspection without parsing a compound structure, and each can be included or omitted atomically in future isolation tests.

---

### C-52 — Violation taxonomy block includes an explicit structural parity declaration (escalates C-48)
**Source**: V-04/V-05 pattern — stating "equal structural weight to Phase 0" within the block opening. C-48 establishes parity by document structure (heading level + position); C-52 requires the block itself to declare that parity explicitly. Converts inferred structural equivalence to a locally verifiable stated constraint: a reviewer can confirm parity by reading the block alone, without examining surrounding document structure.

---

### C-53 — Per-site citations use the fully-qualified block heading string (escalates C-49)
**Source**: V-05 pattern — using exact heading string `Phase 0c Violation Taxonomy` rather than abbreviated form `Phase 0 taxonomy`. C-49 requires explicit citation at every prohibition site; C-53 requires the citation text to be the exact block heading string. Makes drawn-from verifiable by character-level match rather than abbreviation resolution — the citation either matches a block heading verbatim or it does not.

---

## Scoring delta

| Metric | v16 | v17 |
|--------|-----|-----|
| Aspirational criteria | 42 | 45 |
| Aspirational max | 84 | 90 |
| Max composite | 174 | 180 |
| Golden band | 168-174 | 174-180 |
| Strong band | 153-167 | 159-173 |
