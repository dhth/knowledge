---
title: "Move to Foam"
summary:
---

Move to Foam
===

Commands
---

Remove first 4 lines from all markdown files:

```bash
find docs -name '*.md' | xargs sed -i "" '1,4d'
```

Rename index files:

```bash
find docs -name 'index.md' | pbcopy

# vim macro: 0$F/DF/ly$A/^[pa.md^[j0
```

