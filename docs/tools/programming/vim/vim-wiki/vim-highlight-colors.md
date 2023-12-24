Vim Highlight Colors
===

Resources
---

- [How do I customize vimdiff colors?][1]

<!-- Links -->
[1]: https://vi.stackexchange.com/questions/10897/how-do-i-customize-vimdiff-colors

<!-- Links end -->

Highlight colors
---

```vim
hi Search       gui=none    guifg=#282a36          guibg=#ff5555
```

Custom Diff Colors
---

```vim
hi DiffAdd      gui=none    guifg=#1F2F38          guibg=#84B97C
hi DiffChange   gui=none    guifg=none             guibg=none
hi DiffDelete   gui=bold    guifg=#1F2F38          guibg=#DC657D
hi DiffText     gui=bold    guifg=#1F2F38          guibg=#D4B261
```
