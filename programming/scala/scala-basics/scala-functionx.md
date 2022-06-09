Scala FunctionX
===

Resources
---

- [Scala Standard Library 2.13.3 - scala.Function1][1]
- [Functional Programming in Scala | Rock the JVM][2]

<!-- Links -->
[1]: https://www.scala-lang.org/api/2.13.3/scala/Function1.html
[2]: https://rockthejvm.com/courses/728053/lectures/13122612

<!-- Links end -->


Basics
---

```
Function1[Int, Int]
[Int <- Type of first argument, Int <- return type]

Function2[String, String, String]
[String <- Type of first argument, String <- Type of second
argument, <- return type]
```

From [this][2] course lecture:

All Scala functions are instances of FunctionX types.

```scala
val doubler: Function1[Int, Int] = new Function1[Int, Int] {
override def apply(x: Int): Int = 2 * x
}

doubler(4) // 8

// syntantic sugar for the above
val doubler2: Function1[Int, Int] = (x: Int) => 2 * x
// or skip the type
val doubler3 = (x: Int) => 2 * x
```
