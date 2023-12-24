AWK Remove duplicates lines from a file
===

```bash
awk '!seen[$0]++' filename
```
