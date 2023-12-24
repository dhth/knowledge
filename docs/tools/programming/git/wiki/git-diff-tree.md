# git diff-tree

Resources
---

- [git diff-tree][1]

<!-- Links -->
[1]: https://git-scm.com/docs/git-diff-tree


Get names of files changed in a commit
---

The following command returns names of the files ending with `.py` that were
modified in `HEAD`.

```bash
git diff-tree \
    --no-commit-id --name-only \
    --diff-filter=ACMRT -r \
    HEAD -- '*.py'
```

```
A -> added
C -> copied
M -> modified
R -> renamed
T -> changed
```