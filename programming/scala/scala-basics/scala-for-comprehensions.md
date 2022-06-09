Scala For Comprehensions
===

```scala
val allPairs = List(1, 2, 3).flatMap(number => List('a', 'b', 'c').map(letter => s"$number-$letter"))
println(allPairs)
// List(1-a, 1-b, 1-c, 2-a, 2-b, 2-c, 3-a, 3-b, 3-c)

// the above is equivalent to
val allPairsWithForComp = for {
  number <- List(1, 2, 3)
  letter <- List('a', 'b', 'c')
} yield s"$number-$letter"

println(allPairsWithForComp)
// List(1-a, 1-b, 1-c, 2-a, 2-b, 2-c, 3-a, 3-b, 3-c)
```
