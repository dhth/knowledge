Remove last n lines from stdin
===

```bash
echo "1\n2\n3\n4\n"
1
2
3
4
<empty line>
```

```bash
echo "1\n2\n3\n4\n" | ghead -n -1
1
2
3
4
```
