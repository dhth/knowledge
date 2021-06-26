Unix Wiki
===

Diff two directories
---

```bash
diff --brief --recursive -x '.git' -x 'autoload' \
    ~/.config/nvim ~/local.usersnap.com/.config/nvim
```

[Source](https://stackoverflow.com/questions/4804405/search-and-replace-in-vim-across-all-the-project-files).

*Note*: `-i ""` is only for MacOS. More [here](https://stackoverflow.com/questions/34533893/sed-command-creating-unwanted-duplicates-of-file-with-e-extension).

Moving around
---

```bash
# inspiration from https://twitter.com/fatih/status/1381555413083168769
# cd to the root of git repo
alias cdr="cd $(git rev-parse --show-toplevel)"

# use fzf to quickly cd into subdirectories
function c() {
  local selected_directory
  selected_directory=$(fd -t d | fzf --height=6 --layout=reverse)

  if [ -n "$selected_directory" ]; then
    cd $selected_directory
  fi
}
```

Ignore directories with tree
---

```bash
tree -I '__pycache__|node_modules|test_*'
```
