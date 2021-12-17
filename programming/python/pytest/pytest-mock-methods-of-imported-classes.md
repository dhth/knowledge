Pytest Mock Methods of Imported Classes
===

Structure:

```
.
├── bar.py
├── foo.py
└── tests
    └── test_bar.py
```

```python
# foo.py

import requests


class Foo:
    def foos_method(self, *, name: str) -> str:
        params = dict(name=name)
        # demo third party request
        r = requests.get(f"https://httpbin.org/get", params=params)
        return r.json()["args"]["name"]
```


```python
# bar.py

from foo import Foo


class Bar:
    def __init__(self):
        self.foo = Foo()

    def bars_method(self, *, name: str) -> str:
        return f"Response: {self.foo.foos_method(name=name)}"


if __name__ == "__main__":
    bar = Bar()
    print(bar.bars_method(name="test"))
```


```python
# tests/test_bar.py

from bar import Bar
import pytest
from unittest import mock


class TestBar:

    ############
    # SUCCESS #
    ############

    def test_bar_works(self, mocked_foo):
        # GIVEN
        bar = Bar()
        mocked_foo.return_value.foos_method.return_value = "mocked_response"

        # WHEN
        result = bar.bars_method(name="something")

        # THEN
        mocked_foo.assert_called_once()
        mocked_foo.return_value.foos_method.assert_called_once()
        assert result == "Response: mocked_response"
        assert mocked_foo.return_value.foos_method.call_args.kwargs["name"] == "something"


@pytest.fixture
def mocked_foo():
    with mock.patch("bar.Foo") as mocked_foo:
        yield mocked_foo
```
