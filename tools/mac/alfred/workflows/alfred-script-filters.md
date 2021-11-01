Alfred Script Filters
===

Resources
---

- [Script Filter JSON Format][1]
- [sindresorhus/alfy][2]

<!-- Links -->
[1]: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
[2]: https://github.com/sindresorhus/alfy

<!-- Links end -->

Format
---

```json
{"items": [
    {
        "uid": "desktop",
        "type": "file",
        "title": "Desktop",
        "subtitle": "~/Desktop",
        "arg": "~/Desktop",
        "autocomplete": "Desktop",
        "icon": {
            "type": "fileicon",
            "path": "~/Desktop"
        }
    }
]}
```

Ease of search
---

By default, Alfred uses `title` for searching over items. But if the items
contain symbols like "/", "-", "_", it makes it harder for items to show up.

Use `match` to clean up such strings 👇.

```bash
$ python -c "import random, string;print(*[(''.join(random.choice(string.ascii_lowercase+ '-' + '-') for i in range(10))) for j in range(4)], sep='\n')" | jq -R -n -c '[inputs|split(",")|{uid:.[0], title: .[0], match: (.[0]|split("-")|join(" ")), subtitle: .[0], arg: .[0]}] | {items: .}|.' | jq
```

Main transformation to note: `match: (.[0] | split("-") | join(" "))`

```
{
  "items": [
    {
      "uid": "wf-pktieqa",
      "title": "wf-pktieqa",
      "match": "wf pktieqa",
      "subtitle": "wf-pktieqa",
      "arg": "wf-pktieqa"
    },
    {
      "uid": "vea-xkximk",
      "title": "vea-xkximk",
      "match": "vea xkximk",
      "subtitle": "vea-xkximk",
      "arg": "vea-xkximk"
    },
    {
      "uid": "svwavhjbfh",
      "title": "svwavhjbfh",
      "match": "svwavhjbfh",
      "subtitle": "svwavhjbfh",
      "arg": "svwavhjbfh"
    },
    {
      "uid": "xpcm-pt-fm",
      "title": "xpcm-pt-fm",
      "match": "xpcm pt fm",
      "subtitle": "xpcm-pt-fm",
      "arg": "xpcm-pt-fm"
    }
  ]
}

```
