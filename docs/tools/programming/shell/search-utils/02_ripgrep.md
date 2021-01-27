---
title: ripgrep
summary:
---

ripgrep
===

Manual filtering
---

Search for `attachment` in all files named `conftest.py`.

```bash
rg -g 'conftest.py' attachment
```

Don't include certain folders
---

```bash
rg --iglob='!.git/' attachment
```

With Vim
---

```bash
:Rg --hidden --iglob='!.git/' -g 'conftest.py' attachment
``` 

Ripgrep powers [CocSearch](../../vim/plugins/coc/01_cocsearch.md).
