Git Push
===

Git push default behaviour
---

Git's default is `simple`. In this mode, pushes the current branch to its upstream branch, but refuses to push if the upstream's branch name is different from the local one.

```bash
git config --global push.default current
```

Pushes the current branch to a remote branch of the same name.

[:fontawesome-solid-link:
More](https://stackoverflow.com/questions/948354/default-behavior-of-git-push-without-a-branch-specified).
