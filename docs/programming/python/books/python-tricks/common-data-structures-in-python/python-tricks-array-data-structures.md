# Python Tricks Array Data Structures

There are a number of built-in data structures you can choose from when it comes
to implementing arrays in Python. In this chapter we’ve focused on core language
features and data structures included in the standard library only.

If you’re willing to go beyond the Python standard library, third-party packages
like NumPy14 offer a wide range of fast array implementations for scientific
computing and data science.

By restricting ourselves to the array data structures included with Python,
here’s what our choices come down to:

- You need to store arbitrary objects, potentially with mixed data types?

Use a list or a tuple, depending on whether you want an immutable data structure
or not.

- You have numeric (integer or floating point) data and tight packing and
  performance is important?

Try out array.array and see if it does everything you need. Also, consider going
beyond the standard library and try out packages like NumPy or Pandas.

- You have textual data represented as Unicode characters?

Use Python’s built-in str. If you need a “mutable string,” use a list of
characters.

- You want to store a contiguous block of bytes?

Use the immutable bytes type, or bytearray if you need a mutable data struc-
ture.
