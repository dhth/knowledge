# zsh expansions

```bash
echo hello1 hello2 hello3 hello4
echo !:1
# expands to hello1
echo !:2
# expands to hello2
echo !:$
# expands to hello4
echo !#
# expands to the command so far, ie, echo
```
