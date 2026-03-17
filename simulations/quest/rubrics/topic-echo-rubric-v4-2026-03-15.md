Reading the Round 3 scorecard carefully for new patterns before writing v4.

**New patterns visible in Round 3:**

1. **V-03 C-09 PARTIAL (others FAIL)** — The Archaeologist role *structurally induces* counterfactual thinking via the "would the next team carry this as a false assumption?" test, without requiring an explicit per-entry clause. This is mechanically distinct from C-09 (which requires a named clause): structural induction shapes the entire orientation of the skill, not just individual entries. → **C-15: Structural Counterfactual Induction**

2. **V-03 C-12 stronger PARTIAL** — Step 4 groups by "category of misunderstanding — the same blind spot in how the original design materials frame the problem." Grouping by misunderstanding category (blind spot type) is higher-order than root-cause grouping: it reveals the *shape of the original team's ignorance* rather than a topic-organized list. No non-derivability constraint is enforced, hence PARTIAL, but the mechanism itself is an excellence signal. → **C-16: Misunderstanding-Category Synthesis**

---

```markdown
# topic-echo-rubric-v4-2026-03-16.md

## Rubric: `topic-echo` — v4

**Skill**: `topic:echo`
**Version**: v4
**Date**: 2026-03-16
**Criteria count**: 16 (4 essential / 3 recommended / 9 aspirational)

**Formula**:
`(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/9 × 10)`

PARTIAL = 0.5. Max composite = 100. Aspirational tier is a ceiling bonus,
not a score driver. Each full aspirational pass ≈ 1.11 pts.

**Band thresholds**: Gold ≥ 85 + all_essential_pass | Silver ≥ 70 +
all_essential_pass | Bronze ≥ 55 + all_essential_pass | Miss < 55 or any
essential FAIL

---

## Essential Criteria (60 pts — output fails without these)

### C-01 | Surprise Orientation
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains only genuine surprises — findings that
  contradict, reverse, or significantly complicate what was believed or
  designed before the signals arrived. Confirmations (findings that match
  prior expectations) are excluded from the surprise entries.
- **Pass condition**: Every entry in the output names something that was
  not predictable from pre-investigation design materials. An entry that
  restates what the spec already said fails. An entry framed as "this
  confirmed X" fails. PARTIAL if one entry is borderline but the
  remainder are genuine surprises.

### C-02 | Source Signal Tracing
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise names the specific signal artifact or skill type
  that produced it. Vague attribution ("the research", "the signals",
  "investigation") is not acceptable. Tracing must be specific enough
  that a reviewer could locate the source artifact.
- **Pass condition**: Every surprise entry names a specific artifact (e.g.,
  `prove-interview-variate-R3`, `flow-resilience`) or skill type with
  enough precision to locate the source. "The signals" or "our research"
  fails. PARTIAL if one entry has weak attribution but the rest are
  specific.

### C-03 | Design Impact Assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise states its consequence for design: what component,
  flow, constraint, or decision must change as a result. An entry that
  merely reports an interesting finding without naming what changes is
  incomplete.
- **Pass condition**: Every surprise entry contains a design impact clause
  that names a specific artifact, component, or decision. "This is
  interesting" or "worth noting" fails. PARTIAL if one entry has a weak
  impact clause but the rest are specific.

### C-04 | Named and Countable Surprises
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise is a discrete, titled item. The output contains
  at least 2 surprises. A single observation is not a synthesis.
- **Pass condition**: Output has ≥ 2 surprises, each with a distinct name
  or title. An undifferentiated paragraph fails. PARTIAL if titles are
  present but two entries are substantially redundant.

---

## Recommended Criteria (30 pts — output is weaker without these)

### C-05 | Surprise Diversity
- **Weight**: recommended
- **Category**: breadth
- **Text**: Surprises are drawn from more than one signal namespace or
  concern domain (e.g., not all from prove-interview, not all about the
  same component). A set of surprises that all cluster around a single
  source type or system boundary does not constitute an echo — it
  constitutes a partial read.
- **Pass condition**: Surprises span ≥ 2 distinct namespaces or concern
  domains. PARTIAL if signal reading covered multiple namespaces but
  entries cluster around one. A rubric that structurally encourages
  multi-namespace reading satisfies this at PARTIAL without an explicit
  diversity requirement.

### C-06 | Future-Team Framing
- **Weight**: recommended
- **Category**: register
- **Text**: The output is written as institutional memory for the next team
  that walks this path, not as a narrative of the original team's
  experience. Entries are framed as corrections to carry forward, not
  discoveries to celebrate. The audience is the future team; the
  orientation is their ignorance, not the present team's surprise.
- **Pass condition**: Output uses future-team framing in language and
  structure. "We discovered X" fails. "The next team will assume Y; they
  are wrong because Z" passes. PARTIAL if some entries use discovery
  narrative but a forward-framing instruction or collective brief is
  present.

### C-07 | Impact Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Impact clauses name a specific behavior, constraint, or
  decision — not a general area. "This affects the flow design" fails.
  "The retry gate in `flow-resilience` must acquire a lock before
  decrementing the counter" passes. Specificity is the difference between
  an artifact a future engineer can act on and one they must re-derive.
- **Pass condition**: Every impact clause names a specific component,
  behavior, or constraint. A rubric that enforces this in both the entry
  template and a rules section satisfies at PASS (double-enforcement).
  Enforcement in template only is PARTIAL if one entry has a weak clause.

---

## Aspirational Criteria (10 pts — ceiling bonus)

### C-08 | Cross-Signal Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one entry cites two or more distinct signal artifacts
  or skill types as converging evidence for the same surprise. Single-
  source entries are valid; a cross-signal entry demonstrates that
  multiple independent channels independently surfaced the same gap.
- **Pass condition**: ≥ 1 entry names 2+ distinct source artifacts or
  skill types supporting the same finding. PARTIAL if the collective
  brief references cross-signal convergence without a specific entry
  doing so.

### C-09 | Counterfactual Awareness
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one entry contains an explicit counterfactual clause:
  what the team would have built, decided, or shipped if this signal had
  not been gathered. The clause must name a specific wrong outcome, not
  merely state "we would have been unaware."
- **Pass condition**: ≥ 1 entry contains a named counterfactual outcome
  ("without `flow-throttle-variate-R7`, we would have shipped X without
  the backpressure gate"). PARTIAL if the skill's framing mechanism
  structurally induces counterfactual reasoning (see C-15) but no
  explicit clause appears in entries.

### C-10 | Epistemic Delta Tracing
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each entry traces the full epistemic delta: (1) the prior
  assumption held before investigation, (2) the finding that opposes it,
  and (3) the design consequence. All three clauses must appear. A finding
  without a named prior assumption is incompletely traced. A prior
  assumption without a named design consequence is incompletely resolved.
- **Pass condition**: Every entry contains all three clauses. PARTIAL if
  the template requires all three but one entry collapses two clauses.
  A template that requires prior assumption and finding but omits required
  consequence structure is PARTIAL at best.

### C-11 | Confirmation Accounting
- **Weight**: aspirational
- **Category**: completeness
- **Text**: Findings that were confirmations (matched prior expectations)
  are not silently discarded — they are counted and surfaced as a
  separate accountability line in the output artifact. The count gives
  future teams signal about how much of the investigation space was
  expected vs. unexpected.
- **Pass condition**: Output contains a confirmation count or ledger entry
  separate from the surprise entries. "3 confirmations filtered; see
  topic-story." PARTIAL if confirmations are acknowledged in the skill
  scaffolding but routed away without counting.

### C-12 | Collective Next-Team Signal
- **Weight**: aspirational
- **Category**: synthesis
- **Text**: The output contains a synthesis block whose content cannot be
  derived by re-reading the individual entries. The block orients the
  next team to the territory — what kind of problem this is, what the
  dominant shape of the ignorance was, what to watch for — in a way that
  the sum of individual entries cannot reconstruct.
- **Pass condition**: A synthesis block exists whose claims go beyond
  summarizing entries. PARTIAL if a synthesis or clustering step exists
  but its output is derivable from entry re-reading (topic grouping,
  triage annotations, thematic summaries without non-derivable claims).

### C-13 | Collective Brief First-Position Ordering
- **Weight**: aspirational
- **Category**: structure
- **Text**: The synthesis block or collective brief appears before the
  individual surprise entries in the output artifact, not after them.
  Post-hoc synthesis placed after entries is structurally compatible with
  being generated by re-reading the entries. First-position placement
  makes post-hoc summarization structurally impossible for a reader who
  encounters the artifact sequentially.
- **Pass condition**: The synthesis or orientation block appears before
  entry 1 in the output. A synthesis that follows the entries fails,
  regardless of how well-written it is. PARTIAL is not available for
  structural ordering: either it precedes entries or it does not.

### C-14 | Pre-Signal Belief Locking
- **Weight**: aspirational
- **Category**: epistemic hygiene
- **Text**: Prior assumptions are written and locked in the output before
  signal artifacts are read. The locked assumptions must be independently
  verifiable — a reader must be able to confirm that the priors were
  committed before reading, not reconstructed post-hoc to match the
  findings. This prevents the prior assumption clause in C-10 from being
  reverse-engineered from the finding.
- **Pass condition**: The skill produces a prior-assumption ledger or
  belief-locking step that is completed before signal reading begins, and
  the output artifact includes this locked record. PARTIAL if the skill
  instructs the writer to state prior assumptions per entry but provides
  no mechanism to enforce that the prior is written before the signal is
  read.

### C-15 | Structural Counterfactual Induction
- **Weight**: aspirational
- **Category**: mechanism
- **Text**: The skill's framing device — a role, a gatekeeper test, a
  structural question, or a persona orientation — induces counterfactual
  reasoning across all entries without requiring an explicit clause in
  each one. When the framing device asks "would this correct a false
  assumption the next team would carry?" the writer cannot produce an
  entry without implicitly reasoning from future-team ignorance backward
  to present correction. This is mechanically distinct from C-09
  (explicit clause per entry): structural induction shapes the entire
  orientation of the skill execution rather than appending a clause.
- **Pass condition**: The skill contains a role, test, or orientation
  question that makes counterfactual reasoning structurally unavoidable
  during entry production. A test phrased as "what would the next team
  get wrong if they never read this?" qualifies. An instruction to "add a
  counterfactual clause" does not. PARTIAL if role-based orientation
  exists but is stated as optional or can be bypassed without failing the
  entry template.

### C-16 | Misunderstanding-Category Synthesis
- **Weight**: aspirational
- **Category**: synthesis
- **Text**: When the output groups surprises, it groups them by shared
  category of misunderstanding — the same blind spot or structural flaw
  in how the original design materials framed the problem — not by topic
  area, component, or impact tier. Grouping by misunderstanding category
  reveals the shape of the original team's ignorance: "three of the five
  surprises are corrections to the same false assumption about data
  ownership." Topic grouping ("data flow findings," "auth findings")
  cannot produce this. Misunderstanding-category grouping is a strictly
  higher-order synthesis than root-cause or topic clustering.
- **Pass condition**: The synthesis section groups ≥ 2 surprises under a
  label that names the shared misunderstanding or blind-spot type, not
  the topic. "We consistently misread the flow as stateless" qualifies.
  "Flow-related findings" does not. PARTIAL if grouping is attempted and
  the group labels gesture at misunderstanding type but are expressed as
  topic labels (e.g., "state management" rather than "we assumed state
  was caller-managed; it is not").
```

---

**What changed from v3 → v4:**

| Change | Detail |
|--------|--------|
| Criteria count | 14 → 16 |
| Aspirational count | 7 → 9 |
| Per-aspirational weight | ≈ 1.43 pts → ≈ 1.11 pts |
| C-15 added | Structural Counterfactual Induction — role/test-based induction distinct from C-09 explicit clause |
| C-16 added | Misunderstanding-Category Synthesis — blind-spot grouping distinct from topic/root-cause grouping in C-12 |
| C-09 PARTIAL condition | Updated to cross-reference C-15: role-based induction without explicit clause is PARTIAL on C-09 |

The two new criteria are triggered by the same variation (V-03) but capture orthogonal mechanisms: C-15 is about *how counterfactual reasoning is produced* (structurally vs. explicitly), and C-16 is about *how synthesis is organized* (blind-spot shape vs. topic shape).
