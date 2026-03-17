**Round 18 variations written** to `simulations/quest/rubrics/topic-new-rubric-v16-variate-R18-2026-03-15.md`

---

## Variation Map — R18

| ID | Axis | New v16 Criteria Targeted |
|----|------|--------------------------|
| **V-01** | Phrasing register — command throughout | C-51 (`Stop.` + `Record both results.`), C-52 (second-person `"Output you accepted:"`), C-53 (`Stop. You are overriding IR-NN:`) |
| **V-02** | Override mission opener | C-49 (dedicated OVERRIDE MISSION block before all schemas) |
| **V-03** | BEFORE/AFTER failure table | C-54 (labeled SEQUENTIAL PATH / INDEPENDENT PATH contrast table at FER-01/FER-02) |
| **V-04** | Combined: command register + BEFORE/AFTER | C-51 + C-52 + C-53 + C-54 |
| **V-05** | Full integration | All seven: C-49 + C-50 + C-51 + C-52 + C-53 + C-54 + C-55 |

**Key design decisions:**

- C-50 (prohibition clause) is inherited from R17 V-01 and present in all five variations — it was already active; not a new axis.
- C-51 and C-52 are applied together in V-01 since both concern FER-01 phrasing at the same gate (though they're independent criteria, combining them tests phrasing register as a coherent unit).
- C-54 in V-03 restructures the FER registry from a single-row table to a labeled 4-row BEFORE/AFTER comparison block — the SEQUENTIAL PATH column carries the second-person "Output you accepted:" text in V-04/V-05 where C-52 and C-54 are both active.
- C-55 in V-05 adds a `Skip failure recognizable by FER-NN output inspection` suffix to PCR-01 and PCR-02, and explicitly notes PCR-03/PCR-04 have no FER entry (honest about scope — structural-absence failures aren't output-inspection failures).
