Python Imports
===

Following is from David Beazley's talk.

- `import foo` and `from foo import bar` both execute the entire `foo` module.
  The latter is NOT a "smart" import in any way
- Imported functions record their definition environment
    ```python
    # spam.py
    x = 42

    def blah(x):
        print(x)
    ```

    ```
    >>> from spam import blah
    >>> blah.__module__
    'spam'
    >>> blah.__globals__
    { 'x' : 42, ...}
    ```


- `__init__.py` can be used to stitch multiple modules together.
    ```python
    # spam/foo.py

    class Foo:
        ...
    ```

    ```python
    # spam/bar.py

    class Bar:
        ...
    ```

    ```python
    # spam/__init__.py

    from .foo import Foo
    from .bar import Bar
    ```

    ```python
    import spam

    foo = spam.Foo()
    bar = spam.Bar()
    ```
