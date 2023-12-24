# Lists

Slicing
---

```vim
:echo ['a', 'b', 'c', 'd', 'e'][0:2]

" Vim displays ['a', 'b', 'c'] (elements 0, 1
" and 2). You can safely exceed the upper bound as well.
```

```vim
:echo ['a', 'b', 'c', 'd', 'e'][0:100000]

" Vim simply displays the entire list.
```

```vim
:echo ['a', 'b', 'c', 'd', 'e'][-2:-1]

" Slice indexes can be negative.
" Vim displays ['d', 'e'] (elements -2 and -1).
```

```vim
:echo ['a', 'b', 'c', 'd', 'e'][:1]

" ['a', 'b']
```

```vim
:echo ['a', 'b', 'c', 'd', 'e'][3:]

" ['d', 'e'].
```

```vim
:echo "abcd"[0:2]

" abc
```

```vim
:echo "abcd"[-1]

" empty string
```

```vim
:echo abcd"[-2:]

" cd
```

List Functions
---

```vim
:let foo = ['a', 'b']
:echo get(foo, 0, 'default')
:echo get(foo, 100, 'default')

" Vim displays a and default.
```

```vim
:echo join(foo)
:echo join(foo, '---')
:echo join([1, 2, 3], '')

" Vim displays a b, a---b, and 123.
```
