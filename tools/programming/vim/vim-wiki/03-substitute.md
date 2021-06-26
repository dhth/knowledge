Substitute
===

Resources
---
- [:fontawesome-solid-link: Vim
    wiki page on substitute](https://vim.fandom.com/wiki/Search_and_replace)

Substitution Flags
---

```vim
" the 'n' flag is handy if you need to do a dry run before actually
" substituting
:s/old/new/gn  " n returns the number of substitution that will be made
:%&g           " Repeat (on entire file) last substitution without flags, ie,
               " will replace 'old' with 'new'
:s/old/new/gc  " ask for confirmation
```

More on repeat last substitution [:fontawesome-solid-link:
here](https://vimtricks.com/p/vimtrick-repeat-the-last-substitution).

Substitute only in visual block
---

```vim
" first make visual selection
" then :s
" which will expand to :'<,'>
" replace text in visual block using \%V
:'<,'>s/\%Vfoo/bar/g
```

Substitute from current line till end of file
---

```vim
:.,$s/foo/bar/g
" $ corresponds to end of file
```

Substitute from specific line till end of file
---

```vim
:2,$s/foo/bar/g
" from line 2 till end of file
```

Don't error out if missing
---

```vim
:s/foo/bar/e
```

Search with contents of register 0
---

```
:%s/<c-r>0/text to replace with/g
```

Replace with contents of register 0
---

```
:%s/text to search/\=@0/g
```
