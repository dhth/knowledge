pdbpp
===

Use pdbpp's in sticky mode by default
---

pdbpp's `sticky` command keeps the source code fixed in position, and only moves the line highlighter down. To enable it by default, create a `~/.pdbrc.py` file with the following contents:

```python
import pdb
class Config(pdb.DefaultConfig):
    sticky_by_default = True
```

More on this [here](https://gist.github.com/justinabrahms/44b077ee314914b3ff78).

Using with docker
---

Create `.pdbrc.py` file somewhere in the project, and mount it to the container
using volumes.

```yaml
version: '3.8'

services:
  web:
    build: ./project
    command: uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    volumes:
      - ./project/.pdbrc.py:/root/.pdbrc.py
      - ./project:/usr/src/app
```
