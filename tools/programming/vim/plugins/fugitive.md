Fugitive
===

Resources
---

- [Dive into Git history with fugitive.vim](https://advancedweb.hu/dive-into-git-history-with-fugitive-vim/)

- [The Fugitive Series - a retrospective](http://vimcasts.org/blog/2011/05/the-fugitive-series/)


Diffs
---

```bash
`dv` opens diff in vertical split (after :Gstatus)
```

`O`: open file under cursor in a new tab

Vdiff current file with `origin/master`

```bash
:Gvdiffsplit origin/master:%
```

Diff file with previous version

[Diff of current and previous version using vim-fugitive](https://stackoverflow.com/questions/16802629/diff-of-current-and-previous-version-using-vim-fugitive)

```bash
:Gdiff aaffdfds
```

[How to open a split-diff for selected file out of the commit](https://vi.stackexchange.com/questions/16422/how-to-open-a-split-diff-for-selected-file-out-of-the-commit)
