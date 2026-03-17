---
name: signal-trace-component
description: User action tracing through UI component tree, state management, and re-render chain.
allowed-tools: [Read, Write, Glob, Grep]
param_set: analysis
---
Trace a user action through the UI component tree, state management, and renders. For each user action: event fired, component tree traversal, state updates, re-renders triggered, side effects, final UI state. Identify: unnecessary re-renders, missing loading states, error state gaps, accessibility failures. Universal across frontend frameworks. Stock roles: frontend domain expert auto-selected from framework context.

Write artifact to: simulations/trace/component/{topic}-component-{date}.md
