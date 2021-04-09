---
title: "Basics"
summary:
---

Basics
===

Check existence of argument
---

```bash
if [ $# -eq 0 ]
# if no arguments supplied
```

OR
---

```bash
if [ "$#" -eq 0 ] || [ "$#" -ge 2 ] 
# if number of arguments is 0 or greater than equal to 2
```
