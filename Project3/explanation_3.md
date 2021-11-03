## Problem 3 : Rearrange Array Elements

### Reasoning for choosing data structures and/or algorithms

Among sorting algorithms, only heap sort and merge sort ensure time complexity of `O(nlog(n))` in the worst scenario. I choose to merge sort for this problem because its algorithm is more straightforward to understand and simpler to implement than heap sort.

### Time Complexity

- O(nlog(n)) - Time complexity for `mergesort(input_list)` in `rearrange_digits(input_list)` is `O(nlog(n))` because it takes `O(log(n))` to get the list halved until the length of the list becomes 1 and you have to visit every element of the list to conduct `merge(left, right)`, taking `O(n)`. The following for-loop in `rearrange_digits(input_list)` takes `O(n)`. Thus, time complexity for `rearrange_digits(input_list)` is `O(nlog(n))`.

### Space Complexity

- O(n) - `mergesort(input_list)` breaks apart every element but does not require additional space in the sorting process.
