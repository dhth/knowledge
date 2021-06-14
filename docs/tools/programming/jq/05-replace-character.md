---
title: "Replace Character"
summary:
---

Replace Character
===

Use `split("_")|join(" ")`.

```bash
echo file.txt
alfred
alfred_workflows
automation_tools
aws_cdk
```

```bash
echo file.txt \
| jq -R -n -c \
'[inputs|split(",")|{uid:.[0], title: (.[0]|split("_")|join(" ")), arg:.[0]}] | {items: .}'\
| jq
{
  "items": [
    {
      "uid": "alfred",
      "title": "alfred",
      "arg": "alfred"
    },
    {
      "uid": "alfred_workflows",
      "title": "alfred workflows",
      "arg": "alfred_workflows"
    },
    {
      "uid": "automation_tools",
      "title": "automation tools",
      "arg": "automation_tools"
    },
    {
      "uid": "aws_cdk",
      "title": "aws cdk",
      "arg": "aws_cdk"
    }
}
```
