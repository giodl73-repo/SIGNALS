# GitHub Copilot Batch Test
Date: 2026-03-19 | Topic: ai-code-review | Skills: 11 | Duration: ~39 min

## Results: 8 passed / 3 failed (copilot process crash)

| Skill | Result | Size | Note |
|-------|--------|------|------|
| discover-inertia | FAIL | 3KB | Copilot process crash (Node.js SIGSEGV) during file I/O |
| discover-hypothesis | FAIL | 4.4KB | Copilot process crash during file I/O |
| specify-proposal | FAIL | 5.3KB | Copilot process crash during file I/O |
| validate-design | PASS | 6.5KB | Full 5-block review — largest skill, works fine |
| validate-customers | PASS | 2.9KB | 12-persona scoring works |
| simulate-state | PASS | 0.7KB | State trace works |
| rhythm-status | PASS | 2.2KB | Display-only, works perfectly |
| rhythm-decide | PASS | 2.5KB | Campaign orchestration works |
| roles-check | PASS | 2.3KB | Role-based review works |
| signal-health | PASS | 1.4KB | Workspace health check works |
| tools-coverage | PASS | 2.2KB | Coverage stats display works |

## vs Claude batch (same 11 skills): 11/11 passed

| Group | Copilot | Claude |
|-------|---------|--------|
| discover | 0/2 | 2/2 |
| specify | 0/1 | 1/1 |
| validate | 2/2 | 2/2 |
| simulate | 1/1 | 1/1 |
| rhythm | 2/2 | 2/2 |
| roles | 1/1 | 1/1 |
| signal/tools | 2/2 | 2/2 |

## Key findings

1. The 3 failures are copilot process crashes (Node.js SIGSEGV), not prompt content errors.
   The crash occurs during file I/O operations mid-execution. Not a Signal prompt bug.

2. validate-design (6.5KB, most complex skill) passes — disproving the size theory.
   The crashes appear to be a copilot CLI stability issue specific to certain execution paths.

3. The `.prompt.md` format works for 73% of skills directly without modification.
   `mode: agent` + `{{topic}}` substitution works correctly in all passing cases.

4. `signals/` artifact paths are valid for Copilot — Copilot can write to the workspace.

## Next: workaround for crashes
Use `--no-file-io` flag or split the Glob/Read instructions into separate tool calls.
Or test with newer copilot CLI version.
