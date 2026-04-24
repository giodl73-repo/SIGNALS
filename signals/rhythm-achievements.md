You are running /achievements for: {{topic}}

Scan signals/ for artifacts produced on this topic. Check which achievements have been earned.
DISPLAY ONLY — write no files.

---

## STEP 1: Scan artifacts

Find all files matching: signals/**/{{topic}}-*-*.md
Group by namespace using dual-prefix mapping (flat binding uses both old and new names):

  scout/discover namespace: discover-* OR scout-* artifacts
  draft/specify namespace: draft-* OR specify-* artifacts
  review/validate namespace: review-* OR validate-design/validate-code/validate-users/validate-customers/validate-inertia/validate-adoption-blocker artifacts
  flow/simulate namespace: flow-* OR simulate-lifecycle/conversation/trigger/dataflow/integration/throttle/stress/resilience artifacts
  trace namespace: trace-* OR simulate-request/state/contract/component/deployment/migration/permissions artifacts
  prove namespace: prove-* OR discover-hypothesis/discover-websearch/discover-analysis/discover-synthesize artifacts
  listen namespace: listen-* OR validate-feedback/validate-support/validate-adoption artifacts
  rhythm/program namespace: rhythm-* OR program-* artifacts
  roles/topic namespace: roles-* OR org-* OR topic-* artifacts

Count:
- Namespaces touched (N/9 user-facing namespace groups)
- Skills run (unique skill names in artifact filenames)
- Total artifacts produced

---

## STEP 2: Check achievements earned

### EXPLORATION (first use per namespace)
For each namespace where an artifact exists, mark EARNED:
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
- [ ] **Signal Saturated** — 10+ distinct skills run on this topic
- [ ] **Full Scout** — all 8 scout skills: discover-competitors, discover-feasibility, discover-naming, discover-compliance, discover-market, discover-stakeholders, discover-positioning, discover-requirements
- [ ] **Full Prove** — all 7 prove skills: discover-hypothesis, discover-websearch, prove-intelligence, prove-prototype, discover-analysis, prove-interview, discover-synthesize
- [ ] **Full Flow** — all 7 flow skills: flow-lifecycle/simulate-lifecycle, flow-conversation/simulate-conversation, flow-trigger/simulate-trigger, flow-dataflow/simulate-dataflow, flow-integration/simulate-integration, flow-throttle/simulate-throttle, flow-stress/simulate-stress
- [ ] **Full Trace** — all 7 trace skills: simulate-request, simulate-state, simulate-contract, simulate-component, simulate-deployment, simulate-migration, simulate-permissions
- [ ] **Deep Listen** — all 3 listen skills: listen-feedback/validate-feedback, listen-support/validate-support, listen-adoption/validate-adoption

### COVERAGE
- [ ] **Evidence Starter** — 3+ distinct namespace groups covered
- [ ] **Evidence Builder** — 5+ distinct namespace groups covered
- [ ] **Critical Path** — scout/discover + trace + listen namespace groups all present
- [ ] **Fast Coverage** — 5+ namespaces covered (note if all artifacts within the same calendar day)
- [ ] **Pre-Commitment Ready** — 7+ namespace groups covered
- [ ] **Full Coverage** — all 9 namespace groups covered

### CHAIN
- [ ] **Scout-First Spec** — discover-feasibility/scout-feasibility artifact predates any draft-*/specify-* artifact
- [ ] **Evidence-Based Draft** — discover-hypothesis/prove-hypothesis artifact predates any draft-*/specify-* artifact
- [ ] **Grounded Review** — draft-*/specify-* artifact predates review-*/validate-design artifact
- [ ] **Simulation-Before-Build** — simulate-lifecycle/flow-lifecycle predates any trace-type simulate-* artifact
- [ ] **Full Pre-Commit Chain** — scout/discover + draft/specify + review/validate all present in sequence

### QUALITY
- [ ] **Inertia Identified** — any discover-competitors or scout-competitors artifact present
- [ ] **Sharp Hypothesis** — discover-hypothesis/prove-hypothesis artifact contains "specific" and "falsifiable"
- [ ] **The Echo** — rhythm-reflect artifact exists

### DOMAIN
- [ ] **Domain Pioneer** — any artifact produced with domain_roles_active field in frontmatter (at least 1 domain role was loaded during the run)
- [ ] **Platform Expert** — validate-design artifact exists with reviewer_count >= 3 AND domain_roles_active is populated (domain expert reviewers were loaded)
- [ ] **Cross-Domain** — artifacts produced with 2+ distinct domain role areas active (e.g., backend + msft, or backend + dynamics)

### CORP AND CREW
- [ ] **First Review** — any roles-review, org-review, or crew-review artifact exists
- [ ] **PR Reviewed** — any roles-pull-request or org-pr artifact exists
- [ ] **Full Corp** — org-committee artifact exists (full org ROB ran)

### DISCOVERY
- [ ] **Falsified** — discover-hypothesis or prove-hypothesis artifact exists AND contains "INCONCLUSIVE" or "REJECTED" or "FALSIFIED"
  Distinguish: (a) artifact not yet run vs (b) artifact run but hypothesis not yet challenged honestly
- [ ] **Inertia Wins** — any discover-competitors artifact exists AND contains "status quo is sufficient" or "inertia wins" or "do not build"

---

## STEP 3: Display

```
Achievements for: {{topic}}
================================================================

EARNED (N of 38):
  [x] First Signal
  [x] Discover Pioneer
  [x] [other earned]

IN PROGRESS:
  [ ] Critical Path -- need: [missing namespace(s)]
  [ ] Evidence Builder -- covered N/5 namespaces, need [list]

NEXT RECOMMENDED (unlocks the most achievements):
  -> /[skill] {{topic}}    (unlocks: [achievement names])
  -> /[skill] {{topic}}    (unlocks: [achievement names])

DOMAIN WATCH:
  Domain Pioneer: [NOT YET / EARNED] -- install domain roles in .roles/ and run any skill.
  Platform Expert: [NOT YET / EARNED] -- run /validate-design with 3+ domain roles active.

DISCOVERY WATCH:
  Falsified: [NOT YET RUN / RUN BUT NOT FALSIFIED / EARNED]
    NOT YET RUN: run /discover-hypothesis {{topic}}
    RUN BUT NOT FALSIFIED: artifact exists -- investigate honestly, not just to confirm
    EARNED: output contains INCONCLUSIVE, REJECTED, or FALSIFIED
  The Echo: [NOT YET / EARNED] -- run /rhythm-reflect {{topic}} after your session ends.

Coverage: N/9 namespaces | N skills run | N artifacts
Domain roles active: [none / list of role names]
================================================================
```

The "NEXT RECOMMENDED" section always shows the 2 skills that would unlock the most achievements.
Falsified and The Echo always appear in DISCOVERY WATCH -- they are the most important ones.
Falsified is never trivially earned; it requires genuine hypothesis investigation.

If no artifacts exist yet: recommend starting with /discover-competitors {{topic}}
(unlocks: First Signal + Discover Pioneer + Inertia Identified).
