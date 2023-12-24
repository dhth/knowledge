# Scala Partial Functions

Resources
---

- [Partial Functions | Advanced Scala and Functional Programming][1]

<!-- Links -->
[1]: https://www.udemy.com/course/advanced-scala/learn/lecture/10937350#overview

<!-- Links end -->

Basics
---

From [this][1] lecture.

```scala
trait PartialFunction[-A, +B] extends (A => B) {
  def apply(x: A): B
  def isDefinedAt(x: A): Boolean
}

// how to use

val simplePF: PartialFunction[Int, Int] = {
  case 1 => 42
  case 2 => 65
  case 3 => 999
}
```
