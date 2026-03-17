# Quest Score: signal-setup — Round 1

## V-01: Sequential Gate Model

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | Gate 1 explicitly reads CLAUDE.md and checks for Signal section before any write operation |
| C-02 | Preview shown before writing | **PASS** | Gate 2 composes section and shows it in a fenced code block before any write |
| C-03 | Confirmation required | **PASS** | Gate 2 asks `"Append this Signal section to CLAUDE.md? (yes/no)"` — write blocked until yes |
| C-04 | Signal section with skill advertising | **PASS** | Gate 2 specifies namespaces, invocation pattern (`/signal:{namespace}`), and inertia rule |
| C-05 | Idempotent re-run | **PASS** | Gate 1 detects existing section; routes to Gate 4 which reports skip and does no write |
| C-06 | Inertia rule included | **PASS** | Gate 2 mandates the exact inertia rule verbatim in the appended section |
| C-07 | Copilot instructions offered | **PASS** | Gate 3 asks about copilot-instructions.md post-write if file exists |
| C-08 | User feedback on outcome | **PASS** | Gate 3 reports what was written, to which files, at what line |
| C-09 | Preview matches written output | **PASS** | Gate 3 says "Append the **previewed** Signal section" — explicit back-reference prevents drift |
| C-10 | Handles missing CLAUDE.md | **PASS** | Gate 5 is a dedicated path: informs user, shows preview, asks confirmation before creating |

**essential_pass: 5/5 | recommended_pass: 3/3 | aspirational_pass: 2/2**
`Composite = (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = **100**`

---

## V-02: Structured Table Output

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | Step 1 produces a status table before any write; explicit "before doing anything else" |
| C-02 | Preview shown before writing | **PASS** | Step 2 shows full Signal section in a fenced code block |
| C-03 | Confirmation required | **PASS** | Step 3 asks `"Proceed with these changes? (yes/no)"` before writing |
| C-04 | Signal section with skill advertising | **PASS** | Step 2 preview lists all 9 namespaces with sub-skills |
| C-05 | Idempotent re-run | **PASS** | Step 1 says "If Signal section present is yes, skip to Step 4" — Step 4 explicitly does no writes |
| C-06 | Inertia rule included | **PASS** | Step 2 preview includes a dedicated `### Inertia Rule` block |
| C-07 | Copilot instructions offered | **PASS** | Step 2 Proposed Changes table shows it as an optional action; Step 3 asks separately if file exists |
| C-08 | User feedback on outcome | **PASS** | Step 3 requires a Write Report table with file and result columns |
| C-09 | Preview matches written output | **PASS** | Step 3 references "the Signal section" with the preview in scope; no reformulation |
| C-10 | Handles missing CLAUDE.md | **FAIL** | Step 1 notes CLAUDE.md absence but no dedicated handling path — appending to a non-existent file proceeds silently without user messaging |

**essential_pass: 5/5 | recommended_pass: 3/3 | aspirational_pass: 1/2**
`Composite = (5/5 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = **95**`

---

## V-03: Conversational Guide

The spec is **truncated** — it presents only the detection step (checking CLAUDE.md and copilot-instructions.md) and ends mid-sentence. Preview, confirmation, write, idempotency, and outcome reporting phases are absent from the spec as written.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | Explicitly checks CLAUDE.md and copilot-instructions.md |
| C-02 | Preview shown before writing | **FAIL** | Not present in spec |
| C-03 | Confirmation required | **FAIL** | Not present in spec |
| C-04 | Signal section with skill advertising | **FAIL** | No write phase specified |
| C-05 | Idempotent re-run | **FAIL** | No detection-and-skip logic shown |
| C-06 | Inertia rule included | **FAIL** | No content specified for appended section |
| C-07 | Copilot instructions offered | **PASS** | Detection step mentions checking copilot-instructions.md |
| C-08 | User feedback on outcome | **FAIL** | No outcome reporting shown |
| C-09 | Preview matches written output | **FAIL** | No preview or write phase present |
| C-10 | Handles missing CLAUDE.md | **FAIL** | Not addressed |

**essential_pass: 1/5 | recommended_pass: 1/3 | aspirational_pass: 0/2**
`Composite = (1/5 × 60) + (1/3 × 30) + (0/2 × 10) = 12 + 10 + 0 = **22**`

---

## Rankings

| Rank | Variation | Score | All Essential | Band |
|------|-----------|-------|---------------|------|
| 1 | V-01: Sequential Gate Model | **100** | Yes | Golden |
| 2 | V-02: Structured Table Output | **95** | Yes | Golden |
| 3 | V-03: Conversational Guide | **22** | No | Failing |

---

## Excellence Signals (from V-01)

**1. Named gate checkpoints as explicit phase boundaries**
V-01 names each phase as a numbered Gate. This forces the skill to be a sequential state machine — no phase can be implicitly skipped. V-02 uses Steps but doesn't enforce the same gate-level rigor; V-03 had no structure beyond step 1.

**2. Dedicated edge-case gates as first-class paths**
V-01 promotes "Already Configured" and "Missing CLAUDE.md" to their own named gates (Gate 4 and Gate 5) rather than inline conditionals. This ensures edge cases get complete, explicit treatment. V-02 handles idempotency but leaves missing-file implicit; V-03 doesn't reach this at all.

**3. Preview-to-write back-reference prevents content drift**
V-01 Gate 3 says "Append the **previewed** Signal section" — the write is explicitly tied to the preview object. This is what causes C-09 to pass: there's no separate content specification at write time that could diverge. V-02 passes C-09 for the same reason but is slightly less explicit.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named gate checkpoints enforce phase boundaries and prevent lifecycle skipping", "Dedicated edge-case gates (already-configured, missing-file) as first-class paths rather than inline conditionals"]}
```
