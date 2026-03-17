Two new criteria extracted from R20 excellence signals:

---

**C-44 — Phase 2 Tier-Up condition encoded with its own named WRONG/CORRECT block**

Derived from V-02's C-21 excellence. C-21 enumerates WRONG/CORRECT sites as Fields 3, 4, Phase 2 sensitivity, and DIAGNOSTIC PATTERN. V-02 extends this with Phase 2 Tier-Up as a fifth site: the tier-up condition carries a null-movement WRONG instance and a named CORRECT instance inline. The tier-up field has identical null-movement exposure to Phase 2 sensitivity (both encode a destination-tier value subject to C-13 and C-16), so the same generation-time guard that C-17/C-21 require for sensitivity applies equally to the tier-up field. V-01 covers only Phase 2 sensitivity; V-02 covers both.

**C-45 — Null-sensitivity WRONG annotation uses "current = X → destination = X" arrow notation**

Derived from V-02's C-16/C-17 excellence. V-01's null-sensitivity annotation notes the current tier only — `[current = HIGH]` — leaving the destination implicit in the condition prose. V-02 makes both explicit: `[current = HIGH → destination = HIGH — null sensitivity]`. The arrow notation is self-contained: current tier, destination tier, and failure class in one compact label. A reader (or the model during self-evaluation) can confirm destination = current without cross-referencing the condition text and the assigned tier. Same principle as C-22's label-level constraint encoding, applied to inline WRONG example annotations.

---

**Scoring changes**: 37 aspirational criteria (was 35), max 127 pts (was 125), composite = raw / 127 × 100.

Written to `simulations/quest/rubrics/scout-size-rubric-v21-2026-03-17.md`.
