# 1.4: Modeling the Problem

Combinatorial Objects
---

Odds are very good that others have stumbled upon your algorithmic problem
before you, perhaps in substantially different contexts. But to find out what is
known about your particular "widget optimization problem," you can't hope to
look in a book under widget. You must formulate widget optimization in terms of
computing properties of common structures such as: 

- **Permutations** -- which are arrangements, or orderings, of items. For 
example, {1, 4, 3, 2} and {4, 3, 2, 1} are two distinct permutations of the same
set of four integers. We have already seen permutations in the robot
optimization prob- lem, and in sorting. Permutations are likely the object in
question whenever your problem seeks an "arrangement," "tour," "ordering," or
"sequence." 

- **Subsets** -- which represent selections from a set of items. For example, 
{1, 3, 4} and {2} are two distinct subsets of the first four integers. Order
does not matter in subsets the way it does with permutations, so the subsets {1,
3, 4} and {4, 3, 1} would be considered identical. We saw subsets arise in the
movie scheduling problem. Subsets are likely the object in question whenever
your problem seeks a "cluster," "collection," "committee," "group," "packaging,"
or "selection." 

- **Trees** -- which represent hierarchical relationships between items. Trees 
are likely the object in question whenever your problem seeks a "hierarchy,"
"dominance relationship," "ancestor/descendant relationship," or "taxonomy." 

- **Graphs** -- which represent relationships between arbitrary pairs of
objects. Graphs are likely the object in question whenever you seek a "network,"
"circuit," "web," or "relationship." 

- **Points** -- which represent locations in some geometric space. For example,
the locations of McDonald's restaurants can be described by points on a
map/plane.  Points are likely the object in question whenever your problems work
on "sites," "positions," "data records," or "locations." 

- **Polygons** -- which represent regions in some geometric spaces. For example,
the borders of a country can be described by a polygon on a map/plane. Polygons
and polyhedra are likely the object in question whenever you are working on
"shapes," "regions," "configurations," or "boundaries." 

- **Strings** -- which represent sequences of characters or patterns. For
example, the names of students in a class can be represented by strings. Strings
are likely the object in question whenever you are dealing with "text," "charac-
ters," "patterns," or "labels."
