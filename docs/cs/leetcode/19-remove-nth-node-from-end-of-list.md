# 19: Remove Nth Node From End of List

The requirement for one-pass algorithm is misleading. True one-pass for this
kind of problem is impossible ([One-pass
Algorithm](https://en.wikipedia.org/wiki/One-pass_algorithm)).

One way is to iterate through the list, find it's length, then iterate again,
and stop behind the node to be removed, and change references appropriately.

Another approach would be to maintain two pointers to the list, both having `n`
distance between them. Continue iterating over the list, and updating pointers,
until the farther one reaches the end of the list. When this happens, the other
pointer will be at the node to be removed.
