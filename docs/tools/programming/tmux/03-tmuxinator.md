---
title: "Tmuxinator"
summary: 
---

Tmuxinator
===

Conditional logic
---

```
- mkdocs:
    - cd ~/Projects/knowledge
    - workon wiki
    <%- if args[0] == "up" %>
    - mkdocs serve --dirtyreload --dev-addr=localhost:8000
    <%- end %>
```
