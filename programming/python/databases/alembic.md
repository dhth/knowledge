Alembic
===

```bash
# a new column, model, etc. has been added before
alembic revision --autogenerate -m '<describe your changes>'

# review the migration in backend/feedback/alembic/versions

# upgrade to the latest version
alembic upgrade head
```

> Make it a point to downgrade and upgrade whenever a change has a migration, to make sure nothing breaks.

## Field length changes

Alembic doesn't detect field length changes by default, it's configuration has to be modified to detect it.

[Setting up alembic to detect the column length change](http://blog.code4hire.com/2017/06/setting-up-alembic-to-detect-the-column-length-change/)

[Alembic - migration for String length change](https://eshlox.net/2017/08/06/alembic-migration-for-string-length-change)


## Warning

Alembic can make errors when using `context.configure(url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True)`

when using `compare_type`.
