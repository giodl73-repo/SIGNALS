`simulations/quest/golden/campaign-brief-variate-R8-2026-03-16.md` written.

---

## Round 8 Variations — campaign-brief

**R7 recap:** V-02 and V-05 tied at 230/260. Three patterns reached 230 but not 260: timestamp isolation at one structural location, zero-signal rule embedded inside STORY execution note, and bounded/unbounded without action-posture names.

---

### Single-axis variations

**V-01 — C-24 (Timestamp dual-location)**
Adds the isolation rule at two structural locations: inline annotation on the `found` date field format spec, AND a restatement in the STATUS execution note. Hypothesis: the inline annotation fires at format-apply time, before COMPRESSED can elide the execution note. C-25 and C-26 held at R7 form. Expected: 240/260.

**V-02 — C-25 (Zero-signal named rule)**
Promotes the zero-signal mandate from embedded STORY clause to a standalone `ZERO-SIGNAL SYNTHESIS RULE` block placed between CONFIDENCE and STORY — outside either block's execution note — with two explicitly numbered clauses: (1) empty `found` is not grounds for omitting synthesis, (2) question 1 must characterize what uniform absence implies. Hypothesis: the named rule fires as a structural gate before STORY synthesis regardless of `found` coverage level. C-24 and C-26 held at R7 form. Expected: 240/260.

**V-03 — C-26 (Action-posture sub-labels)**
Adds `action: commit with monitoring` and `action: do not commit until resolved` as required sub-labels on the `bounded:`/`unbounded:` classification in VERDICT. Hypothesis: explicit action names make VERDICT self-contained — team derives commit posture without re-reading STORY. C-24 and C-25 held at R7 form. Expected: 240/260.

---

### Combined variations

**V-04 — C-24 + C-25 (no C-26)**
Combines V-01's dual-location timestamp and V-02's named rule. Tests additive independence: if V-04 = 250, both criteria are structurally non-conflicting. If lower than 250, the named rule's inter-block placement may interfere with the path to the STATUS execution note. C-26 absent to isolate the interaction surface.

**V-05 — Full R8 sweep (C-24 + C-25 + C-26)**
All three new criteria on the R7 best base. First variation targeting 260/260. The R9 investigation candidate (from the rubric): whether the `action:` sub-label syntax survives when COMPRESSED abbreviates the VERDICT block at high token pressure — VERDICT is always the last block processed.
