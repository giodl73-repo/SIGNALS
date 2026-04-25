# WorkIQ -- M365 Copilot Query Skill

Query Microsoft internal content through the WorkIQ CLI via the Relay server.

## Input

- **Question(s)**: One or more questions to ask M365 Copilot. Can be free-text queries about internal Microsoft content -- SharePoint docs, Teams messages, emails, eng.ms pages, ADO work items, etc.
- **Output file** (optional): Path to write results. Defaults to printing in conversation.

## Actions to Perform

### 1. Ensure Relay Server is Running

Check if the relay server is up:

```bash
curl -s http://127.0.0.1:8716/list 2>/dev/null
```

- If the curl succeeds (returns JSON), the relay is running. Continue to step 2.
- If the curl fails, tell the user:

> The Relay server is not running. Please start it in a separate terminal:
> ```
> python craftworks/scripts/relay/server.py
> ```
> Then say "ready" and I'll continue.

Do NOT attempt to start the relay server from within Claude Code -- it needs to run as a persistent background process in its own terminal.

### 2. Dispatch the Query

For a **single question**, dispatch via the relay:

```bash
curl -s -X POST http://127.0.0.1:8716/run \
  -H 'Content-Type: application/json' \
  -d '{"script":"scripts/relay/workiq-ask-relay.sh","cwd":"craftworks","args":["THE QUESTION HERE"]}'
```

For **multiple questions**, pass them all as args:

```bash
curl -s -X POST http://127.0.0.1:8716/run \
  -H 'Content-Type: application/json' \
  -d '{"script":"scripts/relay/workiq-ask-relay.sh","cwd":"craftworks","args":["Question 1","Question 2","Question 3"]}'
```

Save the returned `job_id` for polling.

**IMPORTANT**: The questions are passed as `args` array elements, NOT embedded in the script path. The `workiq-ask-relay.sh` script iterates over all args and runs each through the `workiq-ask.cmd` Windows wrapper (required for Entra auth).

### 3. Poll for Completion

WorkIQ queries typically take 30-90 seconds each. Poll the status endpoint:

```bash
curl -s http://127.0.0.1:8716/status/{job_id}
```

Poll every 5 seconds. The job is done when `status` is `"done"` or `"failed"`.

Do NOT use the `/result` endpoint for polling -- it does not block and returns empty output for running jobs.

### 4. Retrieve Results

Once status shows `"done"`:

```bash
curl -s http://127.0.0.1:8716/result/{job_id}
```

The `stdout` field contains the full output with all query results separated by `=== QUERY N ===` headers.

### 5. Present or Save Results

- If the user specified an output file, write the results to that file using the Write tool.
- Otherwise, present a concise summary of the key findings, with the option to save the full output.
- If any query returned empty output, note it -- WorkIQ may have had trouble finding relevant content for that query.

## Writing Multi-Query Scripts

For reusable research (e.g., investigating a topic with multiple angles), create a dedicated `.sh` file in `scripts/relay/`:

```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ASK="$SCRIPT_DIR/workiq-ask.cmd"

echo "=== QUERY 1: Topic angle 1 ==="
cmd.exe //c "$ASK" "Your question about angle 1"
echo ""
echo "---END QUERY 1---"
echo ""

echo "=== QUERY 2: Topic angle 2 ==="
cmd.exe //c "$ASK" "Your question about angle 2"
echo ""
echo "---END QUERY 2---"
```

Then dispatch it:

```bash
curl -s -X POST http://127.0.0.1:8716/run \
  -H 'Content-Type: application/json' \
  -d '{"script":"scripts/relay/your-script.sh","cwd":"craftworks"}'
```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Empty output, exit 0 | workiq ran via Git Bash directly | Always use `cmd.exe //c workiq-ask.cmd` wrapper |
| Relay not responding | Server not started or crashed | Start with `python scripts/relay/server.py` |
| Jobs stuck, no output | Old hung jobs saturating event loop | Restart the relay server |
| Auth failure / empty response | Entra token expired | Run `workiq ask -q "hello"` in a Windows terminal to re-auth |

## Key Files

| File | Purpose |
|------|---------|
| `scripts/relay/server.py` | Relay HTTP server (port 8716) |
| `scripts/relay/jobs.py` | Subprocess job management |
| `scripts/relay/workiq-ask.cmd` | Windows cmd wrapper for workiq (preserves Entra auth) |
| `scripts/relay/workiq-ask-relay.sh` | Multi-question bash entry point |