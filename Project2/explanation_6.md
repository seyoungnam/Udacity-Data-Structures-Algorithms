## Problem 6 : Union and Intersection

### Reasoning for choosing data structures and/or algorithms

For getting union and intersection of multiple sets, using bitwise operators would be the most efficient solution. After getting a set for union and intersection, I add each element in the set to a new linked list.

### Time Complexity

- `union()`: O(n\*m) - It is impossible to get a set for union without comparing all elements from the given two sets.
- `intersection()`: O(n\*m) - Same reason with `union()`.

### Space Complexity

- `union()`: O(n\+m) - The length of `sets` list in `union()` function is the summation of length from both lists.
- `intersection()`: O(n\+m) - Same reason with `union()`.
