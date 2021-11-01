Python Packages
===

Following is from David Beazley's talk.

- Explicit relative imports make refactoring of packages easier
    ```
    spam/
        __init__.py
        foo.py
        bar.py
    ```

    ```python
    # bar.py

    from spam import foo
    ```

    👆 works, but, if we want to rename the `spam` package, we'd have to go in
    the code and refactor the import above.

    Relative imports make this easier.

    ```python
    from . import foo
    ```

    Use leading `.` to move up the hierarchy.
