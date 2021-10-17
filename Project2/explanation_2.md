## Problem 2 : File Recursion

### Reasoning for choosing data sturctures and/or algorithms

**Breadth First Search** is the key algorithm for searching all files in the hierarchical directory structure. To be more specific, a certain directory contains either directories or files. For every directories, append them to the list called `dirs`. For every files, verify the suffix and decide whether the file is added to the list `target_files`.

### Time Complexity

O(n) - All files should be visited at least once to confirm the file contains the suggested suffix.

### Space Complexity

O(n) - In the worst case, all files contains the given suffix and thus should be added to the list. Therefore, the length of the list can be n.
