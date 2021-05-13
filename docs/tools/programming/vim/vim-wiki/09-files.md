---
title: Files
summary:
---

Files
===

File utilities
---

```vim

" expand current file path in command line
cnoremap <expr> %%  getcmdtype() == ':' ? expand('%:h').'/' : '%%'
```
