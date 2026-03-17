Written to `simulations/quest/rubrics/listen-support-rubric-v5-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — listen-support (v5 rubric, 145 pt ceiling)

**Three single-axis variations, then two combinations.**

---

### V-01 — Lifecycle Emphasis (phase buckets)
**Axis**: Explicit 90-day phase labels (P1 days 1–30 / P2 days 31–60 / P3 days 61–90) on every ticket card, with per-phase role priorities and volume/severity character descriptors.

**New mechanisms targeted**: C-17 + C-18 (gap bridge + sentinels; no performance-mode change)

**Hypothesis**: Phase character constrains the model's generation space before it writes each card. A P1 card "knows" it's a first-day onboarding failure — high volume, P0/P1, how-to/config. A P3 card "knows" it's a power-user edge case — low volume, P2/P3. This reduces severity washing (C-06) and volume uniformity (C-07) by embedding the expected distribution in the phase map rather than relying on post-hoc calibration instructions.

---

### V-02 — Phrasing Register (conversational imperative)
**Axis**: Every instruction rewritten as direct imperative ("Write X", "Put Y here", "Make sure Z", "Don't hide orphan gaps").

**New mechanisms targeted**: C-19 (performance-mode declaration in conversational register)

**Hypothesis**: Formal-descriptive phrasing ("The following fields are required...") gives models interpretive latitude that collapses under imperative phrasing. The effect is strongest on the structural enforcement sections — the prohibited sentinel fields and the orphan-gap check — where passive framing most often produces partial compliance.

---

### V-03 — Role Sequence (operational-first)
**Axis**: Three-layer role ordering: Layer 1 = SRE/Support (operational failures), Layer 2 = C-01 through C-12 (customer symptoms), Layer 3 = PM/UX (strategic signals). Each ticket carries a layer label.

**New mechanisms targeted**: C-17 + C-19 (gap bridge + performance-mode; no per-field sentinels)

**Hypothesis**: Operational tickets generated first establish infrastructure root causes before customer-persona noise; the cross-ticket pattern section then reads root causes from Layer 1 rather than having to infer them from Layer 2 symptoms. The layer label also strengthens the Priority Close Order (C-10): a gap preventing Layer 1 P0/P1 tickets structurally outranks a gap preventing Layer 3 P3 tickets.

---

### V-04 — Lifecycle + Role Sequence (combined)
**Axes**: Phase buckets from V-01 + role-priority-per-phase from V-03.

**New mechanisms targeted**: C-17 + C-18 + C-19 all present.

**Hypothesis**: SRE/Support dominate P1 (infrastructure failures in days 1–30); C-01–C-12 dominate P2 (adoption friction at days 31–60); PM/UX concentrate in P3 (strategic signal at days 61–90). The phase-role pairing simultaneously constrains volume calibration (C-07) and severity calibration (C-06) by making the expected distribution explicit at two dimensions rather than one.

---

### V-05 — Full Synthesis R5
**Axes**: Lifecycle + role sequence + output format (summary table preceding full cards).

**New mechanisms targeted**: C-17 + C-18 + C-19 at maximum strength.

**Key addition over V-04**: A **summary table** (Step 4) is generated *before* full card bodies. It locks all controlled-vocabulary values (category, volume, severity) in column-constrained cells before any prose is written. No vocabulary value bleeds into a narrative sentence. The summary table also provides an independent verification surface in Step 8 — the frontmatter verify check confirms that no card body diverged from its summary row.

**Frontmatter verify** (new for R5): After the coverage trace table, the model explicitly confirms that every `Ticket ID / Phase / Category / Persona / Volume / Severity` in the card bodies matches its summary table row. Any mismatch is flagged as a vocabulary error. This is the R5 excellence signal candidate.

---

### Variation Map

| V | Axes | C-17 | C-18 | C-19 | Key differentiator |
|---|------|------|------|------|--------------------|
| V-01 | Lifecycle | yes | yes | no | Phase character constrains calibration |
| V-02 | Register | no | no | yes | Imperative phrasing on sentinel/check sections |
| V-03 | Role seq | yes | no | yes | Operational-first layer structure |
| V-04 | Lifecycle+seq | yes | yes | yes | Phase-role pairing constrains both C-06 + C-07 |
| V-05 | All three | yes | yes | yes | Summary table locks vocab before prose; frontmatter verify gate |
