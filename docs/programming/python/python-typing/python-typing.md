# Python Typing

Modules
---

Type Hints for Exceptions
---

`typing.Type` indicates that the return type is a type, instead of an instance

```python
from typing import List, Type


class SomeCustomExc(Exception):
    pass


class SomeOtherCustomExc(Exception):
    pass


def get_custom_exceptions() -> List[Type[Exception]]:
    return [HasuraSomeCustomExc, SomeOtherCustomExc]
```
