# Call by Name v Call by Value

Resources
---

- [Call by Name and Call by Value | Rock the JVM][1]

<!-- Links -->
[1]: https://rockthejvm.com/courses/830425/lectures/15088100

<!-- Links end -->


CBV: arguments are evaluated before function invocation

CBN: arguments are passed LITERALLY, evaluated at every reference

```scala
// scala
def printTwiceByValue(x: Long): Unit = {
    println(s"By value: $x")
    println(s"By value: $x")
}

printTwiceByValue(System.nanoTime())
// By value: 21857613740708
// By value: 21857613740708

def printTwiceByName(x: => Long): Unit = {
    println(s"By name: $x")
    println(s"By name: $x")
}

printTwiceByName(System.nanoTime())
// By name: 21857614165583
// By name: 21857614264625
```

