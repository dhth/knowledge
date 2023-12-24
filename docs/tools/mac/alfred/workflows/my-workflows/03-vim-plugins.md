# Vim Plugins

Vim's plugin file looks like:

```vim
"...
call plug#begin('~/.local/share/nvim/plugged')

" Plug 'gruvbox-community/gruvbox'
Plug 'lifepillar/vim-gruvbox8'
Plug 'KeitaNakamura/neodark.vim'
Plug 'arzg/vim-colors-xcode'
"...
```

Script filter to search from this file:

```bash
cat $NVIM_DIR/vim-plug/plugins.vim | \
grep "^Plug '" | \
awk -F  "Plug '" '{print $2}' | \
cut -d"'" -f1 | \
$HOMEBREW_DIR/jq -R -n -c \
'[inputs|split(",")|{uid:.[0], title: (.[0]|split("/")|join(" / " )|split("-")|join(" ")), arg:.[0]}] | {items: .}|.'
```

This will generate the following JSON:

```json
{
  "items": [
    {
      "uid": "lifepillar/vim-gruvbox8",
      "title": "lifepillar / vim gruvbox8",
      "arg": "lifepillar/vim-gruvbox8"
    },
    {
      "uid": "KeitaNakamura/neodark.vim",
      "title": "KeitaNakamura / neodark.vim",
      "arg": "KeitaNakamura/neodark.vim"
    },
    {
      "uid": "arzg/vim-colors-xcode",
      "title": "arzg / vim colors xcode",
      "arg": "arzg/vim-colors-xcode"
    }
...
```
