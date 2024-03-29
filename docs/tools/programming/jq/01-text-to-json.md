# Text to JSON

To convert each line in a text file, for example:

```
some value
another value
yet another value
```

to (pretty printed):

```json
{
  "items": [
    {
      "uid": "some value",
      "title": "some value",
      "arg": "some value"
    },
    {
      "uid": "another value",
      "title": "another value",
      "arg": "another value"
    },
    {
      "uid": "yet another value",
      "title": "yet another value",
      "arg": "yet another value"
    }
  ]
}
```

```bash
jq -R -n -c \
    '[inputs|split(",")|{uid:.[0], title: .[0], arg:.[0]}] | {items: .}|.' \
    tasks.txt
```

Useful to convert a text file to script filter input for
- [[alfred]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[alfred]: ../../mac/alfred/alfred.md "Alfred"
[//end]: # "Autogenerated link references"