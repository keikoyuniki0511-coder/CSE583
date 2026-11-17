## My process
### Used `mkdir HW2` and `touch HW2/README.md` to create a new directory and a README.md file in the repository. Recorded the entire gameplay process in README.md and saved screenshots in the HW2 directory after completing each sequence. Finally, used `git add`, `git commit`, and `git push` to upload the HW2 directory to the repository.

## Introduction

### Level intro 1
```bash
git commit && git commit
```

### Level intro 2
```bash
git branch bugFix && git switch bugFix
```

### Level intro 3
```bash
git branch bugFix && git switch bugFix && git commit && git switch main && git commit && git merge bugFix
```

### Level intro 4
```bash
git branch bugFix && git switch bugFix && git commit && git checkout main && git commit && git checkout bugFix && git rebase main
```

## Ramping up
### Level 1
```bash
git switch --detach bugFix
```

### Level 2
```bash
git switch --detach HEAD^
```

### Level 3
```bash
git branch -f bugFix C0
git branch -f main C6
git switch --detach HEAD^
```

### Level 4
```bash
git reset HEAD^
git checkout pushed
git revert pushed
```
## Push & Pull -- Git Remotes!

### Level 1
```bash
git clone
```
### Level 2
```bash
git commit && git switch --detach main && git commit
```

### Level 3
```bash
git fetch
```

### Level 4
```bash
git fetch && git pull
```

### Level 5
```bash
git clone && git fakeTeamwork 2 && git commit && git pull
```

### Level 6
```bash
git commit && git commit && git push
```

### Level 7
```bash
git clone && git fakeTeamwork && git commit && git pull --rebase && git push
```

### Level 8
```bash
git branch -f main o/main && git switch -c feature C2 && git push origin feature
```
