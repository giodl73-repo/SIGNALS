Show the current state of a topic in the terminal. Signal coverage, open gaps, readiness for target outcome. Does NOT write a file -- display only. For a written artifact use topic-report. Globs signals/**/{topic}-* to discover all signals. Cross-references against strategy.md planned signals. Computes coverage percentage.

Write artifact to: none (terminal display only)
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
