## Problem 3 : Huffman Coding

### Reasoning for choosing data sturctures and/or algorithms

In `create_tree` function, the `Counter` function in the `collections` library is utilized to count frequency for each characters in the given data. After sorting each characters by frequency using `sorted` function, build a tree by relying on frequency of each characters. Then in `create_huff_code_dict` function, the tree transforms to the dictionary with a character as key and its Huffman code as value.

For encoding data, loop through the given data character by character and create an encoded string by adding Huffman code for each character.

For decoding data, firstly create the `code_to_char` dictionary with Huffman code as key and its character as value by iterating `huff_code_dict`. Then decode the given encoded data with the help of `code_to_char`.

### Time Complexity

- `huffman_encoding()`: O(nlogn) - `create_tree` takes O(nlogn) for sorting. `create_huff_code_dict` takes O(n) because each leaf node should be visited at least once. The following for loop takes O(n). Thus, the time complexity for `huffman_encoding()` is O(nlogn).
- `huffman_decoding()`: O(n) - In this function, first for loop takes O(n) and the following while loop also takes O(n). Thus, O(n).

### Space Complexity

- `huffman_encoding()`: O(n) - `create_tree` takes O(n) because the tree has n elements. `create_huff_code_dict` also takes O(n) with n key-value pairs. Producing encoded string takes O(1). Thus, O(n).
- `huffman_decoding()`: O(n) - `code_to_char` takes O(n) with n key-value pairs. Producing decoded string takes O(1). Thus, O(n).
