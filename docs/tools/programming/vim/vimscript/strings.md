---
title: "Strings"
summary:
---

Strings
===

Concatenate
---

```
:echom "Hello, " . "world"
```

Special Characters
---

```
:echom "foo\nbar"
```

`^@` is Vim's way of saying "newline character".

Literal Strings
---

```
:echom '\n\\'
```

Vim displays `\n\\`.

String Functions
---

```
:echom len("foo")

:echo split("one,two,three", ",")

:echo join(split("foo bar"), ";")

:echom tolower("Foo")
:echom toupper("Foo")
```
