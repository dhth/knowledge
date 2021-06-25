External Commands
===

Open Urls with pound sign in them
---

Use `shellescape(url, 1)`. (`:h shellescape` for more).

```vim
silent execute "!open " . shellescape("https://docs.aws.amazon.com/cdk/api/latest/python/".l:url, 1)
```
