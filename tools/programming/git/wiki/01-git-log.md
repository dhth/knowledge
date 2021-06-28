Git Log
===

Pretty git log
---

```bash
alias gl='git log --all --color --graph --pretty=format:'"'"'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"'"' --abbrev-commit'
```

More [here](https://git-scm.com/docs/pretty-formats).

See git log for specific branch
---

First, use `git log` with fancy coloring.

```bash
alias glb='git log --color --graph --pretty=format:'"'"'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'"'"' --abbrev-commit'
```

More [here](https://stackoverflow.com/questions/4649356/how-do-i-run-git-log-to-see-changes-only-for-a-specific-branch).

Usage:

```bash
glb origin/master..some branch
```

Since
---

```bash
git log --since="1 month ago"
git log --since="3 days ago"
```

Max count
---

```bash
git log --max-count=100
```
