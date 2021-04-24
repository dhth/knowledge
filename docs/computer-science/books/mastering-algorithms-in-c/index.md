---
title: "Mastering Algorithms in C"
summary:
---

Mastering Algorithms in C
===

Resources
---

- [:fontawesome-solid-book:
    Book](https://learning.oreilly.com/library/view/mastering-algorithms-with/1565924533/)
- [:fontawesome-solid-link: Supplemental
    Resources](https://resources.oreilly.com/examples/9781565924536/)

Chapters Checklist
---

- [ ] I. Preliminaries

    - [ ] 1. Introduction

        - [x] 1.1. An Introduction to Data Structures

        - [ ] 1.2. An Introduction to Algorithms
            - [ ] 1.2.1. General Approaches in Algorithm Design
                - [x] 1.2.1.1. Randomized algorithms
                - [x] 1.2.1.2. Divide-and-conquer algorithms
                - [ ] 1.2.1.3. Dynamic-programming solutions
                - [ ] 1.2.1.4. Greedy algorithms
                - [ ] 1.2.1.5. Approximation algorithms

        - [ ] 1.3. A Bit About Software Engineering

        - [ ] 1.4. How to Use This Book

    - [ ] 2. Pointer Manipulation

        - [ ] 2.1. Pointer Fundamentals

        - [ ] 2.2. Storage Allocation

        - [ ] 2.3. Aggregates and Pointer Arithmetic
            - [ ] 2.3.1. Structures
            - [ ] 2.3.2. Arrays

        - [ ] 2.4. Pointers as Parameters to Functions
            - [ ] 2.4.1. Call-by-Reference Parameter Passing
            - [ ] 2.4.2. Pointers to Pointers as Parameters

        - [ ] 2.5. Generic Pointers and Casts
            - [ ] 2.5.1. Generic Pointers
            - [ ] 2.5.2. Casts

        - [ ] 2.6. Function Pointers

        - [ ] 2.7. Questions and Answers

        - [ ] 2.8. Related Topics

    - [ ] 3. Recursion

        - [ ] 3.1. Basic Recursion

        - [ ] 3.2. Tail Recursion

        - [ ] 3.3. Questions and Answers

        - [ ] 3.4. Related Topics

    - [ ] 4. Analysis of Algorithms

        - [ ] 4.1. Worst-Case Analysis
            - [ ] 4.1.1. Reasons for Worst-Case Analysis

        - [ ] 4.2. O-Notation
            - [ ] 4.2.1. Simple Rules for O-Notation
            - [ ] 4.2.2. O-Notation Example and Why It Works

        - [ ] 4.3. Computational Complexity

        - [ ] 4.4. Analysis Example: Insertion Sort

        - [ ] 4.5. Questions and Answers

        - [ ] 4.6. Related Topics

- [ ] II. Data Structures

    - [ ] 5. Linked Lists

        - [ ] 5.1. Description of Linked Lists

        - [ ] 5.2. Interface for Linked Lists

        - [ ] 5.3. Implementation and Analysis of Linked Lists
            - [ ] 5.3.1. list_init
            - [ ] 5.3.2. list_destroy
            - [ ] 5.3.3. list_ins_next
            - [ ] 5.3.4. list_rem_next
            - [ ] 5.3.5. list_size, list_head, list_tail, list_is_tail,list_data, and list_next

        - [ ] 5.4. Linked List Example: Frame Management

        - [ ] 5.5. Description of Doubly-Linked Lists

        - [ ] 5.6. Interface for Doubly-Linked Lists

        - [ ] 5.7. Implementation and Analysis of Doubly Linked Lists
            - [ ] 5.7.1. dlist_init
            - [ ] 5.7.2. dlist_destroy
            - [ ] 5.7.3. dlist_ins_next
            - [ ] 5.7.4. dlist_ins_ prev
            - [ ] 5.7.5. dlist_remove
            - [ ] 5.7.6. dlist_size, dlist_head, dlist_tail, dlist_is_head, dlist_is_tail, dlist_data, dlist_next, and dlist_ prev

        - [ ] 5.8. Description of Circular Lists

        - [ ] 5.9. Interface for Circular Lists

        - [ ] 5.10. Implementation and Analysis of Circular Lists
            - [ ] 5.10.1. clist_init
            - [ ] 5.10.2. clist_destroy
            - [ ] 5.10.3. clist_ins_next
            - [ ] 5.10.4. clist_rem_next
            - [ ] 5.10.5. clist_size, clist_head, clist_data, and clist_next

        - [ ] 5.11. Circular List Example: Second-Chance Page Replacement

        - [ ] 5.12. Questions and Answers

        - [ ] 5.13. Related Topics

    - [ ] 6. Stacks and Queues

        - [ ] 6.1. Description of Stacks

        - [ ] 6.2. Interface for Stacks

        - [ ] 6.3. Implementation and Analysis of Stacks
            - [ ] 6.3.1. stack_init
            - [ ] 6.3.2. stack_destroy
            - [ ] 6.3.3. stack_ push
            - [ ] 6.3.4. stack_ pop
            - [ ] 6.3.5. stack_ peek, stack_size

        - [ ] 6.4. Description of Queues

        - [ ] 6.5. Interface for Queues

        - [ ] 6.6. Implementation and Analysis of Queues
            - [ ] 6.6.1. queue_init
            - [ ] 6.6.2. queue_destroy
            - [ ] 6.6.3. queue_enqueue
            - [ ] 6.6.4. queue_dequeue
            - [ ] 6.6.5. queue_ peek, queue_size

        - [ ] 6.7. Queue Example: Event Handling

        - [ ] 6.8. Questions and Answers

        - [ ] 6.9. Related Topics

    - [ ] 7. Sets

        - [ ] 7.1. Description of Sets
            - [ ] 7.1.1. Definitions
            - [ ] 7.1.2. Basic Operations
            - [ ] 7.1.3. Properties

        - [ ] 7.2. Interface for Sets

        - [ ] 7.3. Implementation and Analysis of Sets
            - [ ] 7.3.1. set_init
            - [ ] 7.3.2. set_destroy
            - [ ] 7.3.3. set_insert
            - [ ] 7.3.4. set_remove
            - [ ] 7.3.5. set_union
            - [ ] 7.3.6. set_intersection
            - [ ] 7.3.7. set_difference
            - [ ] 7.3.8. set_is_member
            - [ ] 7.3.9. set_is_subset
            - [ ] 7.3.10. set_is_equal
            - [ ] 7.3.11. set_size

        - [ ] 7.4. Set Example: Set Covering

        - [ ] 7.5. Questions and Answers

        - [ ] 7.6. Related Topics

    - [ ] 8. Hash Tables

        - [ ] 8.1. Description of Chained Hash Tables
            - [ ] 8.1.1. Collision Resolution
            - [ ] 8.1.2. Selecting a Hash Function
                - [ ] 8.1.2.1. Division method
                - [ ] 8.1.2.2. Multiplication method

        - [ ] 8.2. Interface for Chained Hash Tables

        - [ ] 8.3. Implementation and Analysis of Chained Hash Tables
            - [ ] 8.3.1. chtbl_init
            - [ ] 8.3.2. chtbl_destroy
            - [ ] 8.3.3. chtbl_insert
            - [ ] 8.3.4. chtbl_remove
            - [ ] 8.3.5. chtbl_lookup
            - [ ] 8.3.6. chtbl_size

        - [ ] 8.4. Chained Hash Table Example: Symbol Tables

        - [ ] 8.5. Description of Open-Addressed Hash Tables
            - [ ] 8.5.1. Collision Resolution
                - [ ] 8.5.1.1. Linear probing
                - [ ] 8.5.1.2. Double hashing

        - [ ] 8.6. Interface for Open-Addressed Hash Tables

        - [ ] 8.7. Implementation and Analysisof Open Addressed Hash Tables
            - [ ] 8.7.1. ohtbl_init
            - [ ] 8.7.2. ohtbl_destroy
            - [ ] 8.7.3. ohtbl_insert
            - [ ] 8.7.4. ohtbl_remove
            - [ ] 8.7.5. ohtbl_lookup
            - [ ] 8.7.6. ohtbl_size

        - [ ] 8.8. Questions and Answers

        - [ ] 8.9. Related Topics

    - [ ] 9. Trees

        - [ ] 9.1. Description of Binary Trees
            - [ ] 9.1.1. Traversal Methods
                - [ ] 9.1.1.1. Preorder traversal
                - [ ] 9.1.1.2. Inorder traversal
                - [ ] 9.1.1.3. Postorder traversal
                - [ ] 9.1.1.4. Level-order traversal
            - [ ] 9.1.2. Tree Balancing

        - [ ] 9.2. Interface for Binary Trees

        - [ ] 9.3. Implementation and Analysis of Binary Trees
            - [ ] 9.3.1. bitree_init
            - [ ] 9.3.2. bitree_destroy
            - [ ] 9.3.3. bitree_ins_left
            - [ ] 9.3.4. bitree_ins_right
            - [ ] 9.3.5. bitree_rem_left
            - [ ] 9.3.6. bitree_rem_right
            - [ ] 9.3.7. bitree_merge
            - [ ] 9.3.8. bitree_size, bitree_root, bitree_is_eob, bitree_is_leaf, bitree_data, bitree_left, bitree_right

        - [ ] 9.4. Binary Tree Example: Expression Processing

        - [ ] 9.5. Description of Binary Search Trees

        - [ ] 9.6. Interface for Binary Search Trees

        - [ ] 9.7. Implementation and Analysis of Binary Search Trees
            - [ ] 9.7.1. Rotations in AVL Trees
                - [ ] 9.7.1.1. LL rotation
                - [ ] 9.7.1.2. LR rotation
                - [ ] 9.7.1.3. RR rotation
                - [ ] 9.7.1.4. RL rotation
            - [ ] 9.7.2. bistree_init
            - [ ] 9.7.3. bistree_destroy
            - [ ] 9.7.4. bistree_insert
            - [ ] 9.7.5. bistree_remove
            - [ ] 9.7.6. bistree_lookup
            - [ ] 9.7.7. bistree_size

        - [ ] 9.8. Questions and Answers

        - [ ] 9.9. Related Topics

    - [ ] 10. Heaps and Priority Queues

        - [ ] 10.1. Description of Heaps

        - [ ] 10.2. Interface for Heaps

        - [ ] 10.3. Implementation and Analysis of Heaps
            - [ ] 10.3.1. heap_init
            - [ ] 10.3.2. heap_destroy
            - [ ] 10.3.3. heap_insert
            - [ ] 10.3.4. heap_extract
            - [ ] 10.3.5. heap_size

        - [ ] 10.4. Description of Priority Queues

        - [ ] 10.5. Interface for Priority Queues

        - [ ] 10.6. Implementation and Analysis of Priority Queues

        - [ ] 10.7. Priority Queue Example: Parcel Sorting

        - [ ] 10.8. Questions and Answers

        - [ ] 10.9. Related Topics

    - [ ] 11. Graphs

        - [ ] 11.1. Description of Graphs
            - [ ] 11.1.1. Search Methods
                - [ ] 11.1.1.1. Breadth-first search
                - [ ] 11.1.1.2. Depth-first search

        - [ ] 11.2. Interface for Graphs

        - [ ] 11.3. Implementation and Analysis of Graphs
            - [ ] 11.3.1. graph_init
            - [ ] 11.3.2. graph_destroy
            - [ ] 11.3.3. graph_ins_vertex
            - [ ] 11.3.4. graph_ins_edge
            - [ ] 11.3.5. graph_rem_vertex
            - [ ] 11.3.6. graph_rem_edge
            - [ ] 11.3.7. graph_adjlist
            - [ ] 11.3.8. graph_is_adjacent
            - [ ] 11.3.9. graph_adjlists, graph_vcount, graph_ecount

        - [ ] 11.4. Graph Example: Counting Network Hops

        - [ ] 11.5. Graph Example: Topological Sorting

        - [ ] 11.6. Questions and Answers

        - [ ] 11.7. Related Topics

- [ ] III. Algorithms

    - [ ] 12. Sorting and Searching

        - [ ] 12.1. Description of Insertion Sort

        - [ ] 12.2. Interface for Insertion Sort

        - [ ] 12.3. Implementation and Analysis of Insertion Sort

        - [ ] 12.4. Description of Quicksort

        - [ ] 12.5. Interface for Quicksort

        - [ ] 12.6. Implementation and Analysis of Quicksort

        - [ ] 12.7. Quicksort Example: Directory Listings

        - [ ] 12.8. Description of Merge Sort

        - [ ] 12.9. Interface for Merge Sort

        - [ ] 12.10. Implementation and Analysis of Merge Sort

        - [ ] 12.11. Description of Counting Sort

        - [ ] 12.12. Interface for Counting Sort

        - [ ] 12.13. Implementation and Analysis of Counting Sort

        - [ ] 12.14. Description of Radix Sort

        - [ ] 12.15. Interface for Radix Sort

        - [ ] 12.16. Implementation and Analysis of Radix Sort

        - [ ] 12.17. Description of Binary Search

        - [ ] 12.18. Interface for Binary Search

        - [ ] 12.19. Implementation and Analysis of Binary Search

        - [ ] 12.20. Binary Search Example: Spell Checking

        - [ ] 12.21. Questions and Answers

        - [ ] 12.22. Related Topics

    - [ ] 13. Numerical Methods

        - [ ] 13.1. Description of Polynomial Interpolation
            - [ ] 13.1.1. Constructing an Interpolating Polynomial
            - [ ] 13.1.2. Evaluating an Interpolating Polynomial

        - [ ] 13.2. Interface for Polynomial Interpolation

        - [ ] 13.3. Implementation and Analysis of Polynomial Interpolation

        - [ ] 13.4. Description of Least-Squares Estimation

        - [ ] 13.5. Interface for Least-Squares Estimation

        - [ ] 13.6. Implementation and Analysis of Least-Squares Estimation

        - [ ] 13.7. Description of the Solution of Equations
            - [ ] 13.7.1. Finding Roots with Newton’s Method
            - [ ] 13.7.2. Computing the Derivative of a Polynomial
            - [ ] 13.7.3. Understanding the First and Second Derivative
            - [ ] 13.7.4. Selecting an Initial Point for Newton’s Method
            - [ ] 13.7.5. How Newton’s Method Works

        - [ ] 13.8. Interface for the Solution of Equations

        - [ ] 13.9. Implementation and Analysis of the Solution of Equations

        - [ ] 13.10. Questions and Answers

        - [ ] 13.11. Related Topics

    - [ ] 14. Data Compression

        - [ ] 14.1. Description of Bit Operations

        - [ ] 14.2. Interface for Bit Operations

        - [ ] 14.3. Implementation and Analysis of Bit Operations
            - [ ] 14.3.1. bit_ get
            - [ ] 14.3.2. bit_set
            - [ ] 14.3.3. bit_xor
            - [ ] 14.3.4. bit_rot_left

        - [ ] 14.4. Description of Huffman Coding
            - [ ] 14.4.1. Entropy and Minimum Redundancy
            - [ ] 14.4.2. Building a Huffman Tree
            - [ ] 14.4.3. Compressing and Uncompressing Data
            - [ ] 14.4.4. Effectiveness of Huffman Coding

        - [ ] 14.5. Interface for Huffman Coding

        - [ ] 14.6. Implementation and Analysis of Huffman Coding
            - [ ] 14.6.1. huffman_compress
            - [ ] 14.6.2. huffman_uncompress

        - [ ] 14.7. Huffman Coding Example: Optimized Networking

        - [ ] 14.8. Description of LZ77
            - [ ] 14.8.1. Maintaining a Dictionary of Phrases
            - [ ] 14.8.2. Compressing and Uncompressing Data
            - [ ] 14.8.3. Effectiveness of LZ77

        - [ ] 14.9. Interface for LZ77

        - [ ] 14.10. Implementation and Analysis of LZ77
            - [ ] 14.10.1. lz77_compress
            - [ ] 14.10.2. lz77_uncompress

        - [ ] 14.11. Questions and Answers

        - [ ] 14.12. Related Topics

    - [ ] 15. Data Encryption

        - [ ] 15.1. Description of DES
            - [ ] 15.1.1. Computing Subkeys
            - [ ] 15.1.2. Enciphering and Deciphering Data Blocks

        - [ ] 15.2. Interface for DES

        - [ ] 15.3. Implementation and Analysis of DES
            - [ ] 15.3.1. des_encipher
            - [ ] 15.3.2. des_decipher

        - [ ] 15.4. DES Example: Block Cipher Modes

        - [ ] 15.5. Description of RSA
            - [ ] 15.5.1. Computing Public and Private Keys
            - [ ] 15.5.2. Enciphering and Deciphering Data Blocks

        - [ ] 15.6. Interface for RSA

        - [ ] 15.7. Implementation and Analysis of RSA
            - [ ] 15.7.1. rsa_encipher
            - [ ] 15.7.2. rsa_decipher

        - [ ] 15.8. Questions and Answers

        - [ ] 15.9. Related Topics

    - [ ] 16. Graph Algorithms

        - [ ] 16.1. Description of Minimum Spanning Trees
            - [ ] 16.1.1. Prim’s Algorithm

        - [ ] 16.2. Interface for Minimum Spanning Trees

        - [ ] 16.3. Implementation and Analysis of Minimum Spanning Trees

        - [ ] 16.4. Description of Shortest Paths
            - [ ] 16.4.1. Dijkstra’s Algorithm

        - [ ] 16.5. Interface for Shortest Paths

        - [ ] 16.6. Implementation and Analysis of Shortest Paths

        - [ ] 16.7. Shortest Paths Example: Routing Tables

        - [ ] 16.8. Description of the Traveling-Salesman Problem
            - [ ] 16.8.1. Applying the Nearest-Neighbor Heuristic

        - [ ] 16.9. Interface for the Traveling-Salesman Problem

        - [ ] 16.10. Implementation and Analysis of the Traveling-Salesman Problem

        - [ ] 16.11. Questions and Answers

        - [ ] 16.12. Related Topics

    - [ ] 17. Geometric Algorithms

        - [ ] 17.1. Description of Testing Whether Line Segments Intersect
            - [ ] 17.1.1. Standard Test for Intersecting Line Segments
            - [ ] 17.1.2. Computer Test for Intersecting Line Segments

        - [ ] 17.2. Interface for Testing Whether Line Segments Intersect

        - [ ] 17.3. Implementation and Analysis of Testing Whether Line Segments Intersect

        - [ ] 17.4. Description of Convex Hulls
            - [ ] 17.4.1. Jarvis’s March

        - [ ] 17.5. Interface for Convex Hulls

        - [ ] 17.6. Implementation and Analysis of Convex Hulls

        - [ ] 17.7. Description of Arc Length on Spherical Surfaces
            - [ ] 17.7.1. Rectilinear and Spherical Coordinates
            - [ ] 17.7.2. Converting Between Coordinate Systems
            - [ ] 17.7.3. Computing the Length of an Arc

        - [ ] 17.8. Interface for Arc Length on Spherical Surfaces

        - [ ] 17.9. Implementation and Analysis of Arc Length on Spherical Surfaces

        - [ ] 17.10. Arc Length Example: Approximating Distances on Earth

        - [ ] 17.11. Questions and Answers

        - [ ] 17.12. Related Topics
