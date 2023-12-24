# Set Workflow Variables Via Script

Resources
---

- [Workflow/environment variables in
    Alfred](https://www.deanishe.net/post/2018/10/workflow/environment-variables-in-alfred/#from-run-script-actions)


Set Variables
---

```bash
source ~/.zsh_env_vars.sh

cat << EOF
{
  "alfredworkflow": {
    "arg": "arg",
    "variables": {
      "WIKI_DIR": "$WIKI_DIR"
    }
  }
}
EOF
```

This would make the workflow variable `var:WIKI_DIR` available in the rest of
the workflow (in the subsequent steps).
