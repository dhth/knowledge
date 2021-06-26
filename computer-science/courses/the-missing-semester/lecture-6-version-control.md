Lecture 6: Version Control
===

Resources
---

- [Lecture 6: Version
    Control][1]
- [Lecture
    Page][2]

[1]: https://www.youtube.com/watch?v=2sjqTHE0zok
[2]: https://missing.csail.mit.edu/2020/version-control/

Introduction
---

Although git's interface is a leaky abstraction, it's underlying design is
beautiful and elegant.

Git's Data Model
---

```text
type blob = array<byte>

type tree = map<string, tree|blob>

type commit = struct {
    parents: array<commit>
    author: string
    message: string
    snapshot: tree
}
```

How these get stored to disk
---

```text
type object = blob | tree | commit
objects = map<string, object>

" store object

def store(o):
    id = sha1(o)
    objects[id] = 0

" load object

def load(id):
    return objects[id]
```

