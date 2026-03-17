---
agent: 'agent'
tools: ['codebase']
description: 'User action tracing through UI component tree, state management, and re-render chain.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace a user action through the UI component tree, state management, and renders. For each user action: event fired, component tree traversal, state updates, re-renders triggered, side effects, final UI state. Identify: unnecessary re-renders, missing loading states, error state gaps, accessibility failures. Universal across frontend frameworks. Stock roles: frontend domain expert auto-selected from framework context.

Write artifact to: simulations/trace/component/{topic}-component-{date}.md
