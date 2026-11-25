# Application security demo (GitHub)

A small, intentionally vulnerable Flask app used to demonstrate GitHub's built-in security features
to a fictitious customer. It contains no real data or secrets. Do not deploy it.

## What each file is for

| File | Demo purpose |
|---|---|
| `app.py` | Deliberate SQL injection for CodeQL to find |
| `requirements.txt` | Old pinned packages for Dependabot alerts and update pull requests |
| `.github/workflows/codeql.yml` | Code scanning with CodeQL on push, pull request and weekly |
| `.github/dependabot.yml` | Weekly Dependabot version updates for pip and GitHub Actions |

## Set up (once, before the interview)

1. Create a **public** repository on your free GitHub account and push these files to `main`.
2. In **Settings > Code security**, turn on: Dependabot alerts, Dependabot security updates,
   secret scanning, and push protection.
3. Wait for the CodeQL run in the **Actions** tab to finish, then open **Security > Code scanning**.
4. Confirm you see a SQL injection alert and Dependabot alerts for `requests` and `pyyaml`.
   Not verified: the exact alerts and free-tier limits. Check them in the GitHub documentation
   and in your own repository before the interview.

## Demo script (about 7 minutes)

1. **Security overview (1 min).** Show the Security tab: alerts grouped by type and severity.
2. **Prioritise (2 min).** Sort Dependabot alerts by severity. Explain why you fix secrets and
   known-vulnerable dependencies first (high value, low developer friction).
3. **Dependabot pull request (1 min).** Open a Dependabot security update pull request and show
   the proposed version bump and the checks that run on it.
4. **Code scanning (2 min).** Open the SQL injection alert, show the data-flow path, and describe
   how you would roll scanning out as warn-only first, then enforce it.
5. **Push protection (1 min).** Try to commit a fake credential and show the block.
   Use a token format taken from GitHub's secret scanning documentation. Never use a real secret.
   Do not commit it beforehand, or it will block your own push.

## Backup if the live demo fails

Record the walkthrough once and take screenshots of each step. Keep them in a folder next to the slides.

## What I tested versus what I would verify

Fill this in after you run it:

- Tested by me: _(for example, CodeQL run completed, alert appeared)_
- Taken from documentation: _(for example, free-tier feature availability)_
- Would validate in a customer environment: _(for example, scan time on large repositories,
  false-positive rate, SSO and permissions model)_
