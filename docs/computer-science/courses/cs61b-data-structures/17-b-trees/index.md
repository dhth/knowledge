---
title: "17: B Trees"
summary: 
---

17: B Trees
===

Asymptotics for tree height
---

Which statement gives you more information about a hotel?

```
A) The most expensive room in the hotel is $639 per night.
B) Every room in the hotel is less than or equal to $639 per night.
```

The answer is `A`, since we know for sure that there is atleast one room in the
hotel that costs $639, whereas there is no guarantee of that in `B`. Moreover, a
large number of hotels, (or motels) would fulfill the statement in `B` (ie, have
rooms that cost a 100 bucks, but would still fulfill the statement).

In the same vein, the one of the following statements about tree height is more
informative:

```
A) Worst case BST height is Θ(N).
B) BST height is O(N).
```

In this case, it's `A`.

Which leads to the question, why is Big O useful? It's because of the following:

- Allows us to make simple blanket statements, e.g. can just say “binary search
is O(log N)” instead of “binary search is Θ(log N) in the worst case”.
- Sometimes don’t know the exact runtime, so use O to give an upper bound.

