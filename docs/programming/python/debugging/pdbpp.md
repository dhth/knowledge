---
title: "pdbpp"
summary:
---

pdbpp
===

Use pdbpp's in sticky mode by default
---

pdbpp's `sticky` command keeps the source code fixed in position, and only moves the line highlighter down. To enable it by default, create a `~/.pdbrc.py` file with the following contents:

```python
import pdb
class Config(pdb.DefaultConfig):
    sticky_by_default = True
```

More on this [here](https://gist.github.com/justinabrahms/44b077ee314914b3ff78).
