---
title: "coc.nvim"
summary:
---

coc.nvim
===

Resources
---
- [:fontawesome-brands-github:
    neoclide/coc.vim](https://github.com/neoclide/coc.nvim)

Modules
---

- [:fontawesome-solid-folder: Language Servers](language-servers/index.md)
- [:fontawesome-solid-file-alt: CocSearch](01-cocsearch.md)
- [:fontawesome-solid-file-alt: Toggle Suggestions or
    Sources](02-toggle-suggestions-or-sources.md)


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
