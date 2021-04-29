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

Integrating directly with the shell
---

`:.!bash` will send the current line to the shell, and replace the line with the
command output. `bash` can be any other shell command.

For example, running `:.!python` on:

```python
for i in range(3): print(f'{i})')
```

will replace the line with

```
0)
1)
2)
```

More [:fontawesome-solid-link:
here](https://rwx.gg/tools/editors/vi/how/magic/).
