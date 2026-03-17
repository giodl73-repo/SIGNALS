Written to `simulations/quest/golden/campaign-brief-variate-R20-2026-03-17.md`.

---

## Variations -- campaign-brief / Round 20

**R19 recap:** C-38 Band 2 confirmed (Band 2-A "thoroughly and at full scope", Band 2-B "substantive rather than abbreviated" -- both score identical to Band 1; depth guidance below explicit parity anchoring does not elevate). V-04 = C-38 PASS ceiling (380/380). V-05 extracted C-39: per-companion operationalization embeds the companion mandate's structural deliverables list directly in the absent-state clause.

**R20 investigation:** Whether C-38 PASS alone (parity constraint, no enumeration) produces element-complete companion output under double-elision, or whether depth-correct but element-incomplete companion output is the failure mode C-39 addresses.

---

### V-01 -- C-38 PASS / C-39 Band 1 (R19 V-04 reprised)
**Axis:** Parity constraint present, no structural deliverables enumeration.
**Absent-state extension (both clauses):** `...at full depth, at parity with what would be produced if the companion's execution note were present in this context.`
**Expected:** 380/390 (C-39 Band 1 -10)
**Behavioral probe:** Does parity constraint alone produce all three STORY questions and all timestamp fields under double-elision?

---

### V-02 -- C-39 Band 2 form-A (element-count partial)
**Axis:** One element named per companion, remainder left to parity inference.
- STATUS absent-state adds: names Q1 for ZERO-SIGNAL SYNTHESIS MANDATE only (Q2/Q3 absent)
- STORY absent-state adds: names per-signal dates for TIMESTAMP ISOLATION only (`current_date:` at header and COMPRESSED-immune behavior absent)
**Expected:** 380/390 (C-39 Band 2-A -10)

---

### V-03 -- C-39 Band 2 form-B (specificity partial)
**Axis:** All elements named per companion, but at summary level without operational specificity.
- STATUS absent-state adds: "full-depth execution requires all three STORY questions to be answered: what the signals (or their absence) imply, what remains genuinely uncertain, and what the team's real exposure is if they commit."
- STORY absent-state adds: "full-depth execution requires timestamps to be structurally isolated: per-signal dates in `found` at item level and `current_date:` at STATUS block header level."
**Expected:** 380/390 (C-39 Band 2-B -10; same as Band 1 and Band 2-A)

---

### V-04 -- C-39 PASS minimum-sufficient (complete enumeration, no non-degradation)
**Axis:** Complete per-companion operationalization from R19 V-05, non-degradation clause excluded.
- STATUS absent-state: full Q1/Q2/Q3 enumeration with specificity, "at the same scope and specificity as when the STORY execution note is present in context"
- STORY absent-state: full timestamp enumeration (`current_date:` at header, per-signal dates at item level, "regardless of blocking gap count or token budget")
**Expected:** 390/390 (C-39 PASS ceiling under v19)

---

### V-05 -- C-39 PASS + non-degradation (R19 V-05 reprised / C-40 candidate probe)
**Axis:** Full R19 V-05 structure -- complete enumeration plus depth-symmetric non-degradation: `"This parity constraint is symmetric: executing this companion mandate does not reduce the present clause's own output depth. Both mandates execute at full depth simultaneously."`
**Expected:** 390/390 (C-39 PASS ceiling; above-ceiling behavioral probe for C-40)
**Behavioral probe:** Does V-04 produce present-clause depth reduction when companion execution burden is high (depth-trading)? Does V-05 foreclose it?
