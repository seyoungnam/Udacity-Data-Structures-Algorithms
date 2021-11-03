## Problem 5 : Autocomplete with Tries

### Reasoning for choosing data structures and/or algorithms

The `Trie` class possesses the `is_word` attribute that checks if the current Node is the last character of a word. A `Trie` structure is optimal to represent the hierarchical structure because it allows us to do very quick lookups of a word and it occupies the least space to store given words.

### Time Complexity

* `TrieNode` class:
    * `insert()`: O(1) - this function initiates a new `TrieNode` instance, creating two variables.
    * `suffixes()`: O(nm) - `n` represents the length of `wordList` and `m` refers to the length of each word. In the worst case, all words contain the input prefix and we have to visit every character of each word.

* `Trie` class:
    * `insert()`: O(n) - `n` represents the length of the input word. To perform `insert()`, we have to visit every character of the word.
    * `find()`: O(n) - `n` represents the length of the word that contains the prefix. In the worst case, the given prefix is as long as its word, we have to visit every character.

### Space Complexity

* `TrieNode` class:
    * `insert()`: O(1) - this function initiates a new `TrieNode` instance, taking constant spaces for the two variables.
    * `suffixes()`: O(n) - In the worst case, all words contain the input prefix and every words in the `wordList` should be stored.

* `Trie` class:
    * `insert()`: O(n) - `n` represents the length of the input word. Each character takes a space.
    * `find()`: O(1) - the functions requires a new space only for `curr` variable.
