---
title: "3.1: Contiguous vs Linked Data Structures"
summary:
---

3.1: Contiguous vs Linked Data Structures
===

Linked lists vs static arrays
---

The relative advantages of linked lists over static arrays include:

- Overflow on linked structures can never occur unless the memory is actually full.
- Insertions and deletions are simpler than for contiguous (array) lists.
- With large records, moving pointers is easier and faster than moving the
items themselves.

while the relative advantages of arrays include:

- Linked structures require extra space for storing pointer fields.
- Linked lists do not allow efficient random access to items.
- Arrays allow better memory locality and cache performance than random pointer jumping.
