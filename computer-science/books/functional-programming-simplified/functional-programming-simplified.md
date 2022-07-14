Functional Programming Simplified
===

Resources
---

- [Official website][1]

<!-- Links -->
[1]: https://alvinalexander.com/photos/functional-programming-simplied-free-pdf-preview/

<!-- Links end -->


Modules
---
- [[the-benefits-of-functional-programming]]

Rules for the book
---

 - There will be no null values.
 - Only pure functions will be used.
 - Immutable values will be used for all fields.
 - Whenever you use an if, you must always also use an else.
 - We won’t create “classes” that encapsulate data and behavior.

Chapter Checklist
---

- [x] 1 Introduction (or, Why I Wrote This Book) 
- [x] 2 Who This Book is For 
- [x] 3 Goals, Part 1: “Soft” Goals of This Book 
- [x] 4 Goals, Part 2: Concrete Goals 
- [x] 5 Goals, Part 3: A Disclaimer 
- [x] 6 Question Everything 
- [x] 7 Rules for Programming in this Book 
- [x] 8 One Rule for Reading this Book 
- [x] 9 What is “Functional Programming”? 
- [ ] 10 What is This Lambda You Speak Of? 
- [x] 11 The Benefits of Functional Programming 
- [x] 12 Disadvantages of Functional Programming 
- [x] 13 The “Great FP Terminology Barrier” 
- [x] 14 Pure Functions
- [x] 15 Grandma’s Cookies (and Pure Functions) 
- [x] 16 Benefits of Pure Functions 
- [x] 17 Pure Functions and I/O 
- [x] 18 Pure Function Signatures Tell All 
- [x] 19 Functional Programming as Algebra 
- [x] 20 A Note About Expression-Oriented Programming 
- [x] 21 Functional Programming is Like Unix Pipelines 
- [x] 22 Functions Are Variables, Too // (Talks about Eta Expansion)
- [x] 23 Using Methods As If They Were Functions 
- [x] 24 How to Write Functions That Take Functions as Input Parameters 
- [x] 25 How to Write a ‘map’ Function 
- [x] 26 How to Use By-Name Parameters 
- [x] 27 Functions Can Have Multiple Parameter Groups 
- [x] 28 Partially-Applied Functions (and Currying) 
- [ ] 29 Recursion: Introduction 
- [ ] 30 Recursion: Motivation 
- [ ] 31 Recursion: Let’s Look at Lists 
- [ ] 32 Recursion: How to Write a ‘sum’ Function 
- [ ] 33 Recursion: How Recursive Function Calls Work 
- [ ] 34 Visualizing the Recursive sum Function 
- [ ] 35 Recursion: A Conversation Between Two Developers 
- [ ] 36 Recursion: Thinking Recursively 
- [ ] 37 JVM Stacks and Stack Frames 
- [ ] 38 A Visual Look at Stacks and Frames 
- [ ] 39 Tail-Recursive Algorithms 
- [ ] 40 A First Look at “State” 
- [ ] 41 A Functional Game (With a Little Bit of State) 
- [x] 42 A Quick Review of Case Classes 
- [ ] 43 Update as You Copy, Don’t Mutate 
- [ ] 44 A Quick Review of for Expressions 
- [ ] 45 How to Write a Class That Can Be Used in a for Expression 
- [ ] 46 Creating a Sequence Class to be Used in a for Comprehension 
- [ ] 47 Making Sequence Work in a Simple for Loop 
- [ ] 48 HowToMakeSequenceWorkasa Single Generator in a for Expression 
- [ ] 49 Enabling Filtering in a for Expression 
- [ ] 50 How to Enable the Use of Multiple Generators in a for Expression 
- [ ] 51 A Summary of the for Expression Lessons 
- [x] 52 Pure Functions Tell No Lies 
- [x] 53 Functional Error Handling (Option, Try, or Either) 
- [x] 54 Embrace The Idioms! 
- [ ] 55 What to Think When You See That Opening Curly Brace 
- [x] 56 A Quick Review of How flatMap Works 
- [x] 57 Option Naturally Leads to flatMap 
- [x] 58 flatMap Naturally Leads to for 
- [x] 59 for Expressions are Better Than getOrElse 
- [ ] 60 Recap: Option -> flatMap -> for 
- [ ] 61 A Note About Things That Can Be Mapped-Over 
- [ ] 62 A Quick Review of Companion Objects and apply 
- [ ] 63 Starting to Glue Functions Together 
- [ ] 64 The “Bind” Concept 
- [ ] 65 GettingClosetoUsingbind in for Expressions 
- [ ] 66 Using a “Wrapper” Class in a for Expression 
- [ ] 67 Making Wrapper More Generic 
- [ ] 68 Changing “new Wrapper” to “Wrapper” 
- [ ] 69 Using bind in a for Expression 
- [ ] 70 How Debuggable, f, g, and h Work 
- [ ] 71 A Generic Version of Debuggable 
- [ ] 72 OneLastDebuggable:UsingList Instead of String 
- [ ] 73 Key Points About Monads 
- [ ] 74 Signpost: Where We’re Going Next 
- [ ] 75 Introduction: The IO Monad 
- [ ] 76 How to Use an IO Monad 
- [ ] 77 Assigning a for Expression to a Function 
- [ ] 78 The IO Monad and a for Expression That Uses Recursion 
- [ ] 79 Diving Deeper Into the IO Monad 
- [ ] 80 I’ll Come Back to the IO Monad 
- [ ] 81 Functional Composition 
- [ ] 82 An Introduction to Handling State 
- [ ] 83 Handling State Manually 
- [ ] 84 Getting State Working in a for Expression 
- [ ] 85 Handling My Golfing State with a State Monad 
- [ ] 86 The State Monad Source Code 
- [ ] 87 Signpost: Getting IO and State Working Together 
- [ ] 88 TryingtoWriteaforExpression with IO and State 
- [ ] 89 Seeing the Problem: Trying to Use State and IO Together 
- [ ] 90 Solving the Problem with Monad Transformers 
- [ ] 91 Beginning the Process of Understanding StateT 
- [ ] 92 Getting Started: We’re Going to Need a Monad Trait 
- [ ] 93 Now We Can Create StateT 
- [ ] 94 Using StateT in a for Expression 
- [ ] 95 Trying to Combine IO and StateT in a for Expression 
- [ ] 96 Fixing the IO Functions With Monadic Lifting 
- [ ] 97 A First IO/StateT for Expression 
- [ ] 98 The Final IO/StateT for Expression 
- [ ] 99 Summary of the StateT Lessons 
- [ ] 100 Signpost: Modeling the world with Scala/FP 
- [ ] 101 What is a Domain Model? 
- [ ] 102 A Review of OOP Data Modeling 
- [ ] 103 Modeling the “Data” Portion of the Pizza POS System with Scala/FP 
- [ ] 104 First Attempts to Organize Pure Functions 
- [ ] 105 Implementing FP Behavior with Modules 
- [ ] 106 Implementing the Pizza POS System Using a Modular Approach 
- [ ] 107 The “Functional Objects” Approach 
- [ ] 108 Demonstrating the “Functional Objects” Approach 
- [ ] 109 Summary of the Domain Modeling Approaches 
- [ ] 110 ScalaCheck 1: Introduction 
- [ ] 111 ScalaCheck 2: A More-Complicated Example 
- [ ] 112 The Problem with the IO Monad 
- [ ] 113 Signpost: Type Classes 
- [ ] 114 Type Classes 101: Introduction 
- [ ] 115 Type Classes 102: The Pizza Class 
- [ ] 116 Type Classes 103: The Cats Library 
- [ ] 117 Lenses, to Simplify “Update as You Copy” 
- [ ] 118 Signpost: Concurrency 
- [ ] 119 Concurrency and Mutability Don’t Mix 
- [ ] 120 Scala Concurrency Tools 
- [ ] 121 Akka Actors 
- [ ] 122 Akka Actor Examples 
- [ ] 123 Scala Futures 
- [ ] 124 A Second Futures Example 
- [ ] 125 Key Points About Futures 
- [ ] 126 A Few Notes About Real World Functional Programming 
- [ ] 127 Signpost: Wrapping Things Up 
- [ ] 128 The Learning Path 
- [ ] 129 Final Summary 
- [ ] 130 Where To Go From Here 
- [ ] A Explaining Scala’s val Function Syntax 
- [ ] B TheDifferencesBetweenvalanddef When Creating Functions 
- [ ] C A Review of Anonymous Functions 
- [ ] D Recursion is Great, But ... 
- [ ] E for expression translation examples 
- [ ] F On Using def vs val To Define Abstract Members in Traits 
- [ ] G Algebraic Data Types

[//begin]: # "Autogenerated link references for markdown compatibility"
[the-benefits-of-functional-programming]: the-benefits-of-functional-programming.md "The Benefits of Functional Programming"
[//end]: # "Autogenerated link references"
