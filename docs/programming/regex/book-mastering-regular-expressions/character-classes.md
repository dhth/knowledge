# Character Classes

`gr[ea]y` matches "grey", and "gray".

`h[1-6]` matches "h1", "h2", "h3", and so on, till "h6".

Multiple dash shorthands can be used, eg. `h[1-6a-z]`.

Dash (`-`) is a metacharacter within a character class if it's not the first
character in the character class. eg. `h[-a-z]`, will match "h-"

Caret (`^`) can be used to create negated character classes. eg. `h[^1-5]` will
not match "h1" to "h5".
