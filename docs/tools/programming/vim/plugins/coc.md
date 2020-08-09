# Coc

## CocSearch

```
:CocSearch whateverstring -A 20
// returns buffer with instances of
// whateverstring along with 20 more lines
```

## Set workspace (for coc-python)

[:fontawesome-solid-link: Unresolved import · Issue #26 · neoclide/coc-python](https://github.com/neoclide/coc-python/issues/26)

```bash
Run :CocList folders.
Press <cr> and edit the path to correct folder.
Run :CocRestart to restart service.
Save a session file to persist workspaceFolders.
```

## Open jump definition in a new tab

[:fontawesome-solid-link: Goto Definition in Vsplit? · Issue #1249 · neoclide/coc.nvim](https://github.com/neoclide/coc.nvim/issues/1249)

```bash
:call CocAction('jumpDefinition', 'tabe')
```

## Move to floating window

`<c-w><c-w>` switches between windows.
