Written to `simulations/quest/golden/campaign-brief-variate-R1-2026-03-16.md`.

---

## campaign-brief — V-01 through V-05 / Round 1

### Variation axes selected

- **Single-axis:** Output format (V-01), Lifecycle emphasis (V-02), Phrasing register (V-03)
- **Combined:** Role sequence + Inertia framing (V-04), Output format + Lifecycle emphasis (V-05)

---

### V-01 — Output format
**Axis:** Dashboard template declared before execution.
**Hypothesis:** Showing the model the complete output skeleton (with named sections for found signals, missing signals, narrative, verdict) forces structural compliance on C-02/C-03/C-08. Models that invent their own shape tend to omit the gap table; models that see named slots fill them.

---

### V-02 — Lifecycle emphasis
**Axis:** Explicit phase gates with `Required output:` checkpoints.
**Hypothesis:** Each sub-skill is a labeled phase with a mandatory deliverable block. The model cannot quietly skip registration or gap enumeration — a skipped phase produces an obviously incomplete dashboard. This is the strongest C-01 and C-05 enforcer.

---

### V-03 — Phrasing register
**Axis:** Conversational imperative second-person narrator voice.
**Hypothesis:** "You are the campaign narrator" + imperative instructions ("First: check whether this topic is registered") reduces task-ownership ambiguity. A model cast as narrator is more likely to synthesize (C-04) than one given a procedure list. Also tends toward denser prose, helping C-08.

---

### V-04 — Role sequence + Inertia framing
**Axis:** Status runs before story; every gap is framed as commit-risk.
**Hypothesis:** Knowing the full coverage map *before* writing the narrative means gaps inform the synthesis rather than being discovered retrospectively. The inertia anchor ("what happens if we commit without this signal?") forces C-07 blocking/optional prioritization to be grounded in real decision exposure, not abstract completeness.

---

### V-05 — Output format + Lifecycle emphasis
**Axis:** Terminal-style compact blocks; prose confined to the STORY section.
**Hypothesis:** Five named blocks (TOPIC, STRATEGY, STATUS, STORY, VERDICT) with all non-narrative content as structured data. C-08 compliance is structural — there is no room for a phase to disappear into prose. The VERDICT is the closing block, where the eye naturally lands (C-06).

---

**Key differentiator to watch in scoring:** V-04 is the only variation that explicitly surfaces inertia risk in the verdict block. V-05 is the only one that enforces the `[STORY]` vs everything-else format split. V-02's `Required output:` gate language is the strongest C-01 enforcement mechanism in the set.
