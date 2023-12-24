Packaging Python Projects
===

```bash
	some_module_proj/
	├── [setup.py](http://setup.py/)
	└── some_module.py
```

The code we want to share is in `some_module.py`:

```python
# appendices/packaging/some_module_proj/some_module.py
def some_func():
   return 42
```

One directory with one module and a [setup.py](http://setup.py/) file is enough to make it installable via pip:

```python
# appendices/packaging/some_module_proj/setup.py
from setuptools import setup
setup(
	name='some_module',
	py_modules=['some_module']
)
```

```bash
$ cd /path/to/code/appendices/packaging
$ pip install ./some_module_proj
Processing ./some_module_proj
Installing collected packages: some-module
Running [setup.py](http://setup.py/) install for some-module ... done
Successfully installed some-module-0.0.0
And we can now use some_module from Python (or from a test):

$ python
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from some_module import some_func
>>> some_func()
42
>>> exit()
```

---

## Creating an Installable Package

Let’s make this code a package by adding an **init**.py and putting the **init**.py file and module in a directory with a package name:

```bash
$ tree some_package_proj/
some_package_proj/
├── [setup.py](http://setup.py/)
└── src
	 └── some_package
		 ├── **init**.py
		 └── some_module.py
```

The content of some_module.py doesn’t change. The **init**.py needs to be written to expose the module functionality to the outside world through the package namespace.

If we do something like this in **init**.py:

```python
import some_package.some_module
```

the client code will have to specify some_module:

```python
import some_package
some_package.some_module.some_func()
```

However, I’m thinking that `some_module.py` is really our API for the package, and we want everything in it to be exposed to the package level. Therefore, we’ll use this form:

```python
# appendices/packaging/some_package_proj/src/some_package/**init**.py
from some_package.some_module import *
```

Now the client code can do this instead:

```python
import some_package

some_package.some_func()
```

We also have to change the `setup.py` file, but not much:

```python
# appendices/packaging/some_package_proj/setup.py
from setuptools import setup, find_packages

setup(
	name='some_package',
	packages=find_packages(where='src'),
	package_dir={'': 'src'},
)
```

Instead of using `py_modules`, we specify `packages`.

This is now installable:

```bash
$ cd /path/to/code/appendices/packaging
$ pip install ./some_package_proj/
Processing ./some_package_proj
Installing collected packages: some-package
Running [setup.py](http://setup.py/) install for some-package ... done
Successfully installed some-package-0.0.0
and usable:

$ python
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from some_package import some_func
>>> some_func()
42
```

Our project is now installable and in a structure that’s easy to build on. You can add a tests directory at the same level of src to add our tests if you want. However, the `setup.py` file is still missing some metadata needed to create a proper source distribution or wheel. It’s just a little bit more work to make that possible.

---

## Creating a Source Distribution and Wheel

For personal use, the configuration shown in the previous section is enough to create a source distribution and a wheel. Let’s try it:

```bash
$ cd /path/to/code/appendices/packaging/some_package_proj/
$ python setup.py sdist bdist_wheel
running sdist
...
warning: sdist: standard file not found:
should have one of README, README.rst, README.txt

running check
warning: check: missing required meta-data: url

warning: check: missing meta-data:
either (author and author_email)
or (maintainer and maintainer_email) must be supplied

running bdist_wheel
...
$ ls dist
some_package-0.0.0-py3-none-any.whl some_package-0.0.0.tar.gz
```

Well, with some warnings, a .whl and a .tar.gz file are created. Let’s get rid of those warnings.

To do that, we need to:

- Add one of these files: README, README.rst, or README.txt.
- Add metadata for url.
- Add metadata for either (author and author_email) or (maintainer and maintainer_email).

The `setup.py`:

```python
appendices/packaging/some_package_proj_v2/setup.py
from setuptools import setup, find_packages

setup(
name='some_package',
description='Demonstrate packaging and distribution',

version='1.0',
author='Brian Okken',
author_email='brian@pythontesting.net',
url='[https://pragprog.com/book/bopytest/python-testing-with-pytest'](https://pragprog.com/book/bopytest/python-testing-with-pytest'%E2%80%8B),

packages=find_packages(where='src'),
package_dir={'': 'src'},
)
```

You should put the terms of the licensing in a LICENSE file. All of the code in this book follows the following license:
Here’s the README.rst:

```python
appendices/packaging/some_package_proj_v2/LICENSE
Copyright (c) 2017 The Pragmatic Programmers, LLC

All rights reserved.

Copyrights apply to this source code.

You may use the source code in your own projects, however the source code
may not be used to create commercial training material, courses, books,
articles, and the like. We make no guarantees that this source code is fit
for any purpose.
```

```markdown
appendices/packaging/some_package_proj_v2/README.rst
====================================================
some_package: Demonstrate packaging and distribution
====================================================

some_package is the Python package to demostrate how easy it is
to create installable, maintainable, shareable packages and distributions.

It does contain one function, called some_func().

.. code-block

>>> import some_package
>>> some_package.some_func()
42

That's it, really.
```

```markdown
appendices/packaging/some_package_proj_v2/CHANGELOG.rst
Changelog
=========

------------------------------------------------------

1.0
---

Changes:
~~~~~~~~

- Initial version.
```

See [http://keepachangelog.com](http://keepachangelog.com/) for some great advice on what to put in your change log. All of the changes to tasks_proj over the course of this book have been logged into a CHANGELOG.rst file.

Let’s see if this was enough to remove the warnings:

```bash
$ cd /path/to/code/appendices/packaging/some_package_proj_v2
$ python setup.py sdist bdist_wheel
running sdist
running build
running build_py
creating build
creating build/lib
creating build/lib/some_package
copying src/some_package/**init**.py
 -> build/lib/some_package
copying src/some_package/some_module.py
 -> build/lib/some_package
installing to build/bdist.macosx-10.6-intel/wheel
running install
running install_lib
creating build/bdist.macosx-10.6-intel
creating build/bdist.macosx-10.6-intel/wheel
creating build/bdist.macosx-10.6-intel/wheel/some_package
copying build/lib/some_package/**init**.py
 -> build/bdist.macosx-10.6-intel/wheel/some_package
copying build/lib/some_package/some_module.py
 -> build/bdist.macosx-10.6-intel/wheel/some_package
running install_egg_info
Copying src/some_package.egg-info to
build/bdist.macosx-10.6-intel/wheel/some_package-1.0-py3.6.egg-info
running install_scripts
creating build/bdist.macosx-10.6-intel/wheel/some_package-1.0.dist-info/WHEEL

$ ls dist
some_package-1.0-py3-none-any.whl some_package-1.0.tar.gz
```

Now, we can put the .whl and/or .tar.gz files in a local shared directory and pip install to our heart’s content:

```bash
$ cd /path/to/code/appendices/packaging/some_package_proj_v2
$ mkdir ~/packages/
$ cp dist/some_package-1.0-py3-none-any.whl ~/packages
$ cp dist/some_package-1.0.tar.gz ~/packages
$ pip install --no-index --find-links=~/packages some_package
Collecting some_package
Installing collected packages: some-package
Successfully installed some-package-1.0
$ pip install --no-index --find-links=./dist some_package==1.0
Requirement already satisfied: some_package==1.0 in
/path/to/venv/lib/python3.6/site-packages
```

Now you can create your own stash of local project packages from your team, including multiple versions of each, and install them almost as easily as packages from PyPI.
