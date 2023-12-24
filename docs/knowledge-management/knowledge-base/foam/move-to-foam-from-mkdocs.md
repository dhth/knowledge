# Move to foam from mkdocs

Just a page to keep track of modifications I had to make to the wiki when moving
from mkdocs to foam.

Commands
---

Remove first 4 lines from all markdown files:

```bash
find docs -name '*.md' | xargs sed -i "" '1,5d'
```

Rename index files:

```bash
find docs -name 'index.md' | pbcopy

# vim macro: 0$F/DF/ly$A/^[pa.md^[j0 (can be used via global)
```

Remove fontawesome links
---

```bash
sed 's/:fontawesome-[a-z-]*: //g'
sed 's/:fontawesome-[a-z-]*://g'
```