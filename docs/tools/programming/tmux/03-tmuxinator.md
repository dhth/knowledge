Tmuxinator
===

Resources
---

- [Dynamic templates with Tmuxinator][1]

<!-- Links -->
[1]: https://github.com/tmuxinator/tmuxinator/issues/658
[2]: https://dev.to/qmenoret/dynamic-templates-with-tmuxinator-4mkh

<!-- Links end -->


Conditional logic
---

[Inspiration](1).

```
- mkdocs:
    - cd ~/Projects/knowledge
    - workon wiki
    <%- if args[0] == "up" %>
    - mkdocs serve --dirtyreload --dev-addr=localhost:8000
    <%- end %>
```

Dynamic session name
---

[Inspiration][2]

```
<% if @args[0] %>
<% WDIR=@args[0] %> 
<% else %>
<% WDIR=ENV["PWD"] %>
<% end %>

name: <%= WDIR.split('/').last.downcase  %>
root: <%= @args[0] %>
```
