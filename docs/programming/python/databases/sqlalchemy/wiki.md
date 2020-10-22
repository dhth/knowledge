Wiki
===

Cascades
---

[:fontawesome-solid-link: Official docs](https://docs.sqlalchemy.org/en/13/orm/cascades.html)

```python
class User(Base):
    # ...

    addresses = relationship("Address", cascade="all, delete-orphan")
```

When, a `User` object is marked for completion, addresses associated with the
object will also be deleted. Same goes for addresses that have been
de-associated from their parent.



