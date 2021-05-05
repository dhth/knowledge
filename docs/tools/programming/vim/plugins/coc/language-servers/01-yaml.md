---
title: "Yaml"
summary:
---

Yaml
===

Resources
---

- [:fontawesome-brands-github: neoclide/coc-yaml: Yaml language server extension
    for coc.nvim](https://github.com/neoclide/coc-yaml)


Schemas
---

- [:fontawesome-solid-link: Schema Store](https://www.schemastore.org/json/)


coc-settings.json
---

```json
{
    "yaml.schemas": {
        "https://raw.githubusercontent.com/awslabs/goformation/v4.18.2/schema/cloudformation.schema.json" :
        ["/*.yaml"]
    },
    "yaml.hover": true,
    "yaml.validate": true,
    "yaml.format.enable": true,
    "yaml.customTags": [
        "!Equals sequence",
        "!FindInMap sequence",
        "!GetAtt",
        "!GetAZs",
        "!ImportValue",
        "!Join sequence",
        "!Ref",
        "!Select sequence",
        "!Split sequence",
        "!Sub"
    ]
}
```
