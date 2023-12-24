# The Benefits of Functional Programming

Testing is easier with pure functions
---

In imperative code, you may have a function like this:

```scala
def doSomethingHidden(o: Order, p: Pizza): Unit ...
```

You can’t tell much about what that method does by looking at its signature, but because it returns nothing (Unit) — presumably it
(a) modifies those variables, or
(b) changes some hidden state, or
(c) interacts with the outside world.

When methods modify hidden state, you end up having to write long test
code like this:

```scala
test("test hidden stuff that has side effects") {
    setUpPizzaState(p)
    setUpOrderState(o, p)
    doSomethingHidden(o, p)
    val result = getTheSideEffectFromThatMethod()
    assertEquals(result, expectedResult)
}
```

In FP you can’t have code like that, so testing is simpler, like this:

```scala
test("test obvious stuff") {
    val result = doSomethingObvious(x, y, z)
    test(result, expectedResult)
}
```
 
