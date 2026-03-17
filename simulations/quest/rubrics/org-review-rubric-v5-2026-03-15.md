**org-review Rubric v5** written to `simulations/quest/rubrics/org-review-rubric-v5-2026-03-15.md`.

---

**What changed v4 → v5:**

Three new aspirational criteria extracted from V-05's excellence patterns:

| Criterion | Pattern | Mechanism |
|-----------|---------|-----------|
| **C-19** — DISPOSITION_CONTRACT as Severity Anchor | Severity semantics inside the named contract bind all reviewer labels universally | Resolves the persistent C-04 partial in bracket architectures without per-section repetition |
| **C-20** — CH-ID as Structural Traceability Identifier | Unique ID per challenge claim; downstream sections carry mandatory pre-printed response fields keyed to that ID | Makes PASS-without-response machine-detectable — ID mismatch can't be paraphrased; complements C-17 (content) with identity-level traceability |
| **C-21** — Contract Cite as Per-Reviewer Audit Trail | Each reviewer section must cite the DISPOSITION_CONTRACT by name as a pre-printed field | Post-hoc algebra rewriting becomes structurally visible at every gate, not just at synthesis |

**Scoring rebalance:** aspirational expands from 10×3 = 30 to 13×3 = 39 pts; essential unchanged at 70; total 109; golden threshold 87 (~80%).

**Dependency chain added:** C-19 depends on C-04, C-20 depends on C-13, C-21 depends on C-16 — each new criterion is an intensification of an existing one, not a free-standing addition.
"). The role set is explicit — reviewers are named
or labeled, not implicit.

*Fails if:* any archetype is absent, or reviewer roles are unlabeled.

---

### C-02 — Artifact Scope (~9 pts)
The review explicitly enumerates the artifact surface under review: spec,
design, feasibility, competitive context, technical constraints, and any
prior decisions that would be invalidated. Nothing material falls outside
the stated scope.

*Fails if:* scope is undefined, or artifacts are discovered mid-review
without scope amendment.

---

### C-03 — Per-Reviewer Findings with Severity (~9 pts)
Each reviewer produces a distinct findings block that includes at least one
finding with an explicit severity label (HIGH / MEDIUM / LOW). Findings are
not pooled into a shared list; each reviewer owns their findings.

*Fails if:* findings are aggregated across reviewers, or severity labels are
absent from any finding.

---

### C-04 — Severity Semantically Anchored (~9 pts)
Severity labels carry commit-gate semantics:
- **HIGH** = this finding blocks commitment to build
- **MEDIUM** = this finding conditions commitment (requires remediation before
  proceeding)
- **LOW** = this finding is advisory; commitment may proceed

Strongest implementations define these semantics explicitly in the review
preamble and repeat them in each reviewer section. A severity label scoped
only to the null hypothesis gate (e.g., "HIGH = artifact does not address
null hypothesis") scores PARTIAL; universal commit-gate semantics must
extend to all gates. A severity label that appears without this mapping is
unanchored and scores PARTIAL.

*Fails if:* severity labels are absent or carry no stated commit-gate
meaning.

---

### C-05 — Lifecycle Coverage (~9 pts)
The review covers all three lifecycle stages: null hypothesis challenge
(does the problem warrant building?), domain assessment (is the artifact
technically sound?), and commitment readiness (is the team prepared to
commit?). Stages are sequenced — null hypothesis runs before domain runs
before commitment.

*Fails if:* any stage is absent or the sequence is reversed.

---

### C-06 — Action Items (~8 pts)
The review produces a traceable action list that distinguishes items by
disposition class: BLOCKED items (must be resolved before any commitment),
CONDITIONAL items (must be resolved before proceeding), and advisory items
(may be deferred). Each item traces to the finding that generated it.

Partial credit for per-reviewer recommendations that are not consolidated
into a disposition-indexed list.

*Fails if:* no action items are produced, or items cannot be traced to
findings.

---

### C-07 — Null Hypothesis Framing (~9 pts)
The null hypothesis — what the team does today instead of building this,
and why that is acceptable — is named and addressed before domain testimony
begins. The challenger runs first. Domain findings do not substitute for a
null hypothesis verdict; the null hypothesis gate produces its own verdict
on its own evidence.

*Fails if:* the null hypothesis is absent, or domain findings are the
primary vehicle for null hypothesis evaluation.

---

### C-08 — Summary with Integrating Narrative (~8 pts)
The review closes with a synthesis section that integrates findings across
reviewers — naming conflicts, convergence, and uncovered areas — before
emitting a disposition. The summary references the null hypothesis verdict
explicitly. It does not simply list findings; it synthesizes them into a
narrative that explains why the disposition is what it is.

*Fails if:* no summary exists, or the summary emits a disposition without
integrating narrative.

---

## Aspirational Criteria (C-09–C-21) — 39 pts

### C-09 — Conflict Detection (3 pts)
The review includes an explicit conflict-detection step that names cases
where two reviewers' findings or recommendations are incompatible — not
merely different in emphasis. The conflict is named as a tension (e.g.,
"Domain says workaround is adequate; Challenger says workaround creates
lock-in") rather than resolved by averaging. Strongest form: a pre-printed
Conflicts field that requires "None detected" if no conflicts exist,
making omission structurally impossible.

*Partial if:* conflicts are detectable from the findings but no explicit
detection mechanism exists.

---

### C-10 — Reviewer Independence (3 pts)
Reviewers write in phase-separated gates. At minimum, the challenger writes
before domain reviewers, so domain testimony cannot retroactively shape
the null hypothesis verdict. Strongest form: domain and lifecycle reviewers
write inside a bracket they cannot see closed, enforcing independence
architecturally rather than by convention.

*Partial if:* independence is stated as a rule but not enforced structurally.

---

### C-11 — Disposition Code (3 pts)
The disposition is expressed as a labeled code from a fixed vocabulary:
READY / CONDITIONAL / BLOCKED. The code appears as a distinct labeled
field, not embedded in prose. This enables mechanical downstream processing
(e.g., gate automation, audit trail) and prevents the disposition from
being absorbed into narrative.

*Partial if:* the disposition vocabulary is present but unlabeled or
embedded in prose.

---

### C-12 — Null Hypothesis Anchor per Role (3 pts)
Every reviewer role carries an explicit null hypothesis stance — a
frame-differentiated assessment of whether the artifact defeats the null
hypothesis from that role's vantage point. The challenger, domain reviewer,
and lifecycle stakeholder each produce a distinct framing (e.g., challenger:
"does the workaround become worse?"; domain: "does the artifact make the
workaround obsolete?"; lifecycle: "is the decision case strong enough to
abandon the workaround?"). Stances that are identical across roles score
PARTIAL.

*Fails if:* null hypothesis engagement is conditional (e.g., "only if Gate 1
fails") rather than universal across all roles.

---

### C-13 — Gate Verdict Propagation (3 pts)
Each gate's verdict is a typed signal that changes the task of downstream
gates — not merely a finding to be aggregated at summary time. Gate 1's
verdict is explicitly received by Gate 2 and changes what Gate 2 must do
(e.g., a CONDITIONAL Gate 1 verdict requires Gate 2 to address the gap,
not just assess the artifact on its own terms). Strongest form: a
pre-printed "Received Gate N Verdict" carry-forward field in each
downstream gate section.

*Partial if:* gates are sequenced but verdicts are only collected at
summary time with no downstream gate receiving them during execution.

---

### C-14 — Disposition Algebra (3 pts)
The mapping from gate verdicts to overall disposition is expressed as an
explicit, stated algebra before the disposition field is filled. The algebra
names the rule for each combination (e.g., "BLOCKED if any gate = FAIL;
CONDITIONAL if no FAIL and ≥1 CONDITIONAL; READY if all PASS"). The
evaluator applies the algebra — they do not reason editorially from
findings. Strongest form: the algebra is stated before the summary section
so the evaluator cannot generate a formula that fits results already in
view (see C-16).

*Partial if:* a disposition code is present but no algebra is stated, or
the algebra appears only after all gate verdicts are visible.

---

### C-15 — Adversarial Bracket Architecture (3 pts)
The challenger runs both before domain testimony (Bracket Opening) and
after all domain and lifecycle sections (Bracket Closing). Domain and
lifecycle reviewers write inside the bracket without seeing the Bracket
Closing, preventing domain evidence from displacing the adversarial frame.
The Bracket Closing reassesses whether domain evidence answered the null
hypothesis challenge, not merely whether the artifact is technically sound.

*Fails if:* the challenger runs only once. A single challenger gate at
the start is gate sequencing (C-07, C-13), not bracket architecture.

---

### C-16 — Pre-run Algebra Commitment (3 pts)
The disposition algebra is committed to in the preamble or a locked
template section that precedes all reviewer gates. A formula that first
appears in the summary section is at risk of post-hoc tailoring — the
evaluator filling the summary has already read all gate verdicts and can
generate a formula that fits the outcome rather than constraining it. When
the algebra is placed before Gate 1, the model cannot rewrite a formula it
did not generate.

Strongest form: the algebra is pre-printed before any reviewer section,
with the summary section explicitly instructed to "evaluate the preamble
formula" rather than produce one.

*Partial if:* disposition algebra is present (C-14) but first appears at
or after the summary step. *Fails if:* C-14 fails.

---

### C-17 — Challenge Text Carry-forward (3 pts)
The challenger's specific challenge claim — not just its verdict code — is
propagated as a quoted or copied field into each downstream gate. Downstream
gates must explicitly answer the challenge text, not merely note the verdict
type received. A domain gate that receives "Gate 0: CONDITIONAL" without the
challenge claim cannot demonstrate answer-to-challenge traceability; a
PASS verdict from a domain gate is not credible unless the challenge claim
is answered.

Strongest form: a pre-printed carry-forward field in every downstream gate
that quotes the challenge verbatim and prohibits a PASS verdict without an
explicit response to the quoted claim.

*Partial if:* the verdict code propagates (C-13) but the challenge claim
does not. *Fails if:* C-13 fails.

---

### C-18 — Bracket Closing Override Authority (3 pts)
The adversarial bracket closing carries explicit override authority: a FAIL
or HOLDS verdict from the closing challenger overrides all prior gate
verdicts, regardless of domain and lifecycle PASses. This rule is stated
explicitly in the review structure. Without stated override authority, a
full domain + lifecycle PASS can wash out the adversarial frame — domain
evidence displaces the null hypothesis verdict rather than answering it.

Strongest form: the Disposition section names "GClose = FAIL overrides all
other gate verdicts" as a rule, and the Bracket Closing section is
structurally positioned to emit a final verdict after the Disposition
algebra receives gate inputs.

*Partial if:* a Bracket Closing section exists (C-15) but carries no stated
override authority. *Fails if:* C-15 fails.

---

### C-19 — DISPOSITION_CONTRACT as Severity Anchor (3 pts)
Commit-gate severity semantics (HIGH / MEDIUM / LOW with universal
commit-gate definitions) are embedded inside the named, immutable
DISPOSITION_CONTRACT preamble block. This binds every downstream severity
label to the universal anchor without requiring per-section repetition —
any reviewer severity label is authoritative only as interpreted against the
contract definition. A review that includes severity semantics in free-form
preamble prose (outside a named, locked contract) scores PARTIAL: the
semantics are present but not contract-bound, and a model can restate them
differently at each reviewer section.

This resolves the persistent C-04 partial in bracket architectures: once
severity semantics are inside the contract, all bracket sections inherit
the definition structurally rather than by instruction.

*Partial if:* severity semantics appear in the preamble but outside a named
immutable contract. *Fails if:* C-04 fails.

---

### C-20 — CH-ID as Structural Traceability Identifier (3 pts)
The challenger assigns a unique identifier (e.g., CH-001) to each challenge
claim. Every downstream reviewer section carries a mandatory pre-printed
response field keyed to that identifier (e.g., "CH-001 RESPONSE:"). A PASS
verdict is structurally prohibited without a populated CH-ID response field.

The identifier makes non-compliance machine-detectable: an ID mismatch or
missing field is a structural deviation that cannot be paraphrased away,
unlike verbatim text carry-forward (C-17) which can be restated to obscure
non-response. CH-ID and C-17 are complementary — C-17 ensures the claim
content travels; C-20 ensures the response is traceable to a specific claim
by identity, not by position or paraphrase.

*Partial if:* challenge claims are carried forward by verbatim text (C-17
satisfied) but without a stable identifier that persists across sections.
*Fails if:* C-13 fails.

---

### C-21 — Contract Cite as Per-Reviewer Audit Trail (3 pts)
Each reviewer section explicitly cites the DISPOSITION_CONTRACT by name
before recording findings or verdicts. The cite line (e.g., "Contract:
DISPOSITION_CONTRACT v1") appears as a pre-printed field in the reviewer
section template, not as an instruction to the model.

This converts post-hoc algebra rewriting from instructionally prohibited to
structurally visible: a reviewer section that produces verdicts without a
contract cite is a detectable deviation at that gate, not only at the
synthesis step. A missing or mismatched cite is an audit-trail gap that
cannot be concealed in narrative. Combined with C-16 (algebra committed
before execution) and C-19 (severity inside contract), a full contract-cite
audit trail makes retroactive formula tailoring structurally impossible
rather than merely discouraged.

*Partial if:* contract citation is instructed but not pre-printed as a
required field in each reviewer section. *Fails if:* C-16 fails.
