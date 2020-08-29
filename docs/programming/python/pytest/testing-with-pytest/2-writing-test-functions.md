Ch 2: Writing Test Functions
===

Test if exception raised
---

```python
# code to be tested
def add(task):  # type: (Task) -> int
    """Add a task (a Task object) to the tasks database."""
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
		...

# test
def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')
```

Test exception message
---

```python
# code to be tested
def start_tasks_db(db_path, db_type):  # type: (str, str) -> None
    """Connect API functions to a db."""
    if not isinstance(db_path, string_types):
        raise TypeError('db_path must be a string')
    global _tasksdb
    if db_type == 'tiny':
        import tasks.tasksdb_tinydb
        _tasksdb = tasks.tasksdb_tinydb.start_tasks_db(db_path)
    elif db_type == 'mongo':
        import tasks.tasksdb_pymongo
        _tasksdb = tasks.tasksdb_pymongo.start_tasks_db(db_path)
    else:
        raise ValueError("db_type must be a 'tiny' or 'mongo'")

# test
def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
				# code only wants "tinydb" or "mongo"
				# will raise ValueError
    exception_msg = excinfo.value.args[:fontawesome-solid-link: 0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
```

Marks
---

```bash
# Mark a function as:
@pytest.mark.get
@pytest.mark.smoke
def some_func():
...

# Register the marks in pytest.ini
# Otherwise pytest will show warnings
[:fontawesome-solid-link: pytest]
markers =
    smoke
    get

# Use marks as follows (can be used with and, or, etc)
pytest -v -m 'smoke and get' test_api_exceptions.py
pytest -v -m 'smoke and not get' test_api_exceptions.py
```

```bash
@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')

pytest test.py -rs
# to see reasons for skipping
```

Running tests based on name
---

```bash
pytest -k _raises
pytest -k "_raises and not delete"
```

Parametrize
---

### Send params directly

```python
@pytest.mark.parametrize('summary, owner, done',
 	                         [:fontawesome-solid-link: ('sleep', None, False),
 	                          ('wake', 'brian', False),
 	                          ('breathe', 'BRIAN', True),
 	                          ('eat eggs', 'BrIaN', False),
 	                          ])

def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
```

### Send params as a variable

```python
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))
 	
task_ids = [:fontawesome-solid-link: 'Task({},{},{})'.format(t.summary, t.owner, t.done)
	            for t in tasks_to_try]
	
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
```

### Using `pytest.param`

```python
@pytest.mark.parametrize('task', [:fontawesome-solid-link: 
 	    pytest.param(Task('create'), id='just summary'),
 	    pytest.param(Task('inspire', 'Michelle'), id='summary/owner'),
 	    pytest.param(Task('encourage', 'Michelle', True), id='summary/owner/done')])

def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
```
