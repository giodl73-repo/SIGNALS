Written to `simulations/quest/rubrics/flow-throttle-rubric-v9-2026-03-16.md`.

---

**Two new criteria extracted from R8 V-05 excellence signals:**

**C-25 — Structured-output exemption class in prose-restriction declaration**
V-05's C-20 declaration adds an explicit list of what is *not prose* (gate decision lines, cross-artifact header lines), making the prose/structured-output boundary self-classifying. Without it, C-23 compliance on a prompt combining C-20+C-23+C-24 requires content interpretation to determine whether gate verdicts need `[prose: item N]` tags. C-25 closes that boundary at the declaration level. An output satisfies C-20 (prose-permitted contexts enumerated) while failing C-25 (exemption class absent — element type classification requires content inspection).

**C-26 — Gate inertia annotation**
V-05's TYPE SCAN GATE carries a "Purpose" annotation that references C-22, names the failure mode prevented (category elision), and explains the gap above C-22 (C-22 ensures the type column structure; the gate ensures a missing category is a structural block, not a post-hoc detectable gap). This is the C-18 inertia-framing pattern applied to a gate step rather than a prohibition or enumeration anchor. An output satisfies C-24 (gate present, PROCEED/BLOCK) while failing C-26 (gate delivers the verdict without explaining why it exists independently of C-22).

**Score impact**: Aspirational 16 → 18 criteria (90 pts), max composite 170 → 180. Golden threshold unchanged.
