Written to `simulations/quest/rubrics/topic-echo-rubric-v13-2026-03-16.md`.

---

**Two new criteria extracted from R13:**

**C-34 | Discard-Log Schema Template** (schema) — Source: R13 V-01 C-10 excellence. The discard log has a format template with named schema slots (`DISCARD: {label} / Route: / Reason: {one sentence} / Destination:`) visible as placeholders in the prompt, plus an explicit interdependency contract: *"C-10 non-derivability cannot be satisfied without it."* This is the C-30/C-28 schema-formalization pattern applied to the discard log — turning content requirements (route, reason, destination) into structurally enforced typed slots. Requires C-10 PASS.

**C-35 | Format-Variant Criterion Non-Relaxation Contract** (meta) — Source: R13 V-03 C-03 note. When a non-prose format (table, structured list) is adopted for echo entries, cell-brevity pressure silently relaxes falsifiability and specificity requirements unless the prompt explicitly re-asserts them. V-03 guards with: *"table brevity does not relax falsifiability or specificity requirements"* + fragment-fill validation. Auto-PASS for prose-only variations. Activates only when a format change is introduced. Requires C-03 PASS.

**Formula delta:**

| Version | Aspirational denominator | Per-criterion weight |
|---------|--------------------------|----------------------|
| v12 | 26 | 0.38 pts |
| **v13** | **28** | **0.36 pts** |

**Score effects under v13 (R13 variations):**
- V-01: 28/28 → **100.00** (unchanged — passes C-34 via format template, C-35 auto-PASS prose)
- V-02: 25/28 → **98.93** (down from 99.23 — fails C-34, no format template; passes C-35 auto-PASS)
- V-03: 25/28 → **98.93** (down from 99.23 — fails C-34, no format template; passes C-35 with table guard)
