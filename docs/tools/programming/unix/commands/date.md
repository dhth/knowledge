# Date

Get epoch in nanoseconds
---

On MacOS, get `coreutils` (`brew install coreutils`).

```bash
echo $(($(date +%s%N)/1000000))
```
