# Functional Programming Made Easier

Modules
---

Chapter Checklist
---

- [x] Introduction
- [x] Learning Functional Programming is Hard.
- [x] Learning Programming is Learning How to Think
- [x] Learning Functional Programming is Learning to Think Differently
- [x] Why Functional Programming?
- [x] You Cannot Describe an Experience
- [x] Barrier to Entry
- [x] Costs of Ownership
- [x] Case Study: Javascript
- [x] Case Study: Elm
- [x] Finding Developers
- [x] Finding Jobs
- [x] Who is This Book For?
- [x] From A to Z
- [x] A, B, X, Y, Z
- [x] A, B, C
- [x] X, Y, Z
- [x] A to Z
- [x] Why PureScript?
- [x] What’s PureScript?
- [x] Why not Haskell or Elm or ...?
- [x] Haskell
- [x] Elm
- [x] Some Other Functional Language
- [x] Why PureScript?
- [x] Four Part Harmony
- [x] Beginner
- [x] Intermediate
- [x] Advanced
- [x] Beyond
- [x] Exercises
- [x] So Many Pages
- [x] I: Beginner
    - [x] 1. Discipline is Freedom
        - [x] 1.1. Global State
        - [x] 1.2. Mutable State
            - [x] 1.2.1. No Variables
            - [x] 1.2.2. No Loops
        - [x] 1.3. Purity
        - [x] 1.4. Optimization
            - [x] 1.4.1. Memoization
            - [x] 1.4.2. Compiler Optimization
        - [x] 1.5. Types
            - [x] 1.5.1. Signal to Noise
            - [x] 1.5.2. Perceived Limits
            - [x] 1.5.3. Cake and Eat It
            - [x] 1.5.4. Cutting Through the Noise
            - [x] 1.5.5. Static Type Costs and Benefits
        - [x] 1.6. Summary
    - [x] 2. The Power of Functions
        - [x] 2.1. Functions as Parameters
        - [x] 2.2. Functions as Return Values
        - [x] 2.3. Higher-order Functions
        - [x] 2.4. Composition
            - [x] 2.4.1. Point-free Notation
        - [x] 2.5. Currying
            - [x] 2.5.1. Partial Application
    - [ ] 3. The Basics of PureScript
        - [ ] 3.1. Types
            - [ ] 3.1.1. Javascript Primitives
- [ ] Boolean Type
- [ ] Char Type
- [ ] String Type
- [ ] Number Type
            - [ ] 3.1.2. PureScript Primitives
- [ ] Int Type
- [ ] Array Type
- [ ] Record Type
- [ ] Syntactical Oddity
            - [ ] 3.1.3. User Types
- [ ] Type Alias
- [ ] Data Type
- [ ] Algebraic Data Types (ADTs)
- [ ] New Types
            - [ ] 3.1.4. Common Library Types
- [ ] Void
- [ ] Unit
- [ ] Maybe
- [ ] Either
- [ ] Maybe vs Either
- [ ] Tuple
- [ ] Either vs Tuple
- [ ] List
        - [ ] 3.2. Pattern Matching
            - [ ] 3.2.1. Case Expression
            - [ ] 3.2.2. String Patterns
            - [ ] 3.2.3. Array Patterns
            - [ ] 3.2.4. List Patterns
            - [ ] 3.2.5. Array vs List
            - [ ] 3.2.6. Record Patterns
        - [ ] 3.3. Logical Control
            - [ ] 3.3.1. If-Then-Else Expression
            - [ ] 3.3.2. Case Expression
            - [ ] 3.3.3. Pattern Matching
            - [ ] 3.3.4. Guards
        - [ ] 3.4. Lambda Functions
        - [ ] 3.5. Wildcards
            - [ ] 3.5.1. Case Expression
            - [ ] 3.5.2. Operator Sections
            - [ ] 3.5.3. Records
        - [ ] 3.6. Bindings
            - [ ] 3.6.1. Where
            - [ ] 3.6.2. Let
        - [ ] 3.7. Binary Operators
            - [ ] 3.7.1. Associativity
            - [ ] 3.7.2. Precedence
            - [ ] 3.7.3. Fixity
        - [ ] 3.8. Comments
        - [ ] 3.9. Inferring Functionality from Type Signatures
        - [ ] 3.10. Summary
    - [ ] 4. Installing PureScript
        - [ ] 4.1. Compiler and Tools
            - [ ] 4.1.1. Installing Node
- [ ] For Node Already Installed
- [ ] For Node NOT Installed
            - [ ] 4.1.2. Create Project
- [ ] Initialize Project for npm and npx
- [ ] Future-proofing
- [ ] Install purescript and spago into your Project
- [ ] Initialize Project for git (Optional)
            - [ ] 4.1.3. Initialize PureScript Project
            - [ ] 4.1.4. A Second Project
        - [ ] 4.2. Editor and Plugins
            - [ ] 4.2.1. Install Extensions
            - [ ] 4.2.2. Configure Extensions
            - [ ] 4.2.3. Configure Editor
    - [ ] 5. Basic Coding in PureScript
        - [ ] 5.1. Prelude
        - [ ] 5.2. Exercise Program
        - [ ] 5.3. Pursuit
        - [ ] 5.4. Writing flip
            - [ ] 5.4.1. Hint for flip
            - [ ] 5.4.2. Code for flip
            - [ ] 5.4.3. Alternative Coding for flip
        - [ ] 5.5. Writing const
            - [ ] 5.5.1. Hint for const
            - [ ] 5.5.2. Code for const
        - [ ] 5.6. The Apply Operator ($)
        - [ ] 5.7. Writing apply
            - [ ] 5.7.1. Hint for ($)
            - [ ] 5.7.2. Code for ($)
        - [ ] 5.8. Writing the Apply Flipped Operator (#)
            - [ ] 5.8.1. Code for applyFlipped and (#)
        - [ ] 5.9. Preparing to Write Data.List Functions
        - [ ] 5.10. Why Data.List and not Data.Array
        - [ ] 5.11. Writing singleton
            - [ ] 5.11.1. Code for singleton
        - [ ] 5.12. Writing null
            - [ ] 5.12.1. Code for null
        - [ ] 5.13. Writing snoc
            - [ ] 5.13.1. Hint for snoc
            - [ ] 5.13.2. Code for snoc
        - [ ] 5.14. Writing length
            - [ ] 5.14.1. Hint for length
            - [ ] 5.14.2. Code for length
        - [ ] 5.15. Tail Recursion
            - [ ] 5.15.1. Observations regarding Tail Recursion
        - [ ] 5.16. Writing head
            - [ ] 5.16.1. Hint for head
            - [ ] 5.16.2. Code for head
        - [ ] 5.17. Writing tail
            - [ ] 5.17.1. Hint for tail
            - [ ] 5.17.2. Code for tail
        - [ ] 5.18. Writing last
            - [ ] 5.18.1. Hint for last
            - [ ] 5.18.2. Code for last
        - [ ] 5.19. Writing init
            - [ ] 5.19.1. Hint for init
            - [ ] 5.19.2. Code for init
        - [ ] 5.20. Writing uncons
            - [ ] 5.20.1. Code for uncons
        - [ ] 5.21. Writing index
            - [ ] 5.21.1. Hint for index
            - [ ] 5.21.2. Code for index
        - [ ] 5.22. Writing !!
            - [ ] 5.22.1. Hint for !!
            - [ ] 5.22.2. Code for !!
        - [ ] 5.23. Writing findIndex
            - [ ] 5.23.1. Hint for findIndex
            - [ ] 5.23.2. Code for findIndex
        - [ ] 5.24. Writing findLastIndex
            - [ ] 5.24.1. Hint for findLastIndex
            - [ ] 5.24.2. Code for findLastIndex
        - [ ] 5.25. Local Function Type Signatures
        - [ ] 5.26. Writing reverse
            - [ ] 5.26.1. Hints for reverse
            - [ ] 5.26.2. Code for reverse
        - [ ] 5.27. Writing concat
            - [ ] 5.27.1. Hint for concat
            - [ ] 5.27.2. Code for concat
        - [ ] 5.28. Writing filter
            - [ ] 5.28.1. Code for filter
            - [ ] 5.28.2. Alternative Coding for filter
        - [ ] 5.29. Tail Recursive version of filter
        - [ ] 5.30. Time vs Space
        - [ ] 5.31. Writing catMaybes
            - [ ] 5.31.1. Hint for catMaybes
            - [ ] 5.31.2. Code for catMaybes
        - [ ] 5.32. Writing range
            - [ ] 5.32.1. Hint for range
            - [ ] 5.32.2. Code for range
        - [ ] 5.33. Optimizing range
        - [ ] 5.34. Writing take
            - [ ] 5.34.1. Hint for take
            - [ ] 5.34.2. Code for take
        - [ ] 5.35. Writing drop
            - [ ] 5.35.1. Code for drop
        - [ ] 5.36. Writing takeWhile
            - [ ] 5.36.1. Code for takeWhile
        - [ ] 5.37. Writing dropWhile
            - [ ] 5.37.1. Code for dropWhile
        - [ ] 5.38. Writing takeEnd
            - [ ] 5.38.1. Hint for takeEnd
        - [ ] 5.39. Another Hint for takeEnd
            - [ ] 5.39.1. Code for takeEnd
        - [ ] 5.40. Writing dropEnd
            - [ ] 5.40.1. Code for dropEnd
        - [ ] 5.41. Writing zip
            - [ ] 5.41.1. Code for zip
        - [ ] 5.42. Writing unzip
            - [ ] 5.42.1. Code for unzip
- [ ] II: Intermediate
    - [ ] 6. Typeclasses
        - [ ] 6.1. The Problem
        - [ ] 6.2. The Solution
        - [ ] 6.3. Constraints
        - [ ] 6.4. Typeclass Requirement
        - [ ] 6.5. Built-in Typeclasses
            - [ ] 6.5.1. Eq Typeclass
            - [ ] 6.5.2. Ord Typeclass
            - [ ] 6.5.3. Show Typeclass
        - [ ] 6.6. Derived Instances
        - [ ] 6.7. Newtype Typeclass
        - [ ] 6.8. Deriving Instances using newtype
        - [ ] 6.9. Overlapping Instances
        - [ ] 6.10. Orphaned Instances
        - [ ] 6.11. Instance Dependencies
        - [ ] 6.12. Multi-Parametric Typeclasses
        - [ ] 6.13. Functional Dependency
    - [ ] 7. Coding Typeclasses
        - [ ] 7.1. Coding Preparation
        - [ ] 7.2. Maybe Data Type
        - [ ] 7.3. Code for Maybe Data Type
        - [ ] 7.4. Writing Eq for Maybe
        - [ ] 7.5. Code for Eq for Maybe
        - [ ] 7.6. Writing Ord for Maybe
        - [ ] 7.7. Hint for Ord for Maybe
        - [ ] 7.8. Code for Ord for Maybe
        - [ ] 7.9. Writing >=
        - [ ] 7.10. Hint for >=
        - [ ] 7.11. Code for >=
        - [ ] 7.12. Writing Show for Maybe
        - [ ] 7.13. Code for Show for Maybe
        - [ ] 7.14. Deriving Eq, Ord and Show for Maybe
        - [ ] 7.15. Hint for Deriving
        - [ ] 7.16. Hint for Deriving Show
        - [ ] 7.17. Code for Eq, Ord and Show for Maybe
        - [ ] 7.18. Deriving Eq, Ord and Show for Either
        - [ ] 7.19. Writing Eq, Ord and Show for Either
        - [ ] 7.20. Creating Our Own Typeclass
        - [ ] 7.21. Hint for ToCSV
        - [ ] 7.22. Code for ToCSV
        - [ ] 7.23. Using ToCSV
        - [ ] 7.24. Another Hint for ToCSV
        - [ ] 7.25. Code for ToCSV
        - [ ] 7.26. Testing ToCSV
        - [ ] 7.27. Writing FromCSV
        - [ ] 7.28. Code for FromCSV
        - [ ] 7.29. Testing FromCSV
    - [ ] 8. Abstract Algebra
        - [ ] 8.1. Binary Operators
            - [ ] 8.1.1. Associative Property
            - [ ] 8.1.2. Commutative Property
        - [ ] 8.2. Closure
        - [ ] 8.3. Magma
        - [ ] 8.4. Semigroup
        - [ ] 8.5. Semigroup Typeclass
        - [ ] 8.6. Monoid
        - [ ] 8.7. Monoid Typeclass
        - [ ] 8.8. Monoids in Programming vs Math
        - [ ] 8.9. Monoids in Programming
        - [ ] 8.10. Groups
        - [ ] 8.11. Group Typeclass
        - [ ] 8.12. Modular Arithmetic and Groups
        - [ ] 8.13. Abelian Group
        - [ ] 8.14. Abelian Group Type Alias
        - [ ] 8.15. Arithmetic Operators in PureScript
        - [ ] 8.16. Semiring
        - [ ] 8.17. Semiring Typeclass
        - [ ] 8.18. Semiring for Functions
        - [ ] 8.19. Semiring Laws for Functions
        - [ ] 8.20. Ring
        - [ ] 8.21. Ring Typeclass
        - [ ] 8.22. Commutative Ring Typeclass
        - [ ] 8.23. Euclidean Ring
        - [ ] 8.24. Summary
    - [ ] 9. Coding Abstract Algebra
        - [ ] 9.1. Writing Semigroup Typeclass
        - [ ] 9.2. Hint for Semigroup Typeclass
        - [ ] 9.3. Code for Semigroup Typeclass
        - [ ] 9.4. Writing Monoid Typeclass
        - [ ] 9.5. Code for Monoid Typeclass
        - [ ] 9.6. Writing Semigroup for AndBool
        - [ ] 9.7. Hint for Semigroup for AndBool
        - [ ] 9.8. Code for Semigroup for AndBool
        - [ ] 9.9. Writing Monoid for AndBool
        - [ ] 9.10. Code for Monoid for AndBool
        - [ ] 9.11. Verify Semigroup Laws for AndBool
        - [ ] 9.12. Writing verifyAndBoolSemigroup
        - [ ] 9.13. Verify Monoid Laws for AndBool
        - [ ] 9.14. Writing verifyAndBoolMonoid
        - [ ] 9.15. Writing Semigroup and Monoid for OrBool
        - [ ] 9.16. Code for Semigroup and Monoid for OrBool
        - [ ] 9.17. Verify Semigroup and Monoid Laws for OrBool
        - [ ] 9.18. Code for Semigroup and Monoid Laws for OrBool
        - [ ] 9.19. Writing Mod4 Data Type
        - [ ] 9.20. Code for Mod4 Data Type
        - [ ] 9.21. Writing Semigroup for Mod4
        - [ ] 9.22. Hint for Semigroup for Mod4
        - [ ] 9.23. Code for Semigroup for Mod4
        - [ ] 9.24. Writing Monoid for Mod4
        - [ ] 9.25. Code for Monoid for Mod4
        - [ ] 9.26. Writing Group Typeclass
        - [ ] 9.27. Code for Group Typeclass
        - [ ] 9.28. Writing Group for Mod4
        - [ ] 9.29. Code for Group for Mod4
        - [ ] 9.30. Writing Eq and Show for Mod4
        - [ ] 9.31. Code for Eq and Show for Mod4
        - [ ] 9.32. Writing verifyMod4Semigroup for Mod4
        - [ ] 9.33. Code for verifyMod4Semigroup for Mod4
        - [ ] 9.34. Writing verifyMod4Monoid for Mod4
        - [ ] 9.35. Code for verifyMod4Monoid for Mod4
        - [ ] 9.36. Writing Semigroup for Maybe
        - [ ] 9.37. Writing Semigroup and Monoid for First
        - [ ] 9.38. Code for Semigroup and Monoid for First
        - [ ] 9.39. Writing Semigroup and Monoid for Last
        - [ ] 9.40. Code for Semigroup and Monoid for First
    - [ ] 10. Folds
        - [ ] 10.1. Fold by other Names
        - [ ] 10.2. Foldable Typeclass
        - [ ] 10.3. Fold Associativity
        - [ ] 10.4. Foldable for List
        - [ ] 10.5. Rewriting length with Folds
    - [ ] 11. Coding Folds
        - [ ] 11.1. Writing reverse
        - [ ] 11.2. Code for reverse
        - [ ] 11.3. Writing max
        - [ ] 11.4. Hint for max
        - [ ] 11.5. Code for max
        - [ ] 11.6. Writing findMax
        - [ ] 11.7. Code for findMax
        - [ ] 11.8. Improving findMax
        - [ ] 11.9. Improved findMax
        - [ ] 11.10. Code for findMax using Fold
        - [ ] 11.11. Code for findMax using NonEmptyList
        - [ ] 11.12. Postmortem of findMax and findMaxNE
        - [ ] 11.13. Writing findMaxNE using foldl1
        - [ ] 11.14. Code for findMaxNE using foldl1
        - [ ] 11.15. Writing foldl1
        - [ ] 11.16. Hint for foldl1
        - [ ] 11.17. Code for foldl1
        - [ ] 11.18. Writing sum
        - [ ] 11.19. Code for sum as a Recursive Function
        - [ ] 11.20. Code for sum as Tail Recursive
        - [ ] 11.21. Code for sum using foldl
        - [ ] 11.22. Hint for sum for Ints and Numbers
        - [ ] 11.23. Code for sum for Ints and Numbers
        - [ ] 11.24. Code for sum using Foldable
        - [ ] 11.25. Using sum with Tree
        - [ ] 11.26. Hint for Foldable for Tree
        - [ ] 11.27. Code for toList Instance for Tree
        - [ ] 11.28. Code for Foldable for Tree
        - [ ] 11.29. Improving on Foldable for Tree
    - [ ] 12. Functors
        - [ ] 12.1. Defining ADTs
        - [ ] 12.2. Semantics
            - [ ] 12.2.1. Name
            - [ ] 12.2.2. Implicit Behavior
            - [ ] 12.2.3. Explicit Behavior
        - [ ] 12.3. Contexts
        - [ ] 12.4. Higher-kinded Types
        - [ ] 12.5. Functions with Simple Types
        - [ ] 12.6. Functors to the Rescue
        - [ ] 12.7. Two Perspectives of map
        - [ ] 12.8. The Power of Abstractions
        - [ ] 12.9. A Little Category Theory
        - [ ] 12.10. Concrete Examples in Hask
        - [ ] 12.11. Functors in Category Theory
        - [ ] 12.12. Functor Laws
        - [ ] 12.13. Verifying the Functor Laws for Maybe
        - [ ] 12.14. Functor Instance for Either
        - [ ] 12.15. Functor Instance for Choice
        - [ ] 12.16. Bifunctor Typeclass
        - [ ] 12.17. Bifunctors in Category Theory
        - [ ] 12.18. Bifunctor Laws
        - [ ] 12.19. Functors in Perspective
    - [ ] 13. Coding Functors
        - [ ] 13.1. Writing Functor Instance for Maybe
        - [ ] 13.2. Code for Functor Instance of Maybe
        - [ ] 13.3. Writing Functor Instance for Either
        - [ ] 13.4. Code for Functor Instance of Either
        - [ ] 13.5. Writing Functor Instance for Tuple
        - [ ] 13.6. Code for Functor Instance of Tuple
        - [ ] 13.7. Writing Functor Instance for Threeple
        - [ ] 13.8. Writing Functor Instance for Threeple
        - [ ] 13.9. Validating the Functor Laws
        - [ ] 13.10. Writing Bifunctor Instance for Either
        - [ ] 13.11. Code for Bifunctor Instance for Either
        - [ ] 13.12. Writing Bifunctor Instance for Tuple
        - [ ] 13.13. Code for Bifunctor Instance for Tuple
        - [ ] 13.14. Writing Bifunctor Instance for Threeple
        - [ ] 13.15. Code for Bifunctor Instance for Threeple
        - [ ] 13.16. Validating the Bifunctor Laws
    - [ ] 14. More Functors
        - [ ] 14.1. Functors of Values
        - [ ] 14.2. Functors of Functions
        - [ ] 14.3. Contravariant Functor
        - [ ] 14.4. Contravariant Laws
        - [ ] 14.5. Contravariant in Category Theory
        - [ ] 14.6. Choosing Functor or Contravariant
        - [ ] 14.7. Polarity
        - [ ] 14.8. Invariant Functor
        - [ ] 14.9. Invariant Laws
        - [ ] 14.10. Homomorphisms
        - [ ] 14.11. Natural Transformations
        - [ ] 14.12. Monoid Homomorphisms
        - [ ] 14.13. Isomorphisms
        - [ ] 14.14. Functor Instances for Function
        - [ ] 14.15. Profunctor
        - [ ] 14.16. Profunctor Laws
        - [ ] 14.17. Profunctor and Isomorphisms
        - [ ] 14.18. Profunctor Perspective
        - [ ] 14.19. Functor Summary
        - [ ] 14.20. Functor Intuition
    - [ ] 15. Coding More Functors
        - [ ] 15.1. Writing the Predicate odd
        - [ ] 15.2. Code for the Predicate odd
        - [ ] 15.3. Writing a Predicate Type
        - [ ] 15.4. Code for a Predicate Type
        - [ ] 15.5. Code for runPredicate
        - [ ] 15.6. Writing Contravariant Instance for Predicate
        - [ ] 15.7. Code for Contravariant Instance for Predicate
        - [ ] 15.8. Folds and Moore Machines
        - [ ] 15.9. Hint for Profunctor for Moore
        - [ ] 15.10. Code for Profunctor for Moore
        - [ ] 15.11. Modeling Folds with Moore Machines
        - [ ] 15.12. Writing a Moore Machine that Folds
        - [ ] 15.13. Code for addr
        - [ ] 15.14. Code for a general addr
        - [ ] 15.15. Writing runFoldL
        - [ ] 15.16. Code for runFoldL
        - [ ] 15.17. Leveraging Moore’s Profunctor Instance
        - [ ] 15.18. Hint for sizer
        - [ ] 15.19. Code for sizer
        - [ ] 15.20. Power of the Functor
- [ ] III: Advanced
    - [ ] 16. Applicative Functors, Traversables and Alternatives
        - [ ] 16.1. Applicative in Haskell
        - [ ] 16.2. Applicative Functors in Category Theory
        - [ ] 16.3. Apply Laws
        - [ ] 16.4. Applicative Laws
        - [ ] 16.5. Applicative Instance for Maybe
        - [ ] 16.6. Applicative Instance for Product Types
        - [ ] 16.7. Applicative Instance for Sum Types
        - [ ] 16.8. An Applicative Example
        - [ ] 16.9. Applicative Effects
        - [ ] 16.10. Functors vs Applicatives with Effects
        - [ ] 16.11. Examples of Applicative Effects
        - [ ] 16.12. Applicative Effects and Commutativity
        - [ ] 16.13. Traversables
        - [ ] 16.14. Traversable for List
        - [ ] 16.15. A Few Words on Context
        - [ ] 16.16. Alt
        - [ ] 16.17. Alt Laws
        - [ ] 16.18. Plus
        - [ ] 16.19. Plus Laws
        - [ ] 16.20. Alternative Functor
    - [ ] 17. Coding Applicatives
        - [ ] 17.1. Writing Applicative Instance for Maybe
        - [ ] 17.2. Code for Applicative Instance for Maybe
        - [ ] 17.3. Writing Applicative Instance for Either
        - [ ] 17.4. Code for Applicative Instance for Either
        - [ ] 17.5. Validation
        - [ ] 17.6. Using Validation
        - [ ] 17.7. Applicative Parsers
        - [ ] 17.8. Parsers in General
        - [ ] 17.9. Writing an Applicative Parser
        - [ ] 17.10. Looking Deeper at our Parser
        - [ ] 17.11. A Common Pattern with Our Parser
        - [ ] 17.12. Using Our Parser
    - [ ] 18. Monads
        - [ ] 18.1. Side-effects
            - [ ] 18.1.1. Composing Side-effect Functions
            - [ ] 18.1.2. Composing Side-effect Function with Pure Ones
            - [ ] 18.1.3. Function Application with Side-effect Functions
        - [ ] 18.2. Debuggable Type
        - [ ] 18.3. Generalizing Debuggable
        - [ ] 18.4. We Created a Monad and More
        - [ ] 18.5. An Alternative Monad Implementation
        - [ ] 18.6. Back to PureScript’s Monad Implementation
        - [ ] 18.7. Recap Bind, Monad and Supporting Functions
        - [ ] 18.8. Haskell’s Monad Implementation
        - [ ] 18.9. Monad Laws
        - [ ] 18.10. Monad Instance for Maybe
        - [ ] 18.11. Working with Maybe Monad
        - [ ] 18.12. Do Notation
        - [ ] 18.13. Cheating with the Applicative Instance and ap
        - [ ] 18.14. Monad Instance for Either
        - [ ] 18.15. Working with Either Monad
        - [ ] 18.16. Adding Monad Instance for Validation
        - [ ] 18.17. Writer Monad
        - [ ] 18.18. Writer Helper Functions
        - [ ] 18.19. Parallel Computations
        - [ ] 18.20. Reader Monad
        - [ ] 18.21. State Monad
        - [ ] 18.22. Using State as a Monadic Validation
        - [ ] 18.23. The Kleisli Category
    - [ ] 19. Coding Monads
        - [ ] 19.1. Writing Monad Instance for Maybe
        - [ ] 19.2. Code for Monad Instance for Maybe
        - [ ] 19.3. Writing Monad Instance for Either
        - [ ] 19.4. Code for Monad Instance for Either
        - [ ] 19.5. Monadic Parsers
        - [ ] 19.6. Coding with Monadic Parsers
        - [ ] 19.7. Writing a Date Parser
        - [ ] 19.8. How Does Parser Actually Work
        - [ ] 19.9. some and many Combinators
        - [ ] 19.10. Using some and many
        - [ ] 19.11. The RWS Monad
    - [ ] 20. Monad Stacks
        - [ ] 20.1. Reducing the need for lift
        - [ ] 20.2. Monad Transformers and their APIs
        - [ ] 20.3. The Error Monad Transformer, ExceptT
        - [ ] 20.4. Monad Stack Order
        - [ ] 20.5. Coding with Monad Transformers
        - [ ] 20.6. Coding with Effect at the Base
        - [ ] 20.7. Coding WriterT
        - [ ] 20.8. Coding ReaderT
        - [ ] 20.9. Making ReaderT Easier to Use
        - [ ] 20.10. The Power of the Combinator
    - [ ] 21. Coding Monad Transformers
        - [ ] 21.1. Writing the StateT Monad Transformer
        - [ ] 21.2. Type Holes and Undefined
        - [ ] 21.3. Back to Writing the StateT Monad Transformer
        - [ ] 21.4. Testing our StateT Implementation
        - [ ] 21.5. Problems with using StateT with ExceptT
        - [ ] 21.6. Guidelines for Using ExceptT
- [ ] IV: Beyond
    - [ ] 22. Synchronous and Asynchronous Effects
        - [ ] 22.1. Working with the Effect Monad
        - [ ] 22.2. Working with the Aff Monad
            - [ ] 22.2.1. Fibers
            - [ ] 22.2.2. Cancelers
            - [ ] 22.2.3. AVars
            - [ ] 22.2.4. Busses
    - [ ] 23. Coding With Effects
        - [ ] 23.1. Simple AVar Program Specification
        - [ ] 23.2. Effects Program Specifications
            - [ ] 23.2.1. Creating a Random Number
            - [ ] 23.2.2. Making a Monad Stack
            - [ ] 23.2.3. Creating a Fiber
            - [ ] 23.2.4. Running a Monad Stack in a Fiber
            - [ ] 23.2.5. Making a Bus
            - [ ] 23.2.6. Publish to a Bus
            - [ ] 23.2.7. Subscribing to a Bus
        - [ ] 23.3. Coding our Effects Program
        - [ ] 23.4. Javascript Runtime with AVars and Busses
    - [ ] 24. JSON and Ajax
        - [ ] 24.1. Generic JSON Encoding and Decoding
            - [ ] 24.1.1. Foreign Module
            - [ ] 24.1.2. Foreign.Generic Module
            - [ ] 24.1.3. Foreign.Generic.Class Module
        - [ ] 24.2. Argonaut JSON Encoding and Decoding
        - [ ] 24.3. Ajax
            - [ ] 24.3.1. GET Request
            - [ ] 24.3.2. POST Request
    - [ ] 25. Coding With Ajax and JSON
        - [ ] 25.1. Ajax Program Specifications
        - [ ] 25.2. Coding Ajax and JSON with Foreign
            - [ ] 25.2.1. Encoding and Sending to the Echo Server
            - [ ] 25.2.2. Decoding the Response Modeled with Reversed Names
            - [ ] 25.2.3. Decoding the Response Using Argonaut
            - [ ] 25.2.4. Serial and Parallel Aff
            - [ ] 25.2.5. Using Parallel with Ajax
    - [ ] 26. Foreign Function Interface (FFI)
        - [ ] 26.1. FFIs That Return PureScript Types
        - [ ] 26.2. FFIs and Effect
        - [ ] 26.3. FFIs and Aff
    - [ ] 27. Coding With FFIs
        - [ ] 27.1. Wrapping an NPM library
        - [ ] 27.2. Reversing JSON Keys in Javascript
    - [ ] 28. Writing a Backend using HTTPure
        - [ ] 28.1. A Brief Primer on HTTPure
            - [ ] 28.1.1. Creating an HTTP Server
        - [ ] 28.2. Routers
        - [ ] 28.3. API For a Front-end Application
        - [ ] 28.4. Modeling the API
        - [ ] 28.5. Coding the Server’s Infrastructure
        - [ ] 28.6. Coding the Account Handler
            - [ ] 28.6.1. Coding loadAccounts
            - [ ] 28.6.2. Coding createAccount
        - [ ] 28.7. Coding the Account Manager
            - [ ] 28.7.1. Code for Password Hash
            - [ ] 28.7.2. Coding startup and shutdown for Account Manager
            - [ ] 28.7.3. Coding verifyLogon
            - [ ] 28.7.4. Finishing the logon Request
            - [ ] 28.7.5. Fleshing out router
        - [ ] 28.8. Coding the Session Manager
            - [ ] 28.8.1. Code for startup, shutdown and verifySession
        - [ ] 28.9. Server Logging
        - [ ] 28.10. Coding the API
            - [ ] 28.10.1. Coding LogoffRequest API Handler
            - [ ] 28.10.2. Coding CreateUserRequest API Handler
            - [ ] 28.10.3. Improving Our Parser
            - [ ] 28.10.4. Coding QueryUsers API Handler
        - [ ] 28.11. Servers in PureScript
    - [ ] 29. Building Front-ends using Halogen
        - [ ] 29.1. Halogen Component Overview
            - [ ] 29.1.1. State
            - [ ] 29.1.2. Actions
            - [ ] 29.1.3. Queries
            - [ ] 29.1.4. Inputs
            - [ ] 29.1.5. Outputs
            - [ ] 29.1.6. Emitters
            - [ ] 29.1.7. Lifecycle
            - [ ] 29.1.8. Slots
            - [ ] 29.1.9. Halogen Model
        - [ ] 29.2. Halogen Example Application
            - [ ] 29.2.1. Creating New Project
            - [ ] 29.2.2. Writing a Counter Component
            - [ ] 29.2.3. Rendering the Counter Component
            - [ ] 29.2.4. Counter Component Query Algebra
            - [ ] 29.2.5. Counter Component as a Child Component
            - [ ] 29.2.6. Emitters
    - [ ] 30. Writing a Front End using Halogen
        - [ ] 30.1. Halogen CSS Library Setup
        - [ ] 30.2. Hash Routing
            - [ ] 30.2.1. Defining Routes
        - [ ] 30.3. Application Monad
        - [ ] 30.4. Capabilities
        - [ ] 30.5. Capability Implementations
        - [ ] 30.6. Router Component
        - [ ] 30.7. Page Component
        - [ ] 30.8. Logon Page
        - [ ] 30.9. Calling the Backend
            - [ ] 30.9.1. CORS Solution
            - [ ] 30.9.2. Static File Server Solution
        - [ ] 30.10. ChangePassword Page
        - [ ] 30.11. Users Page
        - [ ] 30.12. Modal Dialog Component
        - [ ] 30.13. Message Modal Component
        - [ ] 30.14. Customizing the Modal Dialog Component
        - [ ] 30.15. Create Users Modal Component
        - [ ] 30.16. Logoff Page
- [ ] Appendix A: Epilogue