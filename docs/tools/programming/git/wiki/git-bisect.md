Git Bisect
===

```bash
git bisect start <BAD_REF> <GOOD_REF>
git bisect run <TEST_COMMAND>

# example
# git bisect start origin/master niw3o5q
# git bisect run sbt test
```
