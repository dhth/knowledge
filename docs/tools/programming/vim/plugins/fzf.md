---
title: "fzf.vim"
summary:
---

fzf.vim
===

Is powered by [FZF](../../shell/01-fzf.md).

Resources
---

- [:fontawesome-solid-link: junegunn/fzf](https://github.com/junegunn/fzf)
- [:fontawesome-solid-link: junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
- [:fontawesome-solid-link: Improving shell workflows with fzf](https://seb.jambor.dev/posts/improving-shell-workflows-with-fzf/)
- [:fontawesome-solid-link:
    Readme](https://github.com/junegunn/fzf/blob/master/README-VIM.md)

`:GFiles`
---

Wrapper for `git ls-files`. Very handy when only dealing with files associated with git.

`:Files`
---

General purpose search. Uses `FZF_DEFAULT_COMMAND` environment variable under the hood. I'm using [:fontawesome-solid-link: `fd`](https://github.com/sharkdp/fd) for general search, since it respects `.gitignore`.


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

Create file helper using fzf
---

More on `fd` [here](../../shell/search-utils/01_fd.md).

```vim
call fzf#run(fzf#wrap({'source': 'fd -H -t d', 'sink': function('s:CreateFileHelper')}))
" will pop up fzf with directories listed

function! s:CreateFileHelper(command)
    call inputsave()
    let l:file_name_in = input('Enter file name: ')
    call inputrestore()
    if len(l:file_name_in) > 0
        execute "tabnew ".a:command."/".l:file_name_in
    endif
endfunction
```
