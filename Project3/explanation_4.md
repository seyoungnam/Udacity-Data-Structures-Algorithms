## Problem 4 : Dutch National Flag Problem

### Reasoning for choosing data structures and/or algorithms

This algorithm contains three pointers. Pointer `i` traverse the array. Pointer `l` and `r` represent the index to place 0 and 2 respectively. While traversing the array, when point `i` is 0, place the current element to index `l` and element at `l` is placed back to index `i`. Same process happens when the element at index `i` is 2. 

### Time Complexity

- O(n) - We should visit each element from index 0 to the pointer `r` where the left-end 2 is located. In the worst case, `r` could be the right-end of the list. Thus, time complexity is `O(n)`.

### Space Complexity

- O(1) - only `l`, `r`, and `i` variables consume new spaces, regardless of how large the input value is. 
