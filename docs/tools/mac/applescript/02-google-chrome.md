---
title: "Google Chrome"
summary:
---

Google Chrome
===

Get bookmark folders
---

```AppleScript
tell application "Google Chrome"
    tell its bookmark folder "Bookmarks Bar"
        tell its bookmark folder "Another folder"
            get title of its bookmark folders
        end tell
    end tell
end tell
```

Get URL of active tab
---

```AppleScript
tell application "Google Chrome"
    get URL of active tab of first window as text
end tell
```

Get title of active tab
---

```AppleScript
tell application "Google Chrome"
    get title of active tab of first window as text
end tell
```
