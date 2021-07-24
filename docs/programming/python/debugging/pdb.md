pdb
===

Resources
---

- [:fontawesome-solid-play-circle: Clayton Parker - So you think you can PDB? - PyCon 2015](https://www.youtube.com/watch?v=P0pIW5tJrRM)
- [:fontawesome-solid-play-circle: PDB like a
    Pro](https://www.youtube.com/watch?v=yOG36Ae_TJ0)
- [:fontawesome-solid-play-circle: How to become a better programmer through
    pdb-driven development](https://www.youtube.com/watch?v=9dyX19r7hJs)
- [:fontawesome-solid-link: Become a pdb power
    user](https://medium.com/instamojo-matters/become-a-pdb-power-user-e3fc4e2774b2)

My .pdbrc
---

```
alias brr print(f"\n{'='*100}\n")

alias brk print(f'\n\n{"=" * 100}\n\n')

# hack to get around the fact that imports get lost when you step into a call
# [TODO] find a better way
alias rp from rich import print as _print; _print(%1)

alias pl from rich import print as _print; _print(locals(), style="red")

alias cls import shutil; print("\n" * shutil.get_terminal_size().lines)
```

!!! note
    aliases can accept arguments using `%1`, `%2`, and so on.

Print with colors in a pdb session
---

!!! warning
    I no longer use this method since `rich` pretty much handles this on its
    own.

I like to have dictionaries printed with colors in a pdb session. I'm sure there's a better way of doing this, but here's my method:

I write a pdb util function somewhere in my code base.

``` python
# somemodule.pdb_utils.py

import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


def ppd(d):
    s = json.dumps(d, indent=4, sort_keys=True, default=str)
    print(highlight(s, JsonLexer(), TerminalFormatter()))
```

More on this [here](https://stackoverflow.com/questions/26459749/pretty-printing-json-with-ascii-color-in-python).

Then I create an alias to this function in my `~/.pdbrc` file. More on pdbrc aliases [here](https://docs.python.org/3/library/pdb.html#debugger-aliases).

``` bash
alias ppi from somemodule.pdb_utils import *
```

Finally, in my pdb session, I can import my pdb util functions with `ppi`. And, print a dictionary with colors using `ppd(somedict)`.

Use ipython inside pdb
---

[:fontawesome-solid-link: https://stackoverflow.com/questions/53933400/ipython-embed-does-not-use-terminal-colors](https://stackoverflow.com/questions/53933400/ipython-embed-does-not-use-terminal-colors)

Losing terminal echo
---

[:fontawesome-brands-github:
This](https://github.com/saimn/dotfiles/blob/master/pdbrc) might help.
