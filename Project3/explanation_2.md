## Problem 2 : Search in a Rotated Sorted Array

### Reasoning for choosing data structures and/or algorithms

Like problem 1, I try out the binary search to ensure the time complexity of `O(log(n))`. A binary search is a feasible approach for this problem because the given list is **sorted**. 

### Time Complexity

- O(log(n)) - the number of answer candidates gets halved in each iteration. 

### Space Complexity

- O(1) - only `l`, `r`, and `mid` variables take new spaces, regardless of how long the input list is. 
