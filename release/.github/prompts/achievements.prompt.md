---
mode: agent
description: "Show achievements earned for a topic. Scans signals/ artifacts, checks which achievements have been earned across 35 milestones in 8 categories, shows"
---

You are running /achievements for: {value}

Scan signals/ for artifacts produced on this topic. Check which achievements have been
earned. DISPLAY ONLY — write no files.

---

## STEP 1: Scan artifacts

Find all files matching: signals/**/{value}-*-*.md
Also check: signals/discover/, signals/draft/, signals/review/,
signals/flow/, signals/trace/, signals/listen/, signals/prove/,
signals/rhythm/, signals/roles/, signals/scout/, signals/specify/,
signals/validate/, signals/simulate/, signals/program/, signals/topic/

For each artifact found, record:
- Namespace (first path segment under signals/, or inferred from skill prefix)
- Skill name (from filename)
- Date (from filename or frontmatter)

Map skill prefixes to namespaces:
  discover-* / scout-* -> scout/discover namespace
  draft-* / specify-* -> draft/specify namespace
  review-* / validate-design / validate-code / validate-users / validate-customers -> review/validate namespace
  validate-inertia / validate-adoption-blocker -> review/validate namespace (adoption-resistance signals)
  flow-* / simulate-* (flow skills: lifecycle, conversation, trigger, dataflow,
    integration, throttle, stress, resilience) -> flow/simulate namespace
  trace-* / simulate-* (trace skills: request, state, contract, component,
    deployment, migration, permissions) -> trace namespace
  prove-* -> prove namespace
  listen-* / validate-feedback / validate-support / validate-adoption -> listen namespace
  rhythm-* -> rhythm/program namespace
  roles-* / org-* -> roles namespace
  topic-* / program-* -> topic/program namespace

Count:
- Namespaces touched (distinct namespace groups above)
- Skills run (unique skill names in artifact filenames)
- Total artifacts produced

---

## STEP 2: Check achievements earned

### EXPLORATION (first use per namespace)
- [ ] **First Signal** — any artifact exists
- [ ] **Discover Pioneer** — any discover-* or scout-* artifact
- [ ] **Specify Founder** — any draft-* or specify-* artifact
- [ ] **Validate Reviewer** — any review-* or validate-design/validate-code/validate-users/validate-customers artifact
- [ ] **Simulate Tracer** — any flow-* or simulate-lifecycle/conversation/trigger/dataflow/integration/throttle/stress/resilience artifact
- [ ] **Verify Tracer** — any trace-* or simulate-request/state/contract/component/deployment/migration/permissions artifact
- [ ] **Evidence Investigator** — any prove-* or discover-hypothesis/discover-websearch/discover-analysis/discover-synthesize artifact
- [ ] **Adoption Listener** — any listen-* or validate-feedback/validate-support/validate-adoption artifact
- [ ] **Commitment Planner** — any rhythm-*, program-*, or topic-* artifact

### DEPTH
- [ ] **Signal Saturated** — 10 or more distinct skills run on this topic
- [ ] **Full Scout** — all 8 scout/discover skills: discover-competitors, discover-feasibility, discover-naming, discover-compliance, discover-market, discover-stakeholders, discover-positioning, discover-requirements
- [ ] **Full Prove** — all 7 prove skills: discover-hypothesis, discover-websearch, prove-intelligence, prove-prototype, discover-analysis, prove-interview, discover-synthesize
- [ ] **Full Flow** — all 7 flow skills: simulate-lifecycle (or flow-lifecycle), simulate-conversation, simulate-trigger, simulate-dataflow, simulate-integration, simulate-throttle, simulate-stress
- [ ] **Full Trace** — all 7 trace skills: simulate-request, simulate-state, simulate-contract, simulate-component, simulate-deployment, simulate-migration, simulate-permissions
- [ ] **Deep Listen** — all 3 listen skills: validate-feedback (or listen-feedback), validate-support (or listen-support), validate-adoption (or listen-adoption)

### COVERAGE
- [ ] **Evidence Starter** — 3 or more distinct namespace groups covered
- [ ] **Evidence Builder** — 5 or more distinct namespace groups covered
- [ ] **Critical Path** — scout/discover namespace + trace namespace + listen namespace all present
- [ ] **Fast Coverage** — 5 or more namespaces covered; note if all artifacts are from the same calendar day
- [ ] **Pre-Commitment Ready** — 7 or more distinct namespace groups covered
- [ ] **Full Coverage** — all 9 namespace groups covered

### CHAIN
- [ ] **Scout-First Spec** — discover-feasibility or scout-feasibility artifact predates any draft-* / specify-* artifact
- [ ] **Evidence-Based Draft** — discover-hypothesis or prove-hypothesis artifact predates any draft-* / specify-* artifact
- [ ] **Grounded Review** — draft-* or specify-* artifact predates any review-* / validate-design artifact
- [ ] **Simulation-Before-Build** — simulate-lifecycle or flow-lifecycle predates any trace-type simulate-* artifact
- [ ] **Full Pre-Commit Chain** — scout/discover + draft/specify + review/validate all present (in that order)

### QUALITY
- [ ] **Inertia Identified** — any discover-competitors or scout-competitors artifact present
  (inertia is always primary; earning this marks that you ran the competitors skill)
- [ ] **Sharp Hypothesis** — discover-hypothesis artifact exists and contains "specific" and "falsifiable"
- [ ] **The Echo** — rhythm-reflect artifact exists

### DOMAIN
- [ ] **Domain Pioneer** — any artifact has domain_roles_active field in frontmatter (1+ domain role loaded)
- [ ] **Platform Expert** — validate-design artifact exists with reviewer_count >= 3 AND domain_roles_active populated
- [ ] **Cross-Domain** — artifacts produced with 2+ distinct domain role areas active (e.g., backend + msft)

### CORP AND CREW
- [ ] **First Review** — any roles-review, org-review, or crew-review artifact exists
- [ ] **PR Reviewed** — any roles-pull-request or org-pr artifact exists
- [ ] **Full Corp** — org-committee artifact exists (full org ROB ran)

### DISCOVERY
- [ ] **Falsified** — discover-hypothesis or prove-hypothesis artifact exists AND contains "INCONCLUSIVE" or "REJECTED" or "FALSIFIED"
  Check separately: (a) has the skill been run? (b) if run, does the output contain falsification language?
  These are different states: "not yet run" vs "run but hypothesis not yet challenged honestly"
- [ ] **Inertia Wins** — any discover-competitors artifact exists AND contains "status quo is sufficient" or "inertia wins" or "do not build"

---

## STEP 3: Display

```
Achievements for: {value}
================================================================

EARNED (N of 38):
  [x] First Signal
  [x] Discover Pioneer
  [x] [other earned achievements]

IN PROGRESS:
  [ ] Critical Path -- need: [missing namespace(s)]
  [ ] Evidence Builder -- covered N/5 namespaces, need [list]

NEXT RECOMMENDED (unlocks the most achievements):
  -> /[skill] {value}    (unlocks: [achievement names])
  -> /[skill] {value}    (unlocks: [achievement names])

DOMAIN WATCH:
  Domain Pioneer: [NOT YET / EARNED] -- install domain roles in .craft/roles/ and run any skill.
  Platform Expert: [NOT YET / EARNED] -- run /validate-design with 3+ domain roles active.

DISCOVERY WATCH:
  Falsified: [NOT YET RUN / RUN BUT NOT FALSIFIED / EARNED]
    - NOT YET RUN: no discover-hypothesis artifact exists -- run /discover-hypothesis {value}
    - RUN BUT NOT FALSIFIED: artifact exists but no INCONCLUSIVE/REJECTED/FALSIFIED found
      -- investigate honestly, not just to confirm the hypothesis
    - EARNED: artifact contains falsification language
  The Echo: [NOT YET / EARNED] -- run /rhythm-reflect {value} after your session ends.

Coverage: N/9 namespaces | N skills run | N artifacts
Domain roles active: [none / list of role names]
================================================================
```

The "NEXT RECOMMENDED" section always shows the 2 skills that would unlock the most achievements.
Falsified and The Echo always appear in DISCOVERY WATCH with their status -- they are the
most important ones to track.

If no artifacts exist yet: show all achievements as unearned and recommend starting with
/discover-competitors {value} (unlocks: First Signal + Discover Pioneer + Inertia Identified).
