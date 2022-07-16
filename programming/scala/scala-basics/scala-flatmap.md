Scala FlatMap
===

Resources
---

- [Functional Programming in Scala | Rock the JVM][1]

<!-- Links -->
[1]: https://rockthejvm.com/courses/728053/lectures/13122612

<!-- Links end -->

Basics
---

From [this][1] rockthejvm course lecture:

```scala
val aFlatMappedList = List(1, 2, 3).flatMap(x => List(x, 2 * x))
val aFlatMappedListAlternativeSyntax = List(1, 2, 3).flatMap { x =>
    List(x, 2 * x)
}
println(aFlatMappedList)
// List(1, 2, 2, 4, 3, 6)


val allPairs = List(1,2,3).flatMap(number => List('a', 'b', 'c').map(letter => s"$number-$letter"))
println(allPairs)
// List(1-a, 1-b, 1-c, 2-a, 2-b, 2-c, 3-a, 3-b, 3-c)

```
