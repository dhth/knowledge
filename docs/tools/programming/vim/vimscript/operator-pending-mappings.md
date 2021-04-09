---
title: "Operator Pending Mappings"
summary:
---

Operator Pending Mappings
===

Resources
---
- [:fontawesome-solid-link: Book](https://learnvimscriptthehardway.stevelosh.com/chapters/15.html)

Simple operator mapping
---

`d`, `y`, `c` are operators that wait for a movement command (`w`, `i(`, etc.). 
Vim lets you create new movements.

Here's a sweet mapping to directly operator on the contents of the next braces.

```
:onoremap in( :<c-u>normal! f(vi(<cr>
```

```python
def somefunc(param1, param2):
```

When the cursor is somewhere before the braces, running `cin()` will clear out 
the contents of the braces.

Structural breakdown of the mapping:

| Component | Description                  |
|-----------|------------------------------|
| in(       | new movement                 |
| `<c-u>`   |                              |
| normal!   | execute normal mode commands |
| f(        | find next `(`                |
| vi(       | visual selection             |


Operator mapping using `execute`
---
`normal!` doesn't recognize "special characters" like `<cr>`. There are a number 
of ways around this, but the easiest to use and read is execute.

The execute command is used to evaluate a string as if it were a Vimscript 
command.
```
:onoremap ih :<c-u>execute "normal! ?^==\\+$\r:nohlsearch\rkvg_"<cr>
```

When `execute` looks at the string you tell it to run, it will substitute any 
special characters it finds before running it. In this case, `\r` is an escape 
sequence that means "carriage return". The double backslash is also an escape 
sequence that puts a literal backslash in the string.

So, the above command can be seen as:

```
:normal! ?^==\+$<cr>:nohlsearch<cr>kvg_
                ^^^^           ^^^^
                 ||             ||
These are ACTUAL carriage returns, NOT the four characters
"left angle bracket", "c", "r", and "right angle bracket".
```

which can be further broken down as:

```
?^==\+$     " search backwards for a line containing == or more
:nohlsearch " no visual highlight
kvg_        " up one line, highlight to last non-blank character
```
