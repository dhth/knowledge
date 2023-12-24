Understanding the Session and Exceptions
===

Session States
---

- Transient: The instance is not in session, and is not in the database.
- Pending: The instance has been added to the session with add(), but hasn’t
  been flushed or committed.
- Persistent: The object in session has a corresponding record in the database.
- Detached: The instance is no longer connected to the session, but has a record
    in the database.

Inspect Session State
---

```python
cc_cookie = Cookie(
    "chocolate chip",
    "http://some.aweso.me/cookie/recipe.html",
    "CC01",
    12,
    0.50,
)
from sqlalchemy import inspect

insp = inspect(cc_cookie)

for state in ["transient", "pending", "persistent", "detached"]:
    print("{:>10}: {}".format(state, getattr(insp, state)))

"""
transient: True
pending: False
persistent: False
detached: False
"""
```
