# Chapter 3: Effective Functions

3.1 Python's functions are first class
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

Inner functions `whisper` and `yell` can access the text parameter defined in the
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

Instance, Class, and Static Methods Demystified
---

Instance methods can modify instance state, as well as class state (via
`self.__class__` attribute).

Class methods can only modify class state.

Static methods can modify neither.


### Class methods as factory methods

Class methods can be used as factory methods as:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    @classmethod
        def prosciutto(cls):
    return cls(['mozzarella', 'tomatoes', 'ham'])
```

```
>>> Pizza.margherita()
Pizza(['mozzarella', 'tomatoes'])
>>> Pizza.prosciutto()
Pizza(['mozzarella', 'tomatoes', 'ham'])
```
