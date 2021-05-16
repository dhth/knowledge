---
title: "Run Script"
summary:
---

Run Script
===

Use emojis in AppleScript
---

`BOOKMARK_TITLE` is a workflow variable.

```AppleScript
set bookmarkTitle to do shell script "echo " & quoted form of (system attribute "BOOKMARK_TITLE") & " | iconv -f UTF-8-MAC -t MACROMAN"
```

More [:fontawesome-solid-link:
here](https://www.alfredforum.com/topic/15992-applescript-reads-alfred-environment-variables-in-wrong-encoding/).
