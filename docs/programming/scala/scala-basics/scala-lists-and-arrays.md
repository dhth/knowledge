Scala Lists and Arrays
===

Type Inference
---

```scala
// The two are semantically same
val greetStrings = new Array[String](3)
val greetStrings: Array[String] = new Array[String](3)

```

All operations in Scala are method calls
---

```scala
val greetStrings = Array("Hello", ", ", "World")
// is the same as
val greetStrings = Array.apply("Hello", ", ", "World")

// ---

greetStrings(0)
// gets transformed into
greetStrings.apply(0)

// ---

greetStrings(0) = "Hello"
// gets transformed into
greetStrings.update(0, "Hello")
```

Mutability
---

Arrays are mutable (the elements themselves), Lists are not.
