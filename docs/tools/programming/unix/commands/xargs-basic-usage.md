xargs Basic Usage
===

```bash
echo 1 2 3 4 5 6 7 8 | xargs -n1 bash -c 'echo this is each item in a line: $0'
```

```
this is each item in a line: 1
this is each item in a line: 2
this is each item in a line: 3
this is each item in a line: 4
this is each item in a line: 5
this is each item in a line: 6
this is each item in a line: 7
this is each item in a line: 8
```

```bash
echo 1 2 3 4 5 6 7 8 | xargs -n2 bash -c 'echo now it is two items in a line: $0, $1'
```

```
now it is two items in a line: 1, 2
now it is two items in a line: 3, 4
now it is two items in a line: 5, 6
now it is two items in a line: 7, 8
```
