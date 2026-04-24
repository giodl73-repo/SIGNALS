# Signal v0.1 — Shipping Status

**Version**: 0.1 beta
**Target audience**: Microsoft developers, Power Platform teams, BIC users
**Bindings available**: flat (default), grouped, prefixed, domains
**Customer validation**: NPS +30 (12 BIC customer personas, 2026-03-16)

---

## Skill status

**56 golden / 12 draft — out of 68 total**

### Golden (quest-converged, production ready): 56/68

#### scout (8/8)
- scout-competitors
- scout-feasibility
- scout-naming
- scout-compliance
- scout-market
- scout-stakeholders
- scout-positioning
- scout-requirements

#### draft (4/4)
- draft-spec
- draft-proposal
- draft-pitch
- draft-brainstorm

#### review (4/4)
- review-design
- review-code
- review-users
- review-customers

#### flow (7/7)
- flow-lifecycle
- flow-conversation
- flow-trigger
- flow-dataflow
- flow-integration
- flow-throttle
- flow-resilience

#### trace (6/7)
- trace-request
- trace-state
- trace-contract
- trace-component
- trace-deployment
- trace-migration
- (trace-permissions: see Draft section)

#### prove (9/10)
- prove-hypothesis
- prove-websearch
- prove-intelligence
- prove-prototype
- prove-analysis
- prove-interview
- prove-synthesize
- prove-publish
- prove-program
- (prove-topic: see Draft section)

#### listen (3/3)
- listen-feedback
- listen-support
- listen-adoption

#### program (1/1)
- program-plan

#### topic (6/6)
- topic-new
- topic-status
- topic-report
- topic-plan
- topic-story
- topic-echo

#### mock (3/3)
- mock-all
- mock-ns
- mock-review

#### quest (4/4)
- quest-rubric
- quest-variate
- quest-score
- quest-golden

#### meta (1/1)
- trace-skill

### Draft (best available variation, functional): 12/68

The following skills have no quest-converged golden yet. They are implemented and functional
but the prompt body has not completed the variate-score-converge cycle.

#### trace
- trace-permissions

#### prove
- prove-topic

#### corps (newly added namespace, all skills queued)
- corps-scan
- corps-build
- corps-rob
- corps-pr
- corps-chart
- corps-committee
- corps-achievements

#### crew (newly added namespace, all skills queued)
- crew-roles
- crew-review

#### topic
- topic-achievements

---

## Content

- [x] docs/QUICKSTART.md
- [x] docs/ACHIEVEMENTS.md (achievements across 7 categories: exploration, depth, coverage, quality, chain, discovery, corps/crew)
- [x] docs/guides/ (11 namespace guides: scout, draft, review, flow, trace, prove, listen, program, topic, corps, crew)
- [x] PRINCIPLES.md (10 design principles)
- [x] signal.skills.yaml (68 skills, parameters schema, quest_status per skill)
- [x] program.yaml (body_file + param_set wired)
- [x] 4 binding variants (flat, grouped, prefixed, domains)

---

## Install

- [x] install/install-flat.sh
- [x] install/install-grouped.sh
- [x] install/install-prefixed.sh
- [x] install/install-domains.sh

---

## Research

- [x] 22+ papers across 4 tracks in craftworks-research/signals/
- [x] BIC customer validation complete (12 personas, NPS +30)
- [ ] Final panel:module review pending

---

## Known gaps

- 12 skills still converging: trace-permissions, prove-topic, all corps/* and crew/* skills (newly added namespaces), topic-achievements
- signal.manifest.json (upgrade contract) not yet written
- corps/crew namespace skills newly added, quest goldens pending
- quest_status fields in signal.skills.yaml not yet updated for all golden skills (only 3 of 56 annotated)
- CF-01: Double frontmatter in generated SKILL.md (craftworks upstream bug)

---

*Last updated: 2026-03-16*
