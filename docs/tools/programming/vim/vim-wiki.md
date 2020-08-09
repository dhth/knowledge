# Vim Wiki

## Mapping

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

## Split

[:fontawesome-solid-link: Managing Your Splits In Vim](https://www.youtube.com/watch?v=Zir28KFCSQw)

- `:sp` vertical split

- `:vs` horizontal split

- `Ctrl + W _` Make current buffer take entire vertical space

- `Ctrl + W |` Make current buffer take entire horizontal space

- `Ctrl + W =` Make buffers take equal space

- `Ctrl + W r` swap panes

- `set splitbelow splitright`

- `:res +5` make buffer grow by 5 lines vertically

- `:vert res + 5` make pane grow by 5 lines horizontally

## Movement

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

## Modifications

`d2i{` → deletes inner bracket plus one outer bracket

`dip` → deletes a paragraph (contiguous block of text)

## Multi line editing

```bash
#Go to position
Ctrl V
Select
I/A
```

## Copy/Pasting

Vim keeps a history of previous yanks/deletes. `:reg` lists them. `"0p` pastes register at `0`.T

[:fontawesome-solid-link: Remembering previous deletes/yanks](https://vim.fandom.com/wiki/Remembering_previous_deletes/yanks)

## Windows

```bash
<c-w><o>
## make this split take full window
## can be used to closed vim diff buffers quickly
## source: https://github.com/tpope/vim-fugitive/issues/36
```

## Diffing

```bash
:windo diffthis
// diff buffers in current tab
```

## Execute in all tabs

```bash
:windo diffthis
## execute in all windows in current tab

:tabdo windo diffthis
## execute in all tabs in all windows
```

## Sessions

```bash
:mksession ~/vim-sessions/dotfiles.vim
## save current session

:source ~/.vim-sessions/dotfiles.vim
#load saved session

vim -S ~/mysession.vim
## open session from command line
```

## Folds

```bash
## from my vimrc

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

## Resizing

```bash
<C-W> | --> make window take entire horizontal space

<C-W> = --> make windows equal in size
```

## Search and Replace

```bash
## search with contents of register 0
:%s/<c-r>0/text to replace with/g

## replace with contents of register 0
:%s/text to search/\=@0/g
```

## Command Line

```bash
<C-R><C-W> puts the current word in the command line
```

### Show value of command

```bash
#show value of a command
:set command?
#eg. :set background?
## background=light
```

## Custom Commands

[:fontawesome-solid-link: Here's how to create custom workspaces to switch between programming and writing prose in Vim](https://www.reddit.com/r/vim/comments/ckyspu/heres_how_to_create_custom_workspaces_to_switch/)

## Keywords

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

## `g`

```bash
gf ## opens file under cursor
<c-w>gf #opens file under cursor in a new tab
```

## Files

### Create file under cursor

Create and open a non existent file under the cursor

```bash
noremap <leader>grf :tabe %:h/<cfile><CR>
noremap <leader>gcf :tabe <cfile><CR>
```

`grf` will create a file relative to current buffer. `gcf` will use the absolute `<cfile>` path.

More [here](https://stackoverflow.com/questions/6158294/create-and-open-for-editing-nonexistent-file-under-the-cursor) and [here](https://stackoverflow.com/questions/13239464/create-a-new-file-in-the-directory-of-the-open-file-in-vim/13239757).

## Autocommand

### Autocommand structure

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

### Autocommand Groups

It is possible to create duplicate autocommands which might slow down Vim. When a config file is sourced, Vim has no way of knowing if we want to replace an existing autocommand with a new one. A solution to this is to use `augroup`.

```
:augroup testgroup
:    autocmd!
:    autocmd BufWrite * :echom "Cats"
:augroup END
```

`autocmd!` clears out the group, and then Vim defines the autocommands present in the group, preventing duplicates.

## Substitute

### Substitute only in visual block

```bash
# first make visual selection
# then :s
# which will expand to :'<,'>
# replace text in visual block using \%V
:'<,'>s/\%Vfoo/bar/g
```

### Substitute from current line till end of file

```
:.,$s/foo/bar/g
" $ corresponds to end of file
```

### Substitute from specific line till end of file

```
:2,$s/foo/bar/g
" from line 2 till end of file
```

### Pattern not found

```bash
# use :s/foo/bar/e
```

## Switching cases

- `~`: inverts case of current letter
- `g~w`: inverts case of current word

## Increment Number

`<C-a>` increments number under cursor
