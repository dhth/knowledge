# jq Work with Arrays

Setup
---

Source json:

```json
[
{
    "id": 343434,
    "node_id": "hsd73hjsd=",
    "name": "dhth",
    "owner": {
      "login": "dhth",
      "id": 342323
        
    }
},
{
    "id": 454544,
    "node_id": "hsdf3fdfedf=",
    "name": "dhth",
    "full_name": "dhth/dhth",
    "private": false,
    "owner": {
      "login": "jhjh",
      "id": 343434
    }
}
]
```
The jq filter:

```bash
. | map({id: .owner.id}) | {items: .}
```

results in:

```json
{
  "items": [
    {
      "id": 342323
    },
    {
      "id": 343434
    }
  ]
}
```
