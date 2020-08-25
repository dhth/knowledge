g
===

Resources
---
- [:fontawesome-solid-play: Video](https://www.youtube.com/watch?v=JgZu5-FNeMk)
- [:fontawesome-solid-play: Video by ThePrimeagen](https://www.youtube.com/watch?v=CN8p9iL7PPI)

`:g`
---

```
:g/pattern_to_look_for/command
```

A few examples:

```vim
:g/import/m$
" moves all lines containing the word "import" to the end of the file
```

`g`
---

```vim
g<         " reopen output of last command
g&         " replay last substitute command
gU{motion} " uppercase
gu{motion} " lowercase
gF         " go to specific line in a file
11g_       " go to the end of the 10th line below
gv         " re-highlight last highlighted region
gi         " jump to last insert location
```
