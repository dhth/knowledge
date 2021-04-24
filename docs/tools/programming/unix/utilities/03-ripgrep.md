---
title: ripgrep
summary:
---

ripgrep
===

Respources
---

- [:fontawesome-brands-github:
    Guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)

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
