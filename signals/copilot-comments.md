# /copilot-comments — Copilot PR Comment Handler

Retrieve all Copilot review comments on the current PR, triage each (fix or defer), and reply.

## Usage

```
/copilot-comments              # auto-detect PR from current branch
/copilot-comments 426          # explicit PR number
/copilot-comments --check      # just list comments, don't fix or reply
```

## Workflow

### 1. Identify the PR

If no PR number is given, detect from the current branch:
```bash
gh pr list --state open --head "$(git branch --show-current)" --json number,title --jq '.[0].number'
```

### 2. Fetch Copilot comments

```bash
gh api repos/{owner}/{repo}/pulls/{pr}/comments \
  --jq '.[] | select(.user.login | test("copilot|github-actions|bot"; "i")) | {id, path, line, body, created_at}'
```

### 3. Triage each comment

For each comment, classify as one of:

| Action | When | What to do |
|--------|------|------------|
| **FIX** | Simple, correct, low-risk | Make the code change, reply with what was fixed |
| **DEFER** | Architectural, needs discussion, or out of scope | Reply explaining why it's deferred |
| **REJECT** | Incorrect suggestion (e.g., tests prove otherwise) | Reply with evidence |

**Before fixing**: Read the file and understand context. Check if tests validate the current behavior.

### 4. Apply fixes

For FIX items:
1. Read the file at the specified path and line
2. Make the fix
3. Run relevant tests to verify: `cd craft-cli && npx vitest run <relevant-test>`

### 5. Reply to all comments

Reply to each comment using:
```bash
# Write reply to temp file (avoids shell escaping issues)
printf 'Reply text here' > /tmp/copilot-reply.txt
gh api repos/{owner}/{repo}/pulls/comments/{comment_id}/replies \
  -X POST --input /tmp/copilot-reply.txt
```

**IMPORTANT**: Never use `--body` or `-f body=` with inline text for replies — backticks, quotes, and special characters break shell escaping. Always use a temp file.

Alternative (simpler for short replies):
```bash
gh api repos/{owner}/{repo}/pulls/comments/{id}/replies \
  -X POST -f body="Short plain text reply"
```

### 6. Commit and push

After all fixes:
```bash
git add <fixed-files>
git commit -m "Fix Copilot review comments on PR #<number>"
git push
```

## Reply Templates

### FIX
```
Fixed — [one-line description of what changed].
```

### DEFER
```
Acknowledged — deferring to [phase/ticket]. [One-line reason].
```

### REJECT
```
Keeping current behavior — [reason]. [Evidence: test name or spec reference].
```

## Notes

- Copilot comments arrive in two batches (initial review + after CI). Run this skill after both batches.
- The `--check` flag skips fixing and replying — useful for previewing comments.
- Comments on files you didn't change in this PR are usually pre-existing issues surfaced by the large diff. Defer these.
- Always verify fixes don't break tests before replying.