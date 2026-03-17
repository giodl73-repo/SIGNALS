**Round 4 variations written** to `simulations/quest/golden/org-committee-variate-R4-2026-03-16.md`.

---

## Summary

Five complete variations, each targeting a distinct axis while incorporating the two new R4 criteria (C-16 gate, C-17 advocate citation):

| Variation | Axis | What it upgrades from R3 | C-16 mechanism | C-17 mechanism |
|-----------|------|--------------------------|----------------|----------------|
| **V-01** | Lifecycle emphasis | R3 V-01 (no investigation) + adds full investigation phase | `GATE:` inline after investigation block | "Tier 3 voices cite investigation finding by label" in voice rules |
| **V-02** | Output format | R3 V-03 (template) + adds `GATE:` as a required template field + `CITE:` subfield in each Tier 3 block | `GATE:` is a template field — blank = visibly incomplete | `CITE:` is a structural subfield in each Tier 3 voice block |
| **V-03** | Phrasing register | R3 V-02 (best scorer) compressed to ~50% word count | `GATE: YES — non-obvious because [reason]` in-line after investigation | "cite one investigation finding by label" in minimal voice rules |
| **V-04** | Inertia framing | R3 V-04 (inertia-first) + investigation before inertia voice + inertia grounded in findings | `GATE:` on Phase 1 investigation | Tier 3 may cite Phase 1 findings OR INERTIA-FINDING tags |
| **V-05** | Combined (all axes) | R3 V-05 + C-16 as named GATE step + C-17 as `CITE:` structural subfield | Separate **Step 3 — C-16 Gate** with explicit YES/NO output format | `CITE:` subfield required in every Tier 3 voice block, labeled and enforced |

**Key design decision**: C-16 and C-17 are most reliably enforced when they are *structural fields the model must fill in*, not prose instructions it must remember. V-02 and V-05 make both criteria template fields; V-03 makes them inline labels in the voice format; V-01 and V-04 thread them through existing phase structures.
