Good. Now I have all the numbers needed.

---

## Simplification report

**What was removed and why:**

| Category | What | Why |
|----------|------|-----|
| Entire variate scaffolding | "What R19 Left Open" section, variation matrix, per-variation axis/hypothesis/C-42/C-43 preambles | Testing instrumentation, not part of the skill definition |
| 4 of 5 variation bodies | V-02 (FAIL), V-03 (inertia-heavy), V-04 (conversational), V-05 (belt-and-suspenders) | QU5 goal is ONE minimal body, not a testing matrix |
| 9 `<!-- C-42: ... -->` HTML comments | All criterion-labeling annotations in step/guard/gate/template headers | Aspirational C-42 coverage — no behavioral effect |
| 12 `(C-NN, C-NN)` parentheticals in step headings | `(C-07, C-13, C-36)`, `(C-01, C-02, C-06)`, etc. | Documentary cross-references, not instructions |
| `[C-NN]` labels in template slot headers | `(C-23, C-30)`, `(C-20, C-25)`, C-38/C-40/C-41/C-43 in CROSS-TEMPLATE block | Same — aspirational labeling, not behavioral |
| "This guard fires on ... Arch-first design: C-36 ✓, C-35 N/A." | One explanatory sentence per cross-step guard | Fully restated by the condition directly above it |
| CANARY error expansion | `"— writing the canary when the condition is not met"` | Already implied by "PROHIBITED if any field remains" |

**What was NOT removed:** DEFAULT DECISION POSITION (inertia framing — C-22), FORBIDDEN OUTPUTS TRIAD with all 3 exact labels, AUTO-RULE CONTAMINATION GUARD, all 3 cross-step guards with Record blocks, CROSS-TEMPLATE RELATIONSHIP BLOCK (anchors C-03 reason-code placement), both MOCK-ACCEPTED slots with SLOT-VIOLATION/CONTRAST-INCOMPLETE guards, both REAL-REQUIRED templates, all DO NOT proceed gates, Row # columns (low-cost, high-traceability), CANARY + CANARY SUPPRESSED path, full confirmation block.

---

## Essential criteria verification

| Criterion | Still passes? | Evidence in simplified body |
|-----------|--------------|----------------------------|
| C-01 Decision completeness | YES | STEP 2 two-list output; STEP 6 one decision block per namespace |
| C-02 Automatic rule correctness | YES | 3 rules + PHASE GATE + FORBIDDEN OUTPUTS TRIAD + CONTAMINATION GUARD; all fire before role evaluation, non-overridable |
| C-03 MOCK-ACCEPTED reason code | YES | `reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]` with "exact codes only" enforcement |
| C-04 Status fields written back | YES | STEP 8 in-place edit + CANARY ASSERTION verifying 0 MOCK fields remain |
| C-05 Next-steps list in priority order | YES | STEP 7 Priority 1/2/3 lists with `/{skill-id} {topic} — {Artifact state}` format |

**All 5 essential criteria: YES**

---

```json
{"simplified_word_count": 1459, "original_word_count": 11649, "all_essential_still_pass": true}
```
