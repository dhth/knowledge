Lecture 2: Shell Tools and Scripting
===

Notes
---

```bash
# double quotes expand string, single quotes do not

$_
# Last argument of last command

!!
# last command

$?
# error code of last command

false || echo "print this"
# will print

false && echo "print this"
# will not print

false ; echo "print this"
# will print

foo=$(pwd)
# foo will contain the current working directory
```

## Common utils

```bash
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted

# $0 is the name of the script
# $# is the number of arguments given to the program
# $$ is the process id
echo "Running program $0 with $# arguments with pid $$"

# $@ expands to all arguments
# instead of using $1, $2... explicitly
for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

## Expanding

```bash
ls project?
#? expands to only one character, this is called globbing

touch foo{1,2,3,4}
# will expand to touch foo1 foo2 foo3 foo4

touch project{1,2}/file{1,2,3}
# will expand to touch project1/file1 project1/file2 project1/file3 project2/file1 project2/file2 project2/file3

touch {foo,bar}/{a..j}
```

## shebang usage for python scripts
```python
#!/usr/bin/env python

# the first line tells the kernel to execute this script with
# a python interpreter, ie, we can run the script as:
# ./script.py a b c
# instead of python script.py a b c
# using usr/bin/env python increases the portability of the script
# as a machine can have multiple pythons
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```
