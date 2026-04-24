`scout-risk-rubric-v16-2026-03-17.md` written. Here's the summary of what changed:

---

## v15 -> v16: Three new criteria from R16

### C-48 — Violation taxonomy block is structurally independent (escalates C-45)
**Source**: V-01 PARTIAL vs. V-02 PASS gap. V-01 appends the taxonomy as "Phase 0 Part B" (a sub-section inside Phase 0, inheriting its scope). V-02 creates "Phase 0c" as a standalone sibling block of equal weight.

**Rule**: The violation taxonomy must be its own named pre-phase block at the same structural level as the mitigation taxonomy — not embedded as a sub-section of any existing phase.

---

### C-49 — Each typed prohibition site carries an explicit citation to the violation taxonomy (escalates C-45)
**Source**: V-03's per-site citation pattern (e.g., `"format violation (Phase 0 taxonomy)"`). V-01 and V-02 both rely on structural precedence to establish the drawn-from relationship; V-03 makes it explicit at every use site.

**Rule**: Every typed prohibition must include an inline citation to the taxonomy block by name — drawn-from is verifiable by local inspection, not by inferring it from document ordering.

---

### C-50 — Violation taxonomy block includes an explicit closure declaration sentence (escalates C-48)
**Source**: V-04's doubly-closed taxonomy (4 classes + explicit sentence: "This taxonomy is closed. No violation category outside this list may be named at any prohibition site."). V-02 closes by enumeration (convention); V-04 closes by explicit rule (stated constraint).

**Rule**: The taxonomy block must contain a sentence declaring it closed and prohibiting unlisted categories at any prohibition site — converting implicit closed-world convention to an explicit, auditable constraint.

---

## Scoring delta

| Metric | v15 | v16 |
|--------|-----|-----|
| Aspirational criteria | 39 | 42 |
| Aspirational max | 78 | 84 |
| Max composite | 168 | 174 |
| Golden band | 162-168 | 168-174 |
| Strong band | 147-161 | 153-167 |
