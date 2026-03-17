---
name: validate
description: "Validate a design against users and customers. Combines review + listen into a complete
validation brief covering expert opinion, user usability, customer adoption, and
post-ship signal prediction.

Covers:
- review-design     -> multi-expert design review through 6 disciplines
- review-users      -> 5 persona advocates walk through design with usability scores
- review-customers  -> 12 customer personas evaluate for usefulness and would-adopt
- listen-feedback   -> pre-ship customer reaction with per-persona NPS prediction
- listen-adoption   -> adoption curve simulation across Rogers archetypes with chasm analysis

Output: a validation brief with expert findings, per-persona usability scores,
customer adoption prediction, and NPS forecast. Includes a go/no-go readiness
signal with the top 3 blockers if the answer is no-go.

Use after drafting a spec and before committing to engineering scope. The validation
brief surfaces the riskiest assumptions before they become shipped bugs.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: full
---
Validate the design for: {{topic}} against real users and customers.

Run the full validation suite:

1. **review-design** — 6-discipline design review
2. **review-users** — 5-persona user walkthrough  
3. **review-customers** — 12-persona customer NPS analysis
4. **listen-feedback** — predict support ticket themes
5. **listen-adoption** — model the adoption curve

Final output: validation brief at simulations/{{topic}}/validate-{{date}}.md
with findings ranked by adoption impact.
