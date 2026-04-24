---

## Simplification Report

**Original word count**: 1675  
**Simplified word count**: 1490  
**Reduction**: 185 words (11.0%)  
**All essential criteria still pass**: YES

---

### What was removed and why

**Complete sentence removals (no instruction value):**

| Removed | Why |
|---------|-----|
| "Each label-phrase pair is a canonical anchor term for forward-reference in STEPS 2-4." | Explanatory label for a naming convention the executor doesn't act on |
| "STEP 4 INERTIA ANCHOR CHECK will reference the phrases validated at STEP 1 NON-GENERIC CHECK." | Forward reference — STEP 4 check already self-describes the connection |
| "Role names are tentative; update in STEP 2 when candidates are finalized." (from MAP Rules) | Duplicate — same instruction already in CANDIDATE ROSTER |
| "This map is the conformance contract for LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK in STEP 4." | Both named checks already back-reference the MAP directly |
| "If STEP 2 FRAME FILL PRE-ANCHOR CHECK PASS was correctly emitted, this is confirmation." | Reassurance sentence, not an instruction |
| "If not: revise file and re-run CHECK 1, 5A, 5B for the inertia-advocate." | Duplicate of FAIL branch immediately below |
| "Count conforming roles." | Implied by "N of M" output format in PASS/FAIL template |
| "This satisfies LENS AUDIT item 6 and contributes to CROSS-ROLE SPREAD CHECK." | Justification, not instruction |

**Phrase-level compressions:**

| Location | Change | Saved |
|----------|--------|-------|
| PHASE STRUCTURE MAPPING STEP 2 | Removed internal operational detail "(inertia-advocate first, FRAME FILL PRE-ANCHOR CHECK, remaining roles)" — phase mapping doesn't need to document internal sequencing | 9w |
| NON-GENERIC REQUIREMENT | "regardless of context" removed — the listed phrases already show this is absolute | 3w |
| FRAME FILL PRE-ANCHOR CHECK body | Compressed confirmation clause | 13w |
| STEP 2 remaining roles | Full rewrite: "include the BASELINE PROPAGATION MAP assigned term verbatim in lens.verify." vs 27-word version with format examples (already in MAP table) | 27w |
| EARLY INERTIA ANCHOR CHECK body | Streamlined confirmation clause | 7w |
| STEP 4 INERTIA ANCHOR CHECK | Removed "(label + exact phrase, as validated at STEP 1 NON-GENERIC CHECK)" — implied by "verbatim" | 12w |
| CROSS-ROLE SPREAD CHECK header | Removed "(conformance against BASELINE PROPAGATION MAP)" | 5w |

---

### Why 20% was not achieved

The prompt is structurally saturated. The 11% is composed of genuine dead weight. The remaining 89% is:

- **EXIT GATE routing branches** (C-44 requirement — cannot shorten without losing self-routing)
- **Inertia anchor checks** appearing at 4 checkpoints (C-43, C-44 requirements)
- **Format scaffolding** (S/G label notation, citation format, LENS AUDIT items) — removing these causes LLM execution failures
- **Cross-reference bridges** ("from STEP 2 frame fill values", "PROPAGATION MAP assigned term") — each is a pointer that prevents drift across 4 steps

The 20-40% target applies to less structurally constrained prompts. This one has zero narrative prose — every sentence is operational.

---

```json
{"simplified_word_count": 1490, "original_word_count": 1675, "all_essential_still_pass": true}
```
