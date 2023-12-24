# Vim Map Alt Key

MacOS
---

Say you want to map `<ALT+k>` to something. On MacOS, find out what character
`<ALT>` + `k` generates, and use that in the actual mapping. eg. `<ALT+k>`
generates `˚`. So, the mapping is:

```
inoremap ˚ :Whatever<CR>
```
