# Lab 116 - Git commands used

## Creating the repository

```bash
mkdir mypythonrepo
cd mypythonrepo
git init
```
`git init` creates a hidden `.git` directory. That is what makes the folder a
repository.

## Setting my identity

```bash
git config --global user.name "Benard Kimani"
git config --global user.email "benard@example.com"
git config --list
```
Git records the name and email on every commit. Without these the commit fails.

## Checking the status

```bash
git status
```
Shows three things: untracked files, changes not staged, and changes staged for
commit.

## Staging and committing

```bash
touch hello.py
git add hello.py
git status          # hello.py now shows as staged
git commit -m "Add hello.py"
```

`git add` moves the change into the staging area.
`git commit` records the staged changes in the repository.

To stage everything at once:
```bash
git add .
```

## Viewing history

```bash
git log
git log --oneline
git show HEAD
```

## Making another change

```bash
# edit hello.py
git diff                 # what changed but is not staged yet
git add hello.py
git diff --staged        # what is staged but not committed yet
git commit -m "Update the greeting"
```

## Ignoring files

```bash
nano .gitignore
```

Contents:
```
__pycache__/
*.pyc
.env
```

`.gitignore` only affects untracked files. A file that is already tracked keeps
being tracked until you run `git rm --cached filename`.

## Branching

```bash
git branch                       # list branches
git checkout -b new-feature      # create a branch and switch to it
# make changes and commit them
git checkout main                # switch back
git merge new-feature            # merge the branch in
git branch -d new-feature        # delete the merged branch
```

## Undoing things

```bash
git restore filename.py          # discard an unstaged change
git restore --staged filename.py # unstage a file but keep the edit
git commit --amend -m "Better message"
git revert <commit-hash>         # undo a commit that has been pushed
```

## Connecting to a remote

AWS CodeCommit (used in the lab):
```bash
git remote add origin https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo
git push -u origin main
```

GitHub:
```bash
git remote add origin https://github.com/swiftkimani/repo-name.git
git push -u origin main
```

Then day to day:
```bash
git pull    # fetch and merge from the remote
git push    # send commits up
```

## The three areas

```
working directory  --git add-->  staging area  --git commit-->  repository
```

`git status` tells you which area everything is currently in.
