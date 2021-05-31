---
title: "Concat Fields"
summary:
---

Concat Fields
===

Concat string fields
---

```
(.field1 + .field2)
```

Concat string field with number
---

Let's say `tracks.total` is a number.

```
("tracks: " + (.tracks.total|tostring))
```
