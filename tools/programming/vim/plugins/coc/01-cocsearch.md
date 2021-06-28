CocSearch
===

Add lines to search
---

```
:CocSearch whateverstring -A 20
// returns buffer with instances of
// whateverstring along with 20 more lines
```

Search specific files
---

- [[03-ripgrep]]
the scenes, ripgrep arguments can be used with it.

```
:CocSearch -g *test_send_to_*.py attachment
```


