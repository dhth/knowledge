# The Big O Notation

Why ignore constants?
---

The purpose of Big O is that for different classifications, there will be a
point at which one classification supersedes the other in speed, and will remain
faster forever. When that point occurs exactly, however, is not the concern of
Big O.

What to choose when two algorithms have same the Big O class
---

When two algorithms fall under the same classification of Big O, it doesn’t
necessarily mean that both algorithms process at the same speed. After all,
Bubble Sort is twice as slow as Selection Sort even though both are O(N2). So
while Big O is perfect for contrasting algorithms that fall under different
classifications of Big O, when two algorithms fall under the same
classification, further analysis is required to determine which algorithm is
faster.
