# CTCI Big O

Base of logs and exponents
---

The base of a log doesn't matter for big O since logs of different bases are
only different by a constant factor. However, this does not apply to exponents.
The base of an exponent does matter. Compare 2^n and 8^n If you expand 8^n you
get (2^3)^n which equals 2^3n, which equals 2^2n * 2^n. So, 8^n and 2^n are
different by a factor of 2^2n, which is not a constant factor.
