CTCI Technical Questions
===

What You Need to Know
---

Core Data Structures:

- Linked Lists
- Trees, Tries, Graphs
- Stacks & Queues
- Heaps
- Vectors/Arraylists
- Hash Tables

Algorithms:

- Breadth-First Search
- Depth-First Search
- Binary Search
- Merge Sort
- Quick Sort

Concepts:

- Bit Manipulation
- Memory (Stack vs. Heap)
- Recursion
- Dynamic Programming
- Big O Time & Space


Walking Through a Problem
---

- 1) Listen
- 2) Example
- 3) Brute Force
- 4) Optimize
- 5) Walk Through
- 6) Implement
- 7) Test

### Example

Create an example that is specific (eg. use real numbers, strings for a tree),
sufficiently large, and not a special case.

### Brute Force

Come up with a brute force solution, and state that it's a brute force solution,
even if obvious (don't assume that the interviewer would know that you can come
up with a simple solution; always express your thoughts clearly)

### Optimize

- Look for unused info
- Use a fresh example
- Solve it incorrectly; this can sometimes help come up with a better solution
- Make time v. space tradeoff. Storing extra state about a problem can sometimes
    help in optimisation
- Precompute info (eg. sorting beforehand)
- Remove bottenecks
- Remove unnecessary computation
- Remove duplicated work


Removing Bottlenecks
---

Optimise the step that takes the longest time. Consider the following problem:

> Find all pairs of elements in an unsorted array that have a difference of `k`.

A brute force way to find a solution would be to iterate over all pairs of
elements, and see it the condition holds (a runtime of `O(N^2)`). We could sort
the array first, and then perform a binary search for `x+k` and `x-k` for each
`x` in the array. Both steps would be `O(N log N)`. Optimising one step will not
be enough as both have the same runtime.

Finally, we could create a hash table from the elements of the array, and then
just search for `x+k` and `x-k`, resulting in the overall runtime of `O(N)`.

