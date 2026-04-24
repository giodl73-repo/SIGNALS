Written to `simulations/quest/golden/prove-topic-variate-R2-2026-03-15.md`.

---

## prove-topic — Variation Round R2

Five complete variations exploring the axes not covered in R1, targeting C-11/C-12/C-13.

---

### V-01 — Axis: Inertia Framing

**Hypothesis**: Registering the incumbent approach at session open produces confidence levels grounded in a concrete alternative at every stage, rather than untethered hedges introduced only at synthesis.

**C-12 exemplar.** Structure:
- Session Open registers `current_practice` before scout load
- Each evidence stage carries the anchor forward and assesses "vs. inertia anchor (BEATS/MATCHES/ABSENT)"
- Synthesis first sentence names the anchor explicitly; confidence ceiling invokes the anchor when defeated = false
- Prototype test is explicitly designed to distinguish claim from inertia anchor, not just test the claim in isolation

---

### V-02 — Axis: Phrasing Register (conversational)

**Hypothesis**: Conversational instruction prose ("You've loaded the scout record. Now frame your hypothesis.") produces more natural stage completions because the model follows reasoning continuity rather than template fill-in.

**Design decision**: All five stages use guidance language, not structural gates. Stage transitions are narrative bridges ("Say 'hypothesis artifact written' before moving to Act 2"). All essential criteria are satisfied through prose discipline rather than block notation — making this the highest-risk/highest-readability trade-off in the set.

---

### V-03 — Axis: Per-Artifact Path Enforcement

**Hypothesis**: Naming the exact artifact path at every write instruction (`{topic}-hypothesis-{date}.md`, etc.) eliminates prefix drift without requiring recall of a rule stated earlier — because the path is present at the point of use.

**C-13 exemplar.** Every `WRITE ARTIFACT:` block specifies `Path: simulations/prove/{stage}/{topic}-{stage}-{date}.md` inline. No global prefix rule. Closes with an Artifact Registry table that repeats all five paths for verification.

---

### V-04 — Combined: GATE S + Inertia Framing (C-11 + C-12)

**Hypothesis**: The two independent failure modes — hypothesis before scout load, and confidence without baseline — require two independent protections; combining them is the minimum configuration that prevents both simultaneously.

**Structure**: Dual GATE S checkboxes (`[ ] scout record`, `[ ] inertia anchor`) must be stated checked before Stage 1 opens. `gate_s_cleared: true` propagates into hypothesis frontmatter. Inertia anchor referenced at every stage and named in synthesis first sentence. Thin-evidence propagation table aggregates flags from all stages into Stage 5.

---

### V-05 — Combined: GATE S + Inertia Framing + Per-Artifact Paths (C-11 + C-12 + C-13)

**Hypothesis**: The three protections address three distinct failure modes at three different points — hypothesis before scout (C-11), evidence without baseline (C-12), prefix drift mid-session (C-13). Compounding all three blocks each at its point of origin rather than catching it downstream.

**Aspirational ceiling configuration.** Every `WRITE:` block names `File: simulations/prove/{stage}/{topic}-{stage}-{date}.md` explicitly. Campaign Close table repeats all seven paths (including REGISTRATION 1/2) for verification. All three protections have their own line item in the Completion Check.

---

### Axis coverage across R1 + R2

| Axis | R1 | R2 |
|------|----|----|
| Role sequence | V-01 (96) | — |
| Output format | V-02 | — |
| Lifecycle emphasis | V-03 | — |
| Inertia framing | V-04 (partial) | V-01, V-04, V-05 |
| Phrasing register | — | V-02 |
| Per-artifact path enforcement | V-01 (partial) | V-03, V-05 |
| GATE S | V-01 | V-04, V-05 |
