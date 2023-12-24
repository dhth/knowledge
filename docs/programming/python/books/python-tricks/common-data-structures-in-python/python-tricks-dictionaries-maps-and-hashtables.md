Python Tricks: Dictionaries, Maps, and Hashtables
===

ChainMap
---

Lookups search the underlying mappings one by one until a key is found.
Insertions, updates, and deletions only affect the first mapping added to the
chain.

```python
from collections import ChainMap

dict1 = {
        "one": 1,
        "two": 2,
        }

dict2 = {
        "three": 3,
        "four": 4,
        }

chain = ChainMap(dict1, dict2)
```

```
>>> print(chain)
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

>>> print(chain["three"])
3
>>> print(chain["one"])
1

>>> del chain["two"]
>>> print(chain)
ChainMap({'one': 1}, {'three': 3, 'four': 4})

>>> del chain["four"]
Traceback (most recent call last):
  File "/Users/dht93/.pyenv/versions/3.9.4/lib/python3.9/collections/__init__.py", line 994, in __delitem__
    del self.maps[0][key]
KeyError: 'four'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/dht93/Projects/pyds/python_tricks/chain_map_demo.py", line 21, in <module>
    del chain["four"]
  File "/Users/dht93/.pyenv/versions/3.9.4/lib/python3.9/collections/__init__.py", line 996, in __delitem__
    raise KeyError(f'Key not found in the first mapping: {key!r}')
KeyError: "Key not found in the first mapping: 'four'"
```

MappingProxyType
---

```python
>>> from types import MappingProxyType
>>> writable = {'one': 1, 'two': 2}
>>> read_only = MappingProxyType(writable)
# The proxy is read-only:
>>> read_only['one']
1
>>> read_only['one'] = 23
TypeError:
"'mappingproxy' object does not support item assignment"
# Updates to the original are reflected in the proxy:
>>> writable['one'] = 42
>>> read_only
mappingproxy({'one': 42, 'two': 2})
```
