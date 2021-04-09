---
title: "Basic VimScript"
summary:
---

Basic VimScript
===

Comparisons
---

```
:set noignorecase
:if "foo" ==? "FOO"
:    echom "first"
:elseif "foo" ==? "foo"
:    echom "second"
:endif
```

Vim displays first because ==? is the "case-insensitive no matter what the user has set" comparison operator. Now run the following commands:

```
:set ignorecase
:if "foo" ==# "FOO"
:    echom "one"
:elseif "foo" ==# "foo"
:    echom "two"
:endif
```

Vim displays two because ==# is the "case-sensitive no matter what the user has set" comparison operator.
