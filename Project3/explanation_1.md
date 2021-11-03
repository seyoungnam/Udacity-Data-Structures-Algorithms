## Problem 1 : Finding the Square Root of an Integer

### Reasoning for choosing data structures and/or algorithms

To ensure the time complexity of `O(log(n))`, I choose binary search where the length of the given list gets halved by each iteration. if the square value of the mid number is larger than the input value, we will regard values smaller than the square of the mid number as the answer candidate. On the other hand, if the square value of a mid number is smaller than the input value, values larger than the square of the mid number would be considered the answer candidate.

### Time Complexity

- O(log(n)) - the number of answer candidates gets halved in each iteration. 

### Space Complexity

- O(1) - only `l`, `r`, and `mid` variables consume new spaces, regardless of how large the input value is. 
