3: Pytest Fixtures
===

Intro
---

The `@pytest.fixture()` decorator is used to tell pytest that a function is a fixture. When you include the fixture name in the parameter list of a test function, pytest knows to run it before running the test. Fixtures can do work, and can also return data to the test function.

> Test fixtures refer to the mechanism pytest provides to allow the separation of “getting ready for” and “cleaning up after” code from your test functions.

Fixtures
---

GIVEN/WHEN/THEN → Useful to document behaviour of test

```python
# tasks_db is a fixture defined in conftest.py

def test_add_returns_valid_id(tasks_db):
	"""tasks.add(<valid task>) should return an integer."""
	# GIVEN an initialized tasks db
	# WHEN a new task is added
	# THEN returned task_id is of type int
	new_task = Task('do something')
	task_id = tasks.add(new_task)
	assert isinstance(task_id, int)
```

```python
@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
```

### See setup/teardown

```python
pytest --setup-show test.py

"""
platform darwin -- Python 3.8.4, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/dhruvthakur/code/pers/testing/code/ch3/a/tasks_proj/tests, inifile: pytest.ini
collected 3 items / 2 deselected / 1 selected

test_add.py
SETUP    S tmp_path_factory
        SETUP    F tmp_path (fixtures used: tmp_path_factory)
        SETUP    F tmpdir (fixtures used: tmp_path)
        SETUP    F tasks_db (fixtures used: tmpdir)
        func/test_add.py::test_add_returns_valid_id (fixtures used: request, tasks_db, tmp_path, tmp_path_factory, tmpdir).
        TEARDOWN F tasks_db
        TEARDOWN F tmpdir
        TEARDOWN F tmp_path
TEARDOWN S tmp_path_factory
"""
```

Exceptions can be raise from fixtures. These will be reported as  `ERROR` by pytest, instead of a `FAIL`.

Combining multiple fixtures
---

```python
########## FIXTURES ############

@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()

# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database

@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))

@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)

########### TEST ###########

def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task('throw a party'))

    #  THEN the count increases by 1
    assert tasks.count() == 4

########## TEST RUN ########

python -m pytest test_add.py::test_add_increases_count  --disable-pytest-warnings --setup-show
===================================================================== test session starts =====================================================================
platform darwin -- Python 3.8.4, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/dhruvthakur/code/pers/testing/code/ch3/a/tasks_proj/tests, inifile: pytest.ini
collected 1 item

test_add.py
SETUP    S tmp_path_factory
        SETUP    F tmp_path (fixtures used: tmp_path_factory)
        SETUP    F tmpdir (fixtures used: tmp_path)
        SETUP    F tasks_db (fixtures used: tmpdir)
        SETUP    F tasks_just_a_few
        SETUP    F db_with_3_tasks (fixtures used: tasks_db, tasks_just_a_few)
        func/test_add.py::test_add_increases_count (fixtures used: db_with_3_tasks, request, tasks_db, tasks_just_a_few, tmp_path, tmp_path_factory, tmpdir).
        TEARDOWN F db_with_3_tasks
        TEARDOWN F tasks_just_a_few
        TEARDOWN F tasks_db
        TEARDOWN F tmpdir
        TEARDOWN F tmp_path
TEARDOWN S tmp_path_factory
```

Fixture scopes
---

```python
 	import pytest
 	
 	
 	@pytest.fixture(scope='function')
 	def func_scope():
 	    """A function scope fixture."""
 	
 	
 	@pytest.fixture(scope='module')
 	def mod_scope():
 	    """A module scope fixture."""
 	
 	
 	@pytest.fixture(scope='session')
 	def sess_scope():
 	    """A session scope fixture."""
 	
 	
 	@pytest.fixture(scope='class')
 	def class_scope():
 	    """A class scope fixture."""
 	
 	
 	def test_1(sess_scope, mod_scope, func_scope):
 	    """Test using session, module, and function scope fixtures."""
 	
 	
 	def test_2(sess_scope, mod_scope, func_scope):
 	    """Demo is more fun with multiple tests."""
 	
 	@pytest.mark.usefixtures('class_scope')
 	class TestSomething():
 	    """Demo class scope fixtures."""
 	
 	    def test_3(self):
 	        """Test using a class scope fixture."""
 	
 	    def test_4(self):
 	        """Again, multiple tests are more fun."""

"""
pytest --setup-show test_scope.py
 	======================== test session starts ========================
 	collected 4 items
 	
 	test_scope.py
 	SETUP    S sess_scope
 	  SETUP    M mod_scope
 	      SETUP    F func_scope
 	        test_scope.py::test_1
 	          (fixtures used: func_scope, mod_scope, sess_scope).
 	      TEARDOWN F func_scope
 	      SETUP    F func_scope
 	        test_scope.py::test_2
 	          (fixtures used: func_scope, mod_scope, sess_scope).
 	      TEARDOWN F func_scope
 	    SETUP    C class_scope
 	        test_scope.py::TestSomething::()::test_3 (fixtures used: class_scope).
 	        test_scope.py::TestSomething::()::test_4 (fixtures used: class_scope).
 	    TEARDOWN C class_scope
 	  TEARDOWN M mod_scope
 	TEARDOWN S sess_scope
"""
```

Parameterising Fixtures
---

```python
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

task_ids = [:fontawesome-solid-link: 'Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]

@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Using a list of ids."""
    return request.param

def test_add_b(tasks_db, b_task):
    """Using b_task fixture, with ids."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)

"""
test_add_variety2.py
SETUP    S tmpdir_factory
SETUP    S tasks_db_session (fixtures used: tmpdir_factory)
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F b_task[:fontawesome-solid-link: Task(sleep,None,True)]
        func/test_add_variety2.py::test_add_b[:fontawesome-solid-link: Task(sleep,None,True)] (fixtures used: b_task, request, tasks_db, tasks_db_session, tmpdir_factory).
        TEARDOWN F b_task[:fontawesome-solid-link: Task(sleep,None,True)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F b_task[:fontawesome-solid-link: Task(wake,brian,False)]
        func/test_add_variety2.py::test_add_b[:fontawesome-solid-link: Task(wake,brian,False)] (fixtures used: b_task, request, tasks_db, tasks_db_session, tmpdir_factory).
        TEARDOWN F b_task[:fontawesome-solid-link: Task(wake,brian,False)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F b_task[:fontawesome-solid-link: Task(breathe,BRIAN,True)]
        func/test_add_variety2.py::test_add_b[:fontawesome-solid-link: Task(breathe,BRIAN,True)] (fixtures used: b_task, request, tasks_db, tasks_db_session, tmpdir_factory).
        TEARDOWN F b_task[:fontawesome-solid-link: Task(breathe,BRIAN,True)]
        TEARDOWN F tasks_db
        SETUP    F tasks_db (fixtures used: tasks_db_session)
        SETUP    F b_task[:fontawesome-solid-link: Task(exercise,BrIaN,False)]
        func/test_add_variety2.py::test_add_b[:fontawesome-solid-link: Task(exercise,BrIaN,False)] (fixtures used: b_task, request, tasks_db, tasks_db_session, tmpdir_factory).
        TEARDOWN F b_task[:fontawesome-solid-link: Task(exercise,BrIaN,False)]
        TEARDOWN F tasks_db
TEARDOWN S tasks_db_session
TEARDOWN S tmpdir_factory
"""
```
