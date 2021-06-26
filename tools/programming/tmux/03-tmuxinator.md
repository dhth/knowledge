Tmuxinator
===

Conditional logic
---

[Inspiration](https://github.com/tmuxinator/tmuxinator/issues/658).

```
- mkdocs:
    - cd ~/Projects/knowledge
    - workon wiki
    <%- if args[0] == "up" %>
    - mkdocs serve --dirtyreload --dev-addr=localhost:8000
    <%- end %>
```
