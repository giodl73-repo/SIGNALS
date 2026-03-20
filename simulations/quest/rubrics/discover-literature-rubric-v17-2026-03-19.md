v17 written to `simulations/quest/rubrics/discover-literature-rubric-v17-2026-03-20.md`.

**What was added:**

**C-34 — C-33 Compliance Declaration as Named Sub-Section with Per-Element Attestations** (V-05 R16)

The C-33 closing declaration must be a labeled sub-section (e.g., "C-33 Compliance Declaration") that names each of the four C-33 elements by designator with a per-element "confirmed" attestation before declaring C-33 PASS. C-33 requires the four elements to be present; C-34 requires each to be individually named and confirmed within a labeled sub-section. Upgrade pattern: C-34 is to C-33 what C-25 is to C-23 — the structural fact becomes self-auditing at the element level.

**C-35 — Terminal Dependency Chain Completion Statement** (V-05 R16)

The C-34 labeled sub-section contains a terminal chain-completion statement naming the full dependency chain from `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete`. Makes chain position self-evident from the block's final element. C-35 is to C-34 what C-29 is to C-28 — the annotation layer gains an embedded declaration that makes the chain's terminal state procedurally visible.

**Scoring delta:**

| | v16 | v17 |
|--|-----|-----|
| Aspirational criteria | 25 | 27 |
| Aspirational ceiling | 125 | 135 |
| Total ceiling | 215 | **225** |
