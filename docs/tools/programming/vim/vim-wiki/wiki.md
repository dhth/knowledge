Vim Wiki
===

Mapping
---

It's almost always better to use `nnoremap` instead of `nmap` as it ignores recursive mappings. More at [:fontawesome-solid-link: chapter 5](https://learnvimscriptthehardway.stevelosh.com/chapters/05.html) of Learn VimScript the Hard Way.

### Check if mapping exists

```bash
:verbose imap <tab>
```

### Disable a key

```bash
:inoremap <esc> <nop>
```

This effectively disables the escape key in insert mode by telling Vim to perform <nop> (no operation) instead. More [here](https://learnvimscriptthehardway.stevelosh.com/chapters/10.html).

Movement
---

- `gj` move to visual line below (can be used when lines wrap around)

- `W` ignore special characters like ,.

- `t` like f, but moves until the character

- `I` like insert but ignores whitespace

- `A` appends to end of line

- `s` deletes current character and puts in insert mode

- `S` deletes entire line and puts in insert mode

- `%` can go directly to a brace, without needing to put cursor on it first

- `?` searches backwards

- `Ctrl o` go back where you came from

- `Ctrl i` go forwards to where you've been

- `Ctrl ^` move back to last used file

- `:%s` substitute in the entire document

- `:w Ctrl d` will display all available commands that start with w

- `fo ;` ; repeats f in forward direction

- `fo ,` , repeats f in forward direction

- `va(` highlights inner bracket, along with braces

- `mJ` create mark j

- `'J` go to mark j

Lesser used motions
---

- `is` -> inner sentence
- `as` -> around sentence

Modifications
---

`d2i{` → deletes inner bracket plus one outer bracket

`dip` → deletes a paragraph (contiguous block of text)

Multi line editing
---

```bash
#Go to position
Ctrl V
Select
I/A
```

Copy/Pasting
---

Vim keeps a history of previous yanks/deletes. `:reg` lists them. `"0p` pastes register at `0`.T

[:fontawesome-solid-link: Remembering previous deletes/yanks](https://vim.fandom.com/wiki/Remembering_previous_deletes/yanks)

### `:copy`, `:move`

`:copy`, `:move` are solid ways of moving text around without moving the cursor.
Shorthands are `:t`, and `:m` respectively.

```vim
:-15,-10t.
" Copy lines between -15 and -10 and paste it below.
:-15,-10t+5
" Same, but paste it 5 lines below.
```

More [:fontawesome-solid-link:
here](http://vimcasts.org/episodes/long-range-line-duplication/).

Windows
---

```bash
<c-w><o>
## make this split take full window
## can be used to closed vim diff buffers quickly
## source: https://github.com/tpope/vim-fugitive/issues/36
```

Diffing
---

```bash
:windo diffthis
// diff buffers in current tab
```

Execute in all tabs
---

```bash
:windo diffthis
execute in all windows in current tab
---

:tabdo windo diffthis
execute in all tabs in all windows
---
```

Sessions
---

```bash
:mksession ~/vim-sessions/dotfiles.vim
save current session
---

:source ~/.vim-sessions/dotfiles.vim
#load saved session

vim -S ~/mysession.vim
open session from command line
---
```

Folds
---

```bash
from my vimrc
---

"folds on by default
 set foldmethod=indent
"prevents { or } from opening up a fold
set foldopen-=block

" leader fi to toggle opening/closing all folds
let $unrol=0
function UnrolMe()
if $unrol==0
    :exe "normal zR"
    " :exe "normal zA"
    let $unrol=1
else
    :exe "normal zM"
" :exe "normal zC"
    let $unrol=0
endif
endfunction

noremap <leader>fi :call UnrolMe()<CR>

"leader op opens fold
noremap <leader>op zA
"leader cl closes folds
noremap <leader>cl zC
```

Resizing
---

```bash
<C-W> | --> make window take entire horizontal space

<C-W> = --> make windows equal in size
```

Command Line
---

```bash
<C-R><C-W> puts the current word in the command line
```

### Show value of command

```bash
#show value of a command
:set command?
#eg. :set background?
background=light
---
```

Custom Commands
---

[:fontawesome-solid-link: Here's how to create custom workspaces to switch between programming and writing prose in Vim](https://www.reddit.com/r/vim/comments/ckyspu/heres_how_to_create_custom_workspaces_to_switch/)

Keywords
---

```bash
:map means map recursively
:noremap means map non-recursively
:inoremap means map only in insert mode
:nnoremap means map only in normal mode
autocmd is generally used to run commands for a particular filetype
cnoreabbrev is generally used to alias/map commands in the vim command line
set is used to change value of a internal vim variable
let is usually used to change configuration variables for plugins
```

[:fontawesome-solid-link: 3 of the Most Common Beginner Problems in Vim and How To Fix Them](https://medium.com/@evidanary/3-of-the-most-common-beginner-problems-in-vim-and-how-to-fix-them-16e1b95c94a3)

`g`
---

```bash
gf ## opens file under cursor
<c-w>gf #opens file under cursor in a new tab
```

Files
---

### Create file under cursor

Create and open a non existent file under the cursor

```bash
noremap <leader>grf :tabe %:h/<cfile><CR>
noremap <leader>gcf :tabe <cfile><CR>
```

`grf` will create a file relative to current buffer. `gcf` will use the absolute `<cfile>` path.

More [here](https://stackoverflow.com/questions/6158294/create-and-open-for-editing-nonexistent-file-under-the-cursor) and [here](https://stackoverflow.com/questions/13239464/create-a-new-file-in-the-directory-of-the-open-file-in-vim/13239757).

Switching cases
---

- `~`: inverts case of current letter
- `g~w`: inverts case of current word

Increment/Decrement Number
---

`<C-a>` increments number under cursor
`<C-x>` decrements number under cursor
