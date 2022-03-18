CTCI Big O
===

Base of logs and exponents
---

The base of a log doesn't matter for big O since logs of different bases are
only different by a constant factor. However, this does not apply to exponents.
The base of an exponent does matter. Compare 2" and 8". If you expand 8", you
get (23)", which equals 23", which equals 22" * 2". As you can see, 8" and 2°
are different by a factor of 22". That is not a constant factor.
