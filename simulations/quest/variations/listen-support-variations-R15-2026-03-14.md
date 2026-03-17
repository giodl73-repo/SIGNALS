Written to `simulations/quest/rubrics/listen-support-rubric-v14-variate-R15-2026-03-15.md`.

---

## R15 Variations Summary

**Base**: V-04 R14 (265/265 under v14 -- all C-01 through C-43 at ceiling)

**Three new axes probed:**

### V-01 -- Phrasing Register: No-Exception Path Triple-Clause
**Change**: Both no-exception confirmation statements in Pass 2C upgraded from single-clause `"do not paraphrase"` to triple-clause `"do not paraphrase, do not summarize, copy it verbatim word-for-word"`

**Why**: C-43 closes the condensation path in the EXCEPTION SIGN-OFF block. The no-exception path -- executed on nearly every run (most ticket sets have no Phase 1 P0/P1 or Phase 3 P3 exceptions) -- still carries only the single clause. "Short form: Phase 1 no P0/P1" is a summary, not a paraphrase. C-43 doesn't close it there.

### V-02 -- Lifecycle Emphasis: Phase Distribution Pre-Commitment Gate
**Change**: Step 4 acquires a third required item before any cell fills: `PHASE DISTRIBUTION (committed): Phase 1: [N], Phase 2: [N], Phase 3: [N], Total: 8`. Step 4B acquires constraint 0 that checks actual table counts against the declared commitment.

**Why**: Step 4B audits phase distribution post-fill. A pre-fill declaration creates a testable contract, the same structural pattern that makes the inference rule gate effective. The phase distribution has no equivalent pre-commitment.

### V-03 -- Output Format: Switching-Friction Minimum Count Gate
**Change**: "At least one required. At least two are recommended" upgraded to "minimum two required" plus a pre-count declaration block (`SWITCHING-FRICTION COUNT: [N -- minimum 2]`) before any entry. Pass 2B gains a count-match check.

**Why**: The recommendation is advisory -- a single strong entry satisfies the current rubric. A pre-count gate creates the same contract mechanism as the inference rule gate, but for the gap section.

**Combined:**
- **V-04** = V-01 + V-02 (distinct structural slots, no overlap)
- **V-05** = V-01 + V-02 + V-03 (full synthesis)

**Criterion candidates if R15 scores reveal the axes are load-bearing:**
| C-44 | No-Exception Triple-Clause | Closes condensation path in the common (no-exception) path |
| C-45 | Phase Distribution Pre-Commitment | Pre-fill phase contract before any cell is written |
| C-46 | Switching-Friction Count Gate | Pre-count declaration before gap section entries |
