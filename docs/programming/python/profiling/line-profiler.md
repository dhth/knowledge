# line_profiler

## Setup

[:fontawesome-solid-link: rkern/line_profiler](https://github.com/rkern/line_profiler)

```bash
pip install line_profiler
```

```python
%load_ext line_profiler
```

```python
def sum_of_lists(N):
    total = 0
    for i in range(5):
        L = [:fontawesome-solid-link: j ^ (j >> i) for j in range(N)]
        total += sum(L)
    return total
```

## `lprun`

```python
%lprun -f sum_of_lists sum_of_lists(5000)

"""
Timer unit: 1e-06 s

Total time: 0.007278 s
File: <ipython-input-3-f105717832a2>
Function: sum_of_lists at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def sum_of_lists(N):
     2         1          3.0      3.0      0.0      total = 0
     3         6          6.0      1.0      0.1      for i in range(5):
     4         5       7110.0   1422.0     97.7          L = [:fontawesome-solid-link: j ^ (j >> i) for j in range(N)]
     5         5        158.0     31.6      2.2          total += sum(L)
     6         1          1.0      1.0      0.0      return total
"""
```
