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

A first full run took 13 minutes, so keep each step to its time box and do not read alerts aloud.
Open every tab before you start: Security overview, Dependabot alerts, pull request #3, the SQL fix
pull request, and the web editor.

1. **Overview and prioritise (2 min).** Security tab: 7 open Dependabot alerts (2 high, 4 moderate,
   1 low) and 2 open code scanning alerts. Make one point: `app.py` imports only `sqlite3` and
   `flask`, so the `requests` and `pyyaml` alerts are declared but not called by this code.
   Dependabot shows what is declared, not what is reachable. Validate reachability in the customer's code.
2. **Dependabot pull request (1 min).** Open pull request #3 (requests). One pull request clears
   several alerts, so group fixes by package, not by alert. Show the CodeQL check passing on it.
3. **Code scanning (2 min).** Open the SQL injection alert on `main`, then the fix pull request and
   its passing check. Mention the debug mode alert as a prioritisation example. Do not merge the fix.
4. **Push protection (1 min).** In the web editor, paste a Stripe `sk_test_` key and show the block.
   Click Cancel. Never allow the secret and never use a real one. Do not keep the string in the repository.
5. **Close (1 min).** Name the next steps: warn-only code scanning first, then branch protection that
   requires the CodeQL check. `SECURITY.md` and private vulnerability reporting are already added.

## Backup if the live demo fails

Record the walkthrough once and take screenshots of each step. Keep them in a folder next to the slides.

## What I tested versus what I would verify

- Tested by me, on a free public repository:
  - CodeQL ran on `main` and on pull requests, and raised two high alerts in `app.py`
    (SQL injection and Flask debug mode).
  - Dependabot raised alerts and opened pull requests for `flask`, `requests`, `pyyaml` and
    `actions/checkout`. I merged the `pyyaml` pull request. Open alerts fell from 9 to 7.
  - The Dependabot auto-triage preset for development-scoped dependencies is enabled and
    dismissed nothing (Closed = 0).
  - A parameterised-query fix on a branch, with CodeQL run on the pull request.
  - Push protection blocked a Stripe test key in the web editor. I cancelled and nothing was committed.
  - I added `SECURITY.md` and enabled private vulnerability reporting.
  - `app.py` does not import `yaml` or `requests` (checked by reading the imports only).
- Not tested: pushing a secret with `git push` from the command line.
- Taken from documentation, not tested: supported secret patterns, bypass controls and delegated
  bypass, free-tier limits, and behaviour on private repositories.
- Would validate in a customer environment: scan time on large repositories, false-positive rate,
  reachability beyond import checks (including transitive dependencies), SSO and permissions model,
  and licensing for private repositories.
