---
title: "Execute"
summary:
---

Execute
===

Usage
---

`execute` in conjuction with `normal!` let's us escape special characters.

```
:execute "normal! mqA;\<esc>`q"
```

Breakdown:

- `:execute "normal! ..."`: run the sequence of commands as if they were
entered in normal mode, ignoring all mappings, and replacing string escape
sequences with their results.
- `mq`: store the current location in mark "q".  `A`: move to the end of the
- current line and enter insert mode after the last
character.
- `;`: we're now in insert mode, so just put a literal semicolon in the file.
- `\<esc>`: this is a string escape sequence which resolves to a press of the
escape key, which takes us out of insert mode.
- ``q`: return to the exact location of mark "q".

Regex in commands
---

```
:execute "normal! gg" . '/for .\+ in .\+:' . "\<cr>"
```

The middle component will be treated as a literal string, so we don't need to
escape `.\+`.

Very Magic
---

```
:execute "normal! gg" . '/\vfor .+ in .+:' . "\<cr>"
```

This tells Vim to use its "very magic" regex parsing mode, which is pretty much
the same as you're used to in any other programming language.

Escaping characters
---

If the cursor is on the word `don't`:

```
:echom expand("<cWORD>")
" will output don't
```

```
:echom shellescape(expand("<cWORD>"))
" will output 'don'\''t'
```

More [:fontawesome-solid-link:
here](https://learnvimscriptthehardway.stevelosh.com/chapters/32.html).
