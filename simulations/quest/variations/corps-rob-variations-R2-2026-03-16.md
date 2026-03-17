Written to `simulations/quest/golden/corps-rob-variate-R2-2026-03-16.md`.

---

## R2 Summary

**New axes explored:**

| Variation | Axis | Target | Hypothesis |
|-----------|------|--------|------------|
| **V-01** | Severity triage protocol | C-12 | Silent pre-finding triage step anchors the HIGH/LOW distribution — forces discrimination before any label is assigned |
| **V-02** | Conditional verdict itemization | C-11 | Mandatory `CONDITIONS:` block template in every verdict makes enumeration the structural default; N/A is valid for unconditional, burying conditions in prose is structurally awkward |
| **V-03** | Living risk register | C-13 | Status column + update semantics frame the register as present-tense state, not a snapshot — makes re-review operational |
| **V-04** | All three as format rules | C-11+C-12+C-13 | Encode all three v2 aspirational criteria as named format errors to violate, not aspirations to reach — Rule A/B/C with an explicit enforcement section |
| **V-05** | Descriptive register (R1 V-03) + living register + severity triage | C-02+C-12+C-13 | R1 V-03 was the strongest C-02 performer; pair its natural-voice framing with the two most structurally verifiable new criteria without stacking so many rules that role authenticity collapses |

**Key design decisions:**
- V-01's triage step is **silent** (not printed) — keeps the document clean while disciplining the distribution
- V-02's `CONDITIONS: N/A` pattern for unconditional verdicts makes the block structurally present in every case, eliminating the "only show up when conditional" pattern that lets the model skip it
- V-03 introduces **update semantics** (append notes, never delete rows) — this is what makes the register useful for re-review, not just the Status column
- V-04 names violations as "format errors" and adds a `## Format Errors` enforcement section — makes pass/fail structural rather than qualitative
- V-05 avoids stacking V-04's three rules on top of V-03's descriptive register to prevent the mechanical-compliance feel that undermines C-02 role loading
