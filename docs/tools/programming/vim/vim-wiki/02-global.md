---
title: Global
summary:
---

global
===

Resources
---
- [:fontawesome-solid-play-circle: Video](https://www.youtube.com/watch?v=JgZu5-FNeMk)
- [:fontawesome-solid-play-circle: Video by ThePrimeagen](https://www.youtube.com/watch?v=CN8p9iL7PPI)

`:g`
---

```
:g/pattern_to_look_for/command
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

Global in a visual block
---

```vim
:'<,'>g/\%V./norm! 0dt.dw
```

Examples
---

### Move lines to end of file

```vim
:g/import/m$
" moves all lines containing the word 'import' to the end of the file
```

### Make the first word in a markdown list bold

Suppose we have the following list:

```
- word1 -- some text
- word2 -- some text
- word2 -- some text
```

`g` command to make the first word bold:

```vim
:.,$g/^-/norm! wi**^[wea**
```

Getting gq to behave nicely with lists
---

`:set fo-=q` seems to work. Needs more investigation.
