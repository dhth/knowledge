find
===

Find with a pattern and rename
---

Replace `"_"` in all markdown files in a directory with `"-"`.

```bash
find . -type f -name "*_*.md" -exec bash -c 'mv "$0" "${0/_/-}"' {} \;
```

Find and replace recursively in a directory
---

```bash
find docs -name '*.md' | xargs sed -i "" 's/\[/\[:fontawesome-solid-link: /g'
```
