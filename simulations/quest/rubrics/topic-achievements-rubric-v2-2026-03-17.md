Done. Here's what changed in v2:

**3 new aspirational criteria (C-11, C-12, C-13)** extracted from the R1 excellence signals:

- **C-11 (State-column isolation)** — from V-02's table-column enforcement. Rewards structural placement of state values so C-01 is verifiable by scanning one axis, not parsing prose. Passes C-01 is not sufficient; C-11 requires the structure to do the validation work.

- **C-12 (Synthesis placement boundary)** — from V-02's "not buried at the end" rule. Upgrades C-09 from a presence check to a placement check. V-01 failed C-09 because synthesis came after classification; C-12 codifies "before the first category entry" as the only acceptable position.

- **C-13 (Hallucination-safe fallback)** — from V-02's "cite namespace only if unsure" escape hatch. A complement to C-03: C-03 catches fabricated names that appear; C-13 rewards the positive behavior of graceful degradation to namespace-level when evidence is uncertain.

**Scoring formula updated**: `aspirational_pass / 5 * 10` (was `/2`). Max composite remains 100. V-02 would still score 100; V-01 would score 93 (fails C-12 — synthesis after classification).
