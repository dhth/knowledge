Patterns for Cleaner Python
===

Asserts
---

- asserts accept a second expression that can be used to print out useful info,
    eg. `x=5; assert x > 10, f'{x} is not greater than 10'` will raise
    `AssertionError: 5 is not less than 10`
- Don't use asserts for data validation or catching run-time errors (since
 asserts can be globally disabled).
- asserting a tuple will never result in an assertion error (tuples are truthy)
- Use asserts as a debugging aid.

Context Managers
---

```python
with open('hello.txt', 'w') as f:
    f.write('hello, world!')

# is almost equivalent to:
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
```

A context manager is a simple “protocol” (or interface) that your object needs
to follow in order to support the with statement. Basically, all you need to do
is add `__enter__` and `__exit__` methods to an object if you want it to function as
a context manager.  Python will call these two methods at the appropriate times
in the resource management cycle.

There are two ways to support the `with` statement:

### Class Based Context Managers

```python
class ManagedFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
```

### ContextLib

You can use the `contextlib.contextmanager` decorator to define a
generator-based factory function for a resource that will then automatically
support the with statement.
