Effective Functions
===

Python's functions are first class
---

### Functions Can Capture Local State

```python
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

"""
>>> get_speak_func('Hello, World', 0.7)()
'HELLO, WORLD!'
"""
```

Inner functions whisper and yell can access the text parameter defined in the
parent function. Functions that do this are called lexical closures (or just
closures, for short). A closure remembers the values from its enclosing lexical
scope even when the program flow is no longer in that scope.

### Objects can behave like functions

Objects can be made callable using the `__call__` method.

```python
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

"""
>>> plus_3 = Adder(3)
>>> plus_3(4)
7
"""
```
