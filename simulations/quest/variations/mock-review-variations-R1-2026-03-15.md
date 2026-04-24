Written to `simulations/quest/golden/mock-review-variate-R1-2026-03-15.md`.

---

## Round 1 — mock-review Variate

### Axis-Assignment Plan

| V | Axes | Target Criteria | Predicted Effect |
|---|------|-----------------|-----------------|
| V-01 | role-sequence | C-02, C-08 | Auto-rules gated before role eval prevents PM/Architect from softening EVIDENCE-HEAVY flags |
| V-02 | output-format | C-07, C-10 | Prose-first per namespace forces substantive three-role reasoning instead of table-cell compression |
| V-03 | lifecycle-emphasis | C-04, C-05 | Write-back as dedicated Phase 5 with STOP gate makes it non-skippable |
| V-04 | role-sequence + phrasing-register | C-02, C-03, C-04 | DO NOT / MUST gates name the exact forbidden outputs (MOCK-ACCEPTED on EVIDENCE-HEAVY); V-01 auto-gate + strict register combined |
| V-05 | output-format + inertia-framing | C-05, C-09, C-10 | "Skip cost" column makes inertia risk visible per namespace; produces C-09 coverage gap synthesis as natural table output |

---

### Design Rationale

The three single-axis variations target the three essential criteria most likely to fail in a neutral baseline:

- **C-02** fails when auto-rules are interleaved with role evaluation — a PM evaluation can produce a MOCK-ACCEPTED that runs in parallel with an EVIDENCE-HEAVY flag and implicitly overrides it. V-01 gates the auto-rules in a phase that finishes before any role speaks.

- **C-07 / C-10** fail when output format collapses evaluation into a table cell. "Good structure" in a 10-character cell satisfies the form of C-07 but not the substance. V-02 switches to prose-first, which forces sentences.

- **C-04** fails when write-back is described as a side-effect rather than a required step. It is the easiest action to omit because the review artifact alone *feels* complete. V-03 makes it Phase 5 with a STOP gate after Phase 4.

The two combined variations test whether the single-axis gains compound or interfere. V-04 combines the role-sequence gate (V-01) with imperative DO NOT framing — hypothesizing that naming the forbidden output pattern (not just the correct one) is more effective at blocking error modes. V-05 combines prose format with inertia framing via a "Skip cost" column, hypothesizing that forcing Strategy to answer "what happens if you do nothing here?" produces C-09 cross-namespace synthesis as a natural output rather than requiring a separate synthesis step.

**Top combination candidate for Round 2:** V-01 + V-03 — if both pass their targeted criteria, combining the auto-flag gate with the full named-phase scaffold should satisfy C-02, C-04, and C-05 simultaneously without the imperative overhead of V-04.
