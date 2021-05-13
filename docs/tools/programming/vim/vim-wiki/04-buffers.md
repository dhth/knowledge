---
title: Buffers
summary:
---

Buffers
===

Delete all other buffers
---

```vim
command! BufOnly execute '%bdelete|edit #|normal `"'
```

More [:fontawesome-solid-link: here](https://salferrarello.com/vim-close-all-buffers-except-the-current-one/).
