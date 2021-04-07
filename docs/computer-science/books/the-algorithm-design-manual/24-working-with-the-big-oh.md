---
title: "2.4: Working with the Big Oh"
summary: 
---

2.4: Working with the Big Oh
===

Adding functions
---

```
O(f (n)) + O(g(n)) → O(max(f (n), g(n)))  
Ω(f (n)) + Ω(g(n)) → Ω(max(f (n), g(n)))  
Θ(f (n)) + Θ(g(n)) → Θ(max(f (n), g(n)))
```

Multiplying functions
---

```
O(f (n)) ∗ O(g(n)) → O(f (n) ∗ g(n))

Ω(f (n)) ∗ Ω(g(n)) → Ω(f (n) ∗ g(n))

Θ(f (n)) ∗ Θ(g(n)) → Θ(f (n) ∗ g(n))
```
