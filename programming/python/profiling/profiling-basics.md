Profiling Basics
===

- `%time`: Time the execution of a single statement
- `%timeit`: Time repeated execution of a single statement for more accuracy
- `%prun`: Run code with the profiler
- `%lprun`: Run code with the line-by-line profiler
- `%memit`: Measure the memory use of a single statement
- `%mprun`: Run code with the line-by-line memory profiler

(last four not bundled with IPython)

## `prun`

```python
%prun sum_of_lists(1000000)

"""
14 function calls in 0.582 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    0.505    0.101    0.505    0.101 <ipython-input-3-f105717832a2>:4(<listcomp>)
        5    0.036    0.007    0.036    0.007 {built-in method builtins.sum}
        1    0.031    0.031    0.572    0.572 <ipython-input-3-f105717832a2>:1(sum_of_lists)
        1    0.009    0.009    0.581    0.581 <string>:1(<module>)
        1    0.000    0.000    0.582    0.582 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
```
