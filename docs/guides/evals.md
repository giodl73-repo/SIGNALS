# Signal as an Eval Framework: How Every Skill is an Evaluator

## The short version

Signal is a pre-commitment evidence tool. But viewed through the eval lens, every skill is
an evaluator, the quest loop is automated eval-driven improvement, and the 52-skill set is
a 52-dimensional evaluation space for feature decisions. The difference from conventional
evals: Signal evaluates decisions before they are implemented, not code after it is deployed.

---

## Three eval types

Signal skills produce three distinct kinds of evaluations. Knowing which type a skill runs
changes how you interpret its output.

**Structural evals** -- does the artifact have the right shape?

Structural evals check format, completeness, and schema conformance. They are fast, cheap,
and automatable. Signal's quest rubric format criteria are structural evals: does the artifact
have a findings section? Does each finding have a severity? Does the frontmatter include the
required fields?

`craft test eval --all` runs L0 (structural) and L1 (completeness) checks on SKILL.md files.
These are structural evals. They do not know whether the skill's output is good -- only
whether it is present and shaped correctly.

Example: does `/simulate-contract` produce a 7-gate manifest with gate-status on each gate?
That is a structural eval. The output either has the right shape or it does not.

**Behavioral evals** -- does the artifact DO the right thing?

Behavioral evals check whether the skill actually performed its function -- whether the output
reflects the intended behavior, not just the required format. The quest rubric's essential
criteria are behavioral evals: does `/discover-competitors` actually identify why inertia is
HIGH? Does the analysis open with the status quo before named competitors? Does it produce
an AMEND section?

Customer persona reviews are behavioral evals. The NPS prediction from `/validate-feedback`
is a behavioral eval: it checks whether the design actually works for the audience, not
whether the review document has the correct sections.

Navigation study time-to-first-artifact is a behavioral eval. An artifact that takes 12
minutes to produce the first useful finding has a behavioral problem even if its structure
is perfect.

**Epistemic evals** -- does the artifact KNOW the right things?

Epistemic evals check the quality of the underlying knowledge claims: whether the evidence
is sound, whether the reasoning is valid, whether the conclusions would survive scrutiny.
These are the hardest evals to automate and the ones Signal is currently most limited on.

Three epistemic eval dimensions:

- **Reproducibility**: does the same skill on the same topic produce consistent findings
  across runs? If `/discover-competitors` labels the inertia threat HIGH in one run and
  MEDIUM in the next with no change in inputs, that is an epistemic failure.

- **Coverage**: does the topic have enough signal namespaces to form a defensible position?
  A topic with `/discover-competitors` and `/specify-spec` but no validation or simulation
  has structural coverage gaps that could hide critical unknowns.

- **Causal validity**: is the mechanism linking the feature to its intended outcome actually
  sound? This is the dimension Signal currently does not evaluate. A team can have 9/9
  namespace coverage and still have a causally broken hypothesis.

Example: a team gathers 5/5 namespace coverage on "payment-reminders." Every skill runs.
Scores look good. But nobody ever tested whether reminder timing is what drives payment
speed versus invoice amount. The causal assumption is untested. Epistemic eval catches this.
Structural and behavioral evals do not.

---

## The quest loop as automated eval

The quest loop is not a testing framework. It is a convergence loop for finding the best
skill prompt. But its structure is identical to an eval-driven improvement loop:

1. **Define eval criteria** -- `quest-rubric` writes a scoring rubric: ranked criteria,
   weights (essential/recommended/aspirational), pass conditions.
2. **Generate candidates** -- `quest-variate` produces N distinct prompt variations, each
   with a labeled variation axis and a hypothesis about what will change.
3. **Score against criteria** -- `quest-score` runs each variation against the rubric and
   real scenarios. Per-criterion PASS/PARTIAL/FAIL with evidence quotes. Leaderboard.
4. **Extract failure patterns** -- rubric gaps (criteria failing across ALL variations mean
   the rubric is missing something), excellence patterns (one variation consistently outperforms
   others on a specific criterion).
5. **Evolve the rubric** -- add the discovered criterion. Repeat until dual convergence.

Dual convergence means: all scenarios pass AND no new excellence patterns for 2 consecutive
rounds. At that point, the prompt is the golden prompt -- the eval instrument is calibrated.

The rubric grows because it finds failure modes that were not anticipated when the rubric was
written. This is the property that makes quest a real eval loop rather than a fixed test suite.
A test suite checks against known expectations. The quest loop discovers new expectations.

---

## Running evals on your own skills

If you are using Signal to develop or refine skills (not just to gather evidence), the eval
chain is:

```
forge generate                     # produces SKILL.md
craft test eval --all              # L0 (structural) + L1 (completeness) + L2 (quality)
/quest-rubric my-skill             # define what good output looks like
/quest-variate my-skill            # generate prompt variations
/quest-score my-skill              # score variations against rubric
/quest-golden my-skill             # full loop to convergence
```

L0 checks that required fields exist and are non-empty. L1 checks section completeness.
L2 checks quality signals: does the output have enough findings? Are severity ratings
consistent? These are all structural and behavioral evals.

The quest loop handles the harder eval: whether the skill finds what it is supposed to find
across diverse scenarios -- including scenarios the skill author did not anticipate.

---

## The missing eval: causal validity

Signal evaluates whether you HAVE evidence. It does not evaluate whether your causal chain
is sound.

Here is the failure mode: a team runs `/discover-competitors`, `/discover-inertia`,
`/specify-spec`, `/validate-design`, `/validate-feedback`, `/simulate-lifecycle`,
`/simulate-contract`, `/validate-adoption`, and `/govern-story`. Nine namespaces. Full
coverage. The investigation narrative looks complete. The signals are consistent.

But the feature hypothesis is: "automated reminders cause faster payment." The actual causal
driver -- which the external evidence surfaces but which nobody flagged in synthesis -- is
that reminders sent within 3 days of the due date work and reminders sent later do not. The
feature as specced sends reminders at day 7. The feature will not produce the outcome it
claims to produce.

No Signal skill caught this. Not because the skills failed, but because causal validity
requires connecting: (a) the evidence from individual investigation signals, (b) the assumed
mechanism in the spec, and (c) the outcome metric the feature is supposed to move. That
connection has to be made by a human reading across signals.

`/discover-hypothesis` partially addresses this: it forces you to state a falsification
condition before you run evidence. But stating a falsification condition is not the same
as verifying that the causal mechanism is correct. You can have a falsifiable hypothesis
with a broken mechanism.

The eval to add: after `/discover-synthesize` produces its answer, a causal validity check
would ask: "does the mechanism described in the spec actually produce the outcome claimed in
the hypothesis, given the evidence gathered?" That is the frontier. It requires reasoning
about mechanisms, not just evidence coverage.

For now: the team is responsible for making the causal argument explicit. Signal gives you
the evidence. The synthesis is where the mechanism must be stated and defended. If
`/govern-story` does not contain a sentence that reads "the reason this feature produces
outcome X is mechanism Y, and evidence Z supports this mechanism," the epistemic eval has
not been run.

---

## What's next

- **[discover](discover.md)** -- the evidence namespaces, where most epistemic evals live
- **[quest loop](../../simulations/quest/)** -- the automated behavioral eval system
- **[Philosophy](../ai-first-development-philosophy.md)** -- the full catalog of AI-first
  development techniques and their evidence base
