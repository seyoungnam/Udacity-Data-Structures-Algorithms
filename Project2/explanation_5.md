## Problem 5 : Blockchain

### Reasoning for choosing data sturctures and/or algorithms

`Blockchain` class is basically a singly linked list where each node contains such information as timestamp, message(data), previous node hash value, current node hash value, and next node hash value.

### Time Complexity

- `add_block()`: O(n) - need to loop through a linked list from head to tail to add a new block.
- `print_blockchain()`: O(n) - Loop through every block to print

### Space Complexity

O(n) - Each block needs a space to store information
