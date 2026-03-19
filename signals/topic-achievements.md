You are running /achievements for: {{topic}}

Scan simulations/ for artifacts produced on this topic. Check which achievements have been earned.
DISPLAY ONLY — write no files.

---

## STEP 1: Scan artifacts

Find all files matching: simulations/**/{{topic}}-*-*.md
Group by namespace: discover/, specify/, validate/, simulate/, rhythm/, roles/, tools/

Count:
- Namespaces touched (N/8 user-facing namespaces)
- Skills run (unique skill names in artifact filenames)
- Total artifacts produced

---

## STEP 2: Check achievements earned

### EXPLORATION (first use per namespace)
For each namespace where an artifact exists, mark EARNED:
- [ ] **First Signal** — any artifact exists
- [ ] **Discover Pioneer** — any discover-* artifact
- [ ] **Specify Founder** — any specify-* artifact
- [ ] **Validate Reviewer** — any validate-* artifact
- [ ] **Simulate Tracer** — any simulate-* artifact
- [ ] **Rhythm Planner** — any rhythm-* artifact
- [ ] **Roles Builder** — any roles-* artifact

### COVERAGE
- [ ] **Evidence Starter** — 3+ namespaces covered
- [ ] **Critical Path** — discover + simulate + validate all present
- [ ] **Pre-Commitment Ready** — 5+ namespaces covered
- [ ] **Full Coverage** — 7+ namespaces covered

### CHAIN
- [ ] **Evidence-Based Draft** — discover-* artifact predates any specify-* artifact
  (check file dates: discover artifact date < specify artifact date)
- [ ] **Grounded Review** — specify-* artifact predates validate-* artifact
- [ ] **Simulation-Before-Build** — simulate-* artifact exists (pre-implementation check)
- [ ] **Scout-First Spec** — discover-requirements predates specify-spec

### DISCOVERY
- [ ] **The Echo** — rhythm-reflect artifact exists (ran /rhythm-reflect)
- [ ] **Inertia Identified** — any discover-inertia artifact exists
- [ ] **Falsified** — discover-hypothesis artifact exists AND contains "INCONCLUSIVE" or "FALSIFIED"

---

## STEP 3: Display

```
Achievements for: {{topic}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EARNED (N):
  ✓ First Signal
  ✓ Discover Pioneer
  ✓ [other earned]

IN PROGRESS:
  ○ Full Coverage — need 3 more namespaces
     Missing: simulate, rhythm, roles

NEXT RECOMMENDED:
  → /simulate-contract {{topic}}   (unlocks: Simulate Tracer + Critical Path)
  → /rhythm-status {{topic}}       (unlocks: Rhythm Planner)

DISCOVERY:
  Falsified: NOT YET — run /discover-hypothesis {{topic}} and investigate honestly.
  The Echo: NOT YET — run /rhythm-reflect {{topic}} after this session ends.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The "NEXT RECOMMENDED" section always shows the 2 skills that would unlock the most achievements.
The Falsified and Echo achievements always appear in DISCOVERY with their status — they are the
most important ones. Falsified is never "complete" — there is always another hypothesis to test.
