---
title: "Command Line"
summary:
---

Command Line
===

Send escape in a command
---

`<C-v><Esc>` will print `^[` which will send escape in the command.

Join lines
---

Visually select the lines. `:'<,'>j`

Or, `[range]j[lines]`. eg. `5j20` would go to line 5, and join the next 20
lines.
