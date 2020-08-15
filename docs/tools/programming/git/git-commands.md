# Git Commands

## Pretty git log

```bash
alias gl='git log --all --color --graph --pretty=format:'"'"'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"'"' --abbrev-commit'
```

More [here](https://git-scm.com/docs/pretty-formats).

## See git log for specific branch

First, use `git log` with fancy coloring.

```bash
alias glb='git log --color --graph --pretty=format:'"'"'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"'"' --abbrev-commit'
```

More [here](https://stackoverflow.com/questions/4649356/how-do-i-run-git-log-to-see-changes-only-for-a-specific-branch).

Usage:

```bash
glb origin/master..some branch
```

## Remove untracked files

```bash
# dry run
git clean somedirectory -n
# deletes files
git clean somedirectory -f
```

## Get changes from a branch to a specific directory

```bash
git checkout some_branch some_dir
# will only update some_dir with changes from some_branch
```

## Git push default behaviour

Git's default is `simple`. In this mode, pushes the current branch to its upstream branch, but refuses to push if the upstream's branch name is different from the local one.

```bash
git config --global push.default current
```

Pushes the current branch to a remote branch of the same name.

[:fontawesome-solid-link:
More](https://stackoverflow.com/questions/948354/default-behavior-of-git-push-without-a-branch-specified).

## Git stash
```bash
git stash save "message"
git stash list
git stash apply stash@{1}

# interactive mode
git stash save -p "my commit message"
```

[:fontawesome-solid-link: More](https://www.freecodecamp.org/news/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a/).
