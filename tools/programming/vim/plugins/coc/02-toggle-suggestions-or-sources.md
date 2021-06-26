Toggle Suggestions or Sources
===

Toggle suggestions for a file type
---

Under `autoload/ft/markdown.vim`:

```vim
function! ft#markdown#ToggleCocSuggestions()
    let b:coc_suggestions_turned_off = get(b:, 'coc_suggest_disable', 0)
    if b:coc_suggestions_turned_off
        let b:coc_suggest_disable = 0
    else
        let b:coc_suggest_disable = 1
    endif
endfunction
```

This is disable all suggestions for markdown files.


Toggle specific sources
---

```vim
call CocAction('toggleSource', 'around')
call CocAction('toggleSource', 'file')
call CocAction('toggleSource', 'buffer')
```

This might be helpful when you're typing in a markdown file, and don't want
suggestions to show up every now and then. Only snippet suggestions will show
up.
