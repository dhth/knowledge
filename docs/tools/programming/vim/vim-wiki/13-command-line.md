Command Line
===

Resources
---

- [Format JSON in Vim with jq  Today I Learned][1]
- [Integrate Shell Commands Into Vi Workflow][2]

<!-- Links -->
[1]: https://til.hashrocket.com/posts/ha0ci0pvkj-format-json-in-vim-with-jq
[2]: https://rwx.gg/tools/editors/vi/how/magic/

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

More [here][2].

Format embedded JSON in a markdown file
---

Let's say you have some JSON in a markdown file like this:

```
{
"event": {
"op": "INSERT",
"something": "else"
}
}
```

Visually select the lines containing the JSON content, and run

```
:'<,'>!jq
```

Inspiration from [this][1] post.
