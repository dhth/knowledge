jq Slurp
===

```
jq -s : read (slurp) all inputs into an array; apply filter to it;
```

The following results in dict of dicts, what we want is the items in an array
called `items`.

```bash
buku --np --nc -f 4 --stag alfred_workflows | \
    sed 1d | \
    jq -R -n -c 'inputs |split("\t") |{uid: ("buku-"+.[0]), title: .[2], subtitle: .[1], arg:(.[0] + "::" + .[1])}' | \
    jq '{items: .}'
```

```json
{
  "items": {
    "uid": "buku-71",
    "title": "Authorization Guide | Spotify for Developers",
    "subtitle": "https://developer.spotify.com/documentation/general/guides/authorization-guide/",
    "arg": "71::https://developer.spotify.com/documentation/general/guides/authorization-guide/"
  }
}
{
  "items": {
    "uid": "buku-72",
    "title": "Console | Spotify for Developers",
    "subtitle": "https://developer.spotify.com/console/",
    "arg": "72::https://developer.spotify.com/console/"
  }
}
```

```bash
buku --np --nc -f 4 --stag alfred_workflows | \
    sed 1d | \
    jq -R -n -c 'inputs |split("\t") |{uid: ("buku-"+.[0]), title: .[2], subtitle: .[1], arg:(.[0] + "::" + .[1])}' | \
    jq -s '{items: .}'
```

```json
{
  "items": [
    {
      "uid": "buku-71",
      "title": "Authorization Guide | Spotify for Developers",
      "subtitle": "https://developer.spotify.com/documentation/general/guides/authorization-guide/",
      "arg": "71::https://developer.spotify.com/documentation/general/guides/authorization-guide/"
    },
    {
      "uid": "buku-72",
      "title": "Console | Spotify for Developers",
      "subtitle": "https://developer.spotify.com/console/",
      "arg": "72::https://developer.spotify.com/console/"
    }
  ]
}
```
