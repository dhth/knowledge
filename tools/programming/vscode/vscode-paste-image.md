VSCode Paste Image
===

Resources
---

- [Extension Page][1]

<!-- Links -->
[1]: https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image

Trying to make it behave as similar as [md-img-paste](https://github.com/ferrine/md-img-paste.vim).

Settings
---

`settings.json`:

```
{
    "before": ["<leader>", "p"],
    "commands": [
        "extension.pasteImage"
    ]
},
"pasteImage.filePathConfirmInputBoxMode": "onlyName",
"pasteImage.path": "${currentFileDir}/assets",
"pasteImage.showFilePathConfirmInputBox": true,
"pasteImage.namePrefix": "${currentFileNameWithoutExt}-",
```
