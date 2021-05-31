---
title: "Use Environment Variables in Filter"
summary:
---

Use Environment Variables in Filter
===

Using jq arg
---

```bash
PAGER_OFFSET=20
curl -X "GET" "https://someapi.com" | jq --arg PAGER_OFFSET "$PAGER_OFFSET" '.items += [{"uid": "spotify:pager", "title": "spotify:next", "arg": "spotify:pager:20", "subtitle":("results from next page, current offset: "+ $PAGER_OFFSET)}]'
```
