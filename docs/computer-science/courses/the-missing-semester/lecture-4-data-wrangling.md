---
title: "Lecture 3: Data Wrangling"
summary:
---

Lecture 3: Data Wrangling
===

Resources
---
- [:fontawesome-solid-play-circle: Lecture](https://www.youtube.com/watch?v=sz_dsktIjt4)
- [:fontawesome-solid-link: sed](https://en.wikipedia.org/wiki/Sed)
- [:fontawesome-solid-link: Lecture page](https://missing.csail.mit.edu/2020/data-wrangling/)

Commands
---

`sed` stands for "stream editor".

sed is a pretty old tool, so if we want to use newer regex syntax, pass in `-E`
flag to sed.

!!! note
    regular expressions match in a greedy way by default
    `echo 'test string test123' | sed 's/.*test//'`
    will return '123'

- `sort` sorts lines.
- `uniq -c` removes duplicates, and prints counts of items
- `paste -sd+` joins lines with delimiter `+`
- `awk` is great to wrangle columnar data
