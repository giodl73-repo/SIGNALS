**Round 2 Result: Five-way tie at 102.5/110 — all golden.**

The key finding is structural: Round 1's excellence signal (prose template eliminates table cell pressure) was fully absorbed by all five variations. C-03, C-04, C-11, and C-12 now pass universally. The rubric v2 discrimination is exhausted.

**What didn't move:**
- **C-06 (PARTIAL all)** — listing canonical names as examples never prevents synonyms. The fix requires a closed-list declaration as a standalone rule, not inline guidance.
- **C-10 (PARTIAL all)** — "Do not publish" has never produced a PASS across two rounds. Needs a dual-token gate: `COMMIT-STAGE-3-CLEAN` / `COMMIT-STAGE-3-FLAGGED` to force resolution before Stage 4 proceeds.

**Qualitative rankings within the tie:** V-01 and V-04 strongest on C-12 robustness (inline examples); V-05 strongest on C-09 (front-loaded token table); V-03 strongest imperative register; V-02 best candidate pre-screening discipline.

```json
{"top_score": 102.5, "all_essential_pass": true, "new_patterns": ["Prose-template baseline fully absorbed: all five Round 2 variations use labeled prose blocks, making C-03/C-04/C-11/C-12 pass universally and eliminating table cell pressure as a discriminating failure mode — rubric v3 must target new discriminating criteria", "C-06 requires closed-list framing: list-as-example never produces a PASS; the fix is a standalone rule declaring canonical names as the only permitted vocabulary, not inline guidance", "C-10 requires a dual-token gate: instruction-level 'do not publish' never passes; structural fix is COMMIT-STAGE-3-CLEAN vs COMMIT-STAGE-3-FLAGGED forcing resolution before Stage 4 can proceed"]}
```
lementations (inline example filenames make full-phrase compliance concrete); V-05 is the most compressed but still explicit with "Never a fragment" on both fields.

**C-11 — why all five pass:**
Round 1's key excellence signal was fully internalized by all variation designers. Every Stage 4 section uses numbered prose blocks with labeled sub-fields (Surprise / Signal Source / Design Impact). The instruction "No tables" or "Do not use a table" appears in V-01, V-02, V-03, V-04. V-05 achieves the same effect via compressed block format — the absence of table markers is itself the format. C-11 is now baseline, not an innovation.

**C-12 — why all five pass:**
All five explicitly prohibit fragments via some combination of: "Full phrase," "Full sentence," "Never a fragment," "Do not write a fragment," or "any phrase shorter than a complete thought." V-01 and V-04 pair the prohibition with inline examples that demonstrate what full-phrase compliance looks like; the example makes abstraction concrete. V-05's prohibition is present but least scaffolded.

**C-06 — why all five are PARTIAL:**
Every variation lists the 5 canonical dimension names (Feasibility · Usability · Scalability · Adoptability · Correctness) but none explicitly say "use only these names" or "no substitutions." The canonical names appear as examples of what to rate, not as a closed set with prohibited synonyms. A model following any of these variations may substitute "Reliability" for "Correctness" or "Performance" for "Scalability" without violating the prompt's instructions as written. C-06 remains the most persistent failure mode in this skill's rubric.

**C-09 — why V-05 is notable:**
V-05 is the only variation that front-loads the complete token inventory in a reference table before Stage 1. All 7 tokens (COMMIT-STAGE-1 through 6 and COMMIT-ENTRY) are listed with their placement rules. The GATE token choices are explicitly enumerated with a "[GATE token here]" marker in Stage 3. This is the strongest structural treatment of C-09 — the model cannot miss a token because the full protocol is visible from the start. The other four variations embed tokens per-stage, which works but creates omission risk if a stage is compressed or skipped.

**C-10 — why all five are PARTIAL:**
All five include the foreknowledge verdict instruction ("CLEAR or FLAGGED; if FLAGGED, name the belief and artifact. Do not publish.") but none provide a concrete stop-execution mechanism. "Do not publish" is a production-level instruction the model can honor or ignore with equal linguistic ease. No variation adds a structural gate (e.g., a pre-Stage-6 checkpoint that requires the foreknowledge evaluation to complete before continuing). Same limitation as Round 1.

**C-08 — why all five pass:**
V-01/V-02/V-03 explicitly prohibit "investigate alone" ("'Investigate' alone does not pass," "'investigate' alone fails"). V-04 provides a positive example (/flow:throttle) without an anti-investigate prohibition, but the example is specific enough to signal named-skill expectations. V-05 says "At least one named skill or role in the last column" — "named" is sufficient specificity since "investigate" is an action verb, not a named skill or role. All pass, with V-01/V-02/V-03 offering the most explicit enforcement.

---

## Composite Scores

| Variation | Essential (/60) | Recommended (/30) | Aspirational (/20) | **Total** | All Essential Pass? | Golden? |
|-----------|-----------------|-------------------|--------------------|-----------|---------------------|---------|
| **V-01** | **60** | **25** | **17.5** | **102.5** | **Yes** | **Yes** |
| **V-02** | **60** | **25** | **17.5** | **102.5** | **Yes** | **Yes** |
| **V-03** | **60** | **25** | **17.5** | **102.5** | **Yes** | **Yes** |
| **V-04** | **60** | **25** | **17.5** | **102.5** | **Yes** | **Yes** |
| **V-05** | **60** | **25** | **17.5** | **102.5** | **Yes** | **Yes** |

---

## Rankings

All five variations score 102.5/110. This is not a scoring failure — it is the diagnostic result. The five-way tie is the signal.

**Qualitative differentiators within the band:**

1. **V-01 and V-04 — highest C-12 robustness.** Both embed real-looking inline example filenames (e.g., "flow-trigger-golden-2026-03-14.md (flow namespace, March 14)") in the Signal Source field and concrete example sentences in Design Impact. The example demonstrates the target format; instruction + example is more compliance-resistant than instruction alone.

2. **V-05 — highest C-09 robustness.** Dedicated token table at the top means token placement is a known constraint from line 1, not a per-stage reminder. Lowest total prompt verbosity while maintaining all passes.

3. **V-03 — strongest imperative register.** Separate-line imperatives ("Name the artifact. Name the namespace. Give the date. Do not write 'multiple sources.'") create a checklist feel that reduces interpretation ambiguity.

4. **V-02 — clearest candidate pre-screening.** Gate-early structure (Step A: identify candidates in list format; Step B: gate the list) surfaces source and impact specificity failures before prose investment, reducing motivated reasoning.

---

## Excellence Signals from Round 2

**The prose-template baseline is now the floor, not the ceiling.** Round 1's highest-scoring variation (V-05, 93 pts) achieved golden by eliminating table cell pressure. Round 2 applied that lesson universally, raising the floor from 73–93 to 102.5 across all five. The rubric can no longer use C-03/C-04/C-11/C-12 as discriminating criteria in Round 3 — they pass structurally for any variation that includes a prose template.

**C-06 is the next structural problem.** Four consecutive rounds have produced PARTIAL on C-06 across all variations tested. No instruction-level fix has worked because the problem is framing: dimensions are presented as examples ("rate using these") rather than as a closed vocabulary ("the only valid names are"). The fix is a closed-list declaration: "These are the only valid dimension names. Do not substitute. Permitted: Feasibility · Usability · Scalability · Adoptability · Correctness." A variation that adds this language as a standalone rule (not embedded in Stage 1 prose) would test whether C-06 can be cracked.

**C-10 needs a structural gate, not a prohibition.** "Do not publish" has appeared in every variation tested and has never produced a PASS. The foreknowledge evaluation requires a binary decision point — either a Stage 3.5 checkpoint that explicitly asks "does this artifact contain foreknowledge contamination? If yes, HALT" or a COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED dual-token protocol that forces resolution before Stage 4 can proceed.

---

```json
{"top_score": 102.5, "all_essential_pass": true, "new_patterns": ["Prose-template baseline fully absorbed: all five Round 2 variations use labeled prose blocks, making C-03/C-04/C-11/C-12 pass universally and eliminating table cell pressure as a discriminating failure mode — rubric v3 must target new discriminating criteria", "C-06 requires closed-list framing: list-as-example never produces a PASS; the fix is a standalone rule declaring canonical names as the only permitted vocabulary, not inline guidance", "C-10 requires a dual-token gate: instruction-level 'do not publish' never passes; structural fix is COMMIT-STAGE-3-CLEAN vs COMMIT-STAGE-3-FLAGGED forcing resolution before Stage 4 can proceed"]}
```
