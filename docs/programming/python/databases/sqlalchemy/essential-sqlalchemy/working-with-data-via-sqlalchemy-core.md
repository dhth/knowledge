---
title: "Working with data via SQLAlchemy Core"
summary:
---

Working with data via SQLAlchemy Core
===

Schema and Types
---

```python
from datetime import datetime

from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, create_engine)
metadata = MetaData()

cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('customer_number', Integer(), autoincrement=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id'))
)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)

engine = create_engine('sqlite:///:memory:')
metadata.create_all(engine)

connection = engine.connect()
```

Insert
---
```python
from sqlalchemy import insert
ins = insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)

result = connection.execute(ins)

ins = cookies.insert()

result = connection.execute(
    ins,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
)

inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]

result = connection.execute(ins, inventory_list)
```

Select
---
```python
from sqlalchemy.sql import select
s = select([cookies])
rp = connection.execute(s)
results = rp.fetchall()

from sqlalchemy.sql import select
s = cookies.select()
rp = connection.execute(s)
results = rp.fetchall()

"""
>>> type(rp)
<class 'sqlalchemy.engine.result.ResultProxy'>
"""

first_row = results[0]

"""
>>> type(first_row)
<class 'sqlalchemy.engine.result.RowProxy'>

>>> first_row[1]
'chocolate chip'

>>> first_row.cookie_name
'chocolate chip'

>>> first_row[cookies.c.cookie_name]
'chocolate chip'
"""

for record in rp:
    print(record.cookie_name)
```

Select specific columns
---

```python
s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = connection.execute(s)
print(rp.keys())
result = rp.first()
```

Order By
---

```python
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
rp = connection.execute(s)
for cookie in rp:
    print(f'{cookie.quantity} - {cookie.cookie_name}')

from sqlalchemy import desc
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(desc(cookies.c.quantity))

"""
`first()` or `fetchone()` runs a query for all results,
and then accesses the first record.
"""
```

Limit
---
```python
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
s = s.limit(2)
rp = connection.execute(s)
print([result.cookie_name for result in rp])
```
