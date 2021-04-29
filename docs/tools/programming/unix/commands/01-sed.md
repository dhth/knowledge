---
title: "sed"
summary:
---

sed
===

Print a range of lines
---

```bash
sed -n '1,100 p' file.txt
```

Use environment variables in sed
---

```bash
# sed -e "s/$WIKI_DIR\/docs/string_to_replace_with/"  this doesn't work
sed -e 's@'"$WIKI_DIR/docs/"'@string_to_replace_with@'
sed -e "s|$WIKI_DIR/docs/|string_to_replace_with|"
```
