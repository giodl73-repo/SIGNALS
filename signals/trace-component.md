confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace a user action through the UI component tree, state management, and renders. For each user action: event fired, component tree traversal, state updates, re-renders triggered, side effects, final UI state. Identify: unnecessary re-renders, missing loading states, error state gaps, accessibility failures. Universal across frontend frameworks. Stock roles: frontend domain expert auto-selected from framework context.

Write artifact to: signals/trace/component/{topic}-component-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
