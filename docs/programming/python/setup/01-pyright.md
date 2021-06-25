Pyright
===

Resources
---


- [:fontawesome-solid-link:
    pyrightconfig.json](https://github.com/microsoft/pyright/blob/master/docs/configuration.md)
- [:fontawesome-solid-link: Sample pyrightconfig.json
    file](https://github.com/microsoft/pyright/blob/1601a177cdedc35d4d61ed98c622bd0d3754e9a7/docs/configuration.md#sample-config-file)

Project root
---

For a directory structure like:

```
.
├── .gitignore
├── .vim
│   └── coc-settings.json
├── project
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   └── requirements.txt
└── pyrightconfig.json
```

`pyrightconfig.json` would need:

```json
"executionEnvironments": [
    {
        "root": "project"
    }
]
```
