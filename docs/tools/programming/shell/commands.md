Commands
===

Diff two directories
---

```bash
diff --brief --recursive -x '.git' -x 'autoload' ~/.config/nvim ~/local.usersnap.com/.config/nvim
```

Find and replace recursively in a directory
---

```bash
find docs -name '*.md' | xargs sed -i "" 's/\[/\[:fontawesome-solid-link: /g'
```

[:fontawesome-solid-link: Source](https://stackoverflow.com/questions/4804405/search-and-replace-in-vim-across-all-the-project-files).

*Note*: `-i ""` is only for MacOS. More [here](https://stackoverflow.com/questions/34533893/sed-command-creating-unwanted-duplicates-of-file-with-e-extension).
