# Autocommands

Autocommand structure
---

```
:autocmd BufNewFile * :write
         ^          ^ ^
         |          | |
         |          | The command to run.
         |          |
         |          A "pattern" to filter the event.
         |
         The "event" to watch for.
```

An example:

```
:autocmd BufNewFile,BufRead *.html setlocal nowrap

```

As seen here, a single autocommand can be bound to multiple events by separating the events with a comma.

> :help autocmd-events

Autocommand Groups
---

It is possible to create duplicate autocommands which might slow down Vim. When a config file is sourced, Vim has no way of knowing if we want to replace an existing autocommand with a new one. A solution to this is to use `augroup`.

```
:augroup testgroup
:    autocmd!
:    autocmd BufWrite * :echom "Cats"
:augroup END
```

`autocmd!` clears out the group, and then Vim defines the autocommands present in the group, preventing duplicates.


Create Toggleable Autocommands
---

```vim
function! ToggleMarkdownRender()
    if !exists('#MarkdownGlow#BufWritePost')
        augroup MarkdownGlow
            autocmd!
            autocmd BufWritePost,BufWinEnter *.md call ft#markdown#GlowViaVimux()
        augroup END
    else
        augroup MarkdownGlow
            autocmd!
        augroup END
    endif
endfunction
```
