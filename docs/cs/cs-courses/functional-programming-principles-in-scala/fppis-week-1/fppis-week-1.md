# FPPiS Week 1

The Substituion Model
---

Idea -> All evaluation does is reduce an expression to a value.

Formalized in lambda calculus (See Alonzo Church).

Question: Does every expression reduce to a value?
> No. An infinite loop doesn't

Evaluation Strategy
---

call by value v. call by name

 - Advantage of CBV: all parameters are evaluated just once
 - Advantage of CBN: unused parameters are not evaluated

Evaluation Strategy and Termination
---

- If CBV evaluation terminates, then CBN does too
- The other way around is not true
