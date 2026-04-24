# Signal — Role Mapping

Maps every skill to the roles that genuinely improve its output. Roles are only listed
where they add a materially different lens — not assigned by convention.

Cross-cutting roles use the `namespace:role` prefix notation. Bare role names refer to
files in `.roles/`. Customer segment roles (customer/*) and MSFT internal roles
(msft/*) are new additions — see Task 2 output.

---

## Namespace key

| Abbreviation | File |
|---|---|
| pm | .roles/pm.md |
| architect | .roles/architect.md |
| product-marketing | .roles/product-marketing/ROLE.md |
| ux-researcher | .roles/ux-researcher/ROLE.md |
| security | .roles/security/ROLE.md |
| compliance | .roles/compliance/ROLE.md |
| tpm | .roles/tpm/ROLE.md |
| sre | .roles/sre/ROLE.md |
| executive | .roles/executive/ROLE.md |
| inertia | .roles/inertia.md |
| inertia-advocate | .roles/inertia-advocate.md |
| discover:inertia-first | .roles/discover/inertia-first.md |
| discover:evidence-rigor | .roles/discover/evidence-rigor.md |
| discover:falsifiability | .roles/discover/falsifiability.md |
| discover:scope-guardian | .roles/discover/scope-guardian.md |
| specify:commitment-clarity | .roles/specify/commitment-clarity.md |
| specify:reversibility | .roles/specify/reversibility.md |
| specify:scope-integrity | .roles/specify/scope-integrity.md |
| validate:user-centricity | .roles/validate/user-centricity.md |
| validate:adoption-friction | .roles/validate/adoption-friction.md |
| validate:coverage-depth | .roles/validate/coverage-depth.md |
| simulate:contract-integrity | .roles/simulate/contract-integrity.md |
| simulate:failure-mode-coverage | .roles/simulate/failure-mode-coverage.md |
| simulate:inertia-baseline | .roles/simulate/inertia-baseline.md |
| narrate:decision-hygiene | .roles/narrate/decision-hygiene.md |
| narrate:narrative-coherence | .roles/narrate/narrative-coherence.md |
| narrate:commitment-gate | .roles/narrate/commitment-gate.md |
| govern:representation | .roles/govern/representation.md |
| govern:inertia-advocate | .roles/govern/inertia-advocate.md |
| govern:escalation-clarity | .roles/govern/escalation-clarity.md |
| customer:enterprise | .roles/customer/enterprise.md |
| customer:smb | .roles/customer/smb.md |
| customer:isv | .roles/customer/isv.md |
| customer:startup | .roles/customer/startup.md |
| customer:public-sector | .roles/customer/public-sector.md |
| customer:developer | .roles/customer/developer.md |
| msft:pm | .roles/msft/pm.md |
| msft:fte | .roles/msft/fte.md |
| msft:csa | .roles/msft/csa.md |
| msft:field | .roles/msft/field.md |
| msft:tam | .roles/msft/tam.md |

---

## Skill Role Map

| Skill | Primary roles | Cross-cutting | Missing (as of 2026-03-17) |
|---|---|---|---|
| discover-competitors | pm, product-marketing | discover:inertia-first, discover:evidence-rigor | customer:enterprise, customer:startup — different segments weight inertia differently |
| discover-feasibility | pm, architect | discover:evidence-rigor, discover:scope-guardian | msft:fte — first-party implementation constraints invisible to generic architect |
| discover-risk | pm, architect, security | discover:evidence-rigor, discover:falsifiability | customer:enterprise — regulated orgs see risk categories that consumer context misses |
| discover-inertia | pm, inertia | discover:inertia-first | customer:smb, customer:enterprise — switching cost is segment-specific, not universal |
| discover-brainstorm | pm | discover:scope-guardian | — |
| discover-hypothesis | pm, ux-researcher | discover:falsifiability, discover:evidence-rigor | — |
| discover-websearch | pm | discover:evidence-rigor | — |
| discover-analysis | architect, ux-researcher | discover:evidence-rigor, discover:falsifiability | msft:fte — internal telemetry/schema analysis needs platform context |
| discover-synthesize | pm | discover:evidence-rigor, discover:falsifiability, narrate:narrative-coherence | — |
| discover-orchestrate | pm | discover:inertia-first, discover:evidence-rigor, discover:falsifiability | — |
| discover-causal | pm, ux-researcher | discover:falsifiability, discover:evidence-rigor | — |
| discover-coherence | pm | discover:evidence-rigor, discover:falsifiability, narrate:narrative-coherence | — |
| discover-compare | pm, architect | discover:falsifiability, discover:scope-guardian | — |
| discover-competitors-alt | pm, product-marketing | discover:inertia-first, discover:evidence-rigor | customer:enterprise, customer:startup |
| discover-feasibility-alt | pm, architect | discover:evidence-rigor, discover:scope-guardian | msft:fte |
| specify-spec | pm, architect | specify:commitment-clarity, specify:scope-integrity, specify:reversibility | msft:pm — BIC/OKR alignment check belongs here; customer:enterprise — IT approval surface area |
| specify-proposal | pm, architect | specify:commitment-clarity, specify:reversibility | executive — proposals route to exec for go/no-go; msft:pm |
| specify-pitch | pm, product-marketing, executive | narrate:narrative-coherence | customer:enterprise, customer:smb — segment-differentiated pitch framing |
| specify-commitment | pm, tpm | specify:commitment-clarity, specify:scope-integrity, narrate:commitment-gate | msft:pm — OKR/milestone gate language |
| validate-design | pm, ux-researcher, architect | validate:user-centricity, validate:adoption-friction, validate:coverage-depth | customer:developer — bottom-up UX expectations differ sharply from enterprise UX |
| validate-code | architect, security | simulate:contract-integrity | msft:fte — first-party compliance requirements (SFI, SDL) |
| validate-users | ux-researcher | validate:user-centricity, validate:coverage-depth | customer:developer, customer:smb — persona coverage gaps |
| validate-customers | pm | validate:user-centricity, validate:adoption-friction, validate:coverage-depth | customer:enterprise, customer:isv, customer:public-sector — the 12-persona matrix needs segment-specific stress |
| validate-feedback | pm, ux-researcher | validate:user-centricity, validate:adoption-friction | customer:enterprise, customer:smb — feedback framing is segment-specific |
| validate-support | pm, sre | validate:coverage-depth | customer:enterprise — enterprise support SLAs and escalation paths differ from SMB |
| validate-adoption | pm, ux-researcher | validate:adoption-friction, validate:user-centricity | customer:enterprise, customer:smb, customer:startup — adoption arc varies sharply by segment |
| validate-inertia | pm, inertia | validate:adoption-friction, discover:inertia-first | customer:enterprise, customer:smb, customer:developer — inertia profile is segment-specific |
| simulate-lifecycle | architect | simulate:contract-integrity, simulate:failure-mode-coverage | msft:fte — platform runtime constraints; msft:field — real deployment behavior |
| simulate-conversation | architect | simulate:contract-integrity, simulate:failure-mode-coverage | — |
| simulate-stress | architect, sre | simulate:failure-mode-coverage, simulate:inertia-baseline | msft:fte — platform failure modes under Microsoft infrastructure |
| simulate-request | architect | simulate:contract-integrity | msft:fte |
| simulate-state | architect | simulate:contract-integrity, simulate:failure-mode-coverage | — |
| simulate-contract | architect, security | simulate:contract-integrity | msft:fte — first-party contract enforcement patterns |
| simulate-permissions | architect, security | simulate:contract-integrity | msft:fte — first-party RBAC, msft:csa — permissions questions are top customer escalation |
| tools-coverage | — | — | — (meta/internal tool, no external roles) |
| tools-preview | — | — | — |
| tools-accept | — | — | — |
| signal | — | — | — (command index, no review needed) |
| signal-setup | — | — | — |
| signal-layout | — | — | — |
| signal-check | pm | narrate:decision-hygiene, narrate:commitment-gate | msft:pm — BIC/OKR readiness check; customer:enterprise — readiness criteria differ by customer risk tier |
| narrate-status | pm | narrate:decision-hygiene | — |
| narrate-story | pm, product-marketing | narrate:narrative-coherence, narrate:decision-hygiene | customer:enterprise, customer:startup — story framing differs by segment |
| narrate-decide | pm, executive | narrate:decision-hygiene, narrate:commitment-gate, discover:inertia-first | msft:pm |
| narrate-behavior | architect | simulate:contract-integrity, simulate:failure-mode-coverage | msft:fte |
| narrate-qa | pm, ux-researcher | validate:user-centricity, validate:coverage-depth, narrate:commitment-gate | customer:enterprise, customer:developer |
| narrate-brief | pm, executive | narrate:narrative-coherence, narrate:decision-hygiene | msft:pm, msft:csa — CSA needs customer-facing brief framing |
| govern-scan | tpm, architect | govern:representation | msft:pm — org.yaml generation needs BIC org shape |
| govern-build | tpm, executive | govern:representation, govern:inertia-advocate | msft:pm |
| govern-product-review | pm, tpm, executive | govern:representation, govern:inertia-advocate, govern:escalation-clarity | msft:pm, msft:tam — TAM surfaces customer escalations into ROB |
| govern-pull-request | architect, security | govern:escalation-clarity | msft:fte, msft:pm — first-party PR review expectations |
| govern-roles | tpm | govern:representation | msft:pm — BIC org roles have specific shapes not in generic domain |
| govern-chart | tpm | govern:representation | msft:pm |
| govern-check | pm, architect | govern:representation, govern:inertia-advocate, govern:escalation-clarity | — |
| govern-committee | pm, tpm, executive | govern:representation, govern:inertia-advocate, govern:escalation-clarity | msft:pm, msft:tam — enterprise TAM perspective at committee |
| quest-rubric | — | — | — (internal eval tool) |
| quest-variate | — | — | — |
| quest-score | — | — | — |
| quest-golden | — | — | — |

---

## Gap Summary

### Missing customer roles (created in Task 2)

| Segment | Skills where it matters most |
|---|---|
| customer:enterprise | discover-competitors, discover-inertia, validate-customers, validate-adoption, validate-inertia, narrate-story, specify-spec |
| customer:smb | discover-inertia, validate-adoption, validate-inertia, validate-feedback, specify-pitch |
| customer:isv | validate-customers, discover-competitors |
| customer:startup | discover-competitors, validate-adoption, specify-pitch |
| customer:public-sector | discover-risk, validate-customers, specify-spec |
| customer:developer | validate-design, validate-users, narrate-qa |

### Missing MSFT internal roles (created in Task 2)

| Role | Skills where it matters most |
|---|---|
| msft:pm | specify-spec, specify-proposal, specify-commitment, narrate-decide, narrate-brief, govern-product-review |
| msft:fte | discover-feasibility, discover-analysis, simulate-lifecycle, simulate-contract, validate-code, narrate-behavior |
| msft:csa | narrate-brief, govern-committee, simulate-permissions |
| msft:field | simulate-lifecycle, validate-adoption |
| msft:tam | govern-product-review, govern-committee |

### Roles that already exist and are correctly scoped

The existing cross-cutting roles (discover:inertia-first, validate:adoption-friction,
govern:inertia-advocate, narrate:commitment-gate etc.) map cleanly onto their namespace
skills. The gap is entirely in customer segment representation and MSFT-internal context.

---

## Design notes

**Why customer roles are new**

The 12-persona matrix in validate-customers (C-01 through C-12) provides quantified
coverage but those personas are defined inside the skill. The customer/* roles provide
persistent segment lenses that can review ANY skill output — not just validate-customers.
The enterprise customer cares about inertia in governance/procurement terms that no
existing role captures. The SMB customer cares about quick ROI with zero IT overhead.

**Why msft/* roles are new**

Signal is built in a Microsoft context (BIC, Power Platform, D365, Dataverse). Several
skills — specify-spec, narrate-decide, govern-product-review — produce artifacts that
must pass internal Microsoft review gates (OKR alignment, BIC metrics, SFI compliance).
No existing role checks for those constraints. The msft/* roles fill that gap.

**What was NOT added**

Roles like `pm`, `architect`, `security`, `ux-researcher`, `sre` already exist and are
well-scoped. The mapping above uses them where they genuinely improve output. They are
not listed on skills where they would read the output the same way any role would.
