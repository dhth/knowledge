rich
===

[https://github.com/willmcgugan/rich](https://github.com/willmcgugan/rich)

Resources
---

- [Video series on rich](https://calmcode.io/rich/introduction.html)
- [FastAPI and Rich Tracebacks in Development][1]
- [Episode #246 Love your crashes, use Rich to beautify tracebacks  [Python Bytes Podcast]][2]

<!-- Links -->
[1]: https://blog.hay-kot.dev/fastapi-and-rich-tracebacks-in-development/
[2]: https://pythonbytes.fm/episodes/show/246/love-your-crashes-use-rich-to-beautify-tracebacks

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
