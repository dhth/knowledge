Decorators
===

Resources
---
- [:fontawesome-solid-play-circle: Practical Decorators: Pycon 2019](https://www.youtube.com/watch?v=MjHpMCIvwsY)
- [:fontawesome-solid-link: Making your Python decorators even better, with functool.wraps](https://lerner.co.il/2019/05/05/making-your-python-decorators-even-better-with-functool-wraps/)
- [:fontawesome-solid-link: How To Test Python Decorators? How To Bypass A Decorator?](https://codebungalow.com/how-to-test-decorators-in-python/)
- [:fontawesome-solid-link: Python Decorator Tutorial with Example](https://dev.to/apcelent/python-decorator-tutorial-with-example-529f) (has examples of decorators with arguments)


Decorator with arguments
---

```python
from functools import partial, wraps

def print_result(func=None, *, prefix=''):
    if func is None:
        return partial(print_result, prefix=prefix)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{prefix}{result}')
        return result
    return wrapper

# ---------- #

@print_result
def add(a, b):
    return a + b

add(2, 3)  # outputs '5'

@print_result()
def add(a, b):
    return a + b

add(2, 3)  # outputs '5'

@print_result(prefix='The return value is ')
def add(a, b):
    return a + b

add(2, 3)  # outputs 'The return value is 5'
```
