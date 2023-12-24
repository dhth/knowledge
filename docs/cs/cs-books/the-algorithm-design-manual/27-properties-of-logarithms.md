# 2.7: Properties of Logarithms

Two implications of these properties of logarithms are important to appreciate
from an algorithmic perspective:

- The base of the logarithm has no real impact on the growth rate - Compare the
following three values: log2(1,000,000) = 19.9316, log3(1,000,000) = 12.5754,
and log100 (1, 000, 000) = 3. A big change in the base of the logarithm produces
little difference in the value of the log. Changing the base of the log from a
to c involves dividing by logc a. This conversion factor is lost to the Big Oh
notation whenever a and c are constants. Thus we are usually justified in
ignoring the base of the logarithm when analyzing algorithms.

- Logarithms cut any function down to size - The growth rate of the logarithm of
any polynomial function is O(lg n). This follows because loga nb = b·loga n The
power of binary search on a wide range of problems is a consequence of this
observation. Note that doing a binary search on a sorted array of n2 things
requires only twice as many comparisons as a binary search on n things.
Logarithms efficiently cut any function down to size.
