fzf.vim
===

FZF is general purpose command line fuzzy finder, and fzf.vim is the vim companion.

Resources
---

- [:fontawesome-solid-link: junegunn/fzf](https://github.com/junegunn/fzf)

- [:fontawesome-solid-link: junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)

`:GFiles`
---

Wrapper for `git ls-files`. Very handy when only dealing with files associated with git.

`:Files`
---

General purpose search. Uses `FZF_DEFAULT_COMMAND` environment variable under the hood. I'm using [:fontawesome-solid-link: `fd`](https://github.com/sharkdp/fd) for general search, since it respects `.gitignore`. The command I'm using is

```bash
fd -iH
# i for ignoring case
# H for including hidden files
# Since .git is also hidden, I've placed it under ~/.fdignore
# for universal ignoring
```

Search only certain filetype
---

```python
:Rg -t py breakpoint
```

Modifications
---

### Use ripgrep with live preview:

From [:fontawesome-solid-link: https://github.com/junegunn/fzf.vim#example-advanced-ripgrep-integration](https://github.com/junegunn/fzf.vim#example-advanced-ripgrep-integration)

```bash
function! RipgrepFzf(query, fullscreen)
  let command_fmt = 'rg --column --line-number --no-heading --color=always --smart-case -- %s || true'
  let initial_command = printf(command_fmt, shellescape(a:query))
  let reload_command = printf(command_fmt, '{q}')
  let spec = {'options': [:fontawesome-solid-link: '--phony', '--query', a:query, '--bind', 'change:reload:'.reload_command]}
  call fzf#vim#grep(initial_command, 1, fzf#vim#with_preview(spec), a:fullscreen)
endfunction

command! -nargs=* -bang RG call RipgrepFzf(<q-args>, <bang>0)
```
