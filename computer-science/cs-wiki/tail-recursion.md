Tail Recursion
===

The recursive calls occurs as the last call of any code path.

Tail recursion can be advantageous for compilers due to a specific optimization
technique called "tail call optimization" or "tail call elimination." This
optimization helps in reducing the overall stack space used by recursive
function calls.

```scala
// non tail recursive function
def sumUntil(n: Int): Int =
  if (n <= 0) 0
  else n + sumUntil(n - 1)
```

In the recursive case, the addition operation `(n + sumUntil(n - 1))` is not the
last operation. After this addition, the result is still being added to n. This
means there is an additional operation pending after the recursive call
completes.

Since there is an operation (the addition of n) pending after the recursive
call, the call is not in the tail position. The function has to remember to add
n to the result of the recursive call after it returns, and this requires
maintaining a stack frame for each recursive call.

```scala
// tail recursive function
def sumUntilV2(n: Int): Int =
  def sumUntilTailRec(currentNumber: Int, accumulator: Int): Int =
    if (currentNumber <= 0) accumulator
    else sumUntilTailRec(currentNumber - 1, accumulator + currentNumber)
```

1. Understanding the Call Stack: In programming languages, function calls are
   typically managed using a data structure called the call stack. Each time a
   function is called, a new stack frame is created to store local variables,
   parameters, and the return address. When a function completes, its stack
   frame is popped from the stack.

2. Normal Recursion: In normal recursion, each recursive call adds a new stack
   frame, leading to a growing stack. If there are too many recursive calls, it
   can result in a stack overflow, as the stack size is limited.

3. Tail Recursion: Tail recursion has a special property: the recursive call is
   the last operation in the function. Because the recursive call is the last
   thing to be done, there's no need to keep the current function's stack frame
   around.

4. Tail Call Optimization (TCO): TCO is an optimization technique where the
   compiler recognizes tail calls and avoids allocating a new stack frame for
   the recursive call. Instead of creating a new stack frame, the compiler can
   reuse the current function's stack frame for the recursive call.

5. Benefits for Compilers:
    - Reduced Stack Space: TCO allows the compiler to reuse the same stack frame
        for multiple recursive calls, saving space.
    - Prevention of Stack Overflow: Since the stack space is reused, the depth
        of recursion no longer directly correlates with the stack space used,
        reducing the risk of a stack overflow.
    - Improved Performance: The elimination of unnecessary stack frames can lead
        to improved performance as there is less overhead associated with
        managing the call stack.
