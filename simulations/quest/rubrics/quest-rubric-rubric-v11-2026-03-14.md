Written to `simulations/quest/rubrics/quest-rubric-rubric-v11-2026-03-15.md`.

**What changed v10 → v11:**

**C-33** (`contract-structural-equivalence-does-not-propagate-or-equivalent-block-to-role-definition`) — R10 V-01 finding. V-01 satisfies C-32 (AND-framing) but fails C-26 and scores C-25 PARTIAL simultaneously. Contract item 4 operates at the output-state layer; the role definition is a separate propagation target at the generation-behavior layer. A Contract that achieves structural equivalence without anchoring the exact phrase "or equivalent block" in the role definition produces a joint C-25/C-26 failure from one structural root cause.

**C-34** (`stop-condition-advisory-register-causes-joint-c04-c05-failure`) — R10 V-02 ablation finding. Replacing all STOP AND REWRITE with advisory equivalents drops C-04 and C-05 from PASS to PARTIAL simultaneously — one phrasing-register change, two enforcement-dependent criteria fail together. Advisory register is an open filter; imperative register is the sole mechanism that makes C-04 (generic-criterion gateway) and C-05 (binary-condition enforcement) reliably closed.

**Structural updates:**
- Required Sections row 7: C-33 and C-34 added to N/A scope list
- Scoring N/A paragraph: C-33 and C-34 added
- Notes: `**C-33 N/A scope**` and `**C-34 N/A scope**` blocks added; C-32 self-application updated to version 11
- v12 Candidates: rejection-log count updated to 26 aspirational; new candidate `and-gate-contract-does-not-propagate-to-dr-sub-section-labeling` added (from V-01 C-27 PARTIAL pattern); all other candidates carry forward
