# SQLAlchemy Wiki

Cascades
---

[Official docs](https://docs.sqlalchemy.org/en/13/orm/cascades.html)

```python
class User(Base):
    # ...

    addresses = relationship("Address", cascade="all, delete-orphan")
```

When, a `User` object is marked for completion, addresses associated with the
object will also be deleted. Same goes for addresses that have been
de-associated from their parent.


Query on JSON field
---

```python
query = Table.query.filter(Table.json_column.contains({"someField": True}))
```

Single table inheritance alongside mixins
---

A mixin that sets table name for a table can be used for a single table
inheritance scenario by just setting `__tablename__` to `None` in subclasses.

More [
here](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html#controlling-table-inheritance-with-mixins).
