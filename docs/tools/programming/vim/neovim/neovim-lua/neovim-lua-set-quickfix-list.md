# Neovim Lua Set Quickfix List

```
:h setqflist
```

Say you have two python test files like this.

```python
# app/tests/test_something.py
# ...
def test_if_something_happens():  # line number 20
    ...
# ...
```

```python
# app/tests/test_something_too.py
# ...
def test_if_something_happens_too():  # line number 40
    ...
# ...
```

Create QF Using search patterns
---

```lua
local qf_items = {
    {
        filename = "app/tests/test_something.py",
        pattern = "test_if_something_happens",
    },
    {
        filename = "app/tests/test_something_too.py",
        pattern = "test_if_something_happens_too",
    },
}

vim.fn.setqflist({}, 'r', {title="Test results", items=qf_items})
```


Create QF Using Line Numbers
---

```lua
local qf_items = {
    {
        filename = "app/tests/test_something.py",
        lnum = 20,
    },
    {
        filename = "app/tests/test_something_too.py",
        lnum = 40,
    },
}

vim.fn.setqflist({}, 'r', {title="Test results", items=qf_items})
```
