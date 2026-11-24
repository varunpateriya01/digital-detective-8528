# Mission 6 — Git and GitHub

## 1. Mission title
Mission 6 — Git and GitHub

## 2. Task / objective
Use Git to inspect repository state and history, stage and commit a selected change, create a branch, and open a Pull Request.

## 3. Work completed
I inspected the repository status and commit history, created the `update-about` branch, and added a `My Learning` section to the root README. I staged the two documentation files, committed the branch changes, pushed the branch to GitHub, and opened a Pull Request into `main`. The PR is #1, left open and unmerged because merging is only required if the instructor requests it.

### Git command glossary

| Operation | Command | What it does |
|---|---|---|
| Initialize a repository | `git init` | Creates local Git metadata and starts tracking history. |
| Check status | `git status` | Shows the current branch and modified, staged or untracked files. |
| Stage selected changes | `git add README.md` | Selects a file's current changes for the next commit. |
| Create a commit | `git commit -m "message"` | Records staged changes as a named point in history. |
| View history | `git log --oneline` | Shows recent commits in a compact form. |
| Create/list branches | `git branch update-about`; `git branch` | Creates a separate line of work or lists existing branches. |
| Switch branches | `git switch update-about` | Changes the working copy to another branch. |
| Publish a branch | `git push -u origin update-about` | Sends the branch and its commits to GitHub. |
| Retrieve remote changes | `git pull` | Fetches and integrates updates from the tracked remote branch. |

Staging and committing are separate steps. Staging chooses which edits belong in the next snapshot; committing saves that staged snapshot in local history. A branch keeps a proposed change separate from `main`, and a Pull Request lets people review and discuss it before merging.

## 4. Commands / tools used
- `git status --short --branch` — checked the current branch and working tree.
- `git log --oneline` — reviewed the commit history.
- `git switch -c update-about` — created and switched to the feature branch.
- `git add README.md mission-06-git-github/README.md` — staged the selected documentation changes.
- `git commit -m "Complete Git and GitHub collaboration mission"` — recorded the branch changes.
- `git push -u origin update-about` — published the branch.
- GitHub Pull Request page — opened the PR into `main`.

## 5. My understanding
Git records snapshots of a project so changes can be reviewed and recovered. A branch gives one change its own history while the main line stays stable. A Pull Request shows the branch changes for review and makes it possible to discuss or request edits before merging.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- Root `README.md` — includes the `My Learning` section on the `update-about` branch.
- [Pull Request #1](https://github.com/varunpateriya01/digital-detective-8528/pull/1) from `update-about` into `main` — open and not merged.
- Commit history on GitHub — shows separate mission checkpoints.

## 9. Commit details
Commit message: `Complete Git and GitHub collaboration mission`. The branch and PR are visible on GitHub; merge status is open / not merged.
