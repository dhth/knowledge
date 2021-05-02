---
title: "Git Stash"
summary:
---

Git Stash
===

Commands
---

```bash
git stash save "message"
git stash list
git stash apply stash@{1}

git checkout stash@{1} -- somedirectory
# only apply stash changes to specific files

# interactive mode
git stash save -p "my commit message"

# see stashed files
git stash show stash@{1}

# see stash contents
git stash show -p stash@{1}
```

[:fontawesome-solid-link: More](https://www.freecodecamp.org/news/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a/).

Squash last n commits
---
```bash
git reset --soft HEAD~n
git commit -m "new message"
```

More [:fontawesome-brands-stack-overflow: here](https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git/5201642#5201642).
