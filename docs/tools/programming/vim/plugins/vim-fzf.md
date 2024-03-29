# fzf.vim

Powered by [[fzf]].

Resources
---

- [junegunn/fzf](https://github.com/junegunn/fzf)
- [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
- [Improving shell workflows with fzf](https://seb.jambor.dev/posts/improving-shell-workflows-with-fzf/)
- [Readme](https://github.com/junegunn/fzf/blob/master/README-VIM)
- [Call FZF from vim for specific file types only][1]
- [Examples (vim) · junegunn / fzf Wiki][2]

<!-- Links -->
[1]: https://www.reddit.com/r/vim/comments/az5go1/call_fzf_from_vim_for_specific_file_types_only/
[2]: https://github.com/junegunn/fzf/wiki/Examples-(vim)#basic-tutorial

`:GFiles`
---

Wrapper for `git ls-files`. Very handy when only dealing with files associated with git.

`:Files`
---

General purpose search. Uses `FZF_DEFAULT_COMMAND` environment variable under the hood. I'm using [`fd`](https://github.com/sharkdp/fd) for general search, since it respects `.gitignore`.


Search only certain filetype
---

Via [[ripgrep]]:

```python
:Rg -t py breakpoint
```

Via fzf run:

```
call fzf#run(fzf#wrap({'source': 'ls *.md'}))
```

[source][1]

Modifications
---

### Use ripgrep with live preview:

From [https://github.com/junegunn/fzf.vim#example-advanced-ripgrep-integration](https://github.com/junegunn/fzf.vim#example-advanced-ripgrep-integration)

```bash
function! RipgrepFzf(query, fullscreen)
  let command_fmt = 'rg --column --line-number --no-heading --color=always --smart-case -- %s || true'
  let initial_command = printf(command_fmt, shellescape(a:query))
  let reload_command = printf(command_fmt, '{q}')
  let spec = {'options': ['--phony', '--query', a:query, '--bind', 'change:reload:'.reload_command]}
  call fzf#vim#grep(initial_command, 1, fzf#vim#with_preview(spec), a:fullscreen)
endfunction

command! -nargs=* -bang RG call RipgrepFzf(<q-args>, <bang>0)
```

Create file helper using fzf
---

Related to [[fd]].

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

Custom source and sink
---

```vim
" autoload/somemodule.vim

function! s:HelperCommandToRun(command)
    if a:command ==? "first"
        call DoFirstThing()
    elseif a:command ==? "second"
        call DoSecondThing()
    endif
endfunction

function! somemodule#CreateLink()
    let l:commands = [
                \"first",
                \"second",
                \]
    return fzf#run({'source': l:commands, 'sink': function('s:HelperCommandToRun'),  'window': { 'width': 0.2, 'height': 0.4 } })
endfunction
```

Extra key bindings for a list
---

```vim
let g:fzf_action = {
  \ 'ctrl-t': 'tabedit',
  \ 'ctrl-x': 'split',
  \ 'ctrl-v': 'vsplit' }
```

Colors from shell
---

`fzf#run` needs `--ansi` as an option to show [ansi colors](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors). eg.

```vim
function! helpers#GetCommitsForDiffOpen()
    let source = 'git log --graph --since="2 weeks ago" '.get(g:, 'fzf_commits_log_options', '--color=always '.fzf#shellescape('--format=%C(auto)%h%d %s %C(green)%cr'))
    call fzf#run(fzf#wrap({'source': source, 'sink': function('s:CommitHelper'), 'options': '--multi=2 --ansi'}))
endfunction
```

[//begin]: # "Autogenerated link references for markdown compatibility"
[fzf]: ../../unix/utilities/fzf.md "fzf"
[ripgrep]: ../../unix/utilities/ripgrep.md "ripgrep"
[fd]: ../../unix/utilities/fd.md "fd"
[//end]: # "Autogenerated link references"
