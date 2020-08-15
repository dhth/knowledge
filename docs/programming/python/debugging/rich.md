rich
===

[:fontawesome-solid-link: https://github.com/willmcgugan/rich](https://github.com/willmcgugan/rich)

Resources
---

- [:fontawesome-solid-link: Video series on rich](https://calmcode.io/rich/introduction.html)

Custom theme
---

This will let us print stuff in various colors based on the config and the `style` passed to `Console`.

```python
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "red" : "bold red",
    "yellow": "bold yellow"
})

console = Console(theme=custom_theme)
console.print({"a": 1, "b": 2}, style="bad")
```
