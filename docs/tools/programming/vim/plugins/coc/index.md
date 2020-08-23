Coc
===

Resources
---
- [:fontawesome-brands-github:
    neoclide/coc.vim](https://github.com/neoclide/coc.nvim)

Modules
---
- [:fontawesome-solid-file-alt: Coc-Python](coc-python.md)

CocSearch
---

```
:CocSearch whateverstring -A 20
// returns buffer with instances of
// whateverstring along with 20 more lines
```

Open jump definition in a new tab
---

[:fontawesome-solid-link: Goto Definition in Vsplit? · Issue #1249 ·
neoclide/coc.nvim](https://github.com/neoclide/coc.nvim/issues/1249)

```bash
:call CocAction('jumpDefinition', 'tabe')
```

Move to floating window
---

`<c-w><c-w>` switches between windows.
