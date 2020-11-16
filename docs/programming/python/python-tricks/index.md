Python Tricks
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


Chapters Checklist
---

- [ ] Patterns for Cleaner Python
    - [x] Covering Your A** With Assertions 
    - [x] Complacent Comma Placement
    - [ ] Context Managers and the with Statement
    - [ ] Underscores, Dunders, and More 
    - [ ] A Shocking Truth About String Formatting 
    - [ ] “The Zen of Python” Easter Egg
- [ ] Effective Functions
    - [ ] Python’s Functions Are First-Class 
    - [ ] Lambdas Are Single-Expression Functions 
    - [ ] The Power of Decorators 
    - [ ] Fun With `*args` and `**kwargs`
    - [ ] Function Argument Unpacking 
    - [ ] Nothing to Return Here
    - [ ] Object Comparisons: “is” vs “==” 
    - [ ] String Conversion (Every Class Needs a `__repr__`)
    - [ ] Defining Your Own Exception Classes 
    - [ ] Cloning Objects for Fun and Profit 
    - [ ] Abstract Base Classes Keep Inheritance in Check 
    - [ ] What Namedtuples Are Good For
    - [ ] Class vs Instance Variable Pitfalls
    - [ ] Instance, Class, and Static Methods Demystified
- [ ] Common Data Structures in Python
    - [ ] Dictionaries, Maps, and Hashtables 
    - [ ] Array Data Structures
    - [ ] Records, Structs, and Data Transfer Objects 
    - [ ] Sets and Multisets
    - [ ] Stacks (LIFOs) 
    - [ ] Queues (FIFOs)
    - [ ] Priority Queues 
- [ ] Looping & Iteration
    - [ ] Writing Pythonic Loops
    - [ ] Comprehending Comprehensions 
    - [ ] List Slicing Tricks and the Sushi Operator 
    - [ ] Beautiful Iterators
    - [ ] Generators Are Simplified Iterators 
    - [ ] Generator Expressions 
    - [ ] Iterator Chains 
- [ ] Dictionary Tricks
    - [ ] Dictionary Default Values
    - [ ] Sorting Dictionaries for Fun and Profit 
    - [ ] Emulating Switch/Case Statements With Dicts 
    - [ ] The Craziest Dict Expression in the West 
    - [ ] So Many Ways to Merge Dictionaries 
    - [ ] Dictionary Pretty-Printing 
- [ ] Pythonic Productivity Techniques
    - [ ] Exploring Python Modules and Objects 
    - [ ] Isolating Project Dependencies With Virtualenv 
    - [ ] Peeking Behind the Bytecode Curtain 
