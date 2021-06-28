Ch 1: Getting started with Pytest
===

Pytest options
---

```bash
pytest -v tasks/test_four.py::test_asdict
# specify a test function
```

```bash
pytest -k "asdict" --collect-only
# -k is for expressions
# --collect-only shows the tests to be run, without running themx
```

```bash
-x
# exit on first fail
```

```bash
--tb=no
# turn off stack trace
```

```bash
--maxfail=2
# like -x but you can specify the number of tests
# that have to fail before exiting
```

```bash
-s or --capture=no
# turns off output capture for failing tests
# lets hooking into set_trace
```

```bash
-l or --showlocals
```

```bash
--lf
# last failed
```

```bash
-ff
# failed first
```

```bash
--disable-pytest-warnings
# disable warnings
```

```bash
-r
# show extra test summary info as specified by chars
# show extra test summary info as specified by chars
# (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
# (p)passed, (P)passed with output, (a)all except pP.
```
