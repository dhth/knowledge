Functions
===

```
:function DisplayName(name)
:  echom "Hello!  My name is:"
:  echom a:name
:endfunction
```

`a:` represents that the variable is in the argument scope.


```
:function Varg2(foo, ...)
:  echom a:foo
:  echom a:0
:  echom a:1
:  echo a:000
:endfunction

:call Varg2("a", "b", "c")
```

- `a:0`: number of extra arguments
- `a:1`: first extra argument
- `a:000`: list of extra arguments
