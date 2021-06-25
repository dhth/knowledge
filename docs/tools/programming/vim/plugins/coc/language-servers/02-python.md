Python
===

Resources
----
- [:fontawesome-brands-github: neoclide/coc-python](https://github.com/neoclide/coc-python) : Deprecated
- [:fontawesome-brands-github: fannheyward/coc-pyright: Pyright extension for
    coc.nvim](https://github.com/fannheyward/coc-pyright)


!!! note "Deprecated"
    The content below is mainly for coc-python, which has now been deprecated.
    coc-pyright works better. Pyright page
- [[../../../../../../programming/python/setup/01-pyright]]


Setting up interpreter
---
Each project might need a specific python interpreter.

- Create a `.vim` directory at project root.
- Add the following to `.vim/coc-settings.json`
    ```json
    {
        "python.pythonPath": "/Users/dhruvthakur/.virtualenvs/sqlalchemy/bin/python"
    }
    ```


When Coc doesn't pick up the right workspace path
---

[:fontawesome-brands-github: Unresolved import · Issue #26 · neoclide/coc-python](https://github.com/neoclide/coc-python/issues/26)

```
Run :CocList folders.
Press <cr> and edit the path to correct folder.
Run :CocRestart to restart service.
Save a session file to persist workspaceFolders.
```
